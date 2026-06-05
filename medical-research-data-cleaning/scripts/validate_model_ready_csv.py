"""Validate model-ready train/validation CSV files.

Usage:
    python scripts/validate_model_ready_csv.py TRAIN.csv VALID.csv --id id --target outcome
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def is_float(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False


def audit(train_path: Path, valid_path: Path, id_col: str, target_col: str) -> dict:
    train = read_csv(train_path)
    valid = read_csv(valid_path)
    if not train or not valid:
        raise ValueError("Train and validation files must both contain rows.")

    train_cols = list(train[0].keys())
    valid_cols = list(valid[0].keys())
    missing_cells = {
        "train": sum(1 for row in train for value in row.values() if str(value).strip() == ""),
        "valid": sum(1 for row in valid for value in row.values() if str(value).strip() == ""),
    }

    non_numeric = {"train": [], "valid": []}
    for name, rows in [("train", train), ("valid", valid)]:
        for col in rows[0].keys():
            if col == id_col:
                continue
            if any(not is_float(str(row[col]).strip()) for row in rows):
                non_numeric[name].append(col)

    train_ids = {row[id_col] for row in train}
    valid_ids = {row[id_col] for row in valid}

    def target_counts(rows: list[dict[str, str]]) -> dict[str, int]:
        counts: dict[str, int] = {}
        for row in rows:
            counts[row[target_col]] = counts.get(row[target_col], 0) + 1
        return counts

    return {
        "train_rows": len(train),
        "valid_rows": len(valid),
        "train_columns": len(train_cols),
        "valid_columns": len(valid_cols),
        "columns_match": train_cols == valid_cols,
        "missing_cells": missing_cells,
        "non_numeric_columns": non_numeric,
        "id_overlap": len(train_ids & valid_ids),
        "train_target_counts": target_counts(train),
        "valid_target_counts": target_counts(valid),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("train_csv", type=Path)
    parser.add_argument("valid_csv", type=Path)
    parser.add_argument("--id", default="id", dest="id_col")
    parser.add_argument("--target", default="outcome", dest="target_col")
    args = parser.parse_args()

    result = audit(args.train_csv, args.valid_csv, args.id_col, args.target_col)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if (
        not result["columns_match"]
        or result["missing_cells"]["train"]
        or result["missing_cells"]["valid"]
        or result["non_numeric_columns"]["train"]
        or result["non_numeric_columns"]["valid"]
        or result["id_overlap"]
    ):
        raise SystemExit(1)


if __name__ == "__main__":
    main()

