---
id: technique-pr-vllm-ascend-10172
title: "PR Insight: vllm-project/vllm-ascend #10172"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3.5
  - pcp
  - mtp
  - single-batch
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10172"
---

# PR Insight: vllm-project/vllm-ascend #10172

**Title:** [BugFix] fix qwen3.5+pcp+mtp single batch error

## Overview
This PR fixes errors occurring with Qwen3.5 models when using PCP (prefill context parallel) and MTP (multi-token prefix) together in single batch scenarios. The combination of these features caused failures under specific conditions.

## Technical Significance
Fixes Qwen3.5 compatibility with PCP+MTP in single batch scenarios, resolving edge cases where the combination caused errors. Ensures that Qwen3.5 models work correctly with both context parallelism and MTP enabled.

## Related
- `technique-context-parallel`, `technique-mtp`, `technique-qwen3.5`, `pattern-batch-handling`