---
id: tool-aoe-autotuning
title: "Auto-Tuning with AOE"
type: wiki-tool
tags:
  - autotuning
confidence: inferred
sources: []
---

# Auto-Tuning with AOE

The Ascend Optimization Engine (AOE) is a tool that automates the search for optimal kernel configurations, specifically tiling strategies, on Ascend NPUs.

## Core Concepts

AOE uses a Knowledge Base (KB) and a search algorithm to explore different tiling sizes (e.g., how much data to load into the Unified Buffer per loop). The goal is to maximize AI Core utilization and minimize memory access latency.

## Tuning Modes

1. **Operator Tuning**: Focuses on a single operator. AOE compiles the operator with various tiling parameters, measures execution time, and saves the best parameters to the custom knowledge base.
2. **Subgraph Tuning**: Optimizes the fusion of multiple operators within a computation graph, finding the best combination of memory reuse and parallel execution.
3. **Gradient Tuning**: Adjusts the scheduling of gradient calculations during distributed training to overlap communication with computation effectively.

## Example Workflow

To tune an operator using AOE:

```bash
aoe --job_type=1 --model=my_model.om --tune_ops="MyCustomOp" --output=./tuning_results
```
The results are saved in a JSON file that can be ingested by the AscendC compiler to apply the optimized tiling strategy automatically in future runs.
