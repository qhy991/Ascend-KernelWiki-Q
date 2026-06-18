---
id: technique-pr-vllm-ascend-3254
title: "PR Insight: vllm-project/vllm-ascend #3254"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - hccl-optimization
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3254"
---

# PR Insight: vllm-project/vllm-ascend #3254

**Title:** Add restriction conditions to the ApplyTopPTopK operator

## Overview
Add restriction conditions to the ApplyTopPTopK operator : 1 <= K <=1024

## Technical Significance
Adds restriction conditions to the ApplyTopPTopK sampling operator to prevent invalid operations and ensure correct sampling behavior.

## Related
- `hw-cube-unit`
