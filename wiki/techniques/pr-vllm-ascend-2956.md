---
id: technique-pr-vllm-ascend-2956
title: "PR Insight: vllm-project/vllm-ascend #2956"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - eplb
  - load-balance
  - distributed
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2956"
---

# PR Insight: vllm-project/vllm-ascend #2956

**Title:** Dynamic Expert Load Balance with Zero-like-overhead

## Overview
This PR implements SwiftBalancer, an asynchronous expert load balancing mechanism with minimal overhead (1-2ms per layer on NPU, saving 5-8ms decode latency). It addresses host-bound and communication latency issues through async CPU computing, optimized EPLB algorithm, and overlapped weight transfer.

## Technical Significance
SwiftBalancer eliminates the stop-the-world latency of previous EPLB implementations by running expert redistribution asynchronously in a separate worker process. The implementation uses reduced-precision expert token tracking, optimized all-gather communication, and overlapped weight transfer using ibatch_send_recv in async streams.

## Related
- `kernel-moe-ascendc`, `technique-load-balance`, `technique-pipeline-scheduling`