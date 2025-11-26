"""
model2_memory.py

Independent Model 2 implementation (pure function).
Produces DHI_t, DHI2_T{T} continuous columns and prediction columns named:
    pred_T25, pred_T30, pred_T40  (or according to thresholds provided)

Usage:
    df2 = compute_model2_independent(df, gamma=0.2, thresholds=(25,30,40))
"""

from typing import Iterable, List
import pandas as pd
import numpy as np


def _compute_base_dhi(df: pd.DataFrame, dhi0_col: str = "DHI0", drypct_col: str = "DryPct") -> pd.Series:
    """Base DHI_t (same as model1)"""
    return (0.7 * df[dhi0_col].astype(float)) + (0.3 * df[drypct_col].astype(float))


def compute_model2_independent(
    df: pd.DataFrame,
    gamma: float = 0.2,
    thresholds: Iterable[int] = (25, 30, 40),
    dhi0_col: str = "DHI0",
    drypct_col: str = "DryPct",
    time_order_cols: List[str] = ("year", "season"),
    season_sort_key: List[str] = ("MAM", "OND")
) -> pd.DataFrame:
    """
    Compute Model 2 independently for each region and for each threshold.

    - Adds column 'DHI_t' (base index)
    - For each T in thresholds:
        - adds 'DHI2_T{T}' (continuous, memory-applied)
        - adds 'pred_T{T}' (binary prediction, same naming as model0/model1)
    """

    _df = df.copy()

    # sanity checks
    for c in [dhi0_col, drypct_col, "region"] + list(time_order_cols):
        if c not in _df.columns:
            raise KeyError(f"Required column '{c}' not found in DataFrame")

    # deterministic seasonal ordering: create order index
    season_rank = {s: i for i, s in enumerate(season_sort_key)}

    def _order_idx(row):
        y = int(row[time_order_cols[0]])
        s = row[time_order_cols[1]]
        return y * 10 + season_rank.get(s, 99)

    _df["order_idx"] = _df.apply(_order_idx, axis=1)
    _df = _df.sort_values(["region", "order_idx"]).reset_index(drop=True)

    # compute base DHI_t (same as model1 formula)
    _df["DHI_t"] = _compute_base_dhi(_df, dhi0_col=dhi0_col, drypct_col=drypct_col).round(6)

    # for each threshold, compute memory cascading DHI_final and binary predictions
    for T in thresholds:
        final_col = f"DHI2_T{T}"
        pred_col = f"pred_T{T}"     # <-- NOTE: same name pattern as Model 0/1
        _df[final_col] = np.nan

        # process region-by-region in chronological order
        for region in _df["region"].unique():
            sub_idx = _df[_df["region"] == region].index.tolist()
            prev_val = None
            for idx in sub_idx:
                base = float(_df.at[idx, "DHI_t"])
                if prev_val is not None and prev_val > T:
                    value = base + gamma * prev_val
                else:
                    value = base
                _df.at[idx, final_col] = value
                prev_val = value

        # create binary prediction column with **same** pattern as model0/model1
        _df[pred_col] = (_df[final_col] > T).astype(int)

    # keep order_idx for potential debugging but it's safe to drop for final output:
    _df = _df.drop(columns=["order_idx"])

    return _df
