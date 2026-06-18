---
id: technique-pr-vllm-ascend-4221
title: "PR Insight: vllm-project/vllm-ascend #4221"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pcp
  - mtp
  - aclgraph
  - bugfix
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4221"
---

# PR Insight: vllm-project/vllm-ascend #4221

**Title:** [bugfix] pcp + mtp acl graph bugfix

## Overview
This PR fixes a bug when using PCP + MTP with ACLGraph. The issue was that block_table needed to be flattened to avoid irregular attention mask shape, but this influenced block_table address and led to incorrect results in ACLGraph mode. The fix enlarges block_table buffer size and flattens block_table in model_runner prepare_inputs to avoid influencing block_table address.

## Technical Significance
PCP + MTP with ACLGraph requires careful handling of data structures to maintain address stability for graph capture. The block_table flattening is necessary for correct attention mask shapes but must not change addresses for graph replay. The fix ensures proper interaction between PCP, MTP, and ACLGraph optimizations.

## Related
- `technique-context-parallel`, `technique-mtp`, `technique-aclgraph`, `pattern-address-stability`, `technique-attention`