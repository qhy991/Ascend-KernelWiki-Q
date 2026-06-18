---
id: technique-pr-vllm-ascend-7064
title: "PR Insight: vllm-project/vllm-ascend #7064"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - layer-count
  - aclgraph
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7064"
---

# PR Insight: vllm-project/vllm-ascend #7064

**Title:** [Bugfix] Fix incorrect layer count for MTP models in update_aclgraph_sizes

## Overview
Fixes incorrect layer count calculation for MTP models in `update_aclgraph_sizes()` function. For MTP models, the draft model's layer count is stored in `num_nextn_predict_layers` or `mtp_num_hidden_layers` (for Qwen3.5), not in the standard `num_hidden_layers` field.

## Technical Significance
Corrects ACL graph resource allocation for MTP models by using the proper draft model layer count. The fix prevents incorrect resource calculation that would occur when accessing `draft.hf_config.num_hidden_layers`, which returns the main model's layer count instead.

## Related
- `technique-mtp`, `technique-aclgraph`, `technique-layer-count`, `technique-resource-allocation`