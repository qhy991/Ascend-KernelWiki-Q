---
id: technique-pr-vllm-ascend-915
title: "PR Insight: vllm-project/vllm-ascend #915"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - qwen3
  - model-support
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/915"
---

# PR Insight: vllm-project/vllm-ascend #915

**Title:** [Model][0.7.3] Add support for Qwen3-MoE model

## Overview
This PR adds support for the Qwen3-MoE model to vllm-ascend v0.7.3, including model implementation and MoE operator adaptations. The support has been validated through offline and online inference tests plus accuracy verification.

## Technical Significance
Qwen3-MoE represents an important MoE architecture addition to vllm-ascend's supported models. MoE models provide better parameter efficiency and computational efficiency, enabling larger models to run efficiently on Ascend hardware through expert parallelism.

## Related
- `kernel-moe`
- `kernel-qwen3`
- `technique-expert-parallel`