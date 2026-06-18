---
id: technique-pr-samples-2211
title: "PR Insight: Ascend/samples #2211"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - bugfix
  - memory-management
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2211"
---

# PR Insight: Ascend/samples #2211

**Title:** Fix destory

## Overview
This PR fixes a typo in a destroy function name (correcting "destory" to "destroy"). This fixes a bug that could cause build failures or undefined behavior.

## Technical Significance
Proper resource cleanup is critical in GPU/NPU programming to prevent memory leaks and device state corruption. This fix ensures correct destructor behavior.

## Related