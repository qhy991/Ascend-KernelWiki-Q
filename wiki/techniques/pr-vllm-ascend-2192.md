---
id: technique-pr-vllm-ascend-2192
title: "PR Insight: vllm-project/vllm-ascend #2192"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mm-allreduce
  - fusion
  - testing
  - matmul
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2192"
---

# PR Insight: vllm-project/vllm-ascend #2192

**Title:** enable mm allreduce test

## Overview
This PR adds end-to-end tests for using the `npu_mm_all_reduce_base` fusion kernel. The implementation adds test cases to `tests/e2e/multicard/test_external_launcher.py` and minor updates to the linear patch file to enable the fused matmul-allreduce operation during testing.

## Technical Significance
This addition enables validation of the matrix multiplication-allreduce fusion kernel that combines matmul computation with collective communication, reducing memory traffic and improving performance. The tests ensure the fusion kernel works correctly in distributed scenarios and provide confidence in the optimization's correctness.

## Related
- `kernel-matmul-ascendc`, `technique-operator-fusion`, `technique-hccl-optimization`, `kernel-mm-allreduce-fusion`