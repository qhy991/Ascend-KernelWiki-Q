---
id: technique-pr-vllm-ascend-9103
title: "PR Insight: vllm-project/vllm-ascend #9103"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - custom-ops
  - tiling-base
  - build-system
  - ascend950
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9103"
---

# PR Insight: vllm-project/vllm-ascend #9103

**Title:** [Ops][BugFix] Reuse common tiling_base for custom ops

## Overview
This PR refactors the custom operator build system to eliminate duplicate tiling_base and error_log headers across operators. It removes per-operator copies of these headers and includes the common versions from `csrc/common/include/tiling_base/`, affecting operators including recurrent_gated_delta_rule, dispatch_ffn_combine (and bf16/w4_a8 variants), causal_conv1d, and add_rms_norm_bias.

## Technical Significance
The consolidation of tiling_base headers fixes build issues with CANN 9.0 and improves maintainability by eliminating code duplication. The change keeps CeilDiv/CeilAlign in the common host tiling utility and exposes them through the common error_log compatibility header, while kernel-side local error_log headers remain untouched. This refactoring also updates CANN 9.0 Ascend950 SOC naming from ascend910_95 to ascend950.

## Related
- `kernel-ffn-ascendc`, `kernel-attention-ascendc`, `kernel-moe-ascendc`, `technique-operator-fusion`