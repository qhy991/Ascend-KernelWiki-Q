---
id: technique-pr-samples-2805
title: "PR Insight: Ascend/samples #2805"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - build-system
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2805"
---

# PR Insight: Ascend/samples #2805

**Title:** adaptor new ascend-cann-toolkit pkg include path * adaptor new ascend-cann-toolkit pkg include path

## Overview
This PR adapts the sample code build system to the new ascend-cann-toolkit package include path structure. The change ensures compatibility with updated CANN toolkit packaging.

## Technical Significance
Keeping samples synchronized with the CANN toolkit package structure is essential for user success. This adaptation prevents build failures and ensures samples work with the latest Ascend development environment.

## Related
- Build system patterns, CANN toolkit integration