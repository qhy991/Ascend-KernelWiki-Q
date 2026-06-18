---
id: technique-pr-modellink-3381
title: "PR Insight: ModelLink #3381"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - shell-script
  - mixtral
  - mindspore
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/3381"
---

# PR Insight: ModelLink #3381 - Add Mixtral Shell Scripts for MindSpore

## Overview
This PR adds shell scripts (`.sh`) for the Mixtral model in the `master` branch, specifically tailored for the MindSpore backend within the ModelLink repository.

## Technical Details
- **Model**: Mixtral (Mixture of Experts architecture).
- **Component**: Addition of execution/launch shell scripts (`sh`).
- **Framework Track**: MindSpore (`[mindspore]`).

The PR introduces the launcher scripts necessary to run Mixtral training, evaluation, or inference on Ascend NPUs using the MindSpore framework. Shell scripts in ModelLink generally encapsulate the complex arguments needed to start distributed tasks, including NPU device allocation, parallel configurations (e.g., tensor parallel, pipeline parallel, expert parallel), and path configurations.

## Impact
- Enhances usability by providing out-of-the-box launcher scripts for the Mixtral model on Ascend hardware using MindSpore.
- Facilitates easier reproduction of Mixtral runs for developers and researchers.
