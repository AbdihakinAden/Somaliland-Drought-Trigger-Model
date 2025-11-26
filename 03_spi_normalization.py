"""
spi_normalization.py
Normalize SPI into 0–100 dryness scale using reverse min–max scaling.
"""

import pandas as pd


def normalize_spi(
    df,
    spi_col="mean",
    out_col="DHI0",
    spi_min=-2.5,
    spi_max=2.5
):
    """
    Normalize SPI values into a 0–100 drought hazard scale.

    Formula (reverse min–max scaling):
        DHI0 = ((spi_max - SPI) / (spi_max - spi_min)) * 100

    Meaning:
        Lower SPI  => higher dryness => higher DHI0
        Higher SPI => wetter conditions => lower DHI0

    Parameters
    ----------
    df : pd.DataFrame
        Must contain a column with SPI values.
    spi_col : str
        Column name containing SPI values (default: "mean").
    out_col : str
        Output column name for normalized values (default: "DHI0").
    spi_min : float
        Minimum SPI used for scaling (default: -2.5).
    spi_max : float
        Maximum SPI used for scaling (default: 2.5).

    Returns
    -------
    pd.DataFrame
        Copy of df with new column out_col (0–100 scaled index).
    """

    if spi_col not in df.columns:
        raise KeyError(f"Column '{spi_col}' not found in dataframe.")

    scale_range = spi_max - spi_min
    if scale_range <= 0:
        raise ValueError("spi_max must be greater than spi_min.")

    out = df.copy()

    # reverse min–max scaling
    out[out_col] = ((spi_max - out[spi_col]) / scale_range) * 100

    # enforce valid range
    out[out_col] = out[out_col].clip(0, 100).round(3)

    return out
