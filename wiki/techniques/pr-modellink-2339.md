---
id: technique-pr-modellink-2339
title: "PR Insight: Ascend/ModelLink #2339"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - deepseek-v3
  - attention
  - weight-conversion
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2339"
---

# PR Insight: Ascend/ModelLink #2339

**Title:** deepseek v3 attention部分mg2hf

## Overview
This PR implements ModelLink-to-HuggingFace weight conversion for DeepSeekV3 attention components. The conversion handles the specialized MLA (Multi-Head Latent Attention) architecture weight transformation.

## Technical Significance
DeepSeekV3's MLA uses compressed key-value representations that differ from standard attention. Converting these weights requires precise transformation of the compressed latent KV tensors and attention projection matrices. This conversion enables deploying DeepSeekV3 models trained in ModelLink to HuggingFace inference frameworks, ensuring compatibility with the broader ecosystem while maintaining the MLA efficiency benefits on Ascend hardware.

## Related
- `kernel-attention-mla`
- `technique-weight-conversion`
- `technique-kv-compression`