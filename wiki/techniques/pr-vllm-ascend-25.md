---
id: technique-pr-vllm-ascend-25
title: "PR Insight: vllm-project/vllm-ascend #25"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - distributed
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/25"
---

# PR Insight: vllm-project/vllm-ascend #25

**Title:** [attn] fix device of tensors in attention

## Overview
This PR fixes a device placement bug in AscendAttentionBackendImpl where tensors like attention masks were being created on card-0 by default instead of the correct device card. The fix ensures proper multi-card support by creating tensors on the device matching the input.

## Technical Significance
Critical for distributed inference across multiple Ascend NPUs. Without this fix, specifying devices other than npu:0 would cause device conflicts. The change enables proper tensor placement in attention operations for local rank-based device selection.

## Related
- kernel-attention
- technique-hccs-optimization