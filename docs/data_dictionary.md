# Data Dictionary

## `data/case_study/case_U4M11D9P6.csv`

This file describes the automotive-glass industrial-chain case `U4M11D9P6`.

### Common columns

| Column | Description |
| --- | --- |
| `case_id` | Case identifier. |
| `record_type` | Record type: `node_color`, `transport`, or `demand`. |
| `node_id` | Node identifier for node and demand records. |
| `node_name` | Human-readable node name. |
| `node_type` | Chain layer: `upstream`, `midstream`, or `downstream`. |
| `node_order` | Integer order used by the simulation environment and heatmaps. |
| `location` | Node location. |
| `role` | Operational role of the node. |
| `notes` | Brief explanation of the record. |

### Product and node-capability columns

| Column | Description |
| --- | --- |
| `color_index` | Product-color index. |
| `color_id` | Product-color identifier. |
| `color_name` | Product-color name. |
| `capable` | Whether the node can produce or serve the product color. |
| `production_capacity` | Production or service capacity. |
| `inventory_capacity` | Inventory capacity. |
| `initial_inventory` | Initial inventory. |
| `unit_production_cost` | Unit production cost. |
| `changeover_cost` | Cost of product changeover. |
| `unmet_cost` | Penalty cost for unmet demand. |

### Demand columns

| Column | Description |
| --- | --- |
| `demand_mean` | Mean demand for a downstream node and product color. |
| `demand_std` | Demand standard deviation. |

### Transport columns

| Column | Description |
| --- | --- |
| `source_id` | Source node of a feasible transport link. |
| `target_id` | Target node of a feasible transport link. |
| `transport_time` | Transport lead time. |
| `transport_cost` | Unit transport cost. |

## `data/case_study/Fig.10_data.csv`

Long-form seed-level data used for Fig. 10.

| Column | Description |
| --- | --- |
| `method` | Compared method: `Random`, `Rule-based`, or `CSPPO`. |
| `case` | Case identifier. |
| `seed` | Seed index. |
| `episode` | Aggregation label; `seed_mean` indicates one value per seed. |
| `metric` | Metric name, including `OFR`, `Cost`, `PCLB`, and `ACF`. |
| `value` | Metric value. |
| `source_file` | Relative source descriptor used when the public CSV was assembled. |

## `data/case_study/Fig.11_data.csv`

Long-form heatmap data used for Fig. 11.

| Column | Description |
| --- | --- |
| `panel` | Heatmap panel: `capacity` or `logistics_flow`. |
| `method` | Compared method. |
| `row_order`, `col_order` | Matrix row and column indices. |
| `row_label`, `col_label` | Matrix row and column labels. |
| `row_type`, `col_type` | Node layer or column category. |
| `value` | Heatmap value. Blank values indicate infeasible node-color pairs or transport links. |
| `value_label` | Value definition. |

For the capacity panel, values are scaled production-capacity utilization values used in the manuscript heatmap. For the logistics-flow panel, values are mean source-target transport flows.

