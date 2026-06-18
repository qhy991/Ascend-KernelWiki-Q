---
id: technique-pr-vllm-ascend-7487
title: "PR Insight: vllm-project/vllm-ascend #7487"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3.5
  - qwen3-next
  - gdn
  - asynchronous-scheduling
  - prefill-optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7487"
---

# PR Insight: vllm-project/vllm-ascend #7487

**Title:** [Feature]  Optimize Qwen3.5/Qwen3Next GDN prefill by prebuilding chunk metadata

## Overview
This PR optimizes Qwen3.5 and Qwen3Next GDN prefill by prebuilding chunk metadata on CPU, keeping staging buffers in pinned memory, and transferring asynchronously to NPU. This removes host/device synchronization from the critical path, eliminating prefill stalling in asynchronous scheduling scenarios.

## Technical Significance
This optimization matters for prefill-heavy workloads on Ascend. The previous implementation prepared metadata during forward pass, causing frequent CPU intervention and execution bubbles with async scheduling. By prebuilding metadata and using async transfers, it removes H2D/D2H round-trips from the hot path, significantly improving throughput and reducing TTFT for Qwen3.5/Next models.

## Related
- technique-gdn
- technique-asynchronous-scheduling
- technique-prefill-optimization