# Credit Risk Decisioning and Default Prediction

## Project Overview

Financial institutions must balance two competing objectives when evaluating loan applications: expanding access to credit and controlling potential credit losses.

Approving too many high-risk applicants may increase defaults, while rejecting too many creditworthy applicants may reduce revenue and exclude qualified customers.

This project develops an end-to-end credit risk decisioning framework using the Home Credit Default Risk dataset. The goal is not only to predict repayment difficulty, but also to translate predicted default probabilities into practical lending decisions.

The final framework will support three possible outcomes:

- Approve low-risk applications
- Send uncertain applications for manual review
- Decline applications with high estimated risk

## Business Problem

The central business question is:

> How can a lender identify repayment risk while maintaining a reasonable approval rate?

The project will evaluate the trade-off between:

- Approval rate
- Default risk
- Missed lending opportunities
- Expected credit loss
- Manual-review workload

## Project Objectives

1. Analyze applicant and credit-history data
2. Identify missing values, outliers, and possible data leakage
3. Build an interpretable logistic regression baseline
4. Develop a higher-performing LightGBM model
5. Evaluate probability calibration
6. Convert predictions into approve, review, and decline decisions
7. Explain major risk drivers
8. Design a basic model-monitoring framework

## Dataset

This project uses the Home Credit Default Risk dataset.

The main application table contains one row per loan application. Additional tables contain information about previous applications, credit-bureau history, installment payments, credit-card balances, and point-of-sale loans.

Raw data will not be stored in this repository.

## Planned Models

- Logistic Regression
- Random Forest
- LightGBM

## Evaluation Metrics

- ROC-AUC
- Precision-Recall AUC
- Precision
- Recall
- Confusion Matrix
- KS Statistic
- Brier Score
- Calibration Curve
- Approval Rate
- Default Rate
- Expected Financial Loss

## Repository Structure

```text
credit-risk-decisioning/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
├── models/
├── reports/
│   └── figures/
├── dashboard/
├── tests/
├── requirements.txt
└── README.md