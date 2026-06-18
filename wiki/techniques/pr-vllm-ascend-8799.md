---
id: technique-pr-vllm-ascend-8799
title: "PR Insight: vllm-project/vllm-ascend #8799"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - specdecode
  - extract-hidden-states
  - acl-graph
  - kv-cache
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8799"
---

# PR Insight: vllm-project/vllm-ascend #8799

**Title:** [SpecDecode][Feature] Implement AscendExtractHiddenStatesProposer for speculative decoding

## Overview
This PR implements `AscendExtractHiddenStatesProposer` to support the `extract_hidden_states` speculative decoding method on Ascend NPUs. The implementation adapts the base proposer to use ACL graphs for efficiency and implements Ascend-specific logic for preparing next token IDs. The model runner is updated to support KV cache allocation and reshaping for `cache_only_layers` used by this decoding method.

## Technical Significance
The extract_hidden_states method is a speculative decoding approach where the draft model outputs hidden states that are fed directly to the main model rather than requiring explicit token generation. This can improve speculation accuracy and reduce draft model computation. The ACL graph integration leverages Ascend's compiled graph capabilities for efficient inference. Proper KV cache handling for cache_only_layers ensures that only necessary layers maintain KV cache state, reducing memory footprint.

## Related
- `pattern-specdecode`
- `kernel-attention-ascendc`
- `technique-kv-cache-paging`