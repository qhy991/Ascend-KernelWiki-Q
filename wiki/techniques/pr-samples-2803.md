---
id: technique-pr-samples-2803
title: "PR Insight: Ascend/samples #2803"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - validation
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2803"
---

# PR Insight: Ascend/samples #2803

**Title:** fix samples compare

## Overview
This PR fixes the comparison logic in sample validation code. The fix ensures that output verification works correctly when comparing sample results against expected values.

## Technical Significance
Proper validation is critical for sample correctness. Fixed comparison logic prevents false failures and ensures users can trust sample outputs as reference implementations.

## Related
- Validation and testing patterns