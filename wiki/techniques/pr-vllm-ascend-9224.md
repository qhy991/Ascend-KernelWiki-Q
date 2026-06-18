---
id: technique-pr-vllm-ascend-9224
title: "PR Insight: vllm-project/vllm-ascend #9224"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - conv1d
  - gdn
  - operator-fusion
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9224"
---

# PR Insight: vllm-project/vllm-ascend #9224

**Title:** [Feature] GDN and conv1d operators adapted for A5

## Overview
This PR adds A5 hardware support for the GDN (recurrent gated delta rule) and conv1d operators by adapting the existing custom operators to work on the A5 architecture. The changes include modifications to the operator host definitions, kernel implementations for arch35, and build scripts to enable compilation for A5 targets.

## Technical Significance
Enabling these operators on A5 hardware expands the supported model architectures and improves inference performance for models using GDN and conv1d operations, which are critical for certain recurrent and convolutional neural network components. The adaptation involves hardware-specific kernel implementations and tiling strategies optimized for A5's compute capabilities.

## Related
- `technique-operator-fusion`
- `hw-cube-unit`
- `hw-vector-unit`