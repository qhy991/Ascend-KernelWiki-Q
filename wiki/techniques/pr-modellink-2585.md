---
id: technique-pr-modellink-2585
title: "PR Insight: Ascend/ModelLink #2585"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - deepseekv3
  - training
  - mixed-precision
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2585"
---

# PR Insight: Ascend/ModelLink #2585

**Title:** [core-llm][dskv3]fix loss scale for micro batches

## Overview
This PR fixes loss scaling for micro batches in DeepSeekV3 (dskv3) training. The changes address incorrect loss scaling behavior when training with gradient accumulation and micro-batch processing.

## Technical Significance
Correct loss scaling is critical for mixed-precision training to prevent gradient underflow or overflow. For micro-batch training, loss scaling must be synchronized across accumulation steps. This fix ensures numerical stability and convergence when training DeepSeekV3 on Ascend NPUs with gradient accumulation.

## Related
- `technique-mixed-precision`