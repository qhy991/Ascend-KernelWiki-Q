---
id: technique-pr-vllm-ascend-8085
title: "PR Insight: vllm-project/vllm-ascend #8085"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - 310p
  - triton
  - bugfix
  - block-table
  - crash
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8085"
---

# PR Insight: vllm-project/vllm-ascend #8085

**Title:** [BugFix][310p]Fix Triton kernel in block_table crash that caused failures

## Overview
This PR fixes runtime crashes on Ascend 310P devices caused by incorrect execution path selection. The issue occurred because 310P devices do not support Triton kernels, but incomplete CI coverage allowed the 310P execution path to incorrectly enter Triton kernels. The fix adds 310P-specific implementations in `vllm_ascend/_310p/block_table.py` and related files to ensure proper device-specific execution.

## Technical Significance
This fix is critical for 310P device support as it prevents runtime crashes by ensuring device-specific code paths are correctly selected. The PR adds comprehensive 310P implementations for block table management and updates CI to prevent similar issues in the future. It highlights the importance of device-specific kernel dispatch in heterogeneous computing environments.

## Related
- `hw-ascend310p`
- `technique-device-specific-dispatch`