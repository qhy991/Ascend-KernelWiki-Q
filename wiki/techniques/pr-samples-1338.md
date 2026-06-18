---
id: technique-pr-samples-1338
title: "PR Insight: Ascend/samples #1338"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
  - ascend310p
tags:
  - dynamic-batch
  - samples
  - revert
  - naming
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1338"
---

# PR Insight: Ascend/samples #1338

**Title:** 回退 'Pull Request !1334 : 更改动态分档sample名字'

## Overview
This PR reverts the changes from PR #1334 which renamed dynamic batch samples. The revert restores the previous sample naming convention.

## Technical Significance
Naming consistency is important for discoverability and user experience. The revert suggests that the original naming was preferred or that the new naming caused issues.

## Related
- `technique-dynamic-batching`
- `pattern-sample-naming`