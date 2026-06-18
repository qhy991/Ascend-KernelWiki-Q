---
id: technique-pr-samples-1363
title: "PR Insight: Ascend/samples #1363"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - cpu-control
  - bugfix
  - lightweight
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1363"
---

# PR Insight: Ascend/samples #1363

**Title:** 【轻量级 PR】：问题单DTS2022080813673修改ctrlcpu 流程

## Overview
This is a lightweight PR that fixes the CPU control flow issue related to bug report DTS2022080813673. This is likely another part of the same CPU control problem addressed in PRs #1361 and #1362.

## Technical Significance
CPU control flow is important for coordinating between host and device operations. This fix ensures proper CPU-NPU synchronization and task execution in the samples.

## Related
- technique-cpu-npu-synchronization