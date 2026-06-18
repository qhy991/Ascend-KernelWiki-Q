---
id: technique-pr-vllm-ascend-9251
title: "PR Insight: vllm-project/vllm-ascend #9251"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decode
  - refactor
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9251"
---

# PR Insight: vllm-project/vllm-ascend #9251

**Title:** [Refactor][SpecDecode] Move AscendSpecDecodeBaseProposer to llm_base_proposer.py

## Overview
This PR refactors the speculative decoding code by moving the AscendSpecDecodeBaseProposer class to a dedicated llm_base_proposer.py file. The change affects the draft proposer module, test files, and maintains backward compatibility through appropriate imports.

## Technical Significance
Refactoring improves code organization and maintainability by separating the base proposer implementation from specific proposer implementations. This makes the codebase easier to navigate and enables better code reuse across different speculative decoding strategies.

## Related
- `technique-spec-decode`