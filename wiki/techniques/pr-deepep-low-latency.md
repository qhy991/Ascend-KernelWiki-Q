---
id: technique-pr-deepep-low-latency
title: "PR Insight: DeepEP Low-Latency All-to-All"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - networking
  - deepseek
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/546"
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/540"
---

# PR Insight: DeepEP Low-Latency All-to-All

**Source:** [sgl-kernel-npu PR #546](https://github.com/sgl-project/sgl-kernel-npu/pull/546), [PR #540](https://github.com/sgl-project/sgl-kernel-npu/pull/540)

**DeepEP** is the specialized Expert Parallelism (EP) communication library heavily utilized by DeepSeek. When executing MoE models, tokens must be scattered to the NPUs hosting the correct experts, computed, and then gathered back. This relies heavily on `All-to-All` communication over HCCL.

## The Abstraction Refactor

The PRs refactor the DeepEP `Buffer` class to use a strategy abstraction, differentiating between **Normal Mode** and **Low-Latency Mode**.

### 1. Internal Encapsulation of `Alltoall`
In Normal mode, the `Alltoall` strategy is used directly. However, traditional framework-level (PyTorch) All-to-All calls introduce heavy CPU dispatch overhead, which is fatal for latency-sensitive token-by-token decoding.
The PR encapsulates the `Alltoall` operation internally at the Python/C++ boundary, hiding it from the standard autograd dispatcher.

### 2. `low_latency_dispatch` & `low_latency_combine`
For Ascend (CANN), the framework exposes two new APIs externally:
- `low_latency_dispatch()`: Directly triggers the CANN kernel (using the `ops` strategy) to bypass PyTorch streams and inject the token scatter instructions directly into the NPU's Graph Engine.
- `low_latency_combine()`: Fetches the expert outputs.

**Why it matters**: By tightly coupling the CANN operator with the HCCL network queue, the NPU can execute the Expert routing logic and instantly initiate the network transfer without waiting for the host CPU to realize the computation is done. This drastically lowers inter-token latency in DeepSeek's decoding phase.
