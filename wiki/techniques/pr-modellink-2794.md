---
id: technique-pr-modellink-2794
title: "PR Insight: Ascend/ModelLink #2794"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - qwen
  - oom
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2794"
---

# PR Insight: Ascend/ModelLink #2794

**Title:** fix oom of tune of qwen25-32b

## Overview
This PR fixes out-of-memory (OOM) issues during fine-tuning of Qwen2.5 32B model. It addresses memory management problems for this model size.

## Technical Significance
OOM fixes for mid-sized models like Qwen2.5 32B are essential for enabling fine-tuning workflows on Ascend NPUs. This fix allows users to fine-tune this model successfully within available memory constraints.

## Related
- `technique-data-reuse`
- `technique-distributed-training`