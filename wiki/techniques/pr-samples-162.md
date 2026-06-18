---
id: technique-pr-samples-162
title: "PR Insight: Ascend/samples #162"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
  - ascend310p
tags:
  - custom-op
  - version-update
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/162"
---

# PR Insight: Ascend/samples #162

**Title:** Changed version of custom operator to support C75

## Overview
This PR updates custom operator implementations to support the C75 architecture version, ensuring compatibility with newer Ascend hardware generations. It modifies version-specific API calls and hardware feature configurations.

## Technical Significance
Enables custom operator samples to work across multiple Ascend hardware generations, demonstrating version-agnostic programming patterns and backward compatibility considerations in TBE/TIK development.

## Related
- `technique-operator-fusion`