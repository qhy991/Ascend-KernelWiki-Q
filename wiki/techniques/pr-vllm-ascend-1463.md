---
id: technique-pr-vllm-ascend-1463
title: "PR Insight: vllm-project/vllm-ascend #1463"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - pangu-moe
  - h2p
  - communication
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1463"
---

# PR Insight: vllm-project/vllm-ascend #1463

**Title:** [PERF]support H2P communication optimization for PanguProMoe

## Overview
This PR adds H2P (Host-to-Device) communication optimization for PanguProMoE models, improving inference performance.

## Technical Significance
Optimizes host-to-device data transfer for PanguProMoE inference by improving communication patterns and reducing transfer overhead. This is particularly beneficial for large MoE models where parameter loading dominates latency.

## Related
- `kernel-moe`
- `technique-communication-optimization`
- `kernel-pangu`