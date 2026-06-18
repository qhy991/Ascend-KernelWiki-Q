---
id: technique-pr-vllm-ascend-6416
title: "PR Insight: vllm-project/vllm-ascend #6416"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - event-sync
  - bugfix
  - c++
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6416"
---

# PR Insight: vllm-project/vllm-ascend #6416

**Title:** fix: resolve sync bug in DispathFFNCombine when expert num per card is 32

## Overview
This PR fixes a synchronization deadlock issue in the `DispathFFNCombine` module that occurs on NPU cards when the number of experts per card exceeds 16, with the bug manifesting prominently at 32 or 128 experts. The fix modifies C++ kernel files including `dispatch_ffn_combine_kernel.hpp` and related utility headers to resolve the synchronization logic.

## Technical Significance
MoE (Mixture of Experts) inference heavily relies on expert dispatch and combine operations. The deadlock occurred due to synchronization issues when scaling to larger expert counts, which is essential for large-scale MoE models. The fix addresses NPU-specific synchronization patterns, likely involving event synchronization between compute units and ensuring proper barrier handling across expert parallel dispatch operations.

## Related
- `kernel-moe`
- `technique-event-sync`
- `pattern-moe-dispatch`