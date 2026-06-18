---
id: technique-pr-vllm-ascend-1294
title: "PR Insight: vllm-project/vllm-ascend #1294"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mtp
  - torchair
  - graph-mode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1294"
---

# PR Insight: vllm-project/vllm-ascend #1294

**Title:** [0.9.1] [MTP V1] MTP adapt torchair graph mode

## Overview
This PR adapts the MTP (Multi-Token Prediction) V1 implementation to use TorchAir graph mode, enabling graph-optimized execution for speculative decoding workflows.

## Technical Significance
Enables TorchAir's graph compilation and optimization for MTP V1, improving speculative decoding performance on Ascend. The integration spans attention (MLA V1), DeepSeek V2 model support, model runner, and MTP proposer components. This allows TorchAir to fuse operators and optimize memory access patterns across the MTP pipeline, reducing kernel launch overhead and improving inference throughput.

## Related
- `technique-torchair`
- `technique-spec-decode`
- `kernel-attention`