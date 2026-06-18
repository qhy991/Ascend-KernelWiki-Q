---
id: technique-pr-vllm-ascend-6707
title: "PR Insight: vllm-project/vllm-ascend #6707"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - dispatch-ffn-combine
  - bugfix
  - unaligned-access
  - moe
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6707"
---

# PR Insight: vllm-project/vllm-ascend #6707

**Title:** [Bugfix][DispatchFFNCombine] resolve vec error caused by unaligned UB access

## Overview
This PR fixes vector errors in DispatchFFNCombine caused by unaligned UB (Unified Buffer) accesses. It also fixes expert_token_nums being defined on host instead of NPU and resolves multi-core copy issues.

## Technical Significance
Fixes critical memory access violations in MoE dispatch operations. The alignment fixes prevent hardware exceptions and ensure correct vector operations on the NPU's unified buffer, while proper device placement of expert_token_nums improves communication efficiency.

## Related
- `kernel-moe`