---
id: technique-pr-vllm-ascend-9587
title: "PR Insight: vllm-project/vllm-ascend #9587"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - gdn
  - recurrent
  - torch-binding
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9587"
---

# PR Insight: vllm-project/vllm-ascend #9587

**Title:** [BugFix] Route GDN recurrent op through vLLM Ascend torch binding

## Overview
This PR fixes the GDN (Gated Delta Network) recurrent operation by routing it through the vLLM Ascend torch binding instead of alternative paths. The changes affect the recurrent GDN operator's torch adapter, torch bindings, and GDN operator Python interface.

## Technical Significance
Using the proper torch binding ensures correct integration with the vLLM runtime and enables optimizations that are specific to the Ascend backend. The fix prevents potential issues with operator registration, memory management, and execution scheduling.

## Related
- `technique-operator-fusion`
- `hw-cube-unit`