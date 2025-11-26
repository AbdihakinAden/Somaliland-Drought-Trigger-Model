# Data Preparation for Model Development

## ⚠️ Repository Scope
This section covers only the data processing methods used for model development. The full impact database and stakeholder engagement components are not included in this repository.

## Sample Data Coverage
**Period**: 2020-2023  
**Seasons**: 
- MAM (March-April-May) - Primary rainy season
- OND (October-November-December) - Secondary rainy season

**Regions**: Awdal, Sanaag, Sool, Togdheer, Woqooyi Galbeed

## SPI-3 Data Processing
**Source**: Global Drought Observatory (GDO) CHIRPS precipitation data

**Processing Pipeline:**
1. **Extraction**: Clip global SPI-3 to Somaliland boundary
2. **Zonal Statistics**: Calculate regional means using `all_touched=True`
3. **Standardization**: Apply FAO 0-100 hazard scale with ±2.5 cutoff
   - Formula: `SPI_norm = 100 - ((SPI_clipped - (-2.5)) / (2.5 - (-2.5)) * 100)`

## Dry Percentage Calculation
**Purpose**: Spatial drought extent component for Model 1

**Method:**
- Binary mask for SPI < -1.5
- Zonal statistics with `all_touched=True`
- Percentage of dry area per region

## Note on Historical Data
This repository includes sample data for 2020-2023 MAM/OND seasons to demonstrate the methodology. The full thesis used 23 years of data (2000-2023) for model validation.