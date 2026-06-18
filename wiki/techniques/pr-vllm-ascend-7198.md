---
id: technique-pr-vllm-ascend-7198
title: "PR Insight: vllm-project/vllm-ascend #7198"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - precision
  - dispatch-ffn
  - cube-unit
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7198"
---

# PR Insight: vllm-project/vllm-ascend #7198

**Title:** [fix]: fix precision issue in dispatch_ffn_combine_bf16 and remove redundant sync

## Overview
This PR fixes a precision issue in the dispatch_ffn_combine_bf16 operator and removes redundant synchronization operations in the dispatch_ffn_combine operator. The changes affect the C++ AscendC operator implementations for MoE feed-forward networks, including tiling and block epilogue optimization files.

## Technical Significance
This fix is critical for MoE inference accuracy on Ascend hardware. The precision bug in dispatch_ffn_combine_bf16 likely involved incorrect data type handling in the bfloat16 quantization path. Removing redundant sync operations improves performance by eliminating unnecessary pipeline stalls between Cube-unit matrix computations and vector operations in the MoE token dispatch/combine kernels.

## Related
- technique-moe
- technique-double-buffering
- technique-cube-vector-overlap