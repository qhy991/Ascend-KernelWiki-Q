---
id: technique-pr-vllm-ascend-814
title: "PR Insight: vllm-project/vllm-ascend #814"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - multi-step
  - custom-kernel
  - inference
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/814"
---

# PR Insight: vllm-project/vllm-ascend #814

**Title:** [Performance]: Custom AscendC Kernel of Multi-Step Prepare Input

## Overview
This PR implements a custom AscendC kernel for multi-step prepare input operations, addressing issue #807. The kernel improves performance by optimizing the multi-step workflow in vllm-ascend, and includes unit tests and offline inference examples.

## Technical Significance
Multi-step inference is a performance optimization technique that processes multiple tokens in a single step. Custom AscendC kernels provide better utilization of Ascend hardware features compared to generic PyTorch operations, reducing latency and improving throughput for inference workloads.

## Related
- `language-ascendc`
- `technique-multi-step`
- `kernel-inference`