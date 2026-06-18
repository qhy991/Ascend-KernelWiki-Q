---
id: technique-pr-sgl-kernel-npu-396
title: "PR Insight: sgl-project/sgl-kernel-npu #396"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - dispatch-ffn-combine
  - operator-fusion
  - deepep
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/396"
---

# PR Insight: sgl-project/sgl-kernel-npu #396

**Title:** add dispatch_ffn_combine kernel for deepep

## Overview
This PR implements a dispatch_ffn_combine kernel for DeepEP that fuses token dispatch, feed-forward network computation, and expert output combination into a single operation. The comprehensive implementation includes routing quantization, dynamic quantization, sorting, and unpermutation utilities optimized for MoE inference.

## Technical Significance
Fusing dispatch, FFN computation, and combine operations into a single mega-kernel significantly reduces memory traffic and kernel launch overhead for MoE layers. This optimization enables more efficient token-to-expert routing and expert execution, particularly beneficial for large-scale MoE models with hundreds of experts.

## Related
- `kernel-dispatch-ffn-combine`, `kernel-moe-fusion`, `technique-mega-kernel`, `technique-operator-fusion`