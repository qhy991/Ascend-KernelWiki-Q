---
id: technique-pr-vllm-ascend-7902
title: "PR Insight: vllm-project/vllm-ascend #7902"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - 310p
  - fla
  - normalization
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7902"
---

# PR Insight: vllm-project/vllm-ascend #7902

**Title:** [BugFix][310p] Align 310P GDN state semantics with vLLM

## Overview
This PR aligns the FLA (Flash Linear Attention) state layout semantics between vllm-ascend and vLLM for Ascend 310P. The state layout was `[N, HV, V, K]` in vLLM but `[N, HV, K, V]` in vllm-ascend. The PR also replaces manual L2 normalization implementation with operators from PyTorch functional for cleaner code.

## Technical Significance
State layout alignment is critical for model correctness and operator interoperability. The mismatch in GDN (Gated Delta Rule) state semantics would cause incorrect results. Additionally, using functional operators for L2 normalization leverages optimized library implementations rather than manually stitched operations, improving both maintainability and potentially performance.

## Related
- `kernel-attention`
- `pattern-fla`
- `kernel-layernorm`