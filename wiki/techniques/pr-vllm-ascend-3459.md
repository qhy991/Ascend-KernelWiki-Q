---
id: technique-pr-vllm-ascend-3459
title: "PR Insight: vllm-project/vllm-ascend #3459"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - hccl-optimization
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3459"
---

# PR Insight: vllm-project/vllm-ascend #3459

**Title:** [bugfix] fix pipeline parallel for mla & sfa attention backend

## Overview
Fix pipeline parallel break for mla & sfa attention backend caused by a magic number in metadata builder. The error report:

## Technical Significance
Fixes pipeline parallel implementation for MLA and SFA attention backends to ensure correct metadata handling.

## Related
- `hw-cube-unit`
- `technique-hccl-optimization`
