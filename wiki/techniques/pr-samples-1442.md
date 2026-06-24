---
id: technique-pr-samples-1442
title: "PR Insight: Ascend/samples #1442"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - dvpp
  - image-processing
  - update
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1442"
---

# PR Insight: Ascend/samples #1442

**Title:** samples仓中修改DVPP样例中的图片获取链接

## Overview
This PR updates the image download URLs in DVPP (Digital Vision Pre-Processing) samples. The modification ensures that sample images can be successfully downloaded, likely because the original URLs were broken or deprecated.

## Technical Significance
Working image links are essential for samples to be runnable by developers. DVPP is a key hardware accelerator for image preprocessing on Ascend devices, and functional samples help developers understand how to use it effectively.

## Related
- wiki-hardware-dvpp
- technique-image-preprocessing