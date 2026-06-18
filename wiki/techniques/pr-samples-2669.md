---
id: technique-pr-samples-2669
title: "PR Insight: Ascend/samples #2669"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - kernel-direct-call
  - add-custom
  - aclrt
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2669"
---

# PR Insight: Ascend/samples #2669

**Title:** add aclrt launch kernel add_custom sample

## Overview
This PR adds a sample for launching the AddCustom kernel directly using the aclrt API. This provides another reference for kernel invocation patterns, focusing on the runtime API.

## Technical Significance
Multiple kernel invocation samples help developers choose the right pattern for their use case. The aclrt API sample complements other approaches, showing a framework-agnostic method.

## Related
- `pattern-kernel-launch`, `kernel-elementwise`