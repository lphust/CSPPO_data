# Synthetic Case Generation Notes

The numerical experiments use nine constructed manufacturing-chain instances at three scales: small, medium, and large. The instance specifications and fixed instance seeds are listed in `data/synthetic_cases/synthetic_case_configs.csv`.

## Case Families

| Scale | Cases |
| --- | --- |
| Small | S1, S2, S3 |
| Medium | M1, M2, M3 |
| Large | L1, L2, L3 |

Each case specification follows the notation `U{x}M{y}D{z}P{k}`, where `U`, `M`, `D`, and `P` denote the numbers of upstream nodes, midstream nodes, downstream nodes, and products, respectively.

## Parameter Ranges

The parameter ranges are provided in `data/synthetic_cases/parameter_ranges.csv`. They follow the manuscript settings:

- capacities, costs, and demands preserve physical units and non-negativity;
- the ranges introduce heterogeneity across nodes, products, and routes;
- the same generation rules are used across all case sizes, while only the instance size and fixed instance seed change.

For each generated instance, product-line feasibility is checked so that every terminal product has at least one feasible upstream-midstream-downstream path. Residual demand-capacity mismatches are represented by unmet-demand variables in the decision model.

## Reproducibility Scope

This public data package records the fixed case specifications and generation ranges. Full regeneration of training logs requires the accompanying source code and the same training seeds, neural-network settings, and hardware/software environment reported in the manuscript.

