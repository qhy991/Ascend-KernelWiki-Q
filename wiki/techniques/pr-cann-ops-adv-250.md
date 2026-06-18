---
id: technique-pr-cann-ops-adv-250
title: "PR Insight: Ascend/cann-ops-adv #250"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - operator-fusion
  - hccl-optimization
  - layernorm
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/250"
---

# PR Insight: Ascend/cann-ops-adv #250

**Title:** add inplace_matmul_all_reduce_add_rms_norm

## Overview
This PR adds an in-place fused operator that combines matrix multiplication, all-reduce communication, addition, and RMS normalization into a single kernel. The operator is implemented in AscendC and provides memory efficiency by computing the result in-place without allocating additional intermediate buffers.

## Technical Significance
This fused operator is critical for transformer model inference and training, particularly in post-attention computations where the typical pattern is matmul → all-reduce → residual add → RMS norm. By fusing these operations, the PR reduces memory bandwidth pressure and improves performance through reduced kernel launch overhead. The implementation leverages both Cube units for matmul and vector units for normalization, with HCCL integration for efficient all-reduce communication across devices.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
- `technique-matmul-ascendc`
- `technique-layernorm`