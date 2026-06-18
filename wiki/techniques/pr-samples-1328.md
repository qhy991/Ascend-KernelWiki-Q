---
id: technique-pr-samples-1328
title: "PR Insight: Ascend/samples #1328"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
  - ascend310p
tags:
  - dvpp
  - jpege
  - samples
  - cplusplus
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1328"
---

# PR Insight: Ascend/samples #1328

**Title:** update cplusplus/level1_single_api/7_dvpp/jpege_sample/src/common/sample_comm.h.

## Overview
This PR updates the sample_comm.h header file in the DVPP JPEGE sample. The changes improve common utilities and shared functionality for the JPEG encoding sample.

## Technical Significance
Common header files provide reusable functions across sample applications. Updates improve consistency and reduce code duplication in DVPP JPEG encoding samples.

## Related
- `technique-dvpp`
- `pattern-jpeg-encoding`