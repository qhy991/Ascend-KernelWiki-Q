---
id: technique-pr-vllm-ascend-8574
title: "PR Insight: vllm-project/vllm-ascend #8574"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - msprobe
  - aclgraph
  - debugging
  - graph-mode
  - bugfix
  - data-collection
  - configuration
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8574"
---

# PR Insight: vllm-project/vllm-ascend #8574

**Title:** [BugFix] msprobe data collection support aclgraph

## Overview
This PR fixes and clarifies msprobe dump behavior for Ascend graph mode with three goals: 1) Avoid dumping dummy-run data by calling _finalize_dump_data with dump=False in dummy_run. 2) Keep eager/graph debugger invocation compatible by forwarding kwargs to debugger.step(). 3) Update docs to reflect graph-mode constraints. The changes ensure predictable debugger behavior between eager and graph modes.

## Technical Significance
Proper msprobe integration is critical for debugging and profiling in production deployments. The fix prevents unwanted dump artifacts from warmup/dummy paths and ensures compatibility across execution modes. Updated documentation clearly shows configuration support differences between eager and graph modes, improving user experience for debugging workflows.

## Related
- `technique-debugging`
- `technique-graph-mode`
- `technique-profiling`