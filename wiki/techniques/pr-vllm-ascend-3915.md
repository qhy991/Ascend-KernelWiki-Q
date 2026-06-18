---
id: technique-pr-vllm-ascend-3915
title: "PR Insight: vllm-project/vllm-ascend #3915"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/3915"
---

# PR Insight: vllm-project/vllm-ascend #3915

**Title:** [Bugfix] Fix MTP support for lmhead_tensor_parallel_size

## Overview
This PR fixes a bug where enabling MTP with `lmhead_tensor_parallel_size=16` caused inference to hang. The fix addresses issues in vocab parallel embedding and model runner to ensure proper MTP operation with large language head tensor parallelism.

## Technical Significance
Language head tensor parallelism is used for very large models where the output vocabulary layer is too large for a single device. The hang bug reveals synchronization or data flow issues when combining MTP with lm_head TP. Proper support is essential for deploying large-scale models with MTP on multiple Ascend NPUs.

## Related
- `technique-mtp`, `technique-tensor-parallel`, `technique-vocab-parallel`, `pattern-synchronization`