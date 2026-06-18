---
id: technique-pr-mindspeed-tp2d-ring
title: "PR Insight: TP-2D & Ring Attention"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - tensor-parallelism
  - training
  - mindspeed
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2721"
---

# PR Insight: TP-2D & Ring Attention Interplay

**Source:** [MindSpeed PR #2721](https://gitee.com/ascend/MindSpeed/pulls/2721)

Modern LLM training on Ascend clusters uses deeply nested parallelism strategies. **Tensor Parallelism 2D (TP-2D)** slices the model weights across both the row and column dimensions, reducing the communication payload size but increasing the complexity of the communication rings.

## The Bug and The Fix

The PR addresses a critical topology bug: `fix: 修复tp2d不开cp时走ring attn` (Fix: route to Ring Attention when TP-2D is enabled but Context Parallelism (CP) is off).

### Understanding the Interlock
1. **Standard Ring Attention** is typically associated with Context Parallelism (CP), passing key-value chunks in a ring around the HCCS network to process infinitely long sequences.
2. **The Edge Case**: When a training job defines a 2D Tensor Parallel geometry but specifically disables CP (e.g., when the sequence length fits in memory, but the parameter size requires extreme slicing), the native sequence communication graphs would break or fall back to highly inefficient, global All-Gathers.

### The Resolution
MindSpeed's communication graph generator was patched to force the Ascend communication backend to synthesize a localized **Ring Attention** topology specifically over the TP-2D node groups, *even when the global Context Parallelism engine is disabled*. This ensures that the NPU's MTE (Memory Transfer Engine) and HCCL continue to overlap compute with localized ring transfers, preventing a catastrophic drop in TFLOPS.
