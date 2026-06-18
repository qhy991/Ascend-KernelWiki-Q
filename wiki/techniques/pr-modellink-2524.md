---
id: technique-pr-modellink-2524
title: "PR Insight: Ascend/ModelLink #2524"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - tokenizer
  - bugfix
  - feature
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2524"
---

# PR Insight: Ascend/ModelLink #2524

**Title:** 【Adapt】：GPTSentencePieceTokenizer

## Overview
This PR adds or adapts the GPTSentencePieceTokenizer for use in ModelLink. The implementation provides SentencePiece tokenization support for GPT-style models, handling tokenization, encoding, and decoding operations.

## Technical Significance
Proper tokenizer implementation is critical for model correctness and performance. SentencePiece is widely used for multilingual models. The adaptation ensures correct tokenization behavior, padding strategies, and special token handling when training or inferencing on Ascend hardware.

## Related
- `technique-inference`