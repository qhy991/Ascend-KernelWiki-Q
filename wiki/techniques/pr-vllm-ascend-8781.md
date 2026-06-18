---
id: technique-pr-vllm-ascend-8781
title: "PR Insight: vllm-project/vllm-ascend #8781"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - specdecode
  - eagle
  - testing
  - pcp
  - dcp
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8781"
---

# PR Insight: vllm-project/vllm-ascend #8781

**Title:** [Test][SpecDecode] Add tests for set_inputs_first_pass

## Overview
This PR adds comprehensive unit test coverage for the `set_inputs_first_pass` method in `AscendEagleProposer` and `AscendDraftModelProposer`. The tests cover multiple scenarios: default EAGLE pathway (needs_extra_input_slots=False), PCP/DCP mixed scenario with pcp_size > 1, draft model case (extra slots, no shift), and parallel drafting case (extra slots, with shift).

## Technical Significance
Comprehensive test coverage for speculative decoding proposers is critical for ensuring correctness across different drafting configurations. EAGLE (Extrapolation Algorithm for Greater Language-model Efficiency) uses various drafting strategies including PCP (Prefill Cache Picking) and DCP (Decode Cache Picking). The `set_inputs_first_pass` method handles input tensor preparation for the first decoding pass, which is particularly complex when dealing with extra input slots and shift operations in parallel drafting scenarios.

## Related
- `pattern-specdecode`
- `kernel-attention-ascendc`
- `technique-kv-cache-paging`