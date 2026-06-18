---
id: technique-pr-mindspeed-2268
title: "PR Insight: Ascend/MindSpeed #2268"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - reuse-fp32
  - gloo-group
  - bugfix
  - communication
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2268"
---

# PR Insight: Ascend/MindSpeed #2268

**Title:** bugfix: fix bug for reuse_fp32 if disable gloo group

## Overview
This PR fixes a bug related to reuse_fp32 functionality when Gloo communication groups are disabled. Gloo is a collective communication library, and reusing FP32 precision is likely a memory or performance optimization.

## Technical Significance
The fix ensures reuse_fp32 works correctly when Gloo groups are disabled, which is important for configurations using other communication backends. Proper handling of different communication backends is essential for framework flexibility and compatibility.

## Related
- `technique-fp32-optimization`
- `pattern-communication-backend-compatibility`
- `pattern-precision-handling`