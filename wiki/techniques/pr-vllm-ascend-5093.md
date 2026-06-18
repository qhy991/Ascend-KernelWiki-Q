---
id: technique-pr-vllm-ascend-5093
title: "PR Insight: vllm-project/vllm-ascend #5093"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mtp
  - moe
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5093"
---

# PR Insight: vllm-project/vllm-ascend #5093

**Title:** [bugfix] fix mtp accept rate

## Overview
This PR fixes MTP (Multi-Token Prediction) accept rate issues by disabling in_profile_run in the NPU model runner. It also removes redundant attributes defined in gpu_model_runner that are now reused, cleans up redundant MoE method selection logic, and reverts PR #5082 which broke CI.

## Technical Significance
Fixing the MTP accept rate is critical for improving speculating decoding performance on Ascend NPUs. The accept rate directly impacts overall inference throughput in MTP scenarios. The cleanup also reduces code duplication between GPU and NPU model runners.

## Related
- technique-mtp
- technique-speculative-decoding
- technique-moe