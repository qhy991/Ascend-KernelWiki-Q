---
id: technique-pr-modellink-2800
title: "PR Insight: Ascend/ModelLink #2800"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - mindspore
  - moe
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2800"
---

# PR Insight: Ascend/ModelLink #2800

**Title:** [mindspore][bugfix] fix PackProb's patch of moe-unperm2-mem-optim

## Overview
This PR fixes the PackProb operator patch related to MoE unpermute memory optimization in the MindSpore backend. It addresses issues with the memory-efficient MoE routing implementation.

## Technical Significance
MoE (Mixture of Experts) models require careful memory management during expert routing operations. Fixing this patch ensures proper memory optimization for MoE training on Ascend NPUs, reducing memory footprint and improving training efficiency.

## Related
- `technique-moe`
- `technique-data-reuse`