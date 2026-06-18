---
id: technique-pr-modellink-2780
title: "PR Insight: Ascend/ModelLink #2780"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - pipeline-parallel
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2780"
---

# PR Insight: Ascend/ModelLink #2780

**Title:** fix gloo pipeline

## Overview
This PR fixes Gloo backend issues for pipeline parallelism in the PyTorch backend. It addresses communication problems in pipeline training.

## Technical Significance
Gloo is a critical communication backend for distributed training on Ascend NPUs. Fixing pipeline communication issues ensures stable and efficient pipeline parallelism execution, improving training reliability.

## Related
- `technique-pipeline-scheduling`
- `technique-hccl-optimization`