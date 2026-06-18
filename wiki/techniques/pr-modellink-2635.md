---
id: technique-pr-modellink-2635
title: "PR Insight: Ascend/ModelLink #2635"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - training
  - script
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2635"
---

# PR Insight: Ascend/ModelLink #2635

**Title:** update qwen3 error in sh

## Overview
This PR fixes errors in shell scripts related to Qwen3 model training. The changes address script-level issues that were causing errors during Qwen3 training workflows.

## Technical Significance
Script fixes are critical for stable training pipelines on Ascend hardware. Correcting shell errors ensures proper environment setup, data paths, and training command execution, preventing wasted compute resources and failed training runs.

## Related
- `technique-training-script`