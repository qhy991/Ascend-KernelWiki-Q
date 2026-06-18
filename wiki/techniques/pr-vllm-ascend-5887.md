---
id: technique-pr-vllm-ascend-5887
title: "PR Insight: vllm-project/vllm-ascend #5887"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - xlite
  - aclgraph
  - bugfix
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5887"
---

# PR Insight: vllm-project/vllm-ascend #5887

**Title:** [v0.13.0][Bugfix] Fix XliteModelRunner init failed when aclgraph is enabled

## Overview
This PR fixes an initialization failure in XliteModelRunner when aclgraph is enabled. The issue occurred because the graph_capture function from vllm.v1.worker.gpu_model_runner was not properly replaced with the Ascend-specific implementation.

## Technical Significance
Xlite is a graph execution optimization for Ascend NPU. When aclgraph is enabled, the system needs to use the correct graph capture function. The fix ensures that vllm's default graph_capture is replaced with the Ascend-specific implementation, preventing initialization failures. This allows Xlite to work correctly with aclgraph mode, enabling graph optimizations for the Xlite runtime.

## Related
- `technique-xlite`, `technique-aclgraph`, `technique-graph-optimization`