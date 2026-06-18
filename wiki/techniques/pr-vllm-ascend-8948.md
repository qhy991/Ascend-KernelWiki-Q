---
id: technique-pr-vllm-ascend-8948
title: "PR Insight: vllm-project/vllm-ascend #8948"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - vllm
  - aclgraph
  - block-table
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8948"
---

# PR Insight: vllm-project/vllm-ascend #8948

**Title:** [BugFix][310p] Fixing the aclgraph error caused by blocktable

## Overview
This PR fixes an ACL Graph error on Ascend 310P devices by moving the block table's slot mapping computation to the CPU. On 310P, certain device-side arithmetic operations used in the default slot mapping computation are unsupported or cause errors during graph execution. The implementation overrides `BlockTable` for 310P to use NumPy for slot mapping computation and updates `NPUModelRunner` to perform this computation on CPU early in input preparation.

## Technical Significance
Ascend 310P has different device-side operation support compared to 910/910B, requiring adaptation of the block table implementation. The CPU-based slot mapping computation avoids unsupported device-side additions for `positions` and `seq_lens` on 310P, enabling correct ACL Graph execution. This fix is critical for inference on 310P devices, ensuring that the block table works correctly with the more limited device-side operation set while maintaining performance through early CPU computation.

## Related
- `pattern-aclgraph` (ACL Graph execution)
- `pattern-block-table` (Slot mapping computation)
- `hw-ascend310p` (310P hardware constraints)