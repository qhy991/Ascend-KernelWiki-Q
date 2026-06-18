---
id: technique-pr-samples-1011
title: "PR Insight: Ascend/samples #1011"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - calibration
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1011"
---

# PR Insight: Ascend/samples #1011

**Title:** Bug fix: always extract calibration img when rerun cmd

## Overview
Fixes a duplicate issue in the AMCT calibration workflow where calibration images were not being extracted when re-running commands, ensuring reproducibility.

## Technical Significance
Reinforces the importance of correct calibration data handling in quantization workflows. This appears to be the same fix as #1031, potentially applied to different sample directories.

## Related
- `technique-quantization` / `technique-calibration`
