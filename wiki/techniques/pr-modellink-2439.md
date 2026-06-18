---
id: technique-pr-modellink-2439
title: "PR Insight: Ascend/ModelLink #2439"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - training
  - fine-tuning
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2439"
---

# PR Insight: Ascend/ModelLink #2439

**Title:** 调优全参微调最优脚本，修正部分脚本bug

## Overview
This PR optimizes the full-parameter fine-tuning scripts for better performance and fixes bugs in the existing scripts, improving reliability and efficiency of complete model fine-tuning workflows.

## Technical Significance
Full-parameter fine-tuning is resource-intensive; optimized scripts ensure better hardware utilization and faster convergence, while bug fixes prevent training failures or incorrect results.

## Related
- `technique-fine-tuning` / `technique-full-parameter`