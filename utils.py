"""
Utility helpers for season ordering and dataframe tools.
"""

import pandas as pd

def ensure_season_order(df, season_col="season"):
    """
    Ensures a consistent seasonal ordering for MAM → OND.

    Parameters
    ----------
    df : DataFrame
        Must contain a season column.
    season_col : str
        The name of the season column.

    Returns
    -------
    df : DataFrame
        Sorted by region, year, season order.
    """

    season_order = {"MAM": 1, "OND": 2}

    if season_col not in df.columns:
        raise ValueError(f"Column '{season_col}' not found in dataframe.")

    df["season_order"] = df[season_col].map(season_order)
    df = df.sort_values(["region", "year", "season_order"]).drop(columns="season_order")

    return df
