---
id: technique-pr-modellink-2277
title: "PR Insight: Ascend/ModelLink #2277"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - inference
  - lora
  - distributed
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2277"
---

# PR Insight: Ascend/ModelLink #2277

**Title:** 修复(q)Lora多机推理开启DP的问题

## Overview
Fixes an issue with multi-machine inference when data parallelism (DP) is enabled for (q)LoRA (Quantized) Low-Rank Adaptation models. The bug was affecting distributed inference scenarios.

## Technical Significance
Bugfix that enables correct distributed inference for (q)LoRA models with data parallelism. This is important for scaling inference throughput across multiple machines while maintaining LoRA-specific weight injection and quantization handling.

## Related
- technique-hccl-optimization