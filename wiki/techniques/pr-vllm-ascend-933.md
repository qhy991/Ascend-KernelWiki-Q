---
id: technique-pr-vllm-ascend-933
title: "PR Insight: vllm-project/vllm-ascend #933"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mla
  - graph-mode
  - deepseek
  - constraints
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/933"
---

# PR Insight: vllm-project/vllm-ascend #933

**Title:** [MLA][Graph] Improve assertion on Graph mode with MLA

## Overview
This PR improves assertion information for Graph mode with MLA to prevent user confusion. The fused MLA op in graph mode only supports `numHeads / numKvHeads ∈ {32, 64, 128}`, requiring specific TP size adjustments for DeepSeek V3/R1.

## Technical Significance
Clear error messages and constraints help users understand graph mode limitations. Documenting the MLA head ratio constraints enables users to configure their deployments correctly, avoiding runtime failures and ensuring proper tensor parallel size selection for DeepSeek models in graph mode.

## Related
- `kernel-mla`
- `technique-graph-mode`
- `kernel-deepseek`