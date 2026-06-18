---
id: technique-pr-vllm-ascend-6125
title: "PR Insight: vllm-project/vllm-ascend #6125"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mooncake
  - pd-colocation
  - performance
  - logging
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6125"
---

# PR Insight: vllm-project/vllm-ascend #6125

**Title:** improve the ttft when use mooncake

## Overview
This PR improves TTFT (Time To First Token) performance when using Mooncake by reducing logging overhead. The changes modify log levels from INFO to DEBUG in KV transfer pool scheduler and storage modules, reducing I/O overhead during inference.

## Technical Significance
Reducing log verbosity during inference path improves TTFT significantly, with average TTFT improving from 5.74s to 0.80s (85% improvement) and request throughput increasing from 4.88 req/s to 5.34 req/s. This demonstrates that logging can be a non-trivial performance bottleneck in high-throughput inference scenarios.

## Related
- `technique-pd-colocation`, `technique-mooncake`, `technique-i/o-optimization`