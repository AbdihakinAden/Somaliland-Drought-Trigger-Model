"""
dry_percentage.py
Compute dry area % per region: SPI < threshold
"""

import pandas as pd
import geopandas as gpd
import rasterio
from rasterstats import zonal_stats


class DryPercentageExtractor:
    def __init__(self, threshold=-1):
        self.threshold = threshold

    def load_boundary(self, shp_path):
        gdf = gpd.read_file(shp_path)
        region_col = None

        for col in gdf.columns:
            if "ADM1" in col.upper() or "NAME" in col.upper():
                region_col = col
                break

        if region_col is None:
            region_col = gdf.columns[0]

        gdf = gdf.rename(columns={region_col: "region"})
        return gdf[["region", "geometry"]]

    def compute(self, tif_path, gdf):
        with rasterio.open(tif_path) as src:
            spi = src.read(1)
            affine = src.transform
            nodata = src.nodata

        dry_mask = ((spi < self.threshold) & (spi != nodata)).astype(int)
        valid_mask = (spi != nodata).astype(int)

        dry_stats = zonal_stats(gdf, dry_mask, affine=affine, stats=["sum"])
        valid_stats = zonal_stats(gdf, valid_mask, affine=affine, stats=["sum"])

        rows = []
        for i, row in gdf.iterrows():
            dry = dry_stats[i]["sum"]
            total = valid_stats[i]["sum"]
            pct = (dry / total * 100) if total > 0 else 0
            rows.append({"region": row["region"], "DryPct": round(pct, 2)})

        return pd.DataFrame(rows)
