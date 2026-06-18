---
id: technique-pr-soft-fp8-grouped-matmul
title: "PR Insight: Soft FP8 Grouped MatMul for MoE"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - fp8
  - quantization
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/268"
---

# PR Insight: Soft FP8 Grouped MatMul for MoE

**Source:** [sgl-kernel-npu PR #268](https://github.com/sgl-project/sgl-kernel-npu/pull/268)

Supporting Massive Mixture-of-Experts (MoE) models like **Qwen3-MoE-30B-A3B-FP8** and **DeepSeekR1** requires extreme memory bandwidth efficiency. When full hardware FP8 execution paths are not fully exposed, developers implement "Soft FP8".

## The Challenge
In an MoE layer, tokens are routed to various experts (Grouped MatMul). If the expert weights are stored in FP16 or BF16, the MTE (Memory Transfer Engine) bandwidth becomes the primary bottleneck, starving the Cube (Matrix) Unit.

## The "Soft FP8" Solution
This PR implements a software-based FP8 computation path directly within the AscendC operator.

1. **Storage**: Expert weights are stored in Global Memory (GM) in `FP8` (specifically E4M3 or E5M2).
2. **Transfer**: The MTE loads the heavily compressed FP8 weights into the Unified Buffer (UB). This doubles the effective memory bandwidth compared to BF16.
3. **On-the-fly Dequantization**: Before passing the weights to the L0A/L0B buffers for the Cube unit to process, the Vector unit intercepts the FP8 blocks in the UB and performs a rapid **FP8 $\rightarrow$ BF16** dequantization.
4. **Compute**: The Grouped MatMul executes natively in BF16 in the Cube unit.

## Performance Impact
While there is a slight Vector unit overhead for the dequantization step, the massive reduction in Global Memory read latency heavily outweighs the compute cost. The NPU transitions from being *Memory Bandwidth Bound* to *Compute Bound*, significantly accelerating DeepSeek R1 and Qwen3 MoE routing.
