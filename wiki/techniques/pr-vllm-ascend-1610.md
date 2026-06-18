---
id: technique-pr-vllm-ascend-1610
title: "PR Insight: vllm-project/vllm-ascend #1610"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - expert-parallel
  - graph-mode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1610"
---

# PR Insight: vllm-project/vllm-ascend #1610

**Title:** [Bugfix] graph batch size round up to tp size, when enable expert par…

## Overview
This PR fixes graph mode batch size handling when expert parallel is enabled, ensuring correct tensor shapes.

## Technical Significance
Corrects batch size calculation in graph mode to round up to tensor parallel size when expert parallel is active. This prevents shape mismatches in graph compilation that caused failures for distributed MoE inference.

## Related
- `kernel-moe`
- `technique-expert-parallel`
- `technique-graph-mode`