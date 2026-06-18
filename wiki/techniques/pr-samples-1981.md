---
id: technique-pr-samples-1981
title: "PR Insight: Ascend/samples #1981"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - bugfix
  - simulator
  - driver
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1981"
---

# PR Insight: Ascend/samples #1981

**Title:** 修复设备上运行仿真器时，误引用驱动库的问题

## Overview
This PR fixes an issue where the simulator was incorrectly referencing driver libraries when running on the device. The fix ensures proper library linkage for simulator vs. hardware execution modes.

## Technical Significance
Correct library linking is essential for sample code to run in both simulation (development/testing) and hardware (production) environments. Mislinked libraries cause runtime failures, so this fix ensures developers can test in simulation without breaking hardware execution.

## Related
- `technique-ascendc`