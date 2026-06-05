# Medical Research Data Cleaning Skill

[中文说明 / Chinese README](README.zh-CN.md)

This repository contains a disease-agnostic Codex skill for preparing retrospective medical research datasets for statistical analysis or machine-learning modeling.

The installable skill folder is:

```text
medical-research-data-cleaning/
```

## What It Does

- Profiles clinical, laboratory, registry, or EHR datasets.
- Classifies variables for cleaning and modeling.
- Parses reporting-limit values such as below-limit or above-limit results.
- Handles clinically informative missingness when justified.
- Supports same-concept variable merges.
- Applies leakage-safe train/validation preprocessing.
- Creates tree-model and linear-model ready datasets.
- Generates audit reports and manuscript methods text.

## Install Locally

Copy the inner skill folder into your Codex skills directory:

```powershell
Copy-Item -Recurse .\medical-research-data-cleaning $env:USERPROFILE\.codex\skills\
```

Then restart or refresh Codex so the skill metadata is discovered.

## Repository Layout

```text
medical-research-data-cleaning/
  SKILL.md
  agents/openai.yaml
  references/
  scripts/
```

Only the inner `medical-research-data-cleaning/` directory is the skill. This outer README is for GitHub publication.

## Privacy Note

Do not publish patient-level data, private field lists, raw datasets, cleaned datasets, or project-specific variable dictionaries in this repository. Use synthetic examples only.

## Disclaimer

This skill supports reproducible research data preprocessing. It does not provide medical advice and should be reviewed by clinical and statistical collaborators before manuscript submission or deployment.
