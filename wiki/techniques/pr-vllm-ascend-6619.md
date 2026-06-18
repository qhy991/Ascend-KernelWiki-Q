---
id: technique-pr-vllm-ascend-6619
title: "PR Insight: vllm-project/vllm-ascend #6619"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - test-fix
  - triton
  - fusion
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6619"
---

# PR Insight: vllm-project/vllm-ascend #6619

**Title:** [fix bug] fix tensor mismatch bug in sigmoid operate test case

## Overview
This PR fixes a test case bug in test_triton_fusion_ops where a recurrent state tensor was being modified in-place by the fused kernel and then reused for the split implementation path, causing incorrect comparisons. The fix creates separate tensors for each path and changes initialization from torch.randn to torch.ones for determinism.

## Technical Significance
Fixes test correctness issues by ensuring proper tensor isolation between test paths. The change prevents false negatives in fusion kernel validation by maintaining test integrity and determinism.

## Related
- `technique-operator-fusion`