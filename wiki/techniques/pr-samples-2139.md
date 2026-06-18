---
id: technique-pr-samples-2139
title: "PR Insight: Ascend/samples #2139"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - add
  - unaligned
  - ascendc
  - 910c
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2139"
---

# PR Insight: Ascend/samples #2139

**Title:** 对UnalignAddCustomSample算子样例进行调用新增，并出去敏感词910C

## Overview
This PR adds invocation examples for the UnalignAddCustomSample operator and removes references to 910C (likely a sensitive hardware designation or deprecated product name).

## Technical Significance
Unaligned Add samples are important for handling real-world tensor shapes that don't align to hardware boundaries. Removing sensitive terminology ensures compliance with naming conventions.

## Related
- `kernel-elementwise`
- `technique-bank-conflict-avoidance`