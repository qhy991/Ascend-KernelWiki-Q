---
id: technique-pr-vllm-ascend-9489
title: "PR Insight: vllm-project/vllm-ascend #9489"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - 310p
  - rmsnorm-gated
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9489"
---

# PR Insight: vllm-project/vllm-ascend #9489

**Title:** [Performance][310p] Discard native RmsNormGated ops on 310P

## Overview
This PR improves performance on Ascend 310P by discarding native RmsNormGated operations in favor of alternative implementations. The change affects 310P-specific layer normalization code.

## Technical Significance
Native operations may not be optimal on all hardware architectures. Discarding RmsNormGated on 310P and using alternative implementations can provide better performance for this specific device, demonstrating the importance of architecture-specific optimization.

## Related
- `hw-vector-unit`
- `kernel-layernorm`