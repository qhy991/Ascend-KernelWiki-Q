---
id: technique-pr-vllm-ascend-6475
title: "PR Insight: vllm-project/vllm-ascend #6475"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - fia
  - tnd
  - graph-mode
  - padding
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6475"
---

# PR Insight: vllm-project/vllm-ascend #6475

**Title:** [ModelRunner][Fix] Pads query_start_loc to satisfy FIA/TND constraint

## Overview
This PR reverts the previous reversion of query_start_loc padding and fixes the implementation to properly handle both uniform and mixed batches. It consolidates ad-hoc padding into a single helper, copies updated buffers to device, and removes strict assertions that cause false alarms with MLA + PIECEWISE.

## Technical Significance
Properly addresses FIA/TND constraint requirements for graph mode execution on Ascend. The fix handles mixed batch scenarios by inserting dummy requests and ensures correct kernel shapes to prevent mismatches or failures during full graph execution.

## Related
- `technique-graph-mode`