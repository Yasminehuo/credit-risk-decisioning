# DECISION_LOG.md

# Decision Log — Credit Risk Decisioning

This file records only decisions that are supported by the repository or explicitly confirmed by the project owner. Historical reasoning is not invented.

## D001 — Build a dedicated credit-risk portfolio project
**Status:** Confirmed  
**Decision:** Build a new independent credit-risk project for job-search preparation.  
**Context:** The project owner had an earlier exploratory LightGBM delinquency project from College Ave but considered it insufficient as a primary portfolio project.  
**Why:** Explicitly confirmed by the project owner.  
**Ownership:** Project completed individually with ChatGPT guidance.

## D002 — Use the Home Credit Default Risk dataset
**Status:** Confirmed  
**Decision:** Use Home Credit Default Risk as the project dataset.  
**Why:** ChatGPT recommended the dataset; no separate historical rationale should be attributed to the project owner.

## D003 — Restrict baseline modeling to selected application-time features
**Status:** Confirmed implementation; rationale partially reconstructed  
**Decision:** Start the modeling workflow from 32 selected application-time raw features rather than all 122 raw columns.  
**Why:** Feature selection was made incrementally under ChatGPT guidance using the prior EDA/data-dictionary workflow.  
**Do not claim:** That the project owner independently designed the selection framework from first principles unless later confirmed.

## D004 — Split before learned preprocessing
**Status:** Repository verified  
**Decision:** Use a stratified model-train / validation / test workflow and fit learned preprocessing only on model-training data.  
**Supporting implementation:** 196,806 model-train rows, 49,202 validation rows, 61,503 test rows; target rate approximately 8.07% in each split.  
**Reason supported by repository:** Avoid preprocessing leakage and reserve test data for final reporting.

## D005 — Compare unweighted and class-weight-balanced Logistic Regression
**Status:** Repository verified; historical rationale not independently owned  
**Decision:** Train and compare standard and `class_weight="balanced"` Logistic Regression models.  
**Why:** Added under ChatGPT guidance.  
**Supporting result:** Validation ROC-AUC was effectively identical (~0.7466), while the balanced model had a much worse Brier score (0.2047 vs. 0.0687) and mean predicted score far above the observed event rate.  
**Current interpretation:** Class weighting did not improve ranking and harmed raw probability calibration.

## D006 — Preserve the unweighted Logistic Regression as the stronger baseline probability model
**Status:** Supported by results  
**Decision:** Treat unweighted Logistic Regression as the primary baseline for probability-quality comparison.  
**Why:** It matched the balanced model on ranking metrics and had far better Brier score / probability level alignment.  
**Supporting test result:** ROC-AUC 0.74946, PR-AUC 0.23669, KS 0.37101, Brier 0.06819.

## D007 — Build a reduced interpretable Logistic Regression comparison
**Status:** Repository verified; historical rationale ChatGPT-guided  
**Decision:** Compare the full unweighted baseline against a reduced interpretable Logistic Regression.  
**Why:** Added under ChatGPT guidance to explore a performance-versus-interpretability trade-off.  
**Supporting result:** Test ROC-AUC declined from 0.74946 to 0.74546.  
**Caution:** Do not present the specific feature-selection rationale as independently developed unless later reconstructed and understood.

## D008 — Create provisional low / medium / high risk bands
**Status:** Repository verified; explicitly provisional  
**Decision:** Create a three-band analytical segmentation.  
**Implementation:** High-risk cutoff chosen by validation F1; low-risk cutoff based on the 40th percentile of validation scores.  
**Current cutoffs:** ~0.341 and 0.64.  
**Supporting test result:** Observed default rates were ~2.63% low, ~7.62% medium, and ~22.23% high.  
**Important limitation:** These are not approved lending-policy thresholds and are not tied to explicit economics, approval targets, or loss constraints.

## D009 — Do not treat advanced-model work as completed
**Status:** Confirmed  
**Decision:** Random Forest, LightGBM, SHAP, calibration of an advanced model, final decision optimization, dashboarding, and monitoring remain future work.  
**Why:** No repository evidence or unpushed local work exists for these items.

## Future Decision Rule
New entries should be added only when:
1. a real technical/analytical choice has been made,
2. the reason is either documented or confirmed,
3. supporting evidence is recorded where applicable,
4. planned work is not described as completed.
