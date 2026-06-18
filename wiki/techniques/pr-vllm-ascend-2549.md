---
id: technique-pr-vllm-ascend-2549
title: "PR Insight: vllm-project/vllm-ascend #2549"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantmatmul
  - nz-format
  - data-layout
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2549"
---

# PR Insight: vllm-project/vllm-ascend #2549

**Title:** [main][bugfix] Fix MatmulNZ format bug on some machines

## Overview
This PR fixes a bug where quantmatmul failed to run with NZ format on some machines. The fix ensures proper execution under the expected data layout by adding format validation in `vllm_ascend/worker/model_runner_v1.py`.

## Technical Significance
This bugfix ensures correct behavior of quantized matrix multiplication with NZ format across different machine configurations. The fix addresses data layout issues that caused failures on certain hardware, improving cross-platform compatibility for quantized inference.

## Related
- `kernel-matmul-ascendc`, `technique-nz-format`, `technique-data-layout`, `technique-cross-platform-compatibility`