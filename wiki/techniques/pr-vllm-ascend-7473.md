---
id: technique-pr-vllm-ascend-7473
title: "PR Insight: vllm-project/vllm-ascend #7473"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - cudagraph
  - weight-update
  - mla
  - sfa
  - rl-inference
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7473"
---

# PR Insight: vllm-project/vllm-ascend #7473

**Title:** fix(attention): reuse weight address in graph + RL scenario

## Overview
This PR fixes weight address consistency in graph + RL scenarios where graphs are captured once but weights update across iterations. The fix uses copy_() instead of reassignment in AscendMLAImpl and AscendSFAImpl to ensure weight addresses remain consistent, preventing graphs from capturing stale weight addresses.

## Technical Significance
This fix matters for reinforcement learning inference with graph mode on Ascend. In RL scenarios, weights update frequently, but graphs capture weight addresses at capture time. Using .contiguous() or reassignment allocates new addresses, causing graphs to reference stale data. Using copy_() maintains address consistency while updating values, enabling correct weight reuse across RL iterations.

## Related
- technique-graph-mode
- technique-mla
- technique-sfa