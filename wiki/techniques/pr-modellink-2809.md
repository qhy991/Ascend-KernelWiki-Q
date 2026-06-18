---
id: technique-pr-modellink-2809
title: "PR Insight: Ascend/ModelLink #2809"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - qwen
  - performance
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2809"
---

# PR Insight: Ascend/ModelLink #2809

**Title:** update qwen25-7b gbs

## Overview
This PR updates the global batch size (GBS) configuration for Qwen2.5 7B model training in the PyTorch backend. It optimizes batch size settings for Ascend NPU training.

## Technical Significance
Batch size tuning is critical for maximizing throughput and memory utilization on Ascend NPUs. This update improves training efficiency for Qwen2.5 7B by optimizing the batch size configuration.

## Related
- `technique-distributed-training`