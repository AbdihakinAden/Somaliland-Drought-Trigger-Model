"""
spi_extraction.py
Extract zonal SPI values for Somaliland regions.
"""

import geopandas as gpd
import pandas as pd
import rasterio
from rasterstats import zonal_stats


class SPIExtractor:
    def __init__(self, region_keys=("ADM1_EN", "region", "name", "NAME_1")):
        self.region_keys = region_keys

    def load_boundary(self, shp_path):
        gdf = gpd.read_file(shp_path)
        region_col = None

        for col in gdf.columns:
            if col in self.region_keys or "adm1" in col.lower():
                region_col = col
                break

        if region_col is None:
            raise ValueError("Could not find region column in boundary file.")

        gdf = gdf.rename(columns={region_col: "region"})
        return gdf[["region", "geometry"]]

    def load_spi(self, tif_path):
        with rasterio.open(tif_path) as src:
            arr = src.read(1)
            meta = {
                "crs": src.crs,
                "transform": src.transform,
                "nodata": src.nodata
            }
        return arr, meta

    def compute_zonal(self, spi_arr, meta, gdf):
        if gdf.crs != meta["crs"]:
            gdf = gdf.to_crs(meta["crs"])

        stats = zonal_stats(
            vectors=gdf,
            raster=spi_arr,
            affine=meta["transform"],
            stats=["mean", "std", "min", "max", "median", "count"],
            nodata=meta["nodata"]
        )

        out = gdf.copy()
        for key in ["mean", "std", "min", "max", "median", "count"]:
            out[key] = [s[key] for s in stats]

        return out

    def extract(self, boundary_file, tif_file, year=None, season=None):
        gdf = self.load_boundary(boundary_file)
        arr, meta = self.load_spi(tif_file)
        df = self.compute_zonal(arr, meta, gdf)

        if year is not None: df["year"] = year
        if season is not None: df["season"] = season

        return df
