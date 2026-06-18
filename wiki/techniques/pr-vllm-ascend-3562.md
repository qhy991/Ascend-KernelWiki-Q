---
id: technique-pr-vllm-ascend-3562
title: "PR Insight: vllm-project/vllm-ascend #3562"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mrope
  - rotary-embedding
  - operator-fusion
  - accuracy
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3562"
---

# PR Insight: vllm-project/vllm-ascend #3562

**Title:** Revert "Add mrope op fusion (#3509)"

## Overview
This PR reverts the MRoPE (Multi-head Rotary Position Embedding) operator fusion optimization from PR #3509 due to accuracy problems. The revert removes the fusion implementation from `vllm_ascend/ops/rotary_embedding.py` (35 lines deleted) and updates test files accordingly, removing 85 lines of test code that validated the fusion operator.

## Technical Significance
The MRoPE fusion was intended to improve performance but introduced accuracy degradation. This revert underscores the importance of thorough correctness validation for operator fusions, particularly for position encoding operations that critically affect model accuracy. Rotary embedding operations must maintain exact numerical properties for correct token position representation.

## Related
- `technique-rotary-embedding`
- `technique-operator-fusion`
- `technique-mrope`