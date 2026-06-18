---
id: technique-pr-vllm-ascend-1856
title: "PR Insight: vllm-project/vllm-ascend #1856"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - qwen
  - data-parallel
  - all2all
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1856"
---

# PR Insight: vllm-project/vllm-ascend #1856

**Title:** [MoE][Dist] Fix Qwen MoE accuracy bug in DP scenario

## Overview
This PR fixes a Qwen MoE accuracy bug in data parallel scenarios. The issue arises because vLLM's FusedMoE uses All2AllManager with a default branch using Multicast dispatch and all_reduce combine, which are not implemented in vLLM-Ascend, leading to empty operations and accuracy issues.

## Technical Significance
Critical bugfix for MoE distributed training/inference. The temporary workaround fixes accuracy by handling missing All2All algorithm implementations, with a note that refactoring all2all in vLLM-Ascend would be a better long-term solution.

## Related
- `technique-moe`
- `technique-all2all`
- `technique-data-parallel`
- `technique-qwen-moe`