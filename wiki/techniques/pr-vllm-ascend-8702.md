---
id: technique-pr-vllm-ascend-8702
title: "PR Insight: vllm-project/vllm-ascend #8702"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - attention
  - code-refactoring
  - bailing
  - mamba
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8702"
---

# PR Insight: vllm-project/vllm-ascend #8702

**Title:** [Refactor] Replace BailingMoELinearAttention monkey-patching with PluggableLayer

## Overview
This PR replaces runtime monkey-patching of BailingMoELinearAttention methods with a proper PluggableLayer OOT (Out-of-Tree) replacement class. It creates `AscendBailingMoELinearAttention` that inherits from the upstream class and overrides `_forward`, `_prefill_and_mix_infer`, and `_decode_infer` with NPU implementations. The class is registered in `REGISTERED_ASCEND_OPS` for automatic discovery by `CustomOp.register_oot`.

## Technical Significance
This refactoring improves code maintainability and debuggability by making the replacement pattern explicit and traceable through the PluggableLayer registry. Instead of silently overwriting class methods at import time (monkey-patching), the new approach uses a clear inheritance pattern that aligns with how other ops like `AscendMultiHeadLatentAttention` are implemented. This makes the codebase more maintainable and easier to audit.

## Related
- `kernel-moe-ascendc`
- `kernel-attention-ascendc`
- `technique-operator-fusion`