---
id: technique-pr-vllm-ascend-10083
title: "PR Insight: vllm-project/vllm-ascend #10083"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - qwen3.5
  - fused-gdn-gating
  - ascend-a5
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10083"
---

# PR Insight: vllm-project/vllm-ascend #10083

**Title:** [BugFix][Ascend950] fix Qwen3_5 error since fused_gdn_gating is unavailable on A5

## Overview
This PR fixes Qwen3.5 errors on Ascend 950/A5 caused by attempting to use fused_gdn_gating operations that are unavailable on A5 hardware. It provides fallback mechanisms or alternative implementations.

## Technical Significance
Fixes Qwen3.5 compatibility with A5 devices by avoiding unavailable fused_gdn_gating operations. Ensures that Qwen3.5 models run correctly on A5 hardware by using compatible operations or providing appropriate fallbacks.

## Related
- `kernel-gating`, `kernel-fused-operations`, `pattern-hardware-compatibility`