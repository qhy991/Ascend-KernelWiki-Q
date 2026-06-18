---
id: technique-pr-samples-2725
title: "PR Insight: Ascend/samples #2725"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - synchronization
  - event-sync
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2725"
---

# PR Insight: Ascend/samples #2725

**Title:** add hard sync samples

## Overview
This PR adds samples demonstrating hard synchronization on Ascend. Hard sync ensures strict ordering of operations across streams or devices.

## Technical Significance
Hard synchronization is sometimes necessary for correctness when operations have dependencies across streams or devices. These samples help developers understand when and how to use synchronization effectively.

## Related
- `technique-event-sync`, `synchronization-patterns`