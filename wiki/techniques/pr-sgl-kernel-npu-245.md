---
id: technique-pr-sgl-kernel-npu-245
title: "PR Insight: sgl-project/sgl-kernel-npu #245"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - moe
  - notify-dispatch
  - cann8.3
  - bugfix
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/245"
---

# PR Insight: sgl-project/sgl-kernel-npu #245

**Title:** Fix notify dispatch cann8.3

## Overview
Fixes an issue where the A2 notify_dispatch operator gets stuck on CANN 8.3. The fix addresses compatibility problems between the operator implementation and the CANN 8.3 runtime.

## Technical Significance
CANN version compatibility is critical for stable production deployments. This fix prevents deadlocks and hangs that occur specifically with CANN 8.3, ensuring reliable operation across CANN versions. The resolution maintains backward compatibility while fixing the 8.3-specific issues.

## Related
- `wiki-kernel-moe`
- `wiki-technique-cann-compatibility`
- `wiki-technique-bugfix`
- `wiki-technique-deadlock-prevention`