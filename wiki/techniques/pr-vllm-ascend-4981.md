---
id: technique-pr-vllm-ascend-4981
title: "PR Insight: vllm-project/vllm-ascend #4981"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - revert
  - mtp
  - kv-transfer
  - pp
  - deepseekv3
  - pd
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4981"
---

# PR Insight: vllm-project/vllm-ascend #4981

**Title:** Revert "[Bugfix] support mtp kv transfer and pp partition by hand in kv transfer (#4892)"

## Overview
This PR reverts commit 332b547728c24a900a40c47a4eba6f5048117efc which added MTP KV transfer and PP partition support. The reversion is due to breaking DeepSeekV3.2 in PD (prefill-decode disaggregation) scenarios.

## Technical Significance
Rollback of PR #4892 due to incompatibility with DeepSeekV3.2 PD deployments. The fix needs to be redesigned to handle all scenarios correctly.

## Related
- `technique-kv-transfer`
- `technique-pipeline-parallelism`
- `technique-pd-disaggregation`
- `kernel-deepseekv3`
- `technique-mtp`