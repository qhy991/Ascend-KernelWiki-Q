---
id: technique-pr-samples-787
title: "PR Insight: Ascend/samples #787"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - jpeg
  - encoding
  - dvpp
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/787"
---

# PR Insight: Ascend/samples #787

**Title:** fixed jpege

## Overview
This PR fixes issues related to JPEG encoding (jpege) in the samples. JPEG encoding is commonly used for image compression and output, and this fix addresses problems in JPEG encoding operations on Ascend.

## Technical Significance
JPEG encoding is a common post-processing step in vision inference pipelines. This fix ensures that JPEG encoding works correctly on Ascend, likely using DVPP hardware acceleration. Correct JPEG encoding is important for saving inference results, especially in applications that need to output compressed images.

## Related
- JPEG encoding on Ascend
- DVPP image encoding
- Image compression in inference pipelines
- Post-processing workflows