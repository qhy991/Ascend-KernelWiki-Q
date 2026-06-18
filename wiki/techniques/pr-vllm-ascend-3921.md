---
id: technique-pr-vllm-ascend-3921
title: "PR Insight: vllm-project/vllm-ascend #3921"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - tensor-parallel
  - bugfix
  - spec-decoding
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3921"
---

# PR Insight: vllm-project/vllm-ascend #3921

**Title:** [Bugfix] fix MTP support for lmhead_tensor_parallel_size

## Overview
This PR is a duplicate fix of PR #3915 for the same issue: enabling MTP with `lmhead_tensor_parallel_size=16` caused inference to hang. The fix addresses vocab parallel embedding and model runner issues to ensure proper MTP operation with large language head tensor parallelism.

## Technical Significance
The duplicate fix suggests this was a critical bug affecting multiple branches or required multiple fix attempts. Language head tensor parallelism combined with MTP reveals complex interactions in data flow and synchronization that need careful handling to avoid hangs in distributed inference scenarios.

## Related
- `technique-mtp`, `technique-tensor-parallel`, `technique-vocab-parallel`, `pattern-synchronization`