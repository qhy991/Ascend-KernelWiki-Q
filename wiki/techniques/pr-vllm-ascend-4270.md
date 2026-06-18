---
id: technique-pr-vllm-ascend-4270
title: "PR Insight: vllm-project/vllm-ascend #4270"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen2.5-vl
  - mrope
  - fusion
  - bugfix
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4270"
---

# PR Insight: vllm-project/vllm-ascend #4270

**Title:** avoid mrope fusion op when running qwen2.5-vl on a+x machine

## Overview
This PR avoids using MRoPE (Multi-Resolution Position Encoding) fusion operator when running Qwen2.5-VL on A+X machines. The fix addresses compatibility issues with the fusion operator on specific hardware configurations, ensuring correct text VQA accuracy.

## Technical Significance
Hardware-specific operator compatibility is important for correctness across different Ascend configurations. A+X machines have different characteristics that may not support certain fusion operators. Disabling the fusion operator when incompatible ensures correct accuracy while potentially trading off some performance.

## Related
- `technique-mrope`, `technique-qwen2.5-vl`, `pattern-hardware-compatibility`, `pattern-operator-selection`, `technique-fusion`