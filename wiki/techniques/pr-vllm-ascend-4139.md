---
id: technique-pr-vllm-ascend-4139
title: "PR Insight: vllm-project/vllm-ascend #4139"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - custom-ops
  - dispatchgmmcombine
  - ascendc
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4139"
---

# PR Insight: vllm-project/vllm-ascend #4139

**Title:** [Kernel] add custom op DispatchGmmCombineDecode

## Overview
This PR adds a custom AscendC operator `DispatchGmmCombineDecode` for A3 (Ascend 3rd generation) hardware, including complete kernel implementation, Python API, and pytest. The operator implements grouped matrix multiplication with SwiGLU activation and quantization/dequantization for MoE combine operations in the decode phase, optimized for per-token processing.

## Technical Significance
Custom AscendC operators provide hardware-specific optimizations that cannot be achieved with standard PyTorch operators. The DispatchGmmCombineDecode operator is optimized for MoE decode phase operations, handling grouped matmul with SwiGLU and quantization efficiently. Per-token processing optimization is critical for decode phase throughput in MoE models.

## Related
- `technique-moe`, `technique-ascendc`, `pattern-custom-ops`, `technique-quantization`, `technique-swiglu`