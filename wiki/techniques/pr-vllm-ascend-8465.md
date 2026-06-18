---
id: technique-pr-vllm-ascend-8465
title: "PR Insight: vllm-project/vllm-ascend #8465"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - activation
  - swigluoai
  - bugfix
  - enum
  - compatibility
  - gpt-oss
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8465"
---

# PR Insight: vllm-project/vllm-ascend #8465

**Title:** [BugFix] handle enum-based MoE activation in fuse_moe/moe_mlp unquant_apply_mlp

## Overview
This PR fixes a compatibility issue in vllm_ascend/ops/fused_moe/moe_mlp.py for newer vLLM versions. In older versions, activation was a plain string like "swigluoai", but newer versions pass it as a MoEActivation enum. The previous implementation compared activation directly against the string, causing checks to always fail and fall back to the generic torch_npu.npu_swiglu path instead of the intended AscendSwigluOAIAndMul.swiglu_oai_forward path.

## Technical Significance
This fix is critical for correct inference behavior on newer vLLM versions, especially for models like gpt-oss that use activation="swigluoai" in their MoE MLP. The wrong activation path selection could produce incorrect or garbled outputs. The PR demonstrates the importance of handling both string and enum activation types for backward compatibility across vLLM versions.

## Related
- `technique-moe-optimization`
- `technique-activation-functions`
- `technique-version-compatibility`