---
id: technique-pr-vllm-ascend-3005
title: "PR Insight: vllm-project/vllm-ascend #3005"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - async-copy
  - synchronization
  - single-expert
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3005"
---

# PR Insight: vllm-project/vllm-ascend #3005

**Title:** [Bugfix] Fix async copy bug under single expert scenario

## Overview
This PR adds missing barrier synchronization when no implicit synchronize by repeat_interleave is available. Without this fix, async copies of output_splits and input_splits from NPU with non_blocking=True might not complete before later async_all_to_all operations use them.

## Technical Significance
The fix addresses a race condition in async memory operations for single expert scenarios. Proper synchronization is critical for correctness when using non-blocking memory copies and collective communication, preventing data corruption and ensuring reliable execution.

## Related
- `kernel-moe-ascendc`, `technique-event-sync`, `technique-async-copy`