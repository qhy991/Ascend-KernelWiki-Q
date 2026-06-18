---
id: technique-pr-vllm-ascend-6020
title: "PR Insight: vllm-project/vllm-ascend #6020"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eplb
  - memory-optimization
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6020"
---

# PR Insight: vllm-project/vllm-ascend #6020

**Title:** [EPLB][Bugfix]Reduce unnecessary video memory usage

## Overview
This PR reduces unnecessary video memory usage in EPLB by incorporating EPLB warm-up into the profile run and reusing the same gather buffer. Testing on Qwen3-235B shows the OOM issue is resolved while maintaining 86.67% accuracy on AIME2024.

## Technical Significance
EPLB previously allocated separate memory for warm-up and runtime phases, increasing memory consumption. By integrating warm-up into the profile run and reusing gather buffers, the PR significantly reduces memory footprint. This prevents OOM errors in large-scale deployments while maintaining EPLB's load balancing benefits. The optimization is particularly important for large models like Qwen3-235B where memory is at a premium.

## Related
- `technique-eplb`, `technique-memory-optimization`, `technique-buffer-reuse`