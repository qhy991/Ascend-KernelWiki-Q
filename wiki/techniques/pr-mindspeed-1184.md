---
id: technique-pr-mindspeed-1184
title: "PR Insight: Ascend/MindSpeed #1184"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - moe
  - megatron
  - adaptation
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1184"
---

# PR Insight: Ascend/MindSpeed #1184

**Title:** 【master】megatron-moe overlap & tp_extend_ep & zero-memory适配core_r0.7.0

## Overview
This PR adapts Megatron MoE overlap, tp_extend_ep (tensor parallelism extended with expert parallelism), and zero-memory features for core_r0.7.0. These features optimize MoE training performance and memory usage on Ascend hardware.

## Technical Significance
Megatron MoE overlap improves performance by overlapping computation and communication in MoE models. Combined with tensor+expert parallelism and zero-memory optimizations, this enables efficient training of large-scale MoE models on Ascend NPUs and clusters.

## Related
- kernel-moe
- technique-communication-optimization
- technique-cube-vector-overlap