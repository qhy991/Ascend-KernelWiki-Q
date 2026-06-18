---
id: technique-pr-samples-1473
title: "PR Insight: Ascend/samples #1473"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - ascendc
  - one-to-many
  - inference
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1473"
---

# PR Insight: Ascend/samples #1473

**Title:** add one to many sample

## Overview
This PR adds a new sample demonstrating a one-to-many inference pattern in the Ascend samples repository. The sample likely shows how to process multiple outputs or parallel inference scenarios using AscendC operators and the CANN framework.

## Technical Significance
Provides developers with a reference implementation for multi-output inference patterns on Ascend hardware, helping them understand how to handle branching inference flows and efficient multi-output operator design.

## Related
- technique-operator-fusion
- technique-inference-pipeline