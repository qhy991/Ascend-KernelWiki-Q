---
id: technique-pr-vllm-ascend-352
title: "PR Insight: vllm-project/vllm-ascend #352"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - rope
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/352"
---

# PR Insight: vllm-project/vllm-ascend #352

**Title:** [Ops] Use forward_native of rope in batched rope situation or when rotary dim is not equal to head dim.

## Overview
This PR fixes rope embedding by falling back to forward_native in batched scenarios or when rotary dimension differs from head dimension. The change is minimal (2 additions, 3 deletions).

## Technical Significance
Custom RoPE kernels may not handle all tensor shapes correctly. This fix ensures correctness by using the native implementation when custom kernels aren't applicable, preventing errors in edge cases like partial RoPE or batched operations.

## Related
- technique-rope