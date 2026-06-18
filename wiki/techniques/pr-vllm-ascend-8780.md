---
id: technique-pr-vllm-ascend-8780
title: "PR Insight: vllm-project/vllm-ascend #8780"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - sequence-parallel
  - graph-compilation
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8780"
---

# PR Insight: vllm-project/vllm-ascend #8780

**Title:** [BugFix][SP] Preserve graph stringification in MoE sequence parallel pass

## Overview
This PR preserves graph stringification behavior in the `SequenceParallelismMoePass` debug logging. A previous optimization to use lazy logging changed the behavior such that `str(graph)` was only evaluated when debug logging was enabled. However, this eager graph stringification was observable and affected the sequence parallel MoE compilation flow in 2-card e2e tests. The fix explicitly calls `str(graph)` in the logger calls to preserve the previous behavior.

## Technical Significance
This fix addresses a subtle side-effect issue where graph stringification for debug logging was affecting compilation flow. In PyTorch's FX graph manipulation, certain operations can have side effects or trigger internal state changes. The eager stringification was part of the compilation process, and the lazy optimization inadvertently broke this dependency. The fix ensures deterministic compilation behavior for sequence parallel MoE workloads across different logging configurations.

## Related
- `kernel-moe-ascendc`
- `technique-pipeline-scheduling`
- `technique-hccl-optimization`