---
id: technique-pr-sgl-kernel-npu-429
title: "PR Insight: sgl-project/sgl-kernel-npu #429"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - gated-delta-rule
  - gdn
  - qwen3.5
  - mtp
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/429"
---

# PR Insight: sgl-project/sgl-kernel-npu #429

**Title:** move fused_gdn_gating_kernel_without_sigmoid from sglang to sgl-kerne…

## Overview
This PR migrates the fused_gated_delta_rule kernel without sigmoid from sglang to sgl-kernel-npu, enabling optimized gated delta rule computation for Qwen3.5 models with MTP support. The implementation includes comprehensive testing showing accuracy improvements (gsm8k: 97.27% to 97.66%).

## Technical Significance
Migrating optimized kernels from framework to kernel library provides better code organization and reuse across different inference backends. The accuracy improvement demonstrates proper kernel integration while maintaining numerical correctness for Qwen3.5 models with multi-token prediction.

## Related
- `kernel-fused-gated-delta-rule`, `kernel-gated-delta-rule`, `kernel-mtp`