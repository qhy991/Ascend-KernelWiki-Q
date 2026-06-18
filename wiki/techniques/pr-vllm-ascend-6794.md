---
id: technique-pr-vllm-ascend-6794
title: "PR Insight: vllm-project/vllm-ascend #6794"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eplb
  - fused-mc2
  - moe
  - quantization
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6794"
---

# PR Insight: vllm-project/vllm-ascend #6794

**Title:** [EPLB][bugfix] Bugfix for fused mc2

## Overview
This PR fixes bugs related to fused mc2 functionality in the EPLB system, specifically affecting quantization and MoE communication paths. The fix addresses correctness issues in the expert parallelism load balancing implementation.

## Technical Significance
Resolves functional issues in EPLB's fused mc2 operations that impact both MoE and quantized workloads. The fix ensures correct behavior when combining expert selection with communication fusion.

## Related
- `technique-kv-cache-paging`
- `kernel-moe`