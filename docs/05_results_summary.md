# Model Development Results Summary

## ⚠️ Repository Scope
This summary describes the model performance achieved in the complete thesis research. This repository contains the model development code with sample data (2020-2023 MAM/OND) but not the full validation dataset.

## Sample Data Context
**Demonstration Period**: 2020-2023  
**Seasons**: MAM and OND (8 seasonal observations per region)  
**Coverage**: Includes the severe 2020-2023 drought sequence documented in the thesis

## Key Model Development Findings

### Performance Metrics (Thesis Results - Full 23-year validation)
**Model 2 (Memory Effect) with T30 threshold:**
- **F1-Score**: 79.1% (average across regions)
- **Recall**: 88% (drought detection rate)
- **Precision**: 72% (prediction reliability)

### Model Contributions Demonstrated with Sample Data
1. **Memory Effect Enhancement**: Visible in 2020-2023 multi-season drought sequence
2. **Multi-dimensional Approach**: Combined SPI intensity + spatial extent
3. **Seasonal Patterns**: Captures both MAM and OND season characteristics

### Technical Innovations
- **FAO Standardization**: SPI-3 to 0-100 hazard scale
- **Dry Percentage**: Spatial extent quantification for 2020-2023
- **Residual Dryness Index**: Temporal memory effects across consecutive seasons

## Implementation Note
The models in this repository demonstrate the methodological approach using 2020-2023 sample data. For operational deployment with full historical validation, refer to the complete thesis.