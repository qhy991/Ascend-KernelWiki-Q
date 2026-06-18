---
id: technique-pr-vllm-ascend-17
title: "PR Insight: vllm-project/vllm-ascend #17"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - logging
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/17"
---

# PR Insight: vllm-project/vllm-ascend #17

**Title:** [Platform] add dispatch key

## Overview
This PR adds the NPU dispatch key to the platform module, fixing logging output that was incorrectly labeling NPU memory blocks as CPU blocks. The change modifies vllm_ascend/platform.py to correctly distinguish between NPU and CPU in block allocation logging.

## Technical Significance
A minor but important fix for observability on Ascend platforms. Correct logging is essential for debugging and monitoring memory allocation during inference, especially given vllm-ascend's complex memory management with KV caches and attention buffers.

## Related
- technique-logging