---
id: technique-pr-vllm-ascend-10181
title: "PR Insight: vllm-project/vllm-ascend #10181"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - flash-attention
  - attention
  - ascend310p
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10181"
---

# PR Insight: vllm-project/vllm-ascend #10181

**Title:** [Feature][310p] support compressed mask for 310P flashattention and pagedattention-split-fuse

## Overview
This PR updates the Ascend 310P attention implementation to use newer NPU attention operators: `torch_npu._npu_flash_attention_v3` for flash attention and `torch_npu._npu_paged_attention_splitfuse_v2` for paged attention. The update introduces a fixed sequence length of 2048 for the 310P compressed-mask path and configures the flash attention call with proper `mask_type` handling. The PR addresses an issue where positional argument usage in operator calls was fragile due to parameter mismatch on actual NPU hardware, specifically where the 4th positional argument is `pse_shift` not `atten_mask`.

## Technical Significance
This update is critical for Ascend 310P hardware compatibility and performance. The shift to newer NPU operators provides better support for compressed attention masks and more reliable operator invocation on 310P devices. The fix prevents incorrect parameter passing that could lead to incorrect attention computation or crashes, ensuring proper mask type semantics are maintained across different NPU hardware generations.

## Related
- `technique-flash-attention`
- `hw-ascend310p`
- `technique-attention-optimization`