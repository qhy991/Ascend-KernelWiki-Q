---
id: technique-pr-modellink-2717
title: "PR Insight: Ascend/ModelLink #2717"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - moe
  - router
  - refactor
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2717"
---

# PR Insight: Ascend/ModelLink #2717

**Title:** moe router feature patch refactor

## Overview
This PR refactors the feature patch for MoE (Mixture-of-Experts) routing. The refactoring improves code maintainability and potentially optimizes the routing logic for better performance on Ascend hardware.

## Technical Significance
The MoE router is a critical component that determines which experts process each token. Refactoring the feature patch improves code quality and may enable better optimization of expert routing operations on Ascend NPUs, reducing communication overhead and improving load balancing.

## Related
- technique-operator-fusion