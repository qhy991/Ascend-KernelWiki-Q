---
id: technique-pr-vllm-ascend-3409
title: "PR Insight: vllm-project/vllm-ascend #3409"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - moe
  - hccl-optimization
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3409"
---

# PR Insight: vllm-project/vllm-ascend #3409

**Title:** [EPLB]Record expert map without dynamic eplb.

## Overview
1.Record expert map without dynamic eplb.

## Technical Significance
Records expert mappings without dynamic EPLB to simplify MoE routing logic and improve performance.

## Related
- `technique-moe-routing`
