# CSPPO Data Repository

This repository contains the public data package for the manuscript:

**CSPPO: A Multi-Agent Reinforcement Learning Method for Production Capacity Allocation in Manufacturing Industry Chains**

The package is prepared to support verification and reuse of the constructed numerical instances and the automotive-glass case study used in the revised manuscript.

Repository link to use after publication:

```text
https://github.com/lphust/CSPPO_data
```

Replace `your-account` with the final GitHub account name after creating the repository.

## Contents

```text
data/
  case_study/
    case_U4M11D9P6.csv       Automotive-glass case description.
    Fig.10_data.csv          Seed-level case-study metric data for Fig. 10.
    Fig.11_data.csv          Heatmap data for capacity utilization and logistics flow in Fig. 11.
  synthetic_cases/
    synthetic_case_configs.csv   Nine constructed S/M/L simulation cases.
    parameter_ranges.csv         Parameter distributions used to generate numerical cases.
docs/
  data_dictionary.md
  synthetic_case_generation.md
  repository_note_for_response.md
scripts/
  summarize_case_data.py
  validate_case_data.py
```

## Case Study

The real-world case is denoted as `U4M11D9P6`, meaning:

- 4 upstream nodes,
- 11 midstream nodes,
- 9 downstream nodes,
- 6 product colors.

The case CSV uses three record types:

- `node_color`: node attributes, product-color capability, production capacity, inventory, costs, and demand-related fields;
- `transport`: feasible point-to-point transport links between adjacent layers;
- `demand`: downstream demand information by market node and product color.

## Constructed Simulation Cases

The synthetic cases used for numerical experiments are listed in `data/synthetic_cases/synthetic_case_configs.csv`. The generation ranges are listed in `data/synthetic_cases/parameter_ranges.csv`. Fixed instance seeds are provided so that the same case specifications can be regenerated in the accompanying codebase.

## Quick Validation

Install the only required Python dependency:

```bash
pip install -r requirements.txt
```

Validate the repository contents:

```bash
python scripts/validate_case_data.py
```

Print a short case summary:

```bash
python scripts/summarize_case_data.py
```

Expected case-study counts are `4` upstream nodes, `11` midstream nodes, `9` downstream nodes, and `6` product colors.

## Notes

The data files are intended for academic verification and reuse. The repository contains compact public data and figure-ready summaries, not large intermediate training logs or trained model checkpoints.

