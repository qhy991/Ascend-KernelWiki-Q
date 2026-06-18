---
id: technique-pr-vllm-ascend-8269
title: "PR Insight: vllm-project/vllm-ascend #8269"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eplb
  - refactoring
  - cleanup
  - load-balancing
  - expert-parallel
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8269"
---

# PR Insight: vllm-project/vllm-ascend #8269

**Title:** [EPLB][Refactor] Delete DynamicConfig

## Overview
This PR removes the DynamicConfig functionality from the EPLB (Expert Parallel Load Balancing) implementation as it did not work correctly. The cleanup includes removing the DynamicConfig class, updating policy implementations, and adding unit tests for different load balancing policies. The refactoring simplifies the EPLB architecture and focuses on working policy implementations.

## Technical Significance
The removal of non-functional DynamicConfig improves code maintainability and reduces complexity in the EPLB system. The added unit tests provide better coverage for policy implementations, ensuring reliability of expert parallel load balancing. This refactoring demonstrates the importance of removing ineffective features to maintain a clean and functional codebase.

## Related
- `technique-expert-parallel`
- `technique-load-balancing`
- `technique-code-cleanup`