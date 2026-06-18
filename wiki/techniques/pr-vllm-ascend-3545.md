---
id: technique-pr-vllm-ascend-3545
title: "PR Insight: vllm-project/vllm-ascend #3545"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - hccl-optimization
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3545"
---

# PR Insight: vllm-project/vllm-ascend #3545

**Title:** [main] v_proj combining transpose and matmul

## Overview
v_proj combining transpose and matmul

## Technical Significance
Optimizes v_proj by combining transpose and matmul operations for improved performance in attention mechanisms.

## Related
- `hw-cube-unit`
