---
id: technique-pr-vllm-ascend-242
title: "PR Insight: vllm-project/vllm-ascend #242"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - bugfix
  - cann
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/242"
---

# PR Insight: vllm-project/vllm-ascend #242

**Title:** [Fix] Remove npu_group_topk before CANN version update

## Overview
This PR removes the npu_group_topk function from fused_moe.py as a workaround before a CANN (Compute Architecture for Neural Networks) version update. The change adds 16 lines and removes 3.

## Technical Significance
The npu_group_topk function likely relies on CANN operators that are being updated. Removing it temporarily prevents compatibility issues while waiting for the new CANN release. This shows the dependency between vllm-ascend and CANN library versions.

## Related
- kernel-moe