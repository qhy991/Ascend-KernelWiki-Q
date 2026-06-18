---
id: technique-pr-samples-1180
title: "PR Insight: Ascend/samples #1180"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - command-line
  - configuration
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1180"
---

# PR Insight: Ascend/samples #1180

**Title:** add queue_len in cmd

## Overview
This PR adds a queue_len parameter to the command-line interface of a sample application.

## Technical Significance
Queue length configuration is important for pipeline-based applications, allowing developers to tune buffer sizes based on workload characteristics. Proper queue sizing helps balance memory usage in the unified buffer with throughput, enabling efficient pipelining of operations on Ascend hardware.

## Related
- technique-pipeline-scheduling
- technique-double-buffering
- hw-unified-buffer