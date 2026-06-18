---
id: technique-pr-vllm-ascend-9668
title: "PR Insight: vllm-project/vllm-ascend #9668"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - context-parallel
  - moe
  - configuration
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9668"
---

# PR Insight: vllm-project/vllm-ascend #9668

**Title:** [Ops][Misc] Remove VLLM_ASCEND_ENABLE_CONTEXT_PARALLEL

## Overview
This PR removes the environment variable `VLLM_ASCEND_ENABLE_CONTEXT_PARALLEL` and its associated configuration from `AscendConfig`. Previously used for PCP+EP in A2, this variable is no longer needed since `moe_config` now contains `pcp_size` configuration after upstream vllm changes.

## Technical Significance
Simplifies configuration management by removing redundant environment variables, consolidating context parallel configuration into the unified `moe_config.pcp_size` parameter. This reduces configuration surface area and eliminates potential user confusion.

## Related
- `technique-context-parallel`, `technique-moe`