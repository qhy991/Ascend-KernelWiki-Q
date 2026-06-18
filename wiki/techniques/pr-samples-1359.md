---
id: technique-pr-samples-1359
title: "PR Insight: Ascend/samples #1359"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - jpeg-decoding
  - dvpp
  - lightweight
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1359"
---

# PR Insight: Ascend/samples #1359

**Title:** 【轻量级 PR】：update cplusplus/level1_single_api/7_dvpp/jpegd_sample/src/sample_comm_jpegd.cpp.

## Overview
This is a lightweight PR updating the JPEG decoding sample common code in sample_comm_jpegd.cpp. The update likely fixes a minor issue or improves the JPEG decoding implementation in the DVPP samples.

## Technical Significance
Common code updates benefit multiple samples that use shared JPEG decoding functionality. This ensures consistent and correct JPEG decoding across DVPP samples on Ascend hardware.

## Related
- hw-dvpp
- technique-jpeg-decoding