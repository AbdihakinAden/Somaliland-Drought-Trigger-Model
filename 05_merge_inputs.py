"""
merge_inputs.py
Merge SPI extraction, normalized SPI (DHI0), dry percentage, and impact observations
into one master dataset for model validation.
"""

import pandas as pd
from pathlib import Path


def merge_all(
    spi_path="../data/processed/somaliland_spi_2020_2023.csv",
    norm_path="../data/processed/somaliland_spi_normalized.csv",
    drypct_path="../data/processed/somaliland_spi_drypct_2020_2023.csv",
    impact_path="../data/processed/validation_impact_2020_2023.csv",
    out_path="../data/processed/merged_for_models.csv"
):

    spi = pd.read_csv(spi_path)
    norm = pd.read_csv(norm_path)
    dry = pd.read_csv(drypct_path)
    obs = pd.read_csv(impact_path)

    # clean consistent keys
    key = ["region", "year", "season"]

    # merge step-by-step
    df = spi.merge(norm[key + ["DHI0"]], on=key, how="left")
    df = df.merge(dry[key + ["DryPct"]], on=key, how="left")
    df = df.merge(obs[key + ["OBS"]], on=key, how="left")

    # ensure season ordering
    season_order = {"MAM": 1, "OND": 2}
    df["season_order"] = df["season"].map(season_order)
    df = df.sort_values(["region", "year", "season_order"]).drop(columns="season_order")

    # save
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)

    print("✅ merged_for_models.csv created successfully!")
    print("📁 Saved to:", out_path)
    return df
