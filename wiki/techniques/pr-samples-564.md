---
id: technique-pr-samples-564
title: "PR Insight: Ascend/samples #564"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - upgrade
  - file-permissions
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/564"
---

# PR Insight: Ascend/samples #564

**Title:** 优化upgrade时对文件权限的更改

## Overview
This PR optimizes how file permissions are handled during the upgrade process in the samples repository. The changes ensure that file permissions are preserved or appropriately modified during version updates, preventing permission-related issues.

## Technical Significance
Fixes a practical deployment issue where upgrade scripts might break file permissions, causing execution failures. Proper permission handling is essential for maintainable sample code that can be reliably upgraded across versions.

## Related
- `pattern-deployment`