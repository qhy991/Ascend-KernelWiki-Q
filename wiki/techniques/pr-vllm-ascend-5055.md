---
id: technique-pr-vllm-ascend-5055
title: "PR Insight: vllm-project/vllm-ascend #5055"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - kv-cache
  - distributed
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5055"
---

# PR Insight: vllm-project/vllm-ascend #5055

**Title:** [BugFix] Fix mooncake bug in PCP scenario

## Overview
This PR fixes a bug in the mooncake_connector.py file where incorrect arguments were being imported when using PCP (Prefill-Chunked-Prefill). The fix corrects the argument handling to prevent errors in PCP scenarios for vLLM-Ascend.

## Technical Significance
The mooncake connector is critical for distributed KV cache management across Ascend NPU devices. This bugfix ensures correct argument passing in the PCP scenario, which is essential for efficient KV cache sharing and distributed inference coordination between prefill and decode stages.

## Related
- technique-kv-cache-paging
- technique-hccl-optimization