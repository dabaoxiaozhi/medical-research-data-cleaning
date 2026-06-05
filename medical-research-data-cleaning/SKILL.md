---
name: medical-research-data-cleaning
description: Use when preparing retrospective medical research datasets for machine-learning or statistical modeling, including raw data protection, variable classification, detection-limit parsing, clinically informative missingness, train/validation splitting, imputation, outlier handling, categorical encoding, scaling, audit reports, and manuscript-ready methods notes. This skill is disease-agnostic and must not include private project variables or patient-level data.
---

# Medical Research Data Cleaning

Use this skill for retrospective clinical, laboratory, registry, or EHR datasets that need reproducible cleaning and feature engineering before statistical analysis or machine-learning modeling.

## Privacy And Scope

- Do not include patient-level data, private field lists, original variable names, hospital identifiers, or project-specific outcomes inside the skill.
- Keep the skill disease-agnostic. Adapt disease-specific details only in the user workspace outputs.
- Never modify raw data. Write cleaned data, reports, logs, and model-ready files to new output paths.
- Do not invent outcome variables. If the target is missing or ambiguous, ask for the definition.

## Core Principles

- Separate rule-based cleaning from learned preprocessing.
- Split train/validation before fitting imputation, encoders, scalers, feature selectors, resampling, or model hyperparameters.
- Fit learned preprocessing parameters on the training set only and apply them to validation/test sets.
- Preserve auditability with variable classification tables, missingness reports, outlier reports, and concise work records.
- Prefer clinically interpretable transformations over opaque preprocessing unless a sensitivity analysis justifies a complex method.

## Workflow

1. **Profile the data**
   - Identify ID, outcome, demographics, measurements, qualitative variables, and likely duplicate/same-concept fields.
   - Report dimensions, target distribution, duplicate IDs, missingness, parseability, detection-limit symbols, and suspicious extremes.

2. **Classify variables**
   - Use categories such as identifier/outcome, continuous measurement, detection-limit numeric, semi-quantitative, qualitative categorical, clinically retained high-missingness, and default exclusion candidate.
   - Exclude high-missingness variables by default unless clinically important or informative missingness is justified.

3. **Apply rule-based cleaning**
   - Normalize missing tokens and text artifacts.
   - Parse numeric values with reporting-limit symbols.
   - Encode fixed qualitative or semi-quantitative values using documented clinical rules.
   - Merge same-concept variables only with clinical or data-dictionary justification.

4. **Split data**
   - Use a design appropriate to the study, such as stratified train/validation split for a binary outcome.
   - Preserve split IDs so later feature-engineering revisions can reuse the same split.

5. **Handle missing values after split**
   - Use training-set mean for approximately normal continuous variables.
   - Use training-set median for skewed or heavy-tailed continuous variables.
   - Use mode or a justified fixed clinical-normal value for categorical or ordinal variables.
   - Add missingness or measurement indicators only when clinically meaningful or prespecified.

6. **Handle outliers**
   - Apply fixed clinical and physiologic rules where defensible.
   - Replace clearly impossible values with training-fitted imputation values and add outlier indicators.
   - Do not winsorize by default; preserve extreme but clinically plausible values.

7. **Create model-ready datasets**
   - One-hot encode string categorical variables using training-set categories only.
   - Produce a tree-model version without scaling.
   - Produce a linear/SVM/KNN version with training-fitted standardization for continuous numeric features.

8. **Handoff**
   - Report files created or modified, checks run, risks, assumptions, and incomplete steps.
   - Write or update a concise work record in `docs/`.

## References

- Read `references/cleaning-workflow.md` for detailed implementation guidance.
- Read `references/methods-template.md` when drafting manuscript methods.
- Use `scripts/validate_model_ready_csv.py` to validate final train/validation CSV files.

