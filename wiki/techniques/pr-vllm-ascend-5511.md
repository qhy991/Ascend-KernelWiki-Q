---
id: technique-pr-vllm-ascend-5511
title: "PR Insight: vllm-project/vllm-ascend #5511"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - kv-transfer
  - pipeline-parallelism
  - mooncake
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5511"
---

# PR Insight: vllm-project/vllm-ascend #5511

**Title:** [Recover] [Bugfix] support mtp kv transfer and pp partition by hand in kv transfer (#4892) (revert in #4981)

## Overview
This PR recovers functionality from PR #4892 (previously reverted in #4981) that supports MTP KV transfer and manual pipeline parallelism partition in KV transfer. The recovery addresses potential bugs that could affect DeepSeek3.2 in prefill-decode scenarios.

## Technical Significance
Restoring MTP KV transfer with manual pipeline parallelism partitioning enables better resource utilization and communication optimization for speculative decoding in distributed inference scenarios. The KV transfer mechanism reduces redundant computation across pipeline stages while maintaining correctness for complex models like DeepSeek3.2.

## Related
- `technique-speculative-decoding` (MTP algorithm)
- `technique-kv-transfer` (KV cache transfer)
- `technique-pipeline-parallelism` (Pipeline parallel optimization)
- `kernel-deepseek` (DeepSeek model support)