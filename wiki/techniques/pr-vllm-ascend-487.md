---
id: technique-pr-vllm-ascend-487
title: "PR Insight: vllm-project/vllm-ascend #487"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - speculative-decoding
  - testing
  - eagle
  - mtp
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/487"
---

# PR Insight: vllm-project/vllm-ascend #487

**Title:** [3/N][CI/UT] add spec decode e2e UT && [BUGFIX] fix init_logger bug

## Overview
This PR adds EAGLE and MTP correctness tests (487 and 341 lines respectively) using BF16 weights, and fixes an init_logger OOM bug in camem.py by replacing init_logger imports with logger imports across multiple files.

## Technical Significance
Expands speculative decoding test coverage to EAGLE and MTP modes. The logger import fix prevents OOM by avoiding logger reinitialization. BF16 weights enable proper MTP testing on Ascend.

## Related
- technique-speculative-decoding
- technique-eagle
- technique-mtp