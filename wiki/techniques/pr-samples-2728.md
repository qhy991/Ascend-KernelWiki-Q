---
id: technique-pr-samples-2728
title: "PR Insight: Ascend/samples #2728"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - profiling
  - samples
  - tooling
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2728"
---

# PR Insight: Ascend/samples #2728

**Title:** change msprof to msprof op

## Overview
This PR updates samples to use msprof op instead of msprof for profiling. This likely refers to changing how the profiling tool is invoked or integrated, possibly from a general profiler to an operator-specific profiling interface.

## Technical Significance
Proper profiling integration is essential for performance analysis and optimization. Using the correct profiling interface ensures accurate performance measurements and helps developers identify bottlenecks in their kernel implementations.

## Related
- technique-pipeline-scheduling