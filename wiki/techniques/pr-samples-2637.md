---
id: technique-pr-samples-2637
title: "PR Insight: Ascend/samples #2637"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - broadcast
  - tiling
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2637"
---

# PR Insight: Ascend/samples #2637

**Title:** Broadcast tiling bugfix

## Overview
This PR fixes a bug in broadcast tiling logic. Broadcasting allows operations between tensors of different shapes by replicating smaller tensors to match larger ones. Tiling must account for broadcast semantics.

## Technical Significance
Broadcast is a fundamental operation used throughout ML frameworks. Correct tiling for broadcast ensures operations work correctly for tensors of any compatible shapes.

## Related
- `pattern-tiling`, `kernel-elementwise`