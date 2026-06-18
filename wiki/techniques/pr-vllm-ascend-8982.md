---
id: technique-pr-vllm-ascend-8982
title: "PR Insight: vllm-project/vllm-ascend #8982"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - rope
  - sfa
  - attention
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8982"
---

# PR Insight: vllm-project/vllm-ascend #8982

**Title:** [BugFix] Fixed wrong RoPE implementation for GLM5 in sfa_v1.py when using non-Triton operators

## Overview
This PR fixes an incorrect RoPE implementation for GLM5 models in `vllm_ascend/attention/sfa_v1.py` when `HAS_TRITON=False`. The code defaulted to using the `npu_rotary_mul` operator, which uses half-format rotary computation, resulting in incorrect RoPE implementation for GLM5. The fix reuses the existing `is_rope_neox_style=False` configuration for GLM5 to correctly select the `torch_npu.npu_interleave_rope` operator.

## Technical Significance
RoPE (Rotary Position Embedding) implementation correctness is critical for attention accuracy. Using the wrong format (half vs interleaved) causes incorrect positional encoding, leading to degraded model quality. The fix ensures GLM5 uses the correct `npu_interleave_rope` operator when not using Triton, maintaining model accuracy by properly handling the non-Neox-style RoPE format used by GLM5. This prevents accuracy regressions when running GLM5 models with non-Triton operators on Ascend NPUs.

## Related
- `kernel-attention` (RoPE implementation)
- `pattern-glm5` (GLM5 model specifics)
- `technique-non-triton` (Non-Triton operator paths)