---
id: technique-pr-vllm-ascend-6530
title: "PR Insight: vllm-project/vllm-ascend #6530"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - moe
  - all-gather
  - inference
  - token-dispatch
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6530"
---

# PR Insight: vllm-project/vllm-ascend #6530

**Title:** [Feat.]: 310p support MOE models

## Overview
This PR adds comprehensive MoE (Mixture of Experts) model support for Ascend 310P devices. It introduces specialized modules for expert selection, fused MoE layers, optimized all-gather communication, and NPU-specific token dispatching. The implementation registers AscendFusedMoE310 and AscendSharedFusedMoE310 classes.

## Technical Significance
Enables efficient MoE inference on Ascend 310P hardware with platform-specific optimizations. The implementation leverages all-gather communication and custom token dispatching to optimize the expert routing and computation patterns specific to the 310P architecture.

## Related
- `kernel-moe`