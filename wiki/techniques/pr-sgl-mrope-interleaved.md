---
id: technique-pr-sgl-mrope-interleaved
title: "PR Insight: MRoPE Interleaved Data Layout"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - rope
  - multi-modal
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/503"
---

# PR Insight: MRoPE Interleaved Data Layout

**Source:** [sgl-kernel-npu PR #503](https://github.com/sgl-project/sgl-kernel-npu/pull/503)

Traditional Rotary Positional Embeddings (RoPE) are designed for 1D text sequences. However, Multimodal models (like Vision-Language models) utilize **Multimodal RoPE (MRoPE)**, which applies 2D or 3D rotations based on spatial coordinates (e.g., width, height, and time).

## The Data Layout Problem

When calculating MRoPE, the positional frequencies must be applied to the $Q$ and $K$ tensors. 
- In a standard `half-half` layout, the first half of the feature dimension is paired with the second half.
- In an **interleaved** layout, adjacent elements (e.g., index 0 and 1) are paired together to apply the sine/cosine rotation.

## Ascend's Interleaved Mode Solution

This PR adds explicit support for the interleaved mode in the fused `split_qkv_norm_rope` AscendC kernel.

### Why Interleaved is Better for Hardware
Using the interleaved data layout directly aligns with the Ascend Vector unit's continuous memory read patterns. 
1. The NPU can issue a single, continuous `DataCopy` instruction to load the $Q$ vector into the Unified Buffer.
2. The Vector ALU can execute a highly optimized `VMUL` (Vector Multiply) applying the complex rotations to adjacent elements simultaneously using SIMD (Single Instruction, Multiple Data).
3. This avoids the costly memory gathering/scattering required if the NPU had to fetch the first half and second half of the dimensions from disparate HBM locations.
