---
id: technique-pr-samples-1360
title: "PR Insight: Ascend/samples #1360"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - png-decoding
  - dvpp
  - lightweight
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1360"
---

# PR Insight: Ascend/samples #1360

**Title:** 【轻量级 PR】：update cplusplus/level1_single_api/7_dvpp/pngd_sample/src/sample_comm_pngd.cpp.

## Overview
This is a lightweight PR updating the PNG decoding sample common code in sample_comm_pngd.cpp. The update likely fixes a minor issue or improves the PNG decoding implementation in the DVPP samples.

## Technical Significance
Common code updates benefit multiple samples that use shared PNG decoding functionality. This ensures consistent and correct PNG decoding across DVPP samples on Ascend hardware.

## Related
- wiki-hardware-dvpp
- technique-png-decoding