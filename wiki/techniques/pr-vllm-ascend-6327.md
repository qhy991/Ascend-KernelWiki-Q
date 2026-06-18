---
id: technique-pr-vllm-ascend-6327
title: "PR Insight: vllm-project/vllm-ascend #6327"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3-vl
  - moe
  - eagle
  - vision-language
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6327"
---

# PR Insight: vllm-project/vllm-ascend #6327

**Title:** Qwen3-VL-MoE EAGLE support for vLLM-Ascend

## Overview
This PR adds support for Qwen3-VL-MoE models with EAGLE speculative decoding in vLLM-Ascend. The change was made in `vllm_ascend/spec_decode/eagle_proposer.py` to enable Eagle proposer for this model architecture.

## Technical Significance
This enables efficient inference for complex vision-language MoE models using EAGLE speculative decoding, combining the strengths of MoE scaling and Eagle's speedup techniques. The support was validated on Qwen3-VL-30B-A3B-Instruct model.

## Related
- `technique-eagle`
- `technique-moe`
- `technique-vision-language`
- `technique-qwen3`