---
id: technique-pr-vllm-ascend-5579
title: "PR Insight: vllm-project/vllm-ascend #5579"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - gating
  - aclnn
  - custom-op
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5579"
---

# PR Insight: vllm-project/vllm-ascend #5579

**Title:** [Kernel] Add moe_gating_top_k operator support for Ascend NPU

## Overview
This PR adds a custom `moe_gating_top_k` operator for Ascend NPU, replacing the torch_npu implementation. The new operator includes renormalization support for softmax scenarios and provides optimized top-k expert selection for MoE models with comprehensive tiling strategies for different architectures.

## Technical Significance
The custom MoE gating operator provides better performance optimization compared to the generic torch_npu implementation by leveraging Ascend NPU-specific tiling and computation strategies. The renormalization support ensures correctness in softmax scenarios while the custom implementation enables better resource utilization and reduced kernel launch overhead.

## Related
- `pattern-moe` (MoE patterns and operations)
- `kernel-moe` (MoE gating operations)
- `technique-aclnn` (Custom operator development)
- `technique-tiling` (Memory tiling strategies)