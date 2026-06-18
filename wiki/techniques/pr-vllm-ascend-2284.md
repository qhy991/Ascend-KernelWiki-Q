---
id: technique-pr-vllm-ascend-2284
title: "PR Insight: vllm-project/vllm-ascend #2284"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - custom-ops
  - rmsnorm
  - registration
  - out-of-tree
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2284"
---

# PR Insight: vllm-project/vllm-ascend #2284

**Title:** [CustomOp] Register RMSNorm instead of overwrite forward_oot

## Overview
This PR changes the custom operator registration approach for RMSNorm from overwriting `forward_oot` to using `CustomOp.register_oot`. The implementation uses `CustomOp.register_oot(_decorated_op_cls=AscendRMSNorm, name="RMSNorm")` for proper registration and modifies `vllm_ascend/ops/layernorm.py` accordingly.

## Technical Significance
This change improves the custom operator registration pattern by using the official vLLM API instead of method overwriting, which is more maintainable and aligns with vLLM best practices. The registration approach ensures better integration with the custom operator framework and reduces potential conflicts with other extensions.

## Related
- `kernel-layernorm-ascendc`, `technique-custom-ops`, `technique-operator-registration`, `kernel-rmsnorm-ascendc`