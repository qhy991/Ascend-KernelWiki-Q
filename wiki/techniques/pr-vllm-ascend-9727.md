---
id: technique-pr-vllm-ascend-9727
title: "PR Insight: vllm-project/vllm-ascend #9727"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - acl-graph
  - block-table
  - synchronization
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9727"
---

# PR Insight: vllm-project/vllm-ascend #9727

**Title:** [BugFix][310P] Repair 310P Qwen3.5 aclgraph precision

## Overview
This PR fixes incorrect outputs (garbled text) on Ascend 310P when running FULL_DECODE_ONLY ACL graph decode, typically occurring at the first request finish + batch condense step. The root cause was desynchronization between CPU block_table and GPU block_table due to lack of GPU consumer on 310P.

## Technical Significance
Overrides `_update_states()` in `NPUModelRunner310` to call `torch.npu.current_stream().synchronize()` only when `finished_req_ids` is non-empty. This drains in-flight graph replay after condense() and before condensed CPU block table is uploaded and consumed by PA metadata, preventing seq_lens and block_tables from pointing at different batch layouts.

## Related
- `technique-acl-graph`, `technique-event-sync`, `pattern-scheduler`