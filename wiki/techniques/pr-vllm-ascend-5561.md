---
id: technique-pr-vllm-ascend-5561
title: "PR Insight: vllm-project/vllm-ascend #5561"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pcp
  - eplb
  - moe
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5561"
---

# PR Insight: vllm-project/vllm-ascend #5561

**Title:** [Bugfix] fix pcp + eplb error

## Overview
This PR fixes compatibility bugs between PCP (Prefill-Decode Pipeline) and EPLB features. The main fixes include properly including PCP size in word_size calculations to resolve overlap issues and adding user prompts for configuring cp_kv_cache_interleave_size in PCP pooling scenarios.

## Technical Significance
The PCP+EPLB combination is important for optimizing long-context MoE inference, and the bug fix ensures correct resource allocation and memory management when both features are enabled simultaneously. Proper word_size calculation prevents memory allocation errors while user prompts improve configurability.

## Related
- `pattern-moe` (MoE patterns and operations)
- `technique-expert-parallelism` (Expert parallel load balancing)
- `technique-prefill-decode` (Prefill-decode pipeline)
- `technique-kv-cache` (KV cache management)