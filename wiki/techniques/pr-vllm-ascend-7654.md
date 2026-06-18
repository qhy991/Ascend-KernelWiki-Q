---
id: technique-pr-vllm-ascend-7654
title: "PR Insight: vllm-project/vllm-ascend #7654"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - hccl-optimization
  - distributed
  - performance
  - process-group
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7654"
---

# PR Insight: vllm-project/vllm-ascend #7654

**Title:** [Feature] Reuse equivalent HCCL process groups on Ascend

## Overview
This PR introduces HCCL process group reuse optimization for Ascend distributed inference. It modifies the HCCL process group registry and distributed patching to reuse equivalent process groups instead of creating new ones.

## Technical Significance
Reduces communication overhead and resource usage in multi-GPU distributed inference by reusing HCCL process groups. This optimization improves scaling efficiency for tensor parallel and pipeline parallel workloads.

## Related
- `technique-hccl-optimization`, `pattern-distributed-inference`, `hw-hccs`, `technique-process-group-management`