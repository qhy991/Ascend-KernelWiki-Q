---
id: technique-pr-samples-2482
title: "PR Insight: Ascend/samples #2482"
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
  - "https://gitee.com/ascend/samples/pulls/2482"
---

# PR Insight: Ascend/samples #2482

**Title:** fix kernellaunch bug for sim mode

## Overview
This PR continues fixing kernel launch bugs in simulation mode, likely addressing additional scenarios or improving the robustness of the fix from PRs #2454 and #2455.

## Technical Significance
Multiple iterative fixes indicate the complexity of correctly handling kernel launches across simulation and hardware modes. Each fix improves sample reliability for developers testing their kernels without NPU access.

## Related
- `pattern-kernel-launch`, `pattern-development-workflow`