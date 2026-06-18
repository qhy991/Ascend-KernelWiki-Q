---
id: technique-pr-vllm-ascend-3185
title: "PR Insight: vllm-project/vllm-ascend #3185"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - fia
  - performance
  - operation-scheduling
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3185"
---

# PR Insight: vllm-project/vllm-ascend #3185

**Title:** [BugFix]Move to_list in foward_v1 with FIA earlier to build

## Overview
This PR moves to_list operations for actual_seq_lengths_q and seq_lens from forward_v1 to the build operation of attention metadata in FIA (Fused Infer Attention). The change reduces extra time consumed by these operations during forward pass.

## Technical Significance
Moving operations from forward to build phase improves performance by shifting work outside the critical path. The to_list operations are needed for attention metadata preparation, and doing them earlier allows better overlap with other operations, reducing overall inference latency.

## Related
- `kernel-attention-ascendc`, `technique-operation-scheduling`, `pattern-fia-optimization`