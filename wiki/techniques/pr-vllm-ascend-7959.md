---
id: technique-pr-vllm-ascend-7959
title: "PR Insight: vllm-project/vllm-ascend #7959"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decode
  - configuration
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7959"
---

# PR Insight: vllm-project/vllm-ascend #7959

**Title:** [BugFix] Remove the overwriting of the `speculative_config.enforce_eager`

## Overview
This PR removes code that was overwriting `speculative_config.enforce_eager` for DSv32 (DeepSeek V3.2) models. The DSv32 implementation explicitly declares that it only uses eager mode for MTP (Multi-Token Prediction) layers, making the override unnecessary and potentially masking issues.

## Technical Significance
Removing unnecessary configuration overwrites ensures that model-specific settings are honored. The DSv32 explicit eager mode requirement for MTP layers is now respected directly, and the removed code had been masking potential bugs. This change improves configuration transparency and helps identify issues when running DSv32 with full graph execution in the future.

## Related
- `pattern-speculative-decoding`
- `technique-inference-optimization`
- `pattern-dsv32`