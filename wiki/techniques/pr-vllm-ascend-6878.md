---
id: technique-pr-vllm-ascend-6878
title: "PR Insight: vllm-project/vllm-ascend #6878"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - quantization
  - w8a8s
  - w8a8sc
  - state-saving
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6878"
---

# PR Insight: vllm-project/vllm-ascend #6878

**Title:** [Feat][310p] 310P support w8a8s quantization and saving w8a8sc state

## Overview
Enables W8A8S dynamic quantization and W8A8SC static quantization with state saving capabilities for Ascend 310P devices. The implementation includes core quantization methods, metadata generation for saved parameters, and example scripts for saving sharded and compressed model states.

## Technical Significance
Expands quantization support for 310P hardware by adding efficient W8A8S dynamic quantization and enabling state saving for W8A8SC models. The integration with metadata generation ensures proper handling of quantization types in saved model states, improving efficiency and compatibility.

## Related
- `technique-quantization-w8a8`, `technique-quantization-static`, `technique-state-saving`