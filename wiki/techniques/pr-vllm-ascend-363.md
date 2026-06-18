---
id: technique-pr-vllm-ascend-363
title: "PR Insight: vllm-project/vllm-ascend #363"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - w8a8
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/363"
---

# PR Insight: vllm-project/vllm-ascend #363

**Title:** [BugFix]fix w8a8 bug

## Overview
This PR fixes a bug where W8A8 quantization without attention quantization was incorrectly identified as using attention quantization. Changes affect platform.py and quantization config.

## Technical Significance
W8A8 (8-bit weights, 8-bit activations) is a different quantization scheme than KV cache quantization. Misidentifying them could cause incorrect weight loading or attention kernel selection. This fix ensures proper quantization method dispatch.

## Related
- technique-quantization
- technique-w8a8