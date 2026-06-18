---
id: technique-pr-samples-2017
title: "PR Insight: Ascend/samples #2017"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - bugfix
  - memory
  - dtype
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2017"
---

# PR Insight: Ascend/samples #2017

**Title:** 修改代码内获取数据类型占用字节大小错误的bug

## Overview
This PR fixes a bug in code that incorrectly calculates the byte size of data types. The fix corrects memory allocation and size calculations that were using wrong type sizes.

## Technical Significance
Correct byte size calculation is critical for proper memory management in AscendC kernels. Wrong size calculations cause buffer overflows, misaligned memory access, or incorrect tensor stride calculations, all of which lead to runtime errors or incorrect results.

## Related
- `technique-workspace-management`
- `technique-unified-buffer`