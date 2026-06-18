---
id: technique-pr-mindspeed-2701
title: "PR Insight: Ascend/MindSpeed #2701"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspore
  - bugfix
  - pipeline-scheduling
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2701"
---

# PR Insight: Ascend/MindSpeed #2701

**Title:** [mindspore][bugfix][master] avoid pp scheduler shape error

## Overview
This PR fixes a shape error in the pipeline parallel (PP) scheduler when using MindSpore backend. The bug occurred during tensor shape validation in pipeline parallel execution, causing failures when micro-batches had varying or incompatible tensor shapes across pipeline stages.

## Technical Significance
Pipeline parallelism requires careful tensor shape management across micro-batches and stages. This fix ensures proper shape propagation in the PP scheduler, preventing runtime errors during distributed training. It addresses correctness issues in the pipeline scheduling logic that could cause training crashes or incorrect gradient accumulation.

## Related
- `technique-pipeline-scheduling`
- `pattern-microbatch-scheduling`