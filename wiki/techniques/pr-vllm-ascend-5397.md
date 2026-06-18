---
id: technique-pr-vllm-ascend-5397
title: "PR Insight: vllm-project/vllm-ascend #5397"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mha
  - aclgraph
  - padding
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5397"
---

# PR Insight: vllm-project/vllm-ascend #5397

**Title:** [bugfix] Fix MHA model runtime error in aclgraph mode

## Overview
This PR fixes a runtime error in MHA (Multi-Head Attention) models running in ACLGraph mode. The error occurred because QKV tensors in the prefill stage were padded, causing shape inconsistencies with actual_seq_lengths. The fix adds unpadding logic for KV tensors.

## Technical Significance
ACLGraph mode requires precise tensor shape matching. This fix ensures MHA models like MiniCPM-2B and Baichuan-7B work correctly in piecewise graph mode by maintaining consistency between tensor shapes and sequence length metadata.

## Related
- technique-mha
- technique-aclgraph
- technique-padding