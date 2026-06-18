---
id: technique-pr-vllm-ascend-2147
title: "PR Insight: vllm-project/vllm-ascend #2147"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - mindie-turbo
  - cleanup
  - interface
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2147"
---

# PR Insight: vllm-project/vllm-ascend #2147

**Title:** [Misc] Disable quantization in mindie_turbo

## Overview
This PR cherry-picks changes from v0.9.1-dev to disable quantization functions in mindie_turbo, as the interface in vllm-ascend has changed rapidly and the quantization function is no longer needed. The modification removes 8 lines from `vllm_ascend/quantization/quantizer.py`.

## Technical Significance
This cleanup removes deprecated quantization code that was specific to mindie_turbo integration. Since the quantization interface evolved, maintaining the old mindie_turbo-specific code became unnecessary. This simplification reduces codebase complexity and potential confusion by removing stale functionality that no longer serves a purpose.

## Related
- `technique-quantization`, `technique-code-cleanup`, `technique-interface-evolution`