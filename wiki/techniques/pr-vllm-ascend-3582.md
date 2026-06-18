---
id: technique-pr-vllm-ascend-3582
title: "PR Insight: vllm-project/vllm-ascend #3582"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - multistream
  - hccl-optimization
  - aclgraph
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3582"
---

# PR Insight: vllm-project/vllm-ascend #3582

**Title:** [MoE][Multistream] Avoid performing communication in extra stream.

## Overview
This PR prevents communication operations for shared experts from running in the extra stream, as this caused rtMemcpy errors in aclgraph when using shared experts with multistream. It also introduces a global variable for the extra stream object to avoid allocating streams per layer in full-graph mode. Changes were made to `vllm_ascend/ops/common_fused_moe.py` and `vllm_ascend/utils.py`.

## Technical Significance
Communication in extra streams can introduce synchronization issues and memory copy errors, particularly in aclgraph's full-graph mode. By moving shared expert communication out of the extra stream and using a global stream object, this fix reduces resource allocation overhead and prevents rtMemcpy errors, improving stability for multistream MoE inference.

## Related
- `technique-moe`
- `technique-hccl-optimization`
- `technique-multistream`