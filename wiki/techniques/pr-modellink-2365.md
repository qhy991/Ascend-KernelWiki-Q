---
id: technique-pr-modellink-2365
title: "PR Insight: Ascend/ModelLink #2365"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - bugfix
  - pipeline
  - code-cleanup
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2365"
---

# PR Insight: Ascend/ModelLink #2365

**Title:** fix:删除2343中多余代码，完善pipeline

## Overview
This PR removes redundant code added in PR #2343 and completes the pipeline implementation. The cleanup improves code maintainability and ensures proper pipeline parallel execution.

## Technical Significance
Pipeline parallelism requires careful stage management and micro-batch scheduling. Removing redundant code prevents potential race conditions or incorrect state management between pipeline stages. The pipeline improvements likely address synchronization points, gradient accumulation, and stage communication, which are critical for training large models like DeepSeekV3 and Qwen across multiple Ascend nodes.

## Related
- `technique-pipeline-scheduling`
- `technique-hccl-optimization`