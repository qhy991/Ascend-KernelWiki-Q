---
id: technique-pr-vllm-ascend-5574
title: "PR Insight: vllm-project/vllm-ascend #5574"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - prefill-decode
  - kvpool
  - mooncake
  - cleanup
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5574"
---

# PR Insight: vllm-project/vllm-ascend #5574

**Title:** [P/D]Remove mooncake kvpool unused parameter `local_hostname`

## Overview
This PR removes the unused `local_hostname` parameter from the Mooncake KV pool backend, as the local IP is obtained directly via `get_ip()` instead. The cleanup eliminates confusion by removing redundant configuration parameters.

## Technical Significance
Removing unused parameters improves API clarity and reduces configuration complexity for the Mooncake KV pool system. This cleanup ensures that the API reflects actual usage patterns and prevents user confusion when configuring the prefill-decode disaggregated inference system.

## Related
- `technique-prefill-decode` (Prefill-decode disaggregation)
- `technique-kv-transfer` (KV cache transfer)
- `kernel-kv-cache` (KV pool management)