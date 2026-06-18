---
id: technique-pr-samples-1146
title: "PR Insight: Ascend/samples #1146"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - jpegd
  - dvpp
  - api-update
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1146"
---

# PR Insight: Ascend/samples #1146

**Title:** modify jpegd src for use acldvppJpegGetImageInfoV2 and acldvppJpegPredictDecSize.

## Overview
This PR updates the JPEG decoder (JPEGD) sample to use the newer V2 APIs: acldvppJpegGetImageInfoV2 for retrieving JPEG image information and acldvppJpegPredictDecSize for predicting decoder memory requirements. This replaces older API versions with their enhanced counterparts.

## Technical Significance
Migrating to V2 APIs provides better compatibility and potentially improved functionality for JPEG image metadata extraction and memory size prediction. These APIs offer more accurate image information and better memory allocation planning, which is crucial for efficient image preprocessing pipelines on Ascend NPU.

## Related
- JPEG decoder (JPEGD) implementation
- DVPP API migration
- Image metadata extraction
- Memory size prediction