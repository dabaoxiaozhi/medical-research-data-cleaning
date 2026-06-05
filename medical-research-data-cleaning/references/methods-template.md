# Manuscript Methods Template

Use this generic template for a manuscript data cleaning and feature engineering section. Replace bracketed content with study-specific details in the project workspace, not inside the skill.

## Data Cleaning and Feature Engineering

The study dataset was derived from retrospective medical research data containing subject identifiers, candidate predictors, and a predefined outcome. Subject identifiers were checked for uniqueness, and outcome-derived variables were excluded from the predictor set.

Before model development, variables were classified according to their role and data type, including identifier and outcome variables, continuous measurements, reporting-limit numeric variables, qualitative or semi-quantitative variables, clinically retained high-missingness variables, and default exclusion candidates. Variables with high missingness were excluded unless they were clinically important or their missingness was considered informative.

Values containing reporting-limit symbols were parsed into numeric thresholds, and corresponding limit indicators were generated. Qualitative and semi-quantitative results were encoded using predefined clinical rules. Variables representing the same clinical concept were merged according to prespecified source-priority rules.

When missingness was considered clinically informative, unmeasured values were handled using a clinically justified fixed value and a measurement indicator. Otherwise, missing values were imputed after splitting the data.

The dataset was split into training and validation sets using a prespecified design. All learned preprocessing parameters, including imputation values, encoding categories, outlier replacement values, and scaling parameters, were fitted on the training set only and then applied to the validation set.

Continuous variables were imputed using the training-set mean when approximately normally distributed and the training-set median otherwise. Categorical and ordinal variables were imputed using mode or a clinically justified fixed value. Missingness indicators were added for variables with clinically meaningful or prespecified missingness.

Outliers were handled using fixed clinical and physiologic rules. Clearly impossible values were replaced using training-set-fitted imputation values, and outlier indicators were created. Winsorization was not performed in the primary dataset unless prespecified.

Categorical variables were one-hot encoded using categories fitted on the training set only. Separate model-ready datasets were generated as needed for tree-based models and scale-sensitive models.

