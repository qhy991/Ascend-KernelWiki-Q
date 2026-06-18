---
id: technique-pr-vllm-ascend-1516
title: "PR Insight: vllm-project/vllm-ascend #1516"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - documentation
  - pangu-moe
  - 300i
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1516"
---

# PR Insight: vllm-project/vllm-ascend #1516

**Title:** Add Pangu MoE Pro for 300I series docs

## Overview
This PR adds specific documentation for deploying Pangu MoE Pro on Ascend 300I series NPUs.

## Technical Significance
Provides hardware-specific deployment guidance for 300I series, ensuring users can optimize configuration for this specific NPU generation. The documentation addresses 300I's unique capabilities and constraints, improving deployment success rates.

## Related
- `kernel-pangu`
- `kernel-moe`