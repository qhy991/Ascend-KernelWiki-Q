---
id: technique-pr-samples-2801
title: "PR Insight: Ascend/samples #2801"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - build-system
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2801"
---

# PR Insight: Ascend/samples #2801

**Title:** update include path for Libraries * update include path for Libraries

## Overview
This PR updates the include paths for Libraries in the sample code build system. The change reflects updates in the Ascend CANN toolkit package structure to maintain compatibility.

## Technical Significance
Correct include paths are essential for building samples successfully with newer CANN toolkit versions. This update prevents build failures due to package structure changes.

## Related
- Build system patterns, CANN toolkit integration