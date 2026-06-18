---
id: technique-pr-vllm-ascend-2659
title: "PR Insight: vllm-project/vllm-ascend #2659"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - chunked-prefill
  - mla
  - scheduler
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2659"
---

# PR Insight: vllm-project/vllm-ascend #2659

**Title:** [v0.9.1][bugfix] disable the chunked prefill feature in Non-MLA LLMs

## Overview
This PR forcibly disables the chunked prefill feature in Non-MLA models due to suboptimal operator performance. It also enforces ascend scheduler usage in engine v1 mode and disables user-specified `enable_chunked_prefill` in additional_config.

## Technical Significance
The bug fix prevents performance issues by disabling chunked prefill for Non-MLA models where operator performance is suboptimal. The platform.py changes enforce ascend scheduler usage and override user configuration to ensure stable performance. This addresses known performance limitations in the current implementation.

## Related
- `technique-chunked-prefill`
- `technique-mla`
- `technique-scheduler`