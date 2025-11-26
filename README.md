# Somaliland Drought Trigger Model - Model Development

## ⚠️ Repository Scope
**This repository contains ONLY the model development component** of the Master's Thesis:

> "Building the Foundation: A Trigger Model for Anticipatory Drought Action in Somaliland"

### What's Included ✅
- Drought trigger model development (Models 0, 1, 2)
- SPI-3 data processing and standardization
- Dry percentage extraction methodology
- Model validation framework
- **Sample data**: MAM and OND seasons (2020-2023)

### What's Not Included ❌
- Full historical impact database (85 records from 2000-2023)
- Stakeholder co-design process
- Complete operational framework
- Policy recommendations and implementation guidelines

## Sample Data Coverage
- **Period**: 2020-2023
- **Seasons**: MAM (March-May) and OND (October-December)
- **Regions**: All 5 Somaliland administrative regions
- **Includes**: The severe 2020-2023 drought sequence documented in the thesis

## Quick Start
```bash
# Install dependencies
pip install -r requirements.txt

# Run SPI standardization with sample data
python src/spi_standardization.py

# Run dry percentage extraction with sample data
python src/dry_percentage_extraction.py
