---
id: technique-pr-vllm-ascend-3617
title: "PR Insight: vllm-project/vllm-ascend #3617"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mla
  - attribute-error
  - q-proj
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3617"
---

# PR Insight: vllm-project/vllm-ascend #3617

**Title:** [v0.11.0][Fix] Fixes attribute error in MLA implementation

## Overview
This PR fixes an AttributeError in the MLA (Multi-Head Latent Attention) implementation by correcting device attribute access from `q_a_proj` to `q_proj`. The `q_a_proj` attribute doesn't exist on the class instance, causing crashes. The fix was applied to `vllm_ascend/attention/mla_v1.py` with a 1-line change.

## Technical Significance
This is a straightforward bug fix for attribute access in MLA, a key optimization for reducing KV cache memory. Incorrect attribute references cause immediate failures, preventing model loading or execution. The fix ensures proper device allocation for query projection operations in MLA, enabling correct attention computation.

## Related
- `technique-mla`
- `technique-attention`
- `technique-kv-cache-compression`