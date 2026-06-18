---
id: technique-pr-vllm-ascend-10477
title: "PR Insight: vllm-project/vllm-ascend #10477"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - distributed
  - kv-cache
  - ssd
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10477"
---

# PR Insight: vllm-project/vllm-ascend #10477

**Title:** [Feature] SSD support multiple DP in each machine

## Overview
This PR adds support for multiple Data Parallel (DP) instances within a single machine for SSD KV cache offloading. Previously, in single-machine multi-DP scenarios, SSD subdirectories used local rank names, causing conflicts when multiple DP instances had the same local rank (e.g., DP0_TP4 and DP1_TP4 would both use rank_0 through rank_3). The fix changes the subdirectory naming to use global rank instead of local rank, ensuring unique subdirectory names across all DP instances within a machine.

## Technical Significance
This is a critical distributed storage fix for multi-DP SSD deployments. The previous local rank-based naming caused file conflicts when multiple DP instances shared the same machine, leading to "FILE_OPEN_FAIL" errors and KV cache corruption. By using global rank for subdirectory names, each DP instance gets a unique storage namespace even when multiple instances run on the same physical machine. This enables proper SSD KV cache offloading in complex distributed configurations with multiple DP groups per machine.

## Related
- `technique-kv-cache-paging`
- `technique-distributed-inference`
- `technique-ssd-offload`