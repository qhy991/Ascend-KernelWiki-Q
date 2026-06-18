---
id: technique-pr-modellink-2948
title: "PR Insight: Ascend/ModelLink #2948"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - mindspore
  - finetune
  - data-processing
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2948"
---

# PR Insight: Ascend/ModelLink #2948

**Title:** [mindspore][2.1.0][sh&doc]add finetune data convert

## Overview
This PR adds finetune data conversion support for MindSpore 2.1.0 backend in ModelLink. It includes scripts and documentation for converting data into the format required for fine-tuning workflows.

## Technical Significance
Data conversion is a critical preprocessing step for fine-tuning large models on Ascend NPUs. This support enables users to prepare their datasets efficiently for fine-tuning workflows using the MindSpore backend, reducing setup time and potential data pipeline errors.

## Related
- `technique-distributed-training`
- `technique-data-reuse`