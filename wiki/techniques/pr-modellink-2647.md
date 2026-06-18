---
id: technique-pr-modellink-2647
title: "PR Insight: Ascend/ModelLink #2647"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - training
  - pipeline
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2647"
---

# PR Insight: Ascend/ModelLink #2647

**Title:** fix pipeline errors

## Overview
This PR fixes errors in the pipeline parallelism implementation of ModelLink. The changes address specific bugs that cause training failures or incorrect results when using pipeline parallelism on Ascend hardware.

## Technical Significance
Pipeline parallelism errors can cause training to fail silently or produce incorrect results. Fixing these errors ensures reliable and correct distributed training on Ascend NPUs, which is critical for successful training of large-scale models.

## Related
- technique-pipeline-scheduling
- technique-hccl-optimization