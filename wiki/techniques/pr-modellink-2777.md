---
id: technique-pr-modellink-2777
title: "PR Insight: Ascend/ModelLink #2777"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - qwen
  - bugfix
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2777"
---

# PR Insight: Ascend/ModelLink #2777

**Title:** fix scripts of qwen3

## Overview
This PR fixes training scripts for Qwen3 models in ModelLink. It addresses configuration and execution issues for this model family.

## Technical Significance
Qwen3 is a widely-used model family. Fixing these scripts ensures users can successfully train Qwen3 models on Ascend NPUs without encountering script errors, improving platform usability.

## Related
- `technique-distributed-training`