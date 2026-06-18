---
id: technique-pr-modellink-3382
title: "PR Insight: ModelLink #3382"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - scripts
  - mindspore
  - llama
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/3382"
---

# PR Insight: ModelLink #3382 - [mindspore][master]add llama sh

## Overview
This PR introduces shell scripts for the LLaMA model under the MindSpore framework within the ModelLink repository.

## Technical Details
The addition of shell scripts (`sh`) for LLaMA simplifies the execution of training, evaluation, or inference workflows. These scripts typically wrap complex command-line arguments needed by the MindSpore backend, configuring environment variables (such as parallel strategies, device allocation for Ascend NPUs, and memory management) to streamline the usage of the LLaMA model on Ascend hardware.

### Key Changes
- **Framework:** MindSpore
- **Model:** LLaMA
- **Component:** Execution shell scripts

## Impact
This update significantly improves usability for users attempting to run LLaMA models with MindSpore on Ascend 910/910B NPUs by providing ready-to-use executable scripts, reducing the barrier to entry and standardizing the launch configurations.
