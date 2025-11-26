"""
Model 0: Baseline (DHI0 only)
"""

import pandas as pd


def compute_model0(df, dhi_col="DHI0"):
    if dhi_col not in df.columns:
        raise KeyError("DHI0 column missing")
    return df.copy()
