---
id: technique-pr-samples-1793
title: "PR Insight: Ascend/samples #1793"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - resnet
  - acllite
  - samples
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1793"
---

# PR Insight: Ascend/samples #1793

**Title:** 【案例规范整改】sampleResNetQuickStart修复resize使用列表报错

## Overview
This PR fixes a bug in the sampleResNetQuickStart sample where resize operations were incorrectly using lists, causing errors during execution.

## Technical Significance
The QuickStart sample is often the first example developers use when learning Ascend inference. Fixing bugs in this foundational sample prevents confusion and ensures new users have a smooth onboarding experience to the Ascend ACL framework.

## Related
- `wiki-technique-inference`
- `wiki-technique-acl`