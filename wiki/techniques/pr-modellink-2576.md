---
id: technique-pr-modellink-2576
title: "PR Insight: Ascend/ModelLink #2576"
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
  - "https://gitee.com/ascend/ModelLink/pulls/2576"
---

# PR Insight: Ascend/ModelLink #2576

**Title:** 0day新增适配模型 GLM-Z1-Rumination-32B-0414 和模型 GLM-4-32B-Base-0414

## Overview
This PR adds support for two GLM model variants: GLM-Z1-Rumination-32B-0414 and GLM-4-32B-Base-0414. The 0day designation indicates rapid-response support for these newly released models.

## Technical Significance
GLM (General Language Model) variants use specific attention and layer norm configurations. Adding 0day support for new models requires quickly understanding architecture differences and adapting training configurations to leverage Ascend's optimized operators for these 32B parameter models.

## Related
- `technique-training-script`