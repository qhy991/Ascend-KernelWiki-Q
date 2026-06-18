---
id: technique-pr-vllm-ascend-5899
title: "PR Insight: vllm-project/vllm-ascend #5899"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - xlite
  - aclgraph
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5899"
---

# PR Insight: vllm-project/vllm-ascend #5899

**Title:** [Bugfix] Fix XliteModelRunner init failed when aclgraph is enabled

## Overview
This PR fixes an initialization failure in XliteModelRunner when aclgraph is enabled on the main branch. The issue occurred because the graph_capture function from vllm.v1.worker.gpu_model_runner was not properly replaced with the Ascend-specific implementation.

## Technical Significance
Xlite is a graph execution optimization for Ascend NPU. When aclgraph is enabled, the system needs to use the correct graph capture function. The fix ensures that vllm's default graph_capture is replaced with the Ascend-specific implementation in model_runner_v1.py, preventing initialization failures. This allows Xlite to work correctly with aclgraph mode, enabling graph optimizations.

## Related
- `technique-xlite`, `technique-aclgraph`, `technique-graph-optimization`