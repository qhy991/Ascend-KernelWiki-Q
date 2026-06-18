---
id: technique-pr-samples-1978
title: "PR Insight: Ascend/samples #1978"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - inference
  - yolov7
  - build
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1978"
---

# PR Insight: Ascend/samples #1978

**Title:** 【轻量级 PR】：update inference/modelInference/sampleYOLOV7MultiInput/scripts/sample_build.sh.

## Overview
This PR updates the build script for the YOLOV7 multi-input inference sample. The changes modify the shell script used to compile the sample application.

## Technical Significance
Build script updates ensure samples compile correctly with current CANN versions and toolchains. Proper build configuration is essential for developers to successfully compile and run inference samples without encountering build errors.

## Related
- `technique-ascendc`