---
id: technique-pr-vllm-ascend-5189
title: "PR Insight: vllm-project/vllm-ascend #5189"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - refactoring
  - all-reduce
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5189"
---

# PR Insight: vllm-project/vllm-ascend #5189

**Title:** [Refactor][MoE] Reuse vLLM's all_reduce logic

## Overview
This PR refactors the MoE implementation by moving all_reduce logic into `AscendFusedMoE.forward` and reusing vLLM's community all_reduce implementation instead of maintaining custom Ascend-specific logic in the prepare/finalize stages.

## Technical Significance
Reusing community all_reduce logic reduces code duplication and maintenance burden. This aligns the Ascend MoE implementation with upstream vLLM patterns while maintaining performance benefits from Ascend-specific kernels elsewhere in the pipeline.

## Related
- technique-moe
- technique-hccl-optimization
- technique-code-reuse