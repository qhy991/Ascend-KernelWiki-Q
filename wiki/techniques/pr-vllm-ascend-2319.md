---
id: technique-pr-vllm-ascend-2319
title: "PR Insight: vllm-project/vllm-ascend #2319"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mla
  - chunked-prefill
  - oom
  - long-context
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2319"
---

# PR Insight: vllm-project/vllm-ascend #2319

**Title:** [Bugfix] fix the oom when chunkprefill with long context like 64k

## Overview
This PR fixes an out-of-memory (OOM) issue that occurs during chunked prefill with long contexts (64k-128k tokens). The problem was caused by an attention mask declared in mla.py that was needed for splitfuse operations but caused memory issues with MLA chunked prefill. The fix removes the unnecessary mask in `vllm_ascend/worker/model_runner_v1.py`.

## Technical Significance
This bugfix enables chunked prefill to work with very long contexts without running out of memory. By removing the splitfuse mask that was only needed for certain operations, the system avoids allocating large attention masks for long sequences, significantly reducing memory consumption during chunked prefill operations.

## Related
- `kernel-mla-v1`, `kernel-attention-ascendc`, `technique-chunked-prefill`, `technique-memory-optimization`