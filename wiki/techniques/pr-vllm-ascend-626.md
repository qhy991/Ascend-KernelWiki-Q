---
id: technique-pr-vllm-ascend-626
title: "PR Insight: vllm-project/vllm-ascend #626"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - distributed
  - hccl
  - data-parallel
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/626"
---

# PR Insight: vllm-project/vllm-ascend #626

**Title:** Add dp initialize patch with hccl backend

## Overview
This PR adds data parallel process group initialization using the HCCL (Huawei Collective Communication Library) backend as a vllm-ascend patch. Implementation adds distributed patching infrastructure.

## Technical Significance
Data parallelism requires process groups for gradient/weight synchronization. HCCL is Ascend's native communication library. This patch enables efficient distributed data parallel training and inference on Ascend clusters.

## Related
- technique-hccs-optimization
- technique-data-parallel