---
id: technique-pr-vllm-ascend-6590
title: "PR Insight: vllm-project/vllm-ascend #6590"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - batch-invariant
  - ascendc
  - triton
  - operator-selection
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6590"
---

# PR Insight: vllm-project/vllm-ascend #6590

**Title:** implement batch invariant with ascendc

## Overview
This PR implements batch invariant operations using AscendC kernels alongside existing Triton implementations. It adds logic to choose between Triton and AscendC implementations for batch invariant operations, providing flexibility and optimization opportunities.

## Technical Significance
Enables batch invariant operations with AscendC implementations, allowing selection between Triton and AscendC backends based on performance or compatibility requirements. This provides flexibility in deploying batch invariant operations across different scenarios.

## Related
- `technique-batch-invariant`