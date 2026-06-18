---
id: technique-pr-sgl-kernel-npu-371
title: "PR Insight: sgl-project/sgl-kernel-npu #371"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - gated-delta-rule
  - kda-feature
  - mamba
  - qwen
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/371"
---

# PR Insight: sgl-project/sgl-kernel-npu #371

**Title:** feat:[fused_sigmoid_gating_delta_rule_update_npu_kernel] support kda feature--to be aligned with sgl-kernel, for model kimi-linear

## Overview
This PR adds kda (Key-Direct-Attention) feature support to the fused_sigmoid_gating_delta_rule_update_npu_kernel, aligning with sgl-kernel implementation for the Kimi-Linear 480B model. The enhancement enables the kernel to support advanced attention patterns required by the Kimi-Linear architecture.

## Technical Significance
Adding kda feature support extends the gated delta rule kernel to handle more complex attention mechanisms used in state-of-the-art models like Kimi-Linear. This alignment with sgl-kernel ensures compatibility and feature parity across different inference backends while maintaining performance on Ascend hardware.

## Related
- `kernel-fused-sigmoid-gating-delta-rule`, `kernel-gated-delta-rule`, `kernel-mamba`, `technique-feature-parity`