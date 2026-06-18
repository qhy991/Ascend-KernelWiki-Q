---
id: technique-pr-vllm-ascend-9739
title: "PR Insight: vllm-project/vllm-ascend #9739"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - rope
  - quantization
  - dsa
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9739"
---

# PR Insight: vllm-project/vllm-ascend #9739

**Title:** [BugFix][A2/A3]Preserve fp32 RoPE sin/cos for DSA compressor and rota…

## Overview
This PR addresses RoPE (Rotary Position Embedding) handling in DSA compressor contexts, ensuring that fp32 sin/cos values are preserved correctly. The fix prevents precision degradation that could occur during compression and rotation operations.

## Technical Significance
Maintains numerical precision in RoPE computations by preserving fp32 sin/cos values through DSA compressor and rotation operations. Prevents accuracy loss that would otherwise occur from premature dtype conversion, particularly important for long-context scenarios where position embedding errors accumulate.

## Related
- `technique-rope`, `technique-dsa`, `kernel-rope`