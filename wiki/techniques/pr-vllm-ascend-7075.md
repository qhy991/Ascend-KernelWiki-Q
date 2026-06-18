---
id: technique-pr-vllm-ascend-7075
title: "PR Insight: vllm-project/vllm-ascend #7075"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - quantization
  - w8a8sc
  - state-saving
  - 310p
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7075"
---

# PR Insight: vllm-project/vllm-ascend #7075

**Title:** [Feat] [310p] Support w8a8sc quantization method

## Overview
Adds support for the W8A8SC static linear quantization scheme specifically for 310P hardware, enabling more efficient model compression. Also refactors `save_sharded_state_310.py` to avoid multi-process issues during state saving.

## Technical Significance
Expands quantization capabilities for 310P devices by adding W8A8SC static quantization, providing an additional compression option beyond dynamic quantization. The refactoring of state saving improves reliability in multi-process scenarios.

## Related
- `technique-quantization-w8a8`, `technique-quantization-static`, `technique-state-saving`, `technique-310p`