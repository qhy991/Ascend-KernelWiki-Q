---
id: technique-pr-vllm-ascend-2230
title: "PR Insight: vllm-project/vllm-ascend #2230"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - allreduce
  - npu
  - prefill
  - communication-optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2230"
---

# PR Insight: vllm-project/vllm-ascend #2230

**Title:** move with_prefill allreduce from cpu to npu

## Overview
This PR optimizes distributed performance by migrating the with_prefill allreduce operation from CPU to NPU, leveraging NPU network topology acceleration. The change is minimal in `vllm_ascend/worker/model_runner_v1.py` (2 lines) but delivers dramatic performance improvements.

## Technical Significance
This optimization significantly reduces communication overhead and synchronization delays by offloading allreduce operations to the NPU. Benchmark results show the allreduce operation time decreased from 11 ms to 0.3 ms per iteration, demonstrating the benefits of using NPU-native collective operations over CPU-based alternatives.

## Related
- `technique-hccl-optimization`, `technique-communication-offload`, `kernel-allreduce-npu`