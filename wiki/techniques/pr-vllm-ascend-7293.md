---
id: technique-pr-vllm-ascend-7293
title: "PR Insight: vllm-project/vllm-ascend #7293"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mla
  - flash-infer-attention
  - code-refactoring
  - tensor-shaping
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7293"
---

# PR Insight: vllm-project/vllm-ascend #7293

**Title:** [Perf] Simplify FIA prefill context merge path

## Overview
This PR simplifies and hardens MLA (Multi-Head Latent Attention) prefill context merging after FIA migration. It directly builds out_list/lse_list without temporary chunk buffers or cat/stack/split operations, using reshape for safe flattening of non-contiguous tensors.

## Technical Significance
This refactoring improves MLA attention efficiency on Ascend by reducing memory allocation and tensor manipulation overhead. The previous implementation used temporary buffers and multiple tensor operations (cat, stack, split) which added latency. The simplified approach directly constructs output lists and uses reshape for flattening, reducing memory traffic and improving prefill throughput.

## Related
- technique-mla
- technique-flash-infer-attention
- pattern-tensor-optimization