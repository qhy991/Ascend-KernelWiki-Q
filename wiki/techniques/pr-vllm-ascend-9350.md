---
id: technique-pr-vllm-ascend-9350
title: "PR Insight: vllm-project/vllm-ascend #9350"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - a2
  - a3
  - a5
  - compressor
  - ascendc
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9350"
---

# PR Insight: vllm-project/vllm-ascend #9350

**Title:** [Feature][Ops] Support A2/A3 and A5 compressor paths

## Overview
This PR adds support for A2, A3, and A5 hardware architectures to the compressor operator, which is used for DeepSeek V4 attention optimization. The implementation includes separate kernel implementations and tiling strategies for each architecture, with optimized compute and communication overlap patterns.

## Technical Significance
Expanding compressor support across multiple Ascend architectures enables DeepSeek V4 optimizations on a wider range of hardware. The architecture-specific implementations ensure optimal performance on each device, with proper handling of compute unit capabilities, memory hierarchy, and communication patterns.

## Related
- `technique-cube-vector-overlap`
- `kernel-attention`
- `hw-cube-unit`