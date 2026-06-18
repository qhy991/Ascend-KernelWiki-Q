---
id: technique-pr-vllm-ascend-6335
title: "PR Insight: vllm-project/vllm-ascend #6335"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - moe
  - shared-experts
  - inference
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6335"
---

# PR Insight: vllm-project/vllm-ascend #6335

**Title:** [Main2Main][BugFix] Add shared_experts check for AscendSharedFusedMoE

## Overview
This PR adds validation checks for shared experts in `AscendSharedFusedMoE` to handle Qwen3-MoE models that may not have shared experts. The fix adds checks to `multistream_overlap_shared_expert` and `multistream_overlap_gate` functions.

## Technical Significance
The previous implementation assumed shared experts always exist, causing errors with MoE models that use only routed experts. This fix ensures proper handling of both shared-expert and routed-expert-only MoE architectures, improving compatibility with diverse MoE model designs.

## Related
- `technique-moe`
- `technique-shared-experts`
- `technique-qwen3-moe`