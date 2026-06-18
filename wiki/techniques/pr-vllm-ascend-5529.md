---
id: technique-pr-vllm-ascend-5529
title: "PR Insight: vllm-project/vllm-ascend #5529"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - eplb
  - revert
  - bugfix
  - memory-safety
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5529"
---

# PR Insight: vllm-project/vllm-ascend #5529

**Title:** [Bugfix] Revert pr4214 multi-stream collect expert hotpot

## Overview
This PR reverts PR #4214 which attempted to collect expert hotspot data using multiple streams. The multi-stream approach led to memory overwriting and accuracy issues, particularly affecting EPLB (Expert Parallel Load Balancing) performance on Qwen3-MoE models, reducing AIME2024 accuracy from 86.67% to 43.33%.

## Technical Significance
The revert demonstrates the critical importance of memory safety in concurrent stream processing for NPU operations. Multi-stream processing requires careful memory management to avoid race conditions, and the single-stream approach ensures correct expert hotspot collection without compromising inference accuracy.

## Related
- `pattern-moe` (MoE patterns and operations)
- `technique-expert-parallelism` (Expert parallel load balancing)
- `technique-memory-safety` (Multi-stream memory management)