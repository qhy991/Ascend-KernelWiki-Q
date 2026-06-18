---
id: technique-pr-vllm-ascend-2017
title: "PR Insight: vllm-project/vllm-ascend #2017"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - refactoring
  - torchair
  - attention
  - code-organization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2017"
---

# PR Insight: vllm-project/vllm-ascend #2017

**Title:** [3/N][Refactor] Move `torchair_attention` to `torchair` dir

## Overview
This PR refactors the codebase by moving `torchair_attention` to the `torchair` directory and restructuring the class hierarchy. The changes include making `AscendAttentionTorchairBackend` extend `AscendAttentionBackend` and `AscendTorchairMetadata` extend `AscendMetadata` to reduce code duplication.

## Technical Significance
This refactoring improves code organization and reduces duplication by leveraging proper inheritance. The cleaner architecture makes it easier to maintain and extend attention functionality for both torchair and non-torchair backends. Better code organization improves developer productivity and reduces the likelihood of bugs.

## Related
- `technique-torchair`
- `technique-attention`
- `technique-refactoring`