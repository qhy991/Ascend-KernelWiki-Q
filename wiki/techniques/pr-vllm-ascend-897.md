---
id: technique-pr-vllm-ascend-897
title: "PR Insight: vllm-project/vllm-ascend #897"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - all2all
  - deepseek
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/897"
---

# PR Insight: vllm-project/vllm-ascend #897

**Title:** [BugFix] Fix accuracy bugs for unquantized deepseekv3 models

## Overview
This PR fixes accuracy bugs in unquantized DeepSeek V3 models caused by PR #819. It adds all_to_all communication for unquantized cases when ep_size equals world_size and corrects the logic to use ep_size instead of dp_size for all_to_all decisions.

## Technical Significance
Correct communication patterns are critical for MoE model accuracy. The fix ensures that both quantized and unquantized DeepSeek V3 models use appropriate all_to_all communication based on expert parallelism configuration, preventing numerical errors in unquantized scenarios.

## Related
- `kernel-moe`
- `kernel-deepseek`
- `technique-all2all`