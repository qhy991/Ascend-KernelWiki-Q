---
id: technique-pr-sgl-kernel-npu-445
title: "PR Insight: sgl-project/sgl-kernel-npu #445"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - causal-conv1d
  - mtp
  - speculative-decoding
  - qwen3.5
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/445"
---

# PR Insight: sgl-project/sgl-kernel-npu #445

**Title:** Add conv1d update mtp triton kernel. Adapt speculative decoding for update

## Overview
This PR adds a conv1d_update MTP Triton kernel and adapts speculative decoding for update operations in Mamba models. The implementation maintains accuracy while enabling speculative decoding for state updates, with validation showing gsm8k accuracy of 97%+ and ceval accuracy of 92%+ for Qwen3.5-397B.

## Technical Significance
Enabling speculative decoding for Mamba state updates significantly improves inference throughput for models using MTP while maintaining numerical accuracy. The adaptation extends speculative decoding benefits beyond standard attention to recurrent attention mechanisms, providing broad performance improvements for Mamba-based models.

## Related
- `kernel-causal-conv1d`, `kernel-mamba`, `kernel-mtp`, `technique-speculative-decoding`