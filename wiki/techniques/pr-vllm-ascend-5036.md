---
id: technique-pr-vllm-ascend-5036
title: "PR Insight: vllm-project/vllm-ascend #5036"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ut
  - moe
  - moe-mlp
  - cumsum
  - testing
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5036"
---

# PR Insight: vllm-project/vllm-ascend #5036

**Title:** [UT]Ut for function cumsum_group_list in moe_mlp (ref #5025)

## Overview
This PR adds unit tests for the cumsum_group_list function in moe_mlp, which is related to the precision issues fixed in PR #5025.

## Technical Significance
Improves test coverage for the cumsum-to-count conversion logic, preventing future regressions in quantized MoE MLP precision.

## Related
- `kernel-moe-mlp`
- `technique-quantization`
- `kernel-fused-moe`