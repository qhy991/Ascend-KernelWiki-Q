---
id: technique-pr-vllm-ascend-3827
title: "PR Insight: vllm-project/vllm-ascend #3827"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - deepseek
  - allgather
  - gate
  - bugfix
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3827"
---

# PR Insight: vllm-project/vllm-ascend #3827

**Title:** [v0.11.0] [Bugfix] [MoE]fix error in deepseek when using allgather

## Overview
This is a cherry-pick of PR #3824 to the v0.11.0 branch, fixing the DeepSeek MoE allgather error. The fix removes gate-related computations from FusedMoE module in eager/aclgraph mode and deprecates `rm_router_logits` in those modes, adapting the changes for the v0.11.0 directory structure.

## Technical Significance
Backporting this fix ensures v0.11.0 users can run DeepSeek V3/R1 models with allgather communication without errors. The removal of gate computations in eager/aclgraph modes maintains compatibility across different execution backends.

## Related
- `technique-moe`
- `technique-allgather`
- `technique-deepseek`