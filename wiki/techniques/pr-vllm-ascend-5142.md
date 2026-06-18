---
id: technique-pr-vllm-ascend-5142
title: "PR Insight: vllm-project/vllm-ascend #5142"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - matmul
  - mla
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5142"
---

# PR Insight: vllm-project/vllm-ascend #5142

**Title:** fix: use batch_matmul_transpose operator in MLA _v_up_proj for better performance

## Overview
This PR optimizes the MLA (Multi-head Latent Attention) `_v_up_proj` method by using the optimized `torch.ops._C_ascend.batch_matmul_transpose` operator for FP16/BF16 dtypes instead of the less efficient `torch.bmm` with multiple transpose operations.

## Technical Significance
The batch_matmul_transpose operator is specifically optimized for Ascend NPUs to handle matrix multiplication with implicit transpose efficiently. This optimization avoids unnecessary data movement and transpose operations, significantly improving inference performance for MLA-based models on Ascend hardware.

## Related
- technique-matmul
- technique-mla
- technique-performance-optimization