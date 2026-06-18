---
id: technique-pr-mindspeed-2818
title: "PR Insight: ascend/MindSpeed #2818"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - communication
  - memory
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2818"
---

# PR Insight: ascend/MindSpeed #2818

## Overview

**Repository:** `ascend/MindSpeed`
**PR Number:** #2818
**Title:** `[mindspore][master]fix ringattentionupdate`
**Type:** Bugfix

## Context

Ring Attention is a key distributed training method used to scale language model context windows far beyond a single device's memory capacity. It achieves this by distributing attention computation across multiple devices organized in a ring topology, overlapping Key/Value block communication with attention computation. 

In MindSpeed (Huawei Ascend's optimization library for large models), specifically for the MindSpore framework backend, intermediate statistics—such as the running maximum and exponential sum (similar to FlashAttention)—must be consistently updated and synchronized.

## Technical Details

This pull request fixes a bug related to the `ringattentionupdate` routine in the MindSpore implementation. While exact code changes are abstracted, fixes in this critical path generally involve:

1. **Softmax Statistics Rescaling:** Correcting the logic that rescales the previous attention block's output when the current block introduces a new global maximum attention score.
2. **Buffer and Offset Management:** Fixing incorrect memory offsets or tensor shapes during the update phase for Ascend NPU operations.
3. **Communication Overlap:** Resolving race conditions or synchronization errors when updating attention values before the next communication step in the ring completes.

## Architectural Impact

Correcting the Ring Attention update process is vital for ensuring mathematical equivalence with standard self-attention. Without this fix, models training on extremely long sequences (e.g., 1M+ tokens) on Ascend910/910B hardware could experience severe numerical instability, diverging losses, or out-of-bounds memory errors during the Ring Attention forward/backward passes.
