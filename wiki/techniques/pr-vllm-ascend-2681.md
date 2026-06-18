---
id: technique-pr-vllm-ascend-2681
title: "PR Insight: vllm-project/vllm-ascend #2681"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - torchair
  - moe
  - multistream
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2681"
---

# PR Insight: vllm-project/vllm-ascend #2681

**Title:** [bugfix][torchair] fix multistream_moe problems in torchair graph mode

## Overview
This PR fixes two issues with multistream_moe in torchair graph mode: incorrect type checking (`AscendW8A8DynamicFusedMoEMethod` instead of `TorchairAscendW8A8DynamicFusedMoEMethod`) and improper mc2_mask chunking logic in the forward function.

## Technical Significance
The bug fix resolves multistream MoE functionality issues in torchair graph mode. By correcting the type check and ensuring mc2_mask is always chunked regardless of `replace_allreduce` setting, the PR enables proper multistream MoE operation in graph mode, which is critical for distributed MoE inference scenarios.

## Related
- `technique-torchair`
- `technique-moe`
- `technique-multistream`