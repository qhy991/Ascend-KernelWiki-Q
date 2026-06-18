---
id: technique-pr-vllm-ascend-5647
title: "PR Insight: vllm-project/vllm-ascend #5647"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - prefill
  - pcp
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5647"
---

# PR Insight: vllm-project/vllm-ascend #5647

**Title:** [bugfix (pcp)] fix chunked prefill accurancy issue

## Overview
This PR fixes an accuracy issue in PCP (Prefill Cache Prefetch) mode by properly initializing the padded slot mapping buffer to prevent garbage values. The buffer is reused across invocations in PCP mode, so proper initialization is critical.

## Technical Significance
Critical bug fix for chunked prefill accuracy in PCP mode. Uninitialized buffers can cause incorrect prefill results, leading to wrong model outputs. Proper initialization of reused buffers prevents memory corruption and ensures correctness, which is essential for reliable inference in PCP mode.

## Related
- `technique-prefill-optimization`, `technique-caching`, `technique-pcp`