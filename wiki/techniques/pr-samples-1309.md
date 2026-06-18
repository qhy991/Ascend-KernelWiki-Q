---
id: technique-pr-samples-1309
title: "PR Insight: Ascend/samples #1309"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
  - ascend310p
tags:
  - input-handling
  - output
  - memory-management
  - bugfix
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1309"
---

# PR Insight: Ascend/samples #1309

**Title:** 修改了输入为pic时不输出output；修改了内存释放位置

## Overview
This PR fixes two issues: 1) not outputting when input is a picture, and 2) modifying memory release timing. The changes improve correctness and memory safety.

## Technical Significance
Proper output handling prevents silent failures, while correct memory release timing prevents leaks and double-free issues. These fixes improve the reliability of sample applications.

## Related
- `pattern-memory-management`
- `pattern-input-handling`