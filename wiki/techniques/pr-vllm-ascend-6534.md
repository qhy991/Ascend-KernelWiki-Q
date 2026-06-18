---
id: technique-pr-vllm-ascend-6534
title: "PR Insight: vllm-project/vllm-ascend #6534"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - quantization
  - refactor
  - cleanup
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6534"
---

# PR Insight: vllm-project/vllm-ascend #6534

**Title:** [MOE Refactor] Remove QuantType in prepare_finalize.py

## Overview
This PR removes QuantType references from prepare_finalize.py to prevent confusion between different QuantType classes. The cleanup simplifies the MoE quantization preparation logic by removing redundant type handling.

## Technical Significance
Simplifies MoE quantization logic by removing conflicting QuantType class references. This cleanup prevents confusion and potential bugs from type name collisions, making the codebase easier to maintain and understand.

## Related
- `kernel-moe`
- `technique-quantization`