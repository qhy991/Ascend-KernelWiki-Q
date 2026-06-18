---
id: technique-pr-vllm-ascend-8055
title: "PR Insight: vllm-project/vllm-ascend #8055"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - ascendc
  - gdn
  - recurrent
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8055"
---

# PR Insight: vllm-project/vllm-ascend #8055

**Title:** [Feature] Add recurrent ascendc ops

## Overview
This PR adds a new AscendC custom operator `RecurrentGatedDeltaRule` with implementation in `csrc/recurrent_gated_delta_rule/`. The operator supports recurrent Gated Delta Rule computation with comprehensive tiling infrastructure, updated GDN attention core computation paths in `vllm_ascend/ops/gdn.py`, and updated build scripts. Nightly tests and performance benchmarks confirm correctness with accuracy validation on GPQA (85.01) and GSM8K datasets.

## Technical Significance
The new RecurrentGatedDeltaRule AscendC operator provides optimized implementation for recurrent state-space models on Ascend NPUs. The comprehensive tiling infrastructure ensures efficient memory access patterns and utilization of Ascend hardware capabilities (Cube/Vector units). This enables production deployment of recurrent architectures with improved performance over generic implementations, with accuracy maintained through rigorous benchmarking.

## Related
- `kernel-attention` (GDN attention)
- `technique-ascendc` (AscendC operator development)
- `pattern-tiling` (Memory access optimization)