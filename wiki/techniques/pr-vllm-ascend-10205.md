---
id: technique-pr-vllm-ascend-10205
title: "PR Insight: vllm-project/vllm-ascend #10205"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - communication
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10205"
---

# PR Insight: vllm-project/vllm-ascend #10205

**Title:** [BugFix][Performance] Fix MTP copy_valid_sampled_token_count sync

## Overview
This PR fixes a performance issue in Multi-Token Prediction (MTP) where the `copy_` operation in `copy_valid_sampled_token_count` was causing unnecessary host blocking. The root cause was a dtype mismatch: `valid_sampled_token_count_cpu` was `torch.int32` while `valid_sampled_token_count_gpu` was `torch.int64`, causing the operator to generate implicit dtype casting that triggered blocking synchronization. The fix explicitly converts the dtype to match, eliminating the synchronization overhead.

## Technical Significance
This PR demonstrates the importance of dtype consistency for avoiding implicit synchronization in PyTorch/NPU operations. Implicit dtype conversions can trigger host-device synchronization, which is particularly detrimental in inference workloads like MTP where performance is critical. By ensuring explicit dtype matching, this fix eliminates the blocking synchronization and restores performance. This pattern is generally applicable: always match dtypes explicitly across CPU/GPU tensor operations to avoid unintended synchronization points.

## Related
- `technique-mtp`
- `technique-dtype-optimization`
- `technique-host-device-sync`