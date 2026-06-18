---
id: technique-pr-vllm-ascend-6006
title: "PR Insight: vllm-project/vllm-ascend #6006"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - graph-fusion
  - npugraph
  - matmul
  - rmsnorm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6006"
---

# PR Insight: vllm-project/vllm-ascend #6006

**Title:** [Graph][Fusion] Add MatmulAllReduceAddRMSNorm graph fusion for npugraph_ex.

## Overview
This PR builds on PR #5011 to enhance the npu_graph_ex_passes module by adding MatmulAllReduceAddRMSNorm graph fusion support for scenarios with bias terms. It ensures the fusion pattern is correctly registered and matched into the computation graph.

## Technical Significance
Graph fusions combine multiple operators into a single kernel, reducing memory transfers and improving performance. MatmulAllReduceAddRMSNorm is a common pattern in transformer models (FFN layers). The PR adds support for this fusion when bias is present, expanding the npugraph_ex optimization coverage. It also includes ST test cases for regression monitoring, ensuring the fusion works correctly and doesn't introduce correctness issues.

## Related
- `technique-graph-fusion`, `technique-npugraph`, `technique-operator-fusion`