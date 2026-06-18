---
id: technique-pr-vllm-ascend-530
title: "PR Insight: vllm-project/vllm-ascend #530"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - rope
  - ascendc
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/530"
---

# PR Insight: vllm-project/vllm-ascend #530

**Title:** adopt rope in vllm-ascend

## Overview
This PR adopts the custom AscendC rotary embedding kernel in production inference. The C++ implementation generates contiguous query/key tensors, reducing overhead compared to torch_npu's rope which requires contiguous() and index_select() operations.

## Technical Significance
Leverages the custom kernel infrastructure from PR #233 in production. Contiguous tensor generation on the C++ side avoids Python-side memory operations, improving RoPE performance. Currently supports is_neox=True scenarios.

## Related
- technique-rope
- technique-ascendc