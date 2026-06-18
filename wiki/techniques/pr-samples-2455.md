---
id: technique-pr-samples-2455
title: "PR Insight: Ascend/samples #2455"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - kernel-launch
  - bugfix
  - simulation
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2455"
---

# PR Insight: Ascend/samples #2455

**Title:** fix kernellaunch bug for sim mode

## Overview
This PR is a follow-up fix to the kernel launch bug in simulation mode (PR #2454), likely addressing additional edge cases or improving the robustness of the fix.

## Technical Significance
Multiple PRs fixing the same area indicate complexity in the simulation mode implementation. Comprehensive fixes ensure samples work reliably across different simulation scenarios and CANN versions.

## Related
- `pattern-kernel-launch`, `pattern-development-workflow`