---
id: technique-pr-vllm-ascend-1409
title: "PR Insight: vllm-project/vllm-ascend #1409"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - nz-format
  - quantization
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1409"
---

# PR Insight: vllm-project/vllm-ascend #1409

**Title:** [v0.9.1][perf] add a switch for enabling NZ layout in weights and enable NZ for GMM

## Overview
This PR adds a configuration switch to enable NZ format in model weights and enables NZ format for GeMM (Grouped Matrix Multiplication) operations.

## Technical Significance
Improves memory access efficiency and compute utilization by leveraging Ascend's NZ format. The switch allows users to opt-in to NZ format for weight storage, and enabling NZ for GMM operations improves memory bandwidth utilization for large matrix multiplications in quantization workloads.

## Related
- `technique-nz-format`
- `technique-quantization`
- `kernel-matmul`