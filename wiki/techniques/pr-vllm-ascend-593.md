---
id: technique-pr-vllm-ascend-593
title: "PR Insight: vllm-project/vllm-ascend #593"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - speculative-decoding
  - mtp
  - bugfix
  - testing
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/593"
---

# PR Insight: vllm-project/vllm-ascend #593

**Title:** [BUGFIX] main-sd-bugfix && [UT] add mtp UT

## Overview
This PR fixes speculative decoding bugs, adds MTP correctness tests (355 lines), and replaces init_logger imports with logger imports project-wide. Fixes include single-element attn_mask_cache support and removing asserts for spec decode worker.

## Technical Significance
Bug fixes for spec decode with chunked prefill. The logger import fix prevents OOM from reinitialization. MTP tests ensure correctness of DeepSeek's multi-token prediction speculation.

## Related
- technique-speculative-decoding
- technique-mtp
- technique-chunk-prefill