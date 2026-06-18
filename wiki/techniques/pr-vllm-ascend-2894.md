---
id: technique-pr-vllm-ascend-2894
title: "PR Insight: vllm-project/vllm-ascend #2894"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - prefill
  - chunked-prefill
  - mla
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2894"
---

# PR Insight: vllm-project/vllm-ascend #2894

**Title:** [Core] Disable the chunked prefill feature in Non-MLA LLMs

## Overview
This PR disables the chunked prefill feature in Non-MLA (Multi-Linear Attention) models because the performance of operators supporting this functionality is currently suboptimal. The change affects the schedule configuration and platform initialization logic, enforcing that chunked prefill only runs when explicitly enabled by users via ascend_scheduler_config.

## Technical Significance
The PR addresses a performance regression in chunked prefill operators on Ascend NPUs. Chunked prefill is an optimization technique for attention computation during the prefill phase, but the current Ascend operator implementations show suboptimal performance. The fix removes test cases and modifies platform.py to forcibly disable this feature for Non-MLA models, ensuring users opt-in explicitly when performance is acceptable.

## Related
- `kernel-attention-ascendc`, `technique-chunked-prefill`, `technique-mla`