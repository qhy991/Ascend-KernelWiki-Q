---
id: technique-pr-vllm-ascend-2663
title: "PR Insight: vllm-project/vllm-ascend #2663"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - rotary-embedding
  - cleanup
  - code-quality
  - torchair
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2663"
---

# PR Insight: vllm-project/vllm-ascend #2663

**Title:** [Misc] Clean up uesless code in rotary_embedding

## Overview
This PR removes useless code from rotary_embedding.py that was only used for torchair operations. The cleanup removes 31 lines while adding 14 new lines, improving code maintainability.

## Technical Significance
The code cleanup removes torchair-specific code from the general rotary embedding implementation, following previous refactoring that moved torchair operations to dedicated modules. This improves code clarity and reduces maintenance burden by eliminating code that is no longer needed in the general implementation.

## Related
- `technique-rotary-embedding`
- `technique-torchair`
- `technique-code-cleanup`