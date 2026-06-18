---
id: technique-pr-samples-1339
title: "PR Insight: Ascend/samples #1339"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
  - ascend310p
tags:
  - custom-operator
  - 310
  - 910
  - 191
  - compatibility
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1339"
---

# PR Insight: Ascend/samples #1339

**Title:** adapt compile of custom run for 1971/1981/1911

## Overview
This PR adapts the custom operator compilation for Ascend 1971, 1981, and 1911 chips. The changes ensure custom operators can be correctly compiled for these hardware variants.

## Technical Significance
Custom operator support is critical for extending Ascend capabilities. Adapting compilation for different chip variants ensures the custom operator samples work across the Ascend product line.

## Related
- `technique-custom-operator`
- `pattern-cross-hardware`