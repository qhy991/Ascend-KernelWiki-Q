---
id: technique-pr-samples-2454
title: "PR Insight: Ascend/samples #2454"
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
  - "https://gitee.com/ascend/samples/pulls/2454"
---

# PR Insight: Ascend/samples #2454

**Title:** fix kernellaunch bug for sim mode

## Overview
This PR fixes a bug in the kernel launch mechanism when running in simulation mode. Simulation mode allows developers to test AscendC kernels on CPU without requiring NPU hardware, but it has different runtime characteristics.

## Technical Significance
Robust simulation mode is critical for development and debugging, especially when NPU resources are scarce. Fixing kernel launch bugs ensures developers can iterate quickly on their kernels before deploying to hardware.

## Related
- `pattern-kernel-launch`, `pattern-development-workflow`