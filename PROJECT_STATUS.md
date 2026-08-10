# PROJECT_STATUS.md

## Project
Credit Risk Decisioning and Default Prediction

## Purpose
Independent portfolio project created for job-search preparation. The project was completed by Yasmine Huo individually with step-by-step ChatGPT guidance. It was started to build a stronger, more complete credit-risk modeling portfolio project than an earlier exploratory LightGBM project completed during the College Ave internship.

## Current Stage
**Baseline modeling completed; advanced modeling not started.**

The repository currently contains completed work through data audit, business EDA, data dictionary / leakage review, feature engineering, and Logistic Regression baseline modeling. README items such as LightGBM, Random Forest, final approve/review/decline decisioning, expected-loss optimization, SHAP, dashboarding, and monitoring remain planned rather than completed unless later repository evidence verifies otherwise.

## Verified Dataset Facts
- Dataset: Home Credit Default Risk.
- Main labeled application dataset: **307,511 rows x 122 columns**.
- Repayment-difficulty cases: **24,825**.
- Observed target rate: approximately **8.07%**.
- Raw data is intentionally not stored in the repository.

## Completed Work
- Data audit and file validation.
- Business-oriented EDA covering customer segments, affordability, age/employment profile, and external scores.
- Priority-variable data dictionary and leakage review.
- Reusable feature engineering starting from 32 selected application-time variables.
- Stratified model-train / validation / test split.
- Train-only preprocessing with numerical median imputation, missing indicators, scaling, categorical most-frequent imputation, and one-hot encoding.
- Unweighted and class-weight-balanced Logistic Regression baselines.
- Validation-based model comparison and provisional threshold analysis.
- Locked final-test evaluation.
- Full-vs-reduced interpretable Logistic Regression comparison.
- Provisional three-band risk segmentation.

## Verified Split
- Model Train: **196,806 rows**
- Validation: **49,202 rows**
- Test: **61,503 rows**
- Target rate in each split: approximately **8.07%**

## Verified Model Results

### Validation
| Model | ROC-AUC | PR-AUC | KS | Brier | Mean Predicted Score | Observed Rate |
|---|---:|---:|---:|---:|---:|---:|
| Unweighted Logistic Regression | 0.7466 | 0.2259 | 0.3642 | 0.0687 | 0.0816 | 0.0807 |
| Balanced Logistic Regression | 0.7466 | 0.2249 | 0.3645 | 0.2047 | 0.4222 | 0.0807 |

### Locked Final Test
| Model | ROC-AUC | PR-AUC | KS | Brier | Mean Predicted Score | Observed Rate |
|---|---:|---:|---:|---:|---:|---:|
| Unweighted Logistic Regression | **0.74946** | **0.23669** | **0.37101** | **0.06819** | 0.08061 | 0.08073 |
| Balanced Logistic Regression | 0.74944 | 0.23467 | 0.37094 | 0.20240 | 0.42039 | 0.08073 |

Repository-supported interpretation: class weighting produced nearly identical ranking performance but substantially worse raw probability calibration as measured by Brier score and mean predicted score relative to observed default rate.

### Full vs. Reduced Interpretable Logistic Model
| Model | Validation ROC-AUC | Test ROC-AUC | Test PR-AUC | Test KS | Test Brier |
|---|---:|---:|---:|---:|---:|
| Full Unweighted Baseline | 0.74659 | 0.74946 | 0.23669 | 0.37101 | 0.06819 |
| Reduced Interpretable Model | 0.74145 | 0.74546 | 0.23091 | 0.36448 | 0.06847 |

## Provisional Risk Segmentation
Status: **Analytical prototype / provisional; not final lending policy**

Current validation-derived cutoffs:
- Low-risk cutoff: approximately **0.341**
- High-risk cutoff: **0.64**

Current test-set segments:
| Band | Applicants | Portfolio Share | Observed Default Rate | Average Model Score |
|---|---:|---:|---:|---:|
| Low Risk | 24,679 | 40.13% | 2.63% | 0.2233 |
| Medium Risk | 26,492 | 43.07% | 7.62% | 0.4778 |
| High Risk | 10,332 | 16.80% | 22.23% | 0.7440 |

Important limitation: the high-risk threshold was selected to maximize F1 on validation data and the low-risk cutoff was based on a 40% validation-score quantile. These are **not confirmed business-policy thresholds**. The project owner does not yet consider the decision logic fully understood and should study it further before presenting it as a lending strategy.

## Ownership / Guidance Boundary
- Yasmine Huo completed the project individually.
- No other person owns the code or analysis in this repository.
- ChatGPT provided step-by-step project and technical guidance.
- Home Credit was selected based on ChatGPT recommendation.
- Selection of the initial 32 features, the reduced interpretable model, and the comparison of unweighted vs. balanced Logistic Regression were developed under ChatGPT guidance.
- Historical reasoning should not be embellished into independent decision rationales when the user did not personally form or retain that reasoning.

## Work Not Yet Completed
- Random Forest modeling
- LightGBM modeling
- advanced model tuning
- probability calibration for a selected advanced model
- SHAP / final risk-driver explanation
- final model selection
- production-quality approve / review / decline policy
- approval-rate / default-rate optimization
- expected financial-loss optimization
- dashboard / Streamlit app
- model monitoring framework
- completed `src/modeling.py`
- completed `src/evaluation.py`
- completed `src/data_processing.py`
- finalized recruiter-ready README

Presence of packages such as LightGBM, SHAP, Streamlit, Plotly, and imbalanced-learn in `requirements.txt` does not count as completed usage.

## Open Issues
1. The current README mixes completed and planned scope and should later be revised to clearly label current state.
2. The user should understand the rationale and limitations of the current class-weight and threshold experiments before using them in interviews.
3. Risk-band thresholds are not tied to explicit business economics or lending-policy constraints.
4. Advanced-model benchmarking has not started.
5. Evaluation/modeling logic remains notebook-heavy rather than extracted into reusable modules.
6. Recruiter-facing visual artifacts and final project narrative are not complete.

## Exact Next Steps
1. Review and understand the existing Logistic Regression baseline before adding a new model, especially:
   - why class weighting changes probability calibration,
   - ROC-AUC vs. PR-AUC vs. KS vs. Brier score,
   - what F1-based threshold selection means,
   - why the 40% low-risk cutoff is only provisional.
2. After the above is understood, create a LightGBM baseline using the same locked train / validation / test split and application-time feature set.
3. Compare LightGBM against the unweighted Logistic Regression on ROC-AUC, PR-AUC, KS, and Brier score.
4. Only after model comparison, decide whether probability calibration and SHAP analysis are warranted.
5. Do not build the final approve/review/decline framework until threshold logic is tied to explicit business assumptions.

## Maintenance Rule
At the beginning of future work sessions, inspect the current GitHub repository and this file before recommending the next project step. After a meaningful milestone, update this file. Update `DECISION_LOG.md` when a real technical or analytical decision is made, and update `EXPERIENCE_BANK.md` only when new recruiter-safe facts are verified.
