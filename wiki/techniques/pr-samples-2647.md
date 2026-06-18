---
id: technique-pr-samples-2647
title: "PR Insight: Ascend/samples #2647"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - ascendc
  - queue-position
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2647"
---

# PR Insight: Ascend/samples #2647

**Title:** replace QuePosition

## Overview
This PR replaces QuePosition references with updated APIs or constants. The change updates sample code to use newer position-related interfaces for kernel execution or memory management.

## Technical Significance
Proper position handling is critical for tensor buffer management and instruction scheduling in AscendC. Using up-to-date APIs ensures samples demonstrate best practices for tensor placement and execution ordering.

## Related
- `hw-instruction-queue`
- `technique-pipeline-scheduling`