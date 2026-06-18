---
id: technique-pr-vllm-ascend-8779
title: "PR Insight: vllm-project/vllm-ascend #8779"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - attention
  - gqa
  - c8
  - fullgraph
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8779"
---

# PR Insight: vllm-project/vllm-ascend #8779

**Title:** [BugFix] Fixed a bug in GQA C8 fullgraph mode

## Overview
This PR fixes a bug in GQA (Grouped Query Attention) C8 fullgraph mode where the attention mask condition for graph capturing was incorrectly checking the original metadata instead of the potentially overridden local mask variable. The fix changes the condition check in `attention_v1.py` to use the correct mask variable.

## Technical Significance
This bug could cause incorrect graph compilation or execution in fullgraph mode when using GQA with C8 quantization. Fullgraph mode compiles the entire attention computation into a single graph for optimization, and incorrect mask conditions can lead to wrong attention patterns being applied. The fix ensures that mask override semantics are correctly preserved during graph capture, which is essential for correct GQA behavior with padding and masking scenarios.

## Related
- `kernel-attention-ascendc`
- `technique-format-conversion`
- `technique-nz-tiling`