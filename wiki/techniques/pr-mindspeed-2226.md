---
id: technique-pr-mindspeed-2226
title: "PR Insight: Ascend/MindSpeed #2226"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - testing
  - distributed
  - refactor
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2226"
---

# PR Insight: Ascend/MindSpeed #2226

**Title:** refactor:add dist-train ut

## Overview
This PR refactors and adds distributed training unit tests to MindSpeed. The change improves test coverage for distributed training scenarios including tensor parallel, pipeline parallel, and data parallel training configurations.

## Technical Significance
Comprehensive distributed training unit tests are essential for ensuring correctness of complex parallel training strategies on Ascend NPUs. This refactoring improves test infrastructure for validating HCCL communication, gradient synchronization, and model partitioning logic. Better test coverage enables faster development and higher confidence in distributed training features, particularly for advanced parallel strategies like 2D tensor parallel and pipeline parallel with varying sequence lengths.

## Related
- `technique-hccl-optimization`
- `technique-event-sync`