---
id: technique-pr-vllm-ascend-8709
title: "PR Insight: vllm-project/vllm-ascend #8709"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - quantization
  - bailing
  - mamba
  - modelslim
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8709"
---

# PR Insight: vllm-project/vllm-ascend #8709

**Title:** [Ops][Feature] Support Bailing quantization

## Overview
This PR adds ModelSlim quantization configuration support for the `bailing_hybrid` model architecture. It adds module mappings for MoE-related layers (gate_up_proj, experts with gate/up/down projections), attention layers (fused_qkv_a_proj, o_proj), and fixes layer name mapping by unifying `linear_attn` and `self_attn` to `attention` to match quantization weight naming conventions.

## Technical Significance
This feature enables quantization support for BaLing hybrid models, which combine Mamba and Transformer architectures. The ModelSlim integration allows users to leverage hardware-aware quantization schemes optimized for Ascend NPUs. The fix to layer name mapping ensures proper weight quantization across different attention variants in hybrid models, preventing quantization failures due to naming mismatches.

## Related
- `kernel-matmul-ascendc`
- `technique-quantization`
- `kernel-moe-ascendc`