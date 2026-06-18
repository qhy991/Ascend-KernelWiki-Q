---
id: technique-pr-vllm-ascend-1046
title: "PR Insight: vllm-project/vllm-ascend #1046"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - quantization
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1046"
---

# PR Insight: vllm-project/vllm-ascend #1046

**Title:** [Bugfix] Add verification for `quant_action.choices` to avoid `TypeError`

## Overview
This PR fixes a TypeError that occurs when the `choices` attribute in `quant_action` is None. The bug was triggered in `vllm_ascend/platform.py` when checking `ASCEND_QUATIZATION_METHOD not in quant_action.choices`, causing an "argument of type 'NoneType' is not iterable" error during vLLM startup.

## Technical Significance
This fix ensures robust error handling for quantization configuration parsing on Ascend platforms. By adding a null check before attempting to iterate over the choices attribute, the PR prevents crashes when quantization options are not fully initialized, improving system stability for users running quantized models.

## Related
- `technique-quantization`