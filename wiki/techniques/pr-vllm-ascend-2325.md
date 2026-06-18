---
id: technique-pr-vllm-ascend-2325
title: "PR Insight: vllm-project/vllm-ascend #2325"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - lora
  - custom-kernels
  - sgmv
  - graph-mode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2325"
---

# PR Insight: vllm-project/vllm-ascend #2325

**Title:** Add Custom Kernels For LoRA Performance

## Overview
This PR adds two custom operators (sgmv_shrink and sgmv_expand) to address LoRA performance issues and enables graph mode for LoRA operators to enter ACL for improved inference performance. The implementation includes C++ kernels in `csrc/kernels/` with 650 lines of new code, updates to Python bindings and meta registration.

## Technical Significance
This optimization delivers dramatic performance improvements for LoRA inference. Benchmarks on Qwen2.5 7B in ACL graph mode show TTFT, TPOT, and throughput increased by approximately 100%. The custom kernels efficiently handle the grouped matrix-vector multiplication operations that are critical for LoRA adapters, and graph mode integration further reduces overhead.

## Related
- `kernel-lora-ascendc`, `kernel-sgmv-shrink`, `kernel-sgmv-expand`, `technique-aclgraph-integration`