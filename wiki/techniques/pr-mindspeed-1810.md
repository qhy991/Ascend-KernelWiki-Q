---
id: technique-pr-mindspeed-1810
title: "PR Insight: Ascend/MindSpeed #1810"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - pytorch
  - llama
  - feature
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1810"
---

# PR Insight: Ascend/MindSpeed #1810

**Title:** remove --use-legacy-models arg from llama ST, add feature scenario and environmental variable annotations

## Overview
This PR removes the --use-legacy-models argument from LLaMA ST (Sequence Transformer) and adds annotations for feature scenarios and environment variables. The changes modernize the interface and improve documentation.

## Technical Significance
Removing legacy arguments simplifies the user interface and guides users toward newer, better-supported features. Adding scenario and environment variable annotations helps users understand feature dependencies and configuration options for LLaMA training on Ascend NPUs.

## Related
- pytorch-integration
- feature-validation
- configuration-management