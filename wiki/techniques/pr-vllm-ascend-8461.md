---
id: technique-pr-vllm-ascend-8461
title: "PR Insight: vllm-project/vllm-ascend #8461"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decoding
  - hybrid-model
  - async
  - performance
  - synchronization
  - seq-lens
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8461"
---

# PR Insight: vllm-project/vllm-ascend #8461

**Title:** [Feature] adapter async spec decode to hybrid model and optimize performance

## Overview
This PR adapts asynchronous speculative decoding to hybrid models and optimizes performance by deleting configuration code that prevented simultaneous enabling of speculative inference and asynchronous scheduling. The fix references upstream vllm PR #38556 for async spec decoding with hybrid models. By asynchronously and non-blockingly synchronizing correct seq_lens on the NPU to the CPU, the solution ensures attention layer correctness with negligible performance impact.

## Technical Significance
This fix enables important performance optimizations by combining asynchronous scheduling with speculative decoding in hybrid model scenarios. The asynchronous seq_len synchronization is critical for maintaining attention correctness while avoiding blocking operations that would hurt performance. The PR demonstrates how to properly handle NPU-CPU synchronization in complex inference pipelines.

## Related
- `technique-speculative-decoding`
- `technique-asynchronous-inference`
- `technique-hybrid-model`