---
id: technique-pr-samples-2809
title: "PR Insight: Ascend/samples #2809"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - build-system
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2809"
---

# PR Insight: Ascend/samples #2809

**Title:** update include path for Libraries * update include path for Libraries

## Overview
This PR updates the include paths for Libraries in the sample code build system. The change reflects updates in the Ascend CANN toolkit package structure.

## Technical Significance
Correct include paths are essential for building samples successfully. This update ensures samples compile with newer versions of the Ascend CANN toolkit, particularly the ascend-cann-toolkit package structure changes.

## Related
- Build system patterns for AscendC projects