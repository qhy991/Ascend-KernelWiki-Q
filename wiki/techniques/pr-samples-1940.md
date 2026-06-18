---
id: technique-pr-samples-1940
title: "PR Insight: Ascend/samples #1940"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - acl
  - operator
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1940"
---

# PR Insight: Ascend/samples #1940

**Title:** 修改acl调用算子代码内状态码未正确赋值的bug

## Overview
This PR fixes a bug where status codes were not properly assigned in ACL (Ascend Computing Language) operator invocation code. The fix ensures that error handling and status checks work correctly, preventing silent failures or incorrect error reporting when calling ACL operators in the sample code.

## Technical Significance
Proper status code handling is fundamental to robust ACL application development. Incorrect status assignment can mask real errors or cause false positives in error handling, making debugging extremely difficult. This fix demonstrates the correct pattern for status code management when invoking operators on Ascend910/910B.

## Related
- `pattern-error-handling`
- `technique-api-correctness`