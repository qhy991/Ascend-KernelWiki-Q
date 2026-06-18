---
id: technique-pr-vllm-ascend-5800
title: "PR Insight: vllm-project/vllm-ascend #5800"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - lora
  - punica
  - fine-tuning
  - adapters
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5800"
---

# PR Insight: vllm-project/vllm-ascend #5800

**Title:** [0.13.0][Patch] AscendLoRAModelManager.__init__

## Overview
This PR adapts vLLM v0.13.0 by adding a `lora_config` parameter to the `get_punica_wrapper` function and implementing conditional logic for LoRA adapter selection. The implementation creates a new patch file `patch_lora_model_manager.py` that uses custom operators when rank < 128 and falls back to vLLM operators for higher ranks. The patch is registered in the patch initialization system to apply the changes automatically.

## Technical Significance
This adaptation enables proper LoRA support for vLLM v0.13.0 on Ascend by providing optimized custom operators for low-rank LoRA adapters while maintaining compatibility with the standard vLLM implementation for higher ranks. The rank-based selection allows efficient use of custom NPU operators for common low-rank scenarios while leveraging vLLM's implementation for edge cases. This ensures that LoRA fine-tuning and inference work correctly on Ascend hardware with the v0.13.0 codebase, providing both performance optimization and broad compatibility.

## Related
- `technique-lora`, `technique-fine-tuning`, `technique-adapters`, `technique-punica`