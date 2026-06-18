---
id: technique-pr-samples-2745
title: "PR Insight: Ascend/samples #2745"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - dvpp
  - device-management
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2745"
---

# PR Insight: Ascend/samples #2745

**Title:** dvpp sample support device_id setting

## Overview
This PR adds device_id setting support to DVPP (Digital Vision Pre-Processing) samples. The enhancement allows users to specify which Ascend device to use for DVPP operations.

## Technical Significance
DVPP is critical for image and video processing on Ascend. Device_id support enables multi-device workflows and proper resource management in production environments.

## Related
- DVPP patterns, device management patterns