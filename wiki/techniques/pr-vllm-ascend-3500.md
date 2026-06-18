---
id: technique-pr-vllm-ascend-3500
title: "PR Insight: vllm-project/vllm-ascend #3500"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - hccl-optimization
  - speculative-decoding
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3500"
---

# PR Insight: vllm-project/vllm-ascend #3500

**Title:** Revert "[BUGFIX] Mtp torchair pd fix (#3449)"

## Overview
<!--

## Technical Significance
Reverts MTP TorchAir PD fix due to issues, restoring previous implementation.

## Related
- `technique-speculative-decoding`
