---
id: technique-pr-vllm-ascend-5481
title: "PR Insight: vllm-project/vllm-ascend #5481"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - refactoring
  - dataclass
  - code-quality
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5481"
---

# PR Insight: vllm-project/vllm-ascend #5481

**Title:** [Refactor] Formatting output types related to FuseMoE

## Overview
This PR refactors the Fused MoE module by replacing dictionary and tuple output formats with dataclasses for key classes including `MoECommMethod` and `MoETokenDispatcher`. The change improves code maintainability, readability, and extensibility while updating related test files.

## Technical Significance
Using dataclasses instead of raw dictionaries/tuples provides better type safety, clearer API contracts, and easier maintenance for complex MoE operations. This refactoring makes the Fused MoE implementation more robust and easier to extend, particularly important for the complex routing and dispatch logic in MoE layers on Ascend NPU.

## Related
- `pattern-moe` (MoE patterns and operations)
- `technique-fused-moe` (Fused MoE implementation)
- `kernel-moe` (MoE kernel operations)