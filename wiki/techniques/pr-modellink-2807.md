---
id: technique-pr-modellink-2807
title: "PR Insight: Ascend/ModelLink #2807"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - bugfix
  - logging
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2807"
---

# PR Insight: Ascend/ModelLink #2807

**Title:** enable run pipe error log

## Overview
This PR enables error logging for pipeline parallelism runs in the PyTorch backend. It improves error reporting during pipeline training on Ascend NPUs.

## Technical Significance
Better error logging accelerates debugging of pipeline parallelism issues on Ascend NPUs. This improvement helps users quickly identify and resolve problems during distributed training, reducing development time.

## Related
- `technique-pipeline-scheduling`
- `technique-distributed-training`