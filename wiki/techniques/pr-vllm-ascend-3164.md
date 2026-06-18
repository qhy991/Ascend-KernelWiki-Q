---
id: technique-pr-vllm-ascend-3164
title: "PR Insight: vllm-project/vllm-ascend #3164"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - multi-stream
  - torchair
  - chunked-prefill
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3164"
---

# PR Insight: vllm-project/vllm-ascend #3164

**Title:** [bugfix]fix multistream moe in torchair

## Overview
This PR fixes multistream MoE in TorchAir by adding scenario isolation. The multistream MoE optimization was only validated for decode scenarios and couldn't be applied to chunked prefill, so the fix adds judgments to isolate these scenarios.

## Technical Significance
Different execution phases (prefill vs decode) have different requirements and constraints. Isolating multistream optimization to decode-only scenarios prevents correctness issues in chunked prefill, where the optimization may not be valid or could cause errors.

## Related
- `kernel-moe-ascendc`, `technique-multi-stream`, `technique-chunked-prefill`