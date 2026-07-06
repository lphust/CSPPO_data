"""Print a compact summary of the public CSPPO data package."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
CASE_CSV = ROOT / "data" / "case_study" / "case_U4M11D9P6.csv"
FIG10_CSV = ROOT / "data" / "case_study" / "Fig.10_data.csv"
FIG11_CSV = ROOT / "data" / "case_study" / "Fig.11_data.csv"
SYNTHETIC_CASES_CSV = ROOT / "data" / "synthetic_cases" / "synthetic_case_configs.csv"


def main() -> None:
    case_data = pd.read_csv(CASE_CSV)
    node_rows = case_data[case_data["record_type"] == "node_color"].copy()
    node_meta = node_rows.drop_duplicates("node_id")
    transport_rows = case_data[case_data["record_type"] == "transport"]
    demand_rows = case_data[case_data["record_type"] == "demand"]

    print("Case study: U4M11D9P6")
    print("Node counts:")
    for node_type, count in node_meta["node_type"].value_counts().sort_index().items():
        print(f"  {node_type}: {count}")
    print(f"Product colors: {node_rows['color_index'].dropna().astype(int).nunique()}")
    print(f"Transport links: {len(transport_rows)}")
    print(f"Demand records: {len(demand_rows)}")

    fig10 = pd.read_csv(FIG10_CSV)
    print("\nFig.10 seed-level records:")
    print(fig10.groupby(["method", "metric"]).size().unstack(fill_value=0).to_string())

    fig11 = pd.read_csv(FIG11_CSV)
    print("\nFig.11 heatmap records:")
    print(fig11.groupby(["panel", "method"]).size().unstack(fill_value=0).to_string())

    synthetic_cases = pd.read_csv(SYNTHETIC_CASES_CSV)
    print("\nConstructed simulation cases:")
    print(
        synthetic_cases[
            ["case_id", "scale", "instance_specification", "instance_seed"]
        ].to_string(index=False)
    )


if __name__ == "__main__":
    main()

