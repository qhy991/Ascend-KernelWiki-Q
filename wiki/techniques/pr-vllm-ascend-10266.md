---
id: technique-pr-vllm-ascend-10266
title: "PR Insight: vllm-project/vllm-ascend #10266"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - speculative-decoding
  - configuration
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10266"
---

# PR Insight: vllm-project/vllm-ascend #10266

**Title:** [BugFix] [Kimi] Fix dense draft model (Kimi-MLA) misidentified as MoE

## Overview
This PR fixes a configuration propagation issue where dense draft models were incorrectly identified as MoE models during speculative decoding setup. vLLM's configuration loading mechanism automatically propagates the main model's configuration attributes to the draft model, which caused Kimi-K2.6 based draft models (specifically `lightseekorg/kimi-k2.6-eagle3-mla`) to inherit the main model's MoE attributes even though Kimi-K2.6 is a dense model. This misidentification caused fatal errors when `VLLM_ASCEND_ENABLE_FLASHCOMM1=1` was enabled, as vLLM would attempt to execute MoE-specific optimization paths on the dense draft model.

## Technical Significance
This fix prevents critical initialization failures when using dense draft models with MoE main models in FlashComm1-enabled environments. The issue demonstrates the importance of proper model type detection in speculative decoding, where draft and main models may have different architectures. By preventing incorrect MoE attribute propagation, the fix ensures that dense draft models correctly bypass MoE-specific communication pathways, enabling proper support for Kimi-K2.6 as a draft model in Ascend environments.

## Related
- `technique-moe`
- `technique-speculative-decoding`
- `technique-flashcomm`