---
id: technique-pr-vllm-ascend-4220
title: "PR Insight: vllm-project/vllm-ascend #4220"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - prefix-cache
  - testing
  - qwen3
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4220"
---

# PR Insight: vllm-project/vllm-ascend #4220

**Title:** [TEST]Update prefixcache perf threshold for qwen3-32b-int8

## Overview
This PR updates the prefix cache performance threshold for Qwen3-32B-int8 from 0.4 to 0.8, reflecting improvements in the baseline performance. The change ensures that performance tests accurately reflect current capabilities and don't fail due to outdated thresholds.

## Technical Significance
Prefix cache performance thresholds need periodic updates as baseline performance improves. Keeping thresholds accurate ensures tests provide meaningful validation of performance regressions. The improvement from 0.4 to 0.8 indicates significant baseline performance gains for prefix cache operations.

## Related
- `technique-prefix-cache`, `pattern-testing`, `technique-qwen3`, `pattern-performance-baseline`