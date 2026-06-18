---
id: technique-pr-vllm-ascend-5758
title: "PR Insight: vllm-project/vllm-ascend #5758"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - dispatch-gmm-combine
  - eagle3
  - moe
  - w8a8
  - speculative-decoding
  - configuration
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5758"
---

# PR Insight: vllm-project/vllm-ascend #5758

**Title:** [Feature]Enable DispatchGmmCombineDecode when eagle is moe with w8a8 or not moe [RFC: issue 5476]

## Overview
This PR refines the logic for enabling the `DispatchGmmCombineDecode` operator during EAGLE/EAGLE-3 speculative decoding. The operator does not support non-W8A8 scenarios and cannot share communication domains with standard `Dispatch`/`Combine` operators. The fix enables `DispatchGmmCombineDecode` only when the draft model uses a non-MoE architecture or is MoE with W8A8 quantization, rather than unconditionally disabling it for all EAGLE scenarios. The implementation updates the utility functions in `utils.py` to check draft model configuration precisely.

## Technical Significance
This optimization enables more efficient speculative decoding by allowing the fused `DispatchGmmCombineDecode` operator to be used in compatible EAGLE scenarios. The previous blanket disable was too conservative and prevented performance improvements when the draft model architecture was compatible. The refined logic checks whether the draft model is MoE with non-W8A8 quantization, and only disables the operator in that specific case. Testing on Qwen3-235B with EAGLE-3 speculative decoding shows maintained accuracy (80.00% on aime2024), confirming the correctness of the refined operator selection logic.

## Related
- `technique-speculative-decoding`, `technique-eagle3`, `technique-moe`, `technique-w8a8`, `technique-operator-fusion`