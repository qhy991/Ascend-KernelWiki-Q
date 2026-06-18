---
id: technique-pr-vllm-ascend-6947
title: "PR Insight: vllm-project/vllm-ascend #6947"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decode
  - interface-refactoring
  - eagle
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6947"
---

# PR Insight: vllm-project/vllm-ascend #6947

**Title:** [Spec Decode]clean up spec decode interface

## Overview
Refactors the speculative decoding proposer interface to align with upstream vLLM, removing the local `Proposer` interface and renaming methods to `propose`. This is the first step toward removing class registration and adding Ascend-specific methods once upstream architecture is ready.

## Technical Significance
Improves compatibility with upstream vLLM by standardizing the speculative decoding interface. The refactoring simplifies the architecture and prepares for future integration with upstream changes while maintaining Ascend-specific optimizations.

## Related
- `technique-spec-decode`, `technique-interface-standardization`, `technique-eagle`