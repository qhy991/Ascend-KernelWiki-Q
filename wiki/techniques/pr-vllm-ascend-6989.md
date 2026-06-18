---
id: technique-pr-vllm-ascend-6989
title: "PR Insight: vllm-project/vllm-ascend #6989"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - fia
  - installation
  - cann-8.5.1
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6989"
---

# PR Insight: vllm-project/vllm-ascend #6989

**Title:** [bugs] fix install FIA sh

## Overview
Updates the replacement shell script for the FIA (Fused Infer Attention Score) operator FD feature in CANN 8.5.1. The fix addresses installation issues with the FIA operator on updated CANN versions.

## Technical Significance
Ensures correct installation of FIA operators on CANN 8.5.1 by updating the shell script to handle changes in the operator distribution. This maintains compatibility with the latest CANN updates and enables FIA features.

## Related
- `technique-fia`, `technique-attention`, `technique-installation`