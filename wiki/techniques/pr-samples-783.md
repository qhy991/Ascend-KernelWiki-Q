---
id: technique-pr-samples-783
title: "PR Insight: Ascend/samples #783"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - nuq
  - quantization
  - configuration
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/783"
---

# PR Insight: Ascend/samples #783

**Title:** 更新NUQ用例的json文件，消除warning

## Overview
This PR updates the JSON configuration files for NUQ (Neural Network Unified Quantization) test cases to eliminate warning messages that appear during execution. This involves refining the configuration parameters to meet current requirements.

## Technical Significance
Cleaning up warning messages improves the user experience and ensures that the NUQ quantization samples run cleanly without spurious warnings. This helps developers focus on genuine issues rather than configuration noise during quantization workflow testing.

## Related
- N/A (configuration cleanup)