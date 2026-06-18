---
id: technique-pr-vllm-ascend-2988
title: "PR Insight: vllm-project/vllm-ascend #2988"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-cache
  - nz-format
  - deepseek
  - decode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2988"
---

# PR Insight: vllm-project/vllm-ascend #2988

**Title:** [Bugfix] fix kv nz accuracy bug

## Overview
This PR fixes a KV cache NZ format accuracy bug in DeepSeek R1 models. When enable_kv_nz is true, the output was invalid due to incorrect usage of torch_npu.npu_kv_rmsnorm_rope_cache during the decode stage, producing corrupted output text.

## Technical Significance
The fix ensures correctness of KV cache NZ format operations during the decode phase. NZ format improves memory bandwidth utilization but requires careful handling of rope cache normalization. The bug caused complete output corruption, highlighting the importance of correct operator usage in NZ format workflows.

## Related
- `technique-nz-format`, `technique-kv-cache-paging`, `kernel-deepseek-ascendc`