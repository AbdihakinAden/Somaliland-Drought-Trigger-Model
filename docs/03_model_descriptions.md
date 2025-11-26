# Drought Trigger Models - Development

## ⚠️ Model Development Focus
This repository implements the three drought detection models from the thesis using sample data (2020-2023 MAM/OND). The operational Ready-Set-Go! framework and stakeholder co-designed actions are not included.

## Model 0: Baseline SPI-3
- **Input**: Normalized SPI-3 values only
- **Purpose**: Establish performance baseline
- **Method**: Simple threshold-based detection

## Model 1: Two-Tier Drought Hazard Index (DHI)
- **Formula**: `DHI = 0.7 × SPI_norm + 0.3 × Dry_Percentage`
- **Innovation**: Combines intensity + spatial extent

## Model 2: Memory Effect (Residual Dryness Index)
- **Formula**: `RDI_t = DHI_t + [γ × DHI_{t-1}] if DHI_{t-1} > T`
- **Memory Coefficient**: γ = 0.2
- **Innovation**: Incorporates carry-over drought stress

## Sample Data Application
**Demonstration Period**: 2020-2023 MAM/OND seasons  
**Memory Effect**: Applied across consecutive seasons within the sample period

## Threshold Optimization
- **Tested**: T25, T30, T40
- **Selected**: T30 based on F1-Score/Recall balance
- **Note**: Full validation used 23 years of impact data (not included)