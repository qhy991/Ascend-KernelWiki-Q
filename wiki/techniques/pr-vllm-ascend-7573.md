---
id: technique-pr-vllm-ascend-7573
title: "PR Insight: vllm-project/vllm-ascend #7573"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - mxfp8
  - a5
  - load-balancing
  - ascend950
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7573"
---

# PR Insight: vllm-project/vllm-ascend #7573

**Title:** [A5][bugfix] Fix fused MoE A5 MXFP8 scale normalization, load-balance routing and gating_topk ops

## Overview
This PR fixes A5 MXFP8 MoE scale handling in the fused MoE path. It normalizes MXFP8 activation scales to the packed 3D layout expected by A5 kernels, refines MXFP8 force load-balancing path in profiling runs, and enables npu_gating_top_k from torch_npu instead of custom op on Ascend950.

## Technical Significance
This fix matters for A5 MXFP8 MoE correctness and performance on Ascend950. Proper scale normalization ensures correct quantization behavior in fused MoE operations. The torch_npu gating_top_k provides better performance than custom ops. Together, these changes enable efficient MXFP8 quantized MoE inference on the latest Ascend hardware.

## Related
- technique-moe
- technique-mxfp8
- technique-load-balancing