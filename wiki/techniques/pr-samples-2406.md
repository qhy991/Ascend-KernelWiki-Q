---
id: technique-pr-samples-2406
title: "PR Insight: Ascend/samples #2406"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - matmul
  - group-matmul
  - optimization
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2406"
---

# PR Insight: Ascend/samples #2406

**Title:** 新增group matmul优化实践用例

## Overview
This PR adds optimization practice samples for group matrix multiplication. Group matmul (batched GEMM with different dimensions per batch item) is common in MoE transformers and attention mechanisms. The samples demonstrate optimization techniques for this workload pattern.

## Technical Significance
Group matmul optimization is non-trivial because each batch item may have different dimensions, complicating tiling and scheduling. These samples provide practical patterns for handling variable-sized workloads efficiently on Ascend hardware.

## Related
- `kernel-matmul-ascendc`, `technique-pipeline-scheduling`, `kernel-moe`