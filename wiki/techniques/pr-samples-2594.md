---
id: technique-pr-samples-2594
title: "PR Insight: Ascend/samples #2594"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - jpeg
  - vpc
  - rc-mode
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2594"
---

# PR Insight: Ascend/samples #2594

**Title:** jpegd_vpc_jpege sample support rc mode

## Overview
This PR adds RC (Run Complete) mode support to the jpegd_vpc_jpege sample. The sample demonstrates JPEG decode, VPC (Vision Processing Center) processing, and JPEG encode operations, now with RC mode capability.

## Technical Significance
JPEG codec operations are fundamental for image processing workloads. VPC operations enable efficient image transformations. RC mode support ensures the sample demonstrates complete pipeline execution patterns.

## Related
- `technique-format-conversion`
- `hw-vector-unit`
- `technique-pipeline-scheduling`