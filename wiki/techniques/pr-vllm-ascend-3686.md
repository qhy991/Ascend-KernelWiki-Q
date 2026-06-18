---
id: technique-pr-vllm-ascend-3686
title: "PR Insight: vllm-project/vllm-ascend #3686"
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
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3686"
---

# PR Insight: vllm-project/vllm-ascend #3686

**Title:** [v0.11.0][BugFix][P/D] Modify the recalculation logic to prevent waiting requests from filling up the D node KVCache

## Overview
This is a cherry-pick of PR #3641 to the v0.11.0 branch, fixing recalculation logic in disaggregated (P/D) inference. It prevents waiting requests from filling up the decode node's KV cache by modifying `vllm_ascend/core/recompute_scheduler.py` and example configurations for load balancing proxy servers.

## Technical Significance
Backporting critical memory management fixes to release branches prevents OOM conditions in production. The fix ensures fair KV cache allocation in disaggregated inference, where waiting requests could otherwise consume disproportionate memory and cause failures on decode nodes.

## Related
- `technique-kv-cache`
- `technique-disaggregated-inference`
- `technique-scheduler-optimization`