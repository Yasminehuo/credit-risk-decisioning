# EXPERIENCE_BANK.md

# Credit Risk Decisioning — Verified Experience Bank

## Status
**In Progress — Baseline modeling completed; advanced modeling not started**

## Context
Independent portfolio project for job-search preparation. Completed individually by Yasmine Huo with step-by-step ChatGPT guidance.

## Recruiter-Safe Project Summary
Built an end-to-end credit-risk modeling workflow on Home Credit Default Risk application data, covering data audit, business-oriented EDA, leakage review, reusable feature engineering, train/validation/test preprocessing, interpretable Logistic Regression baselines, model evaluation, and provisional risk segmentation.

## Verified Facts

### Data
- Home Credit Default Risk application dataset.
- 307,511 labeled applications.
- 122 original columns in the primary training table.
- 24,825 repayment-difficulty cases.
- Approximately 8.07% target rate.

### Data Understanding / EDA
- Completed a data-quality audit.
- Completed business-oriented EDA focused on customer segments, affordability, age/employment profile, and external credit scores.
- Completed a priority-variable data dictionary and leakage review.
- Do not claim a manual dictionary for every one of the 122 columns.

### Feature Engineering
- Began baseline modeling from 32 selected application-time raw variables.
- Built reusable feature engineering in `src/feature_engineering.py`.
- Created features covering:
  - age / employment history,
  - affordability,
  - household-per-person ratios,
  - loan structure,
  - employment stability,
  - external-score aggregates,
  - bureau inquiries,
  - missingness.
- Implemented special-value handling, division-by-zero protection, sanity checks, and missingness features.

### Modeling Workflow
- Used a stratified train / validation / test workflow:
  - 196,806 model-train rows,
  - 49,202 validation rows,
  - 61,503 test rows.
- Fit learned preprocessing on model-training data only.
- Used median imputation, numerical missing indicators, standardization, most-frequent categorical imputation, and one-hot encoding.
- Compared unweighted and class-weight-balanced Logistic Regression.
- Compared a full unweighted baseline with a reduced interpretable Logistic Regression.

### Verified Final-Test Results
Primary unweighted Logistic Regression:
- ROC-AUC: **0.74946**
- PR-AUC: **0.23669**
- KS: **0.37101**
- Brier score: **0.06819**

Reduced interpretable Logistic Regression:
- Test ROC-AUC: **0.74546**
- Test PR-AUC: **0.23091**
- Test KS: **0.36448**
- Test Brier score: **0.06847**

### Provisional Risk Segmentation
Analytical three-band segmentation only; not a final lending policy.

Test-set observed default rates:
- Low Risk: **2.63%**
- Medium Risk: **7.62%**
- High Risk: **22.23%**

Do not claim:
- that these thresholds were approved by a lender,
- that the bands represent production underwriting decisions,
- that there was real financial impact,
- that approval/review/decline policy optimization is complete.

## Ownership Boundary
Safe claims:
- Independently completed the code and analysis.
- ChatGPT provided project and technical guidance.
- No teammate or collaborator owns repository code or analysis.

Do not claim:
- that all technical choices were independently originated without guidance,
- historical reasoning that the project owner does not remember or understand,
- business impact on a real lender or portfolio.

## Completed vs. Planned

### Completed
- Data audit
- Business EDA
- Priority-variable data dictionary
- Leakage review
- Feature engineering
- Reusable feature-engineering module
- Stratified train/validation/test split
- Preprocessing pipeline
- Unweighted Logistic Regression
- Balanced Logistic Regression
- Validation comparison
- Locked test evaluation
- Reduced interpretable Logistic comparison
- Provisional risk bands

### Planned / Not Completed
- Random Forest
- LightGBM
- advanced tuning
- advanced-model calibration
- SHAP analysis
- final model selection
- expected-loss optimization
- final approve/review/decline policy
- dashboard / Streamlit app
- monitoring framework
- production deployment

## Current Resume-Safe Bullets

- Built a credit-risk modeling workflow on 307K+ Home Credit applications, combining data-quality checks, business-oriented EDA, leakage review, and reusable feature engineering for affordability, employment, external-score, bureau-inquiry, and missingness signals.
- Developed a stratified train/validation/test Logistic Regression pipeline with train-only preprocessing and evaluated ROC-AUC, PR-AUC, KS, and Brier score, achieving **0.749 test ROC-AUC** on the unweighted baseline.
- Compared full and reduced interpretable Logistic Regression models and created provisional risk bands whose observed test-set default rates ranged from **2.63% in the low-risk segment to 22.23% in the high-risk segment**.

## Interview Caution
Before using class weighting, threshold selection, or risk-band logic in a deep-dive interview, the project owner should be able to explain:
- ROC-AUC vs. PR-AUC,
- KS statistic,
- Brier score / calibration,
- why class weighting distorted probability levels,
- why F1-based thresholds are not automatically lending-policy thresholds,
- why a 40% low-risk quantile is an analytical assumption rather than a business rule.
