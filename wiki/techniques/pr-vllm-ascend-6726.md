---
id: technique-pr-vllm-ascend-6726
title: "PR Insight: vllm-project/vllm-ascend #6726"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - fusion
  - quantization
  - rms-norm
  - npugraph-ex
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6726"
---

# PR Insight: vllm-project/vllm-ascend #6726

**Title:** [bugfix] adapt bugfix for norm_quant_fusion_pass to npugraph_ex

## Overview
This PR adapts bugfixes from norm_quant_fusion_pass to graphex_norm_quant_fusion_pass for the npugraph_ex backend. It replaces torch.ops.npu.npu_add_rms_norm with torch.ops._C_ascend.npu_add_rms_norm_bias and improves fusion by passing bias directly instead of using separate add operations.

## Technical Significance
Ensures consistency and correctness of RMSNorm quantization fusion patterns in npugraph_ex graph compilation. The improved fusion reduces operation count and improves performance by eliminating separate bias addition operations.

## Related
- `technique-operator-fusion`
- `technique-quantization`