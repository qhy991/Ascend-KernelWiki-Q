---
id: technique-pr-vllm-ascend-9678
title: "PR Insight: vllm-project/vllm-ascend #9678"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - context-parallel
  - spec-decode
  - attention
  - mask-optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9678"
---

# PR Insight: vllm-project/vllm-ascend #9678

**Title:** [Performance]irregular mask build for pcp/dcp+spec decode

## Overview
This PR implements irregular mask construction for DCP + speculative decoding scenarios. Previously, one decode step would split into (1 + num_spec_decodes) separate requests with frequent KV cache transfers. The new approach generates irregular masks in `pcp_utils.py` and passes them to FIA operators with BSND layout.

## Technical Significance
Reduces KV cache transfer frequency in DCP + spec decode scenarios by enabling irregular mask handling. For Qwen3-30B with 128 concurrent requests, 3.5k input tokens, and 1.5k output tokens, ITL improves by 6-7 ms. The approach forces BSND layout in FIA when masks are irregular, requiring graph and eager mode updates.

## Related
- `technique-context-parallel`, `technique-spec-decode`, `kernel-attention`, `kernel-mla`