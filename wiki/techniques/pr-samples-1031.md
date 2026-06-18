---
id: technique-pr-samples-1031
title: "PR Insight: Ascend/samples #1031"
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
  - "https://gitee.com/ascend/samples/pulls/1031"
---

# PR Insight: Ascend/samples #1031

**Title:** Bug fix: always extract calibration img when rerun cmd

## Overview
Fixes a bug in the AMCT (Ascend Model Compression Toolkit) calibration workflow where calibration images were not being extracted when re-running commands, causing reproducibility issues.

## Technical Significance
Ensures correct calibration data handling in quantization workflows, which is critical for model accuracy after compression. The fix likely addresses state management in the AMCT calibration pipeline.

## Related
- `technique-quantization` / `technique-calibration`
