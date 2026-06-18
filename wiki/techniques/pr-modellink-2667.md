---
id: technique-pr-modellink-2667
title: "PR Insight: Ascend/ModelLink #2667"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - pipeline-parallel
  - feature
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2667"
---

# PR Insight: Ascend/ModelLink #2667

**Title:** [pytorch][feature]dualpipe in sft

## Overview
This PR adds dual-pipeline support for supervised fine-tuning (SFT) in the PyTorch backend. It enables more efficient pipeline parallelism during fine-tuning workflows.

## Technical Significance
Dual-pipeline parallelism improves throughput during fine-tuning by better utilizing Ascend NPU resources. This feature increases training efficiency for SFT tasks, reducing time-to-convergence for fine-tuning large models.

## Related
- `technique-pipeline-scheduling`
- `technique-distributed-training`