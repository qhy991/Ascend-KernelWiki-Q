---
id: technique-pr-vllm-ascend-10258
title: "PR Insight: vllm-project/vllm-ascend #10258"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - moe
  - swiglu
  - deepseek
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10258"
---

# PR Insight: vllm-project/vllm-ascend #10258

**Title:** [BugFix][DeepSeek] Preserve no-group dequant SwiGLU clamp

## Overview
This PR fixes a precision issue in DeepSeek-V4-Pro shared-expert quantization by preserving no-group semantics for `npu_dequant_swiglu_quant`. The previous fix #9600 synthesized a `[x.size(0)]` group_index tensor for no-group cases, which changed the tiling key from the no-group `200000000+` family to the has-group `100000000+` family. This caused decode-stage corruption where the first token was correct but subsequent tokens drifted. The fix routes the arch32 int32 no-group `swiglu_mode=1` path into the DSK no-group kernel using `groupNum_=1` for tiling checks, ensuring clamp semantics are honored while maintaining no-group behavior.

## Technical Significance
This is a critical quantization correctness fix that demonstrates the importance of preserving no-group semantics in MoE quantization kernels. The synthetic group_index approach fundamentally changed kernel behavior, moving from a no-group specialization to a has-group path with different index handling. The fix maintains the original no-group tiling key family and uses `groupNum_=1` internally for tiling checks without changing the no-group semantics. This ensures that clamp limits are properly applied in the no-group case while avoiding the corruption issues caused by the incorrect has-group path.

## Related
- `technique-quantization`
- `technique-moe`
- `technique-deepseek`