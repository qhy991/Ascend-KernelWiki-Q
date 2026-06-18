---
id: technique-pr-vllm-ascend-3769
title: "PR Insight: vllm-project/vllm-ascend #3769"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - sfa
  - mla
  - deepseek
  - refactoring
  - chunk-prefill
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3769"
---

# PR Insight: vllm-project/vllm-ascend #3769

**Title:** [Model][3/N] Refactor sfa into mla and remove deepseek_v3_2.py

## Overview
This is the final PR in a three-part refactoring series that converts SFA (Structured Fused Attention) implementations to MLA (Multi-Head Latent Attention) and removes the standalone `deepseek_v3_2.py` model file. The changes include removing 976 lines from `vllm_ascend/attention/sfa_v1.py`, adding 535 lines, deleting 658 lines from `vllm_ascend/models/deepseek_v3_2.py`, and consolidating DeepSeek v3.2 logic into MLA-based implementations via patches.

## Technical Significance
This consolidation reduces code duplication and maintenance burden by unifying SFA and MLA implementations. After this PR, all DeepSeek-related code uses MLA, enabling chunk-prefill with correct accuracy for DeepSeek V3.2 models. The refactoring reduces total code size while improving correctness and maintainability across different attention implementations.

## Related
- `technique-mla`
- `technique-sfa`
- `technique-refactoring`