---
id: technique-pr-vllm-ascend-8828
title: "PR Insight: vllm-project/vllm-ascend #8828"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - specdecode
  - eagle
  - testing
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8828"
---

# PR Insight: vllm-project/vllm-ascend #8828

**Title:** [Test][SpecDecode] Add prepare_inputs UTs

## Overview
This PR adds comprehensive unit tests for `AscendEagleProposer.prepare_inputs` and `prepare_inputs_padded` methods. The test coverage includes scenarios with and without token rejection, single request handling, and validation of critical output fields including token_indices, num_actual_tokens, query_start_loc, token_indices_to_sample, and num_rejected_tokens_gpu.

## Technical Significance
EAGLE speculative decoding relies on complex input preparation logic that handles token rejection and batching. The `prepare_inputs` methods must correctly identify which proposed tokens were accepted or rejected by the main model and prepare the input tensors for the next drafting iteration. Comprehensive test coverage ensures correctness across rejection scenarios, which is essential for speculative decoding accuracy and performance.

## Related
- `pattern-specdecode`
- `kernel-attention-ascendc`
- `technique-kv-cache-paging`