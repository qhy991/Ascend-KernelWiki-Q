---
id: technique-pr-vllm-ascend-3221
title: "PR Insight: vllm-project/vllm-ascend #3221"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3-next
  - tp
  - moe
  - upstream-sync
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3221"
---

# PR Insight: vllm-project/vllm-ascend #3221

**Title:** [BugFix] Fix Qwen3-Next because of TP Attn + EP MoE modified

## Overview
This PR fixes Qwen3-Next inference failures caused by upstream vLLM changes to the TP (Tensor Parallel) Attention + EP (Expert Parallel) MoE module from PR #24982. The upstream changes introduced breaking changes that required adaptation.

## Technical Significance
Combining TP attention with EP MoE is a complex configuration that requires careful coordination between tensor and expert parallelism. The upstream changes modified this coordination, requiring fixes to maintain compatibility. This demonstrates the complexity of maintaining parallelism features across different backends.

## Related
- `kernel-qwen3-next-ascendc`, `technique-expert-parallelism`, `pattern-upstream-sync`