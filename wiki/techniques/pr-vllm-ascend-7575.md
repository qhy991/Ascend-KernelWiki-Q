---
id: technique-pr-vllm-ascend-7575
title: "PR Insight: vllm-project/vllm-ascend #7575"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - triton
  - slot-mapping
  - block-table
  - kernel-optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7575"
---

# PR Insight: vllm-project/vllm-ascend #7575

**Title:** [model_runner_v2]:optimize the performance of the _compute_slot_mappings_kernel

## Overview
This PR optimizes the _compute_slot_mappings_kernel for Ascend NPUs by implementing a new Triton kernel with NPU-specific optimizations. The optimization includes using tl.gather for non-contiguous memory access and replacing modulo operations to avoid performance degradation from scalar computation.

## Technical Significance
This optimization matters for block table management performance on Ascend. The slot mapping kernel computes physical KV cache block locations for each token. Scalar operations like modulo are inefficient on NPUs. By using gather operations and optimizing memory access patterns, the kernel better utilizes NPU vector units and reduces compute overhead.

## Related
- technique-triton
- technique-kv-cache-paging