---
id: technique-pr-vllm-ascend-1229
title: "PR Insight: vllm-project/vllm-ascend #1229"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - refactoring
  - fused-moe
  - quantization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1229"
---

# PR Insight: vllm-project/vllm-ascend #1229

**Title:** [refactor] Refactoring AscendFusedMoE

## Overview
This PR refactors the AscendFusedMoE implementation by consolidating code into a single file and integrating branch conditions into a unified `get_fused_moe_state` function. The refactoring removes obsolete environment variables (`VLLM_ENABLE_MC2`, `USING_LCCL_COM`) and aligns parameter naming with upstream vLLM by using `enable_expert_parallel` instead of `expert_tensor_parallel_size`.

## Technical Significance
The refactoring improves code maintainability and reduces complexity by eliminating redundant environment variables and consolidating MoE logic. By aligning with vLLM's parameter conventions, this PR ensures better compatibility and reduces maintenance burden. The cleaner architecture makes it easier to understand and extend MoE functionality for Ascend.

## Related
- `technique-fused-moe`
- `technique-moe`
- `technique-expert-parallel`