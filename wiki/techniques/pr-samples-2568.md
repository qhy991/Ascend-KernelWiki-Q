---
id: technique-pr-samples-2568
title: "PR Insight: Ascend/samples #2568"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - dumptensor
  - printf
  - code-organization
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2568"
---

# PR Insight: Ascend/samples #2568

**Title:** 修改dumptensor和printf样例的位置

## Overview
This PR modifies the location of dumptensor and printf samples in the repository structure. The reorganization improves code organization and makes these debugging/utility samples easier to find.

## Technical Significance
DumpTensor and printf are essential debugging tools for kernel development. Proper organization of these utility samples helps developers quickly find examples for tensor inspection and kernel debugging.

## Related
- `technique-data-reuse`
- `hw-unified-buffer`