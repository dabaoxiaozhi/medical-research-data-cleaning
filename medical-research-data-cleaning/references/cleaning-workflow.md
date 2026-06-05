# Medical Research Data Cleaning Workflow Reference

## Expected Inputs

- A de-identified or research-approved table in CSV or Excel format.
- A unique subject, encounter, or record identifier.
- A clearly defined outcome or analysis target when modeling is requested.
- A data dictionary or clinical explanation when variable meanings are ambiguous.

## Recommended Output Structure

- `data_clean/`: cleaned and model-ready datasets.
- `results/`: missingness, parsing, outlier, split, encoding, and validation reports.
- `docs/`: methods notes, work records, data dictionaries, and assumptions.
- `scripts/`: reproducible processing scripts.

## Variable Classification

Classify variables before transformation:

- identifier and outcome variables.
- continuous clinical or laboratory measurements.
- numeric values with reporting-limit symbols.
- semi-quantitative variables.
- qualitative categorical variables.
- clinically retained high-missingness variables.
- default exclusion candidates.

Keep the classification table in the project workspace, not in this skill.

## Reporting-Limit Values

Values such as below-limit or above-limit results should be treated as censored/reporting-limit values.

Recommended outputs:

- numeric threshold value.
- limit indicator: below limit, exact value, or above limit.
- optional raw-value audit column, excluded from final model-ready data.

## Informative Missingness

In retrospective medical data, a test may be missing because clinicians did not order it. This can carry clinical information.

Use a clinically informed approach only when justified:

- fixed normal or low-risk value for unmeasured results.
- measurement indicator.
- source indicator when multiple measurement contexts exist.
- clear documentation of the assumption.

If the clinical meaning is uncertain, use routine imputation and document uncertainty.

## Same-Concept Merges

Merge fields only when clinical review or a data dictionary confirms that they represent the same concept.

Recommended outputs:

- merged value.
- source indicator.
- missing indicator.
- audit report showing source usage.

Apply the same merge rules to all data splits.

## Missing Imputation

Fit imputation on training data only:

- mean for approximately normal continuous variables.
- median for skewed continuous variables.
- mode or fixed clinical-normal value for categorical/ordinal variables.
- constant value for flags when clinically meaningful.

Add missing indicators only when missingness is clinically meaningful, prespecified, or above a project-defined threshold.

## Outlier Handling

Outlier processing should be conservative:

- replace physiologically impossible values using training-fitted imputation values.
- add outlier indicators for changed values.
- retain extreme values that may reflect true severe disease.
- avoid default winsorization.

Keep a detailed outlier report with split, ID, variable, original value, replacement value, rule, and action.

## Model-Ready Datasets

Create separate outputs when needed:

- tree-model dataset: numeric values and one-hot encoded categoricals, no scaling.
- linear-model dataset: same encoding plus train-fitted standardization for continuous numeric variables.

Do not standardize IDs, outcomes, binary indicators, one-hot columns, missing indicators, measurement indicators, outlier indicators, or reporting-limit flags.

