---
id: technique-pr-vllm-ascend-3892
title: "PR Insight: vllm-project/vllm-ascend #3892"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - aclgraph
  - graph-mode
  - spec-decoding
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3892"
---

# PR Insight: vllm-project/vllm-ascend #3892

**Title:** [Feat] Support MTP to running in full graph mode

## Overview
This PR enables Multi-Token Proposal (MTP) speculative decoding to run in FULL_DECODE_ONLY graph mode for improved performance. The changes include isolating main model and MTP data with `_mtp_graph_params`, padding metadata in mla_v1 for fullgraph mode, fixing essential data addresses for model.forward, adapting to ACLGraph capture framework by rebuilding MTP model with ACLGraphWrapper, adding common attention metadata updates in MTP, and adapting data update for multiple speculative tokens.

## Technical Significance
Running MTP in full graph mode significantly improves speculative decoding performance on Ascend NPUs by reducing Python overhead and enabling better operator fusion. The technical challenge involves properly handling different data paths for main model vs MTP model in graph capture mode, ensuring attention metadata is correctly padded and updated, and maintaining correctness when num_speculative_tokens > 1. This represents a major performance optimization for MTP-based speculative decoding.

## Related
- `technique-spec-decoding`, `technique-aclgraph`, `technique-graph-capture`, `technique-mtp`