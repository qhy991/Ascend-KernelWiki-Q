---
id: technique-pr-modellink-2448
title: "PR Insight: Ascend/ModelLink #2448"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - training
  - qwen
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2448"
---

# PR Insight: Ascend/ModelLink #2448

**Title:** 问题单: 优化Qwen25-32B全参微调性能

## Overview
This PR optimizes full-parameter fine-tuning performance for Qwen2.5-32B models, improving training throughput and efficiency on Ascend NPU hardware.

## Technical Significance
Performance optimizations for large 32B models enable faster training cycles and better hardware utilization, critical for production fine-tuning workflows where time and compute costs are significant factors.

## Related
- `technique-fine-tuning` / `technique-performance-optimization` / `technique-qwen`