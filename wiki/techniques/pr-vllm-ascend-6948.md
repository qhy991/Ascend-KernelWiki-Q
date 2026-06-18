---
id: technique-pr-vllm-ascend-6948
title: "PR Insight: vllm-project/vllm-ascend #6948"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - fullgraph
  - d-nodes
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6948"
---

# PR Insight: vllm-project/vllm-ascend #6948

**Title:** [v0.16.0][P/D][Bugfix] Support ALL D-Nodes in fullgraph when running MTP in PD

## Overview
Fixes a bug in v0.16.0 recompute_scheduler for MTP (Multi-Token Prediction) models running in fullgraph mode with parallel disaggregation. The fix ensures all D-Nodes are properly supported in fullgraph scenarios.

## Technical Significance
Resolves performance issues in MTP with fullgraph by fixing the recompute scheduler logic. The improvement reduced ITL (inter-token latency) from 75ms to 67ms, demonstrating significant performance gains.

## Related
- `technique-mtp`, `technique-fullgraph`, `technique-d-nodes`, `technique-recompute`