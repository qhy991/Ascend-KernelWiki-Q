---
id: technique-pr-vllm-ascend-6860
title: "PR Insight: vllm-project/vllm-ascend #6860"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - aclgraph
  - spec-decode
  - full-graph
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6860"
---

# PR Insight: vllm-project/vllm-ascend #6860

**Title:** [Feature] Support the merged graph for mtp

## Overview
Adds support for merged ACL graph execution in MTP (Multi-Token Prediction) speculative decoding. The implementation includes adding `AscendAttentionState.SpecDecoding` in eagle_proposer for MLA and SFA, modifying `update_graph_params` in MLA to support draft model full graph, adding persistent tensors for `seq_lens` and `query_start_loc`, and updating padding logic in eagle_proposer.

## Technical Significance
Enables more efficient MTP execution by supporting full graph mode for draft models, reducing overhead from graph switching. The merged graph approach maintains stateful tensor requirements needed for SFA while optimizing speculative decoding performance.

## Related
- `technique-mtp`, `technique-aclgraph`, `technique-spec-decode`, `technique-mla`