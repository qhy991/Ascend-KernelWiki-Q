---
id: technique-pr-samples-2655
title: "PR Insight: Ascend/samples #2655"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - kernel-direct-call
  - add-custom
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2655"
---

# PR Insight: Ascend/samples #2655

**Title:** kernel直调AddCustom样例更新

## Overview
This PR updates the AddCustom sample to use direct kernel invocation. Direct kernel invocation bypasses high-level APIs, giving developers finer control over kernel launch parameters and scheduling.

## Technical Significance
Direct kernel invocation is useful for advanced optimizations where fine-grained control is needed. The updated sample provides a reference for this lower-level approach.

## Related
- `pattern-kernel-launch`, `kernel-elementwise`