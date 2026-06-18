---
id: technique-pr-vllm-ascend-500
title: "PR Insight: vllm-project/vllm-ascend #500"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - speculative-decoding
  - medusa
  - mlp
  - ngram
  - testing
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/500"
---

# PR Insight: vllm-project/vllm-ascend #500

**Title:** [SpecDecode] Add spec decode support

## Overview
This PR backports speculative decoding support (from #252 and #423) to enable MEDUSA, MLP, and n-gram speculators on Ascend. Implementation includes 3000+ lines of tests and worker patches for draft model execution with MLA support.

## Technical Significance
Comprehensive speculative decoding support on Ascend. The backport brings feature parity across branches, enabling all major speculation techniques. MLA support in draft models is critical for DeepSeek-based speculation.

## Related
- technique-speculative-decoding
- technique-medusa
- technique-mlp
- technique-ngram
- technique-mla