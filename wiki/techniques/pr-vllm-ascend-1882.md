---
id: technique-pr-vllm-ascend-1882
title: "PR Insight: vllm-project/vllm-ascend #1882"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - multistream
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1882"
---

# PR Insight: vllm-project/vllm-ascend #1882

**Title:** [BUGFIX][v0.9.1] repair moe error when set multistream.

## Overview
This PR repairs MoE execution errors that occur when multistream mode is enabled. The fix addresses the interaction between MoE expert routing and multistream parallel execution.

## Technical Significance
Bugfix for MoE multistream compatibility. Multistream execution requires careful coordination with expert routing to ensure correct tensor shapes and execution order across multiple streams.

## Related
- `technique-moe`
- `technique-multistream`