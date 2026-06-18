---
id: technique-pr-samples-862
title: "PR Insight: Ascend/samples #862"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - nlp
  - bert
  - bugfix
  - sequence-length
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/862"
---

# PR Insight: Ascend/samples #862

**Title:** fix bert maxlen

## Overview
This PR fixes an issue related to the maximum sequence length (maxlen) parameter in the BERT sample. The fix likely corrects handling of variable-length sequences or fixes buffer allocation for the maximum supported sequence length.

## Technical Significance
Proper sequence length handling is critical for NLP models like BERT. This fix addresses a bug that could cause incorrect results, crashes, or performance issues when processing text with specific sequence lengths. It demonstrates how to correctly configure input dimensions and memory allocation for transformer models on Ascend NPU.

## Related
- BERT inference on Ascend
- Sequence length handling in transformers
- NLP model input preprocessing
- Memory allocation for variable-length inputs