---
id: technique-pr-vllm-ascend-2570
title: "PR Insight: vllm-project/vllm-ascend #2570"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - token-dispatcher
  - refactor
  - quantization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2570"
---

# PR Insight: vllm-project/vllm-ascend #2570

**Title:** [main] [refactor] refactor fused_moe.py to enable token_dispatchers

## Overview
This PR refactors the fused_moe implementation to enable token_dispatchers in eager mode, replacing the fused_experts_with_xxx approach. The refactoring affects multiple files including MoE dispatcher, quantization modules, and test suites.

## Technical Significance
The refactoring significantly improves MoE operation flexibility by enabling token dispatchers to work in eager mode. Key changes include simplifying `fused_moe.py` (reducing from 612 to 230 deletions while adding 230 new lines), updating the token dispatcher, and refactoring quantization implementations (w4a8 and w8a8). This improves code maintainability and enables better token routing in MoE layers.

## Related
- `technique-moe`
- `technique-token-dispatcher`
- `technique-quantization`