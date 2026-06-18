---
id: technique-pr-vllm-ascend-6468
title: "PR Insight: vllm-project/vllm-ascend #6468"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - dispatch-ffn-combine
  - kernel-optimization
  - communication-optimization
  - moe
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6468"
---

# PR Insight: vllm-project/vllm-ascend #6468

**Title:** [Kernel]: Optimize DispatchFFNCombine performance

## Overview
This PR optimizes the DispatchFFNCombine operator performance through three key improvements: merging tokens and scales transmission for better communication efficiency, decoupling multi-core dependencies to reduce waiting bubbles via tile-granularity communication, and optimizing full-card synchronization overhead before unpermute operations.

## Technical Significance
Significantly reduces execution latency of the DispatchFFNCombine operator on Ascend devices. The optimizations focus on communication patterns between cores, reducing synchronization overhead and improving data transfer efficiency. The tile-granularity communication approach minimizes pipeline bubbles, while unified token/scale transmission reduces HCCS communication traffic.

## Related
- `kernel-moe`
- `technique-hccl-optimization`
- `technique-pipeline-scheduling`