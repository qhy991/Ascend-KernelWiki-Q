---
id: technique-pr-vllm-ascend-3641
title: "PR Insight: vllm-project/vllm-ascend #3641"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-cache
  - disaggregated
  - p-d
  - recalculation
  - scheduler
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3641"
---

# PR Insight: vllm-project/vllm-ascend #3641

**Title:** [BugFix][P/D] Modify the recalculation logic to prevent waiting requests from filling up the D node KVCache

## Overview
This PR fixes recalculation logic in disaggregated (P/D) inference to prevent waiting requests from filling up the decode node's KV cache. Changes were made to `vllm_ascend/core/recompute_scheduler.py` and example configurations for load balancing proxy servers, modifying how recalculations are scheduled to avoid memory pressure.

## Technical Significance
In disaggregated inference with prefill (P) and decode (D) separation, waiting requests can accumulate KV cache on the decode node, causing memory exhaustion. This fix prevents the recalculation scheduler from allowing waiting requests to consume disproportionate KV cache space, ensuring fair memory allocation and preventing OOM conditions.

## Related
- `technique-kv-cache`
- `technique-disaggregated-inference`
- `technique-scheduler-optimization`