---
id: technique-pr-modellink-2567
title: "PR Insight: Ascend/ModelLink #2567"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - glm
  - 0day
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2567"
---

# PR Insight: Ascend/ModelLink #2567

**Title:** 0day新增适配模型 GLM-Z1-9B-0414 GLM-4-32B-0414

## Overview
This PR adds support for two GLM model variants: GLM-Z1-9B-0414 and GLM-4-32B-0414. The 0day designation indicates rapid-response support for these newly released models, covering both small (9B) and large (32B) sizes.

## Technical Significance
GLM models have unique architectural features that require specific training configurations. Supporting both 9B and 32B sizes demonstrates ModelLink's flexibility across scales. The implementation must handle efficient distributed training and memory optimization for both model sizes on Ascend hardware.

## Related
- `technique-training-script`