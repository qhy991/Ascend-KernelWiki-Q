---
id: technique-pr-vllm-ascend-8657
title: "PR Insight: vllm-project/vllm-ascend #8657"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - attention
  - lightning-attn
  - mamba
  - triton
  - tiling
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8657"
---

# PR Insight: vllm-project/vllm-ascend #8657

**Title:** [Attention][Feature] adapt bailing_moe_linear on Ascend

## Overview
This PR adapts BaLing 2.5/2.6 series models to run on Ascend hardware. Key changes include aligning pagesize padding between linear attention and MLA (Multi-head Latent Attention), and fixing NPU incompatibility in the upstream vLLM lightning_attn implementation. The lightning_attn modifications resolve UB overflow issues and optimize tiling strategies and Triton kernel implementation for better performance.

## Technical Significance
This adaptation enables BaLing models (which use Mamba architecture with lightning attention) to run efficiently on Ascend NPUs. The lightning_attn fixes address fundamental compatibility issues by resolving undefined behavior overflow problems and optimizing memory access patterns. The tiling strategy improvements are crucial for maximizing NPU performance with the unique attention mechanism used by these models.

## Related
- `kernel-attention-ascendc`
- `technique-nz-tiling`
- `technique-triton-optimization`
- `pattern-mamba`