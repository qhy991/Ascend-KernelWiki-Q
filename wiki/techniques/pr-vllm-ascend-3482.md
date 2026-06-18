---
id: technique-pr-vllm-ascend-3482
title: "PR Insight: vllm-project/vllm-ascend #3482"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - hccl-optimization
  - decode
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3482"
---

# PR Insight: vllm-project/vllm-ascend #3482

**Title:** [Fix] Clears unused slot mappings and fix accuracy issue with MLA models when enabling `FULL_DECODE_ONLY`

## Overview
MLA and GQA use different computation logic: MLA slice batches and only compute on the actually valid tokens. That means outer padding must be handled carefully — the accuracy issue this PR fixes was caused by stale data in `slot_mapping` being reused by subsequent inference steps.

## Technical Significance
Clears unused slot mappings and fixes accuracy issues with MLA models when enabling FULL_DECODE_ONLY mode.

## Related
- `hw-cube-unit`
