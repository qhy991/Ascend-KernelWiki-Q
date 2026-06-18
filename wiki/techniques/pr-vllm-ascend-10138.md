---
id: technique-pr-vllm-ascend-10138
title: "PR Insight: vllm-project/vllm-ascend #10138"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bincount
  - triton
  - repetition-penalty
  - grid-overflow
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10138"
---

# PR Insight: vllm-project/vllm-ascend #10138

**Title:** [Bugfix] Fix bincount Triton kernel grid overflow with repetition_penalty

## Overview
This PR fixes grid overflow issues in the bincount Triton kernel when using repetition_penalty. The kernel would exceed grid size limits under certain conditions, causing execution failures.

## Technical Significance
Fixes grid size management in bincount kernel to prevent overflow when repetition_penalty is applied. Ensures that the kernel runs correctly within hardware grid size limits, preventing failures during sampling with repetition penalty.

## Related
- `kernel-triton`, `kernel-bincount`, `technique-sampling`, `pattern-grid-management`