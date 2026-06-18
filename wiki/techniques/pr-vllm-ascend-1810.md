---
id: technique-pr-vllm-ascend-1810
title: "PR Insight: vllm-project/vllm-ascend #1810"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decode
  - refactoring
  - v0-deprecation
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1810"
---

# PR Insight: vllm-project/vllm-ascend #1810

**Title:** [Misc][V0 Deprecation] Remove Draft Model Runner Used for V0 Spec Decode

## Overview
This PR removes the draft model runner used for V0 spec decode as part of a larger effort to deprecate V0 code paths. This is part of issue #1620 which tracks the removal of legacy V0 components.

## Technical Significance
Code maintenance and deprecation. Removing unused or legacy code paths reduces maintenance burden and focuses effort on the newer V1 architecture. Spec decode functionality remains available through updated implementations.

## Related
- `technique-spec-decode`
- `technique-v0-deprecation`