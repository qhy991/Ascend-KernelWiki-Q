---
id: technique-pr-vllm-ascend-5775
title: "PR Insight: vllm-project/vllm-ascend #5775"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - npugraph-ex
  - static-kernel
  - online-inference
  - fx-graph
  - compilation
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5775"
---

# PR Insight: vllm-project/vllm-ascend #5775

**Title:** [Feature]refactor the npugraph_ex config, support online-infer with static kernel

## Overview
This PR refactors the npugraph_ex configuration to support online inference with static kernels. The changes include modifying the default static kernel configuration to false, adding support for online inference with static kernels, and fixing issues with FX graph modifications that caused abnormal model return types. The implementation updates `ascend_config.py`, `compiler_interface.py`, and `platform.py` to handle the new configuration options and proper graph modification handling.

## Technical Significance
This refactoring enables more flexible kernel compilation strategies by allowing online inference with static kernels while making static kernel usage opt-in via configuration. The key improvement is fixing FX graph modification issues that were causing type problems in model return values. The new configuration structure provides clearer control over npugraph_ex behavior with separate enable flags for the overall system and for static kernel usage. This allows users to leverage static kernel benefits when appropriate while maintaining default compatibility with online inference patterns.

## Related
- `technique-graph-mode`, `technique-static-kernel`, `technique-compilation`, `technique-fx-graph`