---
id: technique-pr-vllm-ascend-5657
title: "PR Insight: vllm-project/vllm-ascend #5657"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-connector
  - ucm
  - register-kv-cache
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5657"
---

# PR Insight: vllm-project/vllm-ascend #5657

**Title:** [Bugfix]Add register_kv_cache in ucm_connector

## Overview
This PR adds the register_kv_cache function to the UCM connector to adapt to different KV cache shapes. UCM optimized the initialization of store by moving it into register_kv_caches, requiring this API addition.

## Technical Significance
Enables UCM (Unified Cache Management) connector to handle diverse KV cache shapes properly. The register_kv_cache API allows UCM to initialize storage correctly based on the actual cache dimensions, which is essential for supporting various model configurations and memory layouts efficiently.

## Related
- `technique-kv-cache-paging`, `technique-ucm`