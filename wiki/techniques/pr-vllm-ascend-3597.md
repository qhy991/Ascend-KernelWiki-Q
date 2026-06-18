---
id: technique-pr-vllm-ascend-3597
title: "PR Insight: vllm-project/vllm-ascend #3597"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - aclgraph
  - batch-size
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3597"
---

# PR Insight: vllm-project/vllm-ascend #3597

**Title:** [Bugfix][MTP] Fix performance degradation when mtp>1

## Overview
This PR fixes performance degradation when MTP (multi-text-prompt) count exceeds 1. The issue occurs because mtp>1 can result in larger batch sizes than aclgraph's maximum batch size limit, forcing the draft model to fall back to eager mode instead of aclgraph. The fix was implemented in `vllm_ascend/utils.py` with 20 lines of new logic.

## Technical Significance
When batch sizes exceed aclgraph limits, falling back to eager mode significantly impacts performance. This fix likely implements better batch size handling or adaptive scheduling to keep the draft model in aclgraph mode even with MTP>1, preventing the performance penalty of eager execution. Maintaining aclgraph execution is crucial for achieving optimal inference throughput.

## Related
- `technique-mtp`
- `technique-aclgraph`
- `technique-batch-optimization`