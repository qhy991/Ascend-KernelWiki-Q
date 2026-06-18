---
id: technique-pr-vllm-ascend-7455
title: "PR Insight: vllm-project/vllm-ascend #7455"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - cudagraph
  - accuracy-testing
  - logprob-comparison
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7455"
---

# PR Insight: vllm-project/vllm-ascend #7455

**Title:** [Misc] Refactor aclgraph accuracy test to use logprob-based comparison

## Overview
This PR refactors ACLGraph accuracy tests to use a two-tier logprob accuracy check instead of text-match assertions. For prefill (token 0), it asserts token ID matches and logprob within atol. For decode (tokens 1-2), if chosen tokens match, compare logprobs directly; if they differ, cross-lookup baseline token in compiled top-20 distribution and assert logprob within decode_atol.

## Technical Significance
This refactoring matters for graph mode validation on Ascend. Text-match assertions were too brittle for floating-point differences in compiled mode. The logprob-based approach tolerates minor argmax drift from floating-point differences while still catching distribution divergence, enabling more robust accuracy testing of compiled graphs.

## Related
- technique-graph-mode
- pattern-accuracy-testing