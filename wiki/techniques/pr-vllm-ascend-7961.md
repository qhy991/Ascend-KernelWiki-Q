---
id: technique-pr-vllm-ascend-7961
title: "PR Insight: vllm-project/vllm-ascend #7961"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - mla
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7961"
---

# PR Insight: vllm-project/vllm-ascend #7961

**Title:** [v0.18.0][BugFix]Revert the code: Replace npu_ring_mla with FIA with MLA prefill

## Overview
This PR reverts previous changes that switched MLA (Multi-Head Latent Attention) prefill from `npu_ring_mla` to `npu_fused_infer_attention_score` (FIA). The change restores `npu_ring_mla` for MLA prefill operations, removes redundant metadata tracking, and updates tests to mock the ring-based MLA kernel instead of deprecated FIA functions.

## Technical Significance
MLA is a key attention optimization for reducing KV cache memory. The `npu_ring_mla` operator is the intended implementation for MLA prefill on Ascend, providing better performance and alignment with the architecture. Reverting to `npu_ring_mla` ensures optimal MLA performance and simplifies the codebase by removing unnecessary metadata structures.

## Related
- `kernel-attention`
- `pattern-mla`
- `kernel-npu-ring-mla`