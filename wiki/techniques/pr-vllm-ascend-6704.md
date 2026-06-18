---
id: technique-pr-vllm-ascend-6704
title: "PR Insight: vllm-project/vllm-ascend #6704"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - rms-norm
  - fusion
  - 310p
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6704"
---

# PR Insight: vllm-project/vllm-ascend #6704

**Title:** [Feat.][310P] addrmsnorm for 300I DUO

## Overview
This PR integrates the npu_add_rms_norm fused kernel for RMSNorm operations with residual connections on 310P devices. It replaces the two-step process (manual residual addition followed by RMSNorm) with a single, more efficient fused operation.

## Technical Significance
Optimizes models utilizing RMSNorm with residual connections on 310P architecture through operator fusion. The fused kernel reduces memory traffic and improves throughput by combining residual addition and normalization into a single operation.

## Related
- `technique-layernorm`
- `technique-operator-fusion`