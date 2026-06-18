---
id: technique-pr-vllm-ascend-5665
title: "PR Insight: vllm-project/vllm-ascend #5665"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ffn
  - tensorlist
  - dispatch-ffn
  - ascendc
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5665"
---

# PR Insight: vllm-project/vllm-ascend #5665

**Title:** support TensorList for dispatchFFNCombine

## Overview
This PR adds TensorList support to the dispatchFFNCombine operator, implementing host-side and kernel-side changes to handle TensorList inputs in the FFN dispatch and combination operations.

## Technical Significance
Enhances the dispatchFFNCombine operator to support TensorList inputs, which is important for handling variable-length sequences and batched operations more efficiently. The changes span both host-side C++ code for operator registration and kernel-side implementations for tiling and execution strategies.

## Related
- `kernel-ffn-ascendc`, `technique-operator-fusion`, `technique-tensorlist`