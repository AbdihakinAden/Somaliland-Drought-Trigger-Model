# Validation Methodology for Model Development

## ⚠️ Validation Scope
This repository demonstrates the validation methodology used in the thesis with sample data (2020-2023 MAM/OND). The full historical impact database (85 records across 2000-2023) is not included.

## Sample Data Coverage
**Validation Period**: 2020-2023  
**Seasons**: 
- 4 years × 2 seasons = 8 seasonal observations per region
- MAM and OND seasons included

## Binary Classification Framework
**Method from thesis:**
- **Positive (Drought)**: Any documented impact in database
- **Negative (No-drought)**: No documented impacts
- **Validation**: Per region/season basis

## Validation Metrics
- **Accuracy**: Overall classification correctness
- **Precision**: Reliability of drought predictions  
- **Recall**: Ability to detect actual drought events
- **F1-Score**: Harmonic mean balancing precision/recall

## Performance Reference
**Thesis Results (Model 2 - T30) - Full 23-year validation:**
- **F1-Score**: 79.1% (average)
- **Recall**: 88% (drought detection)
- **Precision**: 72% (prediction reliability)

**Note**: These results were achieved using the full 2000-2023 impact database and are provided for reference.