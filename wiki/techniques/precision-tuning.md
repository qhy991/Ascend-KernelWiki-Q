---
id: technique-precision-tuning
title: "Precision Tuning & Accumulation"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - accuracy
confidence: inferred
sources: []
---

# Precision Tuning & Accumulation

Handling mixed precision correctly is essential to achieving maximum TFLOPS on Ascend without sacrificing model convergence or inference accuracy.

## The Cube Unit Precision Model
The Cube Unit (Matrix Multiply engine) natively supports several precisions, but the accumulation path is critical:
- **Input Precisions**: `fp16`, `bf16`, `int8`, `int4`.
- **Internal Accumulation**: Regardless of input, the Cube unit accumulates dot-products into a higher precision internally (e.g., `fp32` for `fp16` inputs, or `int32` for `int8` inputs) inside the L0C buffer.

### Avoiding Overflow
When computing $Q \cdot K^T$ in Attention, the sequence lengths can be massive. If you force the L0C to downcast the accumulated results back to `fp16` before applying the Max/Exp operations in the Softmax, you risk `NaN` or `Inf` due to `fp16`'s low dynamic range (max ~65504).
- **Solution**: Output the intermediate $S$ matrix as `fp32` from the Cube to the Unified Buffer (UB). Perform the Vector Unit reductions (Max/Sum) in `fp32`, and only cast back to `fp16` for the final $P$ output.

## Native Bfloat16 (910B+)
Ascend 910B introduced native hardware support for `bfloat16`. 
- `bfloat16` shares the same dynamic range as `fp32` (8-bit exponent), virtually eliminating overflow risks in LLM attention and gradient accumulation.
- **Migration**: When porting from 910A to 910B, swap `half` data types to `bfloat16_t` in your AscendC `GlobalTensor` and `LocalTensor` declarations. Ensure the MTE data transfers align with 2-byte increments.

## Vector Unit Precision
The Vector unit handles element-wise ops (`Exp`, `Log`, `Add`). While it supports `fp16`, it achieves identical or near-identical throughput on `fp32` for many instructions. Do not eagerly downcast to `fp16` in the Vector pipeline if accuracy is paramount; keep accumulators in `fp32` until writing to GM.
