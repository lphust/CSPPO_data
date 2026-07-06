"""Validate the public CSPPO data package.

The script intentionally depends only on pandas and the files in this
repository, so it can be run after downloading the GitHub data package.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
CASE_CSV = ROOT / "data" / "case_study" / "case_U4M11D9P6.csv"
FIG10_CSV = ROOT / "data" / "case_study" / "Fig.10_data.csv"
FIG11_CSV = ROOT / "data" / "case_study" / "Fig.11_data.csv"
SYNTHETIC_CASES_CSV = ROOT / "data" / "synthetic_cases" / "synthetic_case_configs.csv"
PARAMETER_RANGES_CSV = ROOT / "data" / "synthetic_cases" / "parameter_ranges.csv"


def require_columns(data: pd.DataFrame, columns: set[str], path: Path) -> None:
    missing = columns.difference(data.columns)
    if missing:
        raise ValueError(f"{path} is missing columns: {sorted(missing)}")


def validate_case_csv() -> None:
    data = pd.read_csv(CASE_CSV)
    require_columns(
        data,
        {
            "case_id",
            "record_type",
            "node_id",
            "node_type",
            "node_order",
            "color_index",
            "color_id",
            "capable",
            "production_capacity",
            "inventory_capacity",
            "initial_inventory",
            "unit_production_cost",
            "changeover_cost",
            "unmet_cost",
            "demand_mean",
            "source_id",
            "target_id",
            "transport_time",
            "transport_cost",
        },
        CASE_CSV,
    )

    record_types = set(data["record_type"].dropna().unique())
    expected_record_types = {"node_color", "transport", "demand"}
    if not expected_record_types.issubset(record_types):
        raise ValueError(
            f"{CASE_CSV} record types are {sorted(record_types)}, "
            f"expected at least {sorted(expected_record_types)}"
        )

    node_rows = data[data["record_type"] == "node_color"].copy()
    node_meta = node_rows.drop_duplicates("node_id")
    counts = node_meta["node_type"].value_counts().to_dict()
    expected_counts = {"upstream": 4, "midstream": 11, "downstream": 9}
    for node_type, expected in expected_counts.items():
        actual = int(counts.get(node_type, 0))
        if actual != expected:
            raise ValueError(f"Expected {expected} {node_type} nodes, found {actual}.")

    colors = sorted(node_rows["color_index"].dropna().astype(int).unique().tolist())
    if len(colors) != 6:
        raise ValueError(f"Expected 6 product colors, found {len(colors)}.")

    if (node_rows["production_capacity"].dropna().astype(float) < 0).any():
        raise ValueError("Production capacities must be non-negative.")
    if (node_rows["inventory_capacity"].dropna().astype(float) < 0).any():
        raise ValueError("Inventory capacities must be non-negative.")


def validate_fig10() -> None:
    data = pd.read_csv(FIG10_CSV)
    require_columns(
        data,
        {"method", "case", "seed", "episode", "metric", "value", "source_file"},
        FIG10_CSV,
    )
    expected_methods = {"Random", "Rule-based", "CSPPO"}
    expected_metrics = {
        "Leader reward",
        "Average follower reward",
        "OFR",
        "Cost",
        "PCLB",
        "ACF",
    }
    if set(data["method"].unique()) != expected_methods:
        raise ValueError(f"Unexpected Fig.10 methods: {sorted(data['method'].unique())}")
    if set(data["metric"].unique()) != expected_metrics:
        raise ValueError(f"Unexpected Fig.10 metrics: {sorted(data['metric'].unique())}")


def validate_fig11() -> None:
    data = pd.read_csv(FIG11_CSV)
    require_columns(
        data,
        {
            "panel",
            "method",
            "row_order",
            "row_label",
            "row_type",
            "col_order",
            "col_label",
            "col_type",
            "value",
            "value_label",
        },
        FIG11_CSV,
    )
    expected_panels = {"capacity", "logistics_flow"}
    expected_methods = {"Random", "Rule-based", "CSPPO"}
    if set(data["panel"].unique()) != expected_panels:
        raise ValueError(f"Unexpected Fig.11 panels: {sorted(data['panel'].unique())}")
    if set(data["method"].unique()) != expected_methods:
        raise ValueError(f"Unexpected Fig.11 methods: {sorted(data['method'].unique())}")


def validate_synthetic_cases() -> None:
    cases = pd.read_csv(SYNTHETIC_CASES_CSV)
    require_columns(
        cases,
        {
            "case_id",
            "scale",
            "upstream",
            "midstream",
            "downstream",
            "products",
            "instance_specification",
            "instance_seed",
            "train_horizon",
            "eval_horizon",
        },
        SYNTHETIC_CASES_CSV,
    )
    if len(cases) != 9:
        raise ValueError(f"Expected 9 constructed cases, found {len(cases)}.")

    ranges = pd.read_csv(PARAMETER_RANGES_CSV)
    require_columns(
        ranges,
        {"parameter", "symbol", "distribution_or_value", "unit_or_meaning"},
        PARAMETER_RANGES_CSV,
    )


def main() -> None:
    validate_case_csv()
    validate_fig10()
    validate_fig11()
    validate_synthetic_cases()
    print("Validation passed.")
    print(f"Case CSV: {CASE_CSV.relative_to(ROOT)}")
    print(f"Fig.10 data: {FIG10_CSV.relative_to(ROOT)}")
    print(f"Fig.11 data: {FIG11_CSV.relative_to(ROOT)}")
    print(f"Synthetic cases: {SYNTHETIC_CASES_CSV.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

