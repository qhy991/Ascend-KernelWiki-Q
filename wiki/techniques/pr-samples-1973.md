---
id: technique-pr-samples-1973
title: "PR Insight: Ascend/samples #1973"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - dataset
  - device
  - refactoring
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1973"
---

# PR Insight: Ascend/samples #1973

**Title:** modify dataset device to adjust code changes

## Overview
This PR modifies dataset device handling to adapt to code changes elsewhere in the samples repository. The update ensures dataset loading works correctly with modified code paths.

## Technical Significance
Dataset handling is critical for training and inference samples. Device-side dataset modifications ensure data flows correctly between host memory and device memory, which is essential for efficient data transfer and kernel execution on the NPU.

## Related
- `technique-ascendc`
- `technique-mte`