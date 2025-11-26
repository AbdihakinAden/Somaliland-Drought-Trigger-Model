"""
Model 1: DHI1 = 0.7 * DHI0 + 0.3 * DryPct
"""

import pandas as pd


def compute_model1(df, out_col="DHI1"):
    _df = df.copy()
    _df[out_col] = 0.7 * _df["DHI0"] + 0.3 * _df["DryPct"]
    _df[out_col] = _df[out_col].clip(0, 100).round(3)
    return _df
