---
id: technique-pr-vllm-ascend-2609
title: "PR Insight: vllm-project/vllm-ascend #2609"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - moe
  - bugfix
  - mc2-operator
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2609"
---

# PR Insight: vllm-project/vllm-ascend #2609

**Title:** [Bugfix] Fix mc2 operator error in aclgraph + ep<16 scenario

## Overview
This PR fixes a MC2 operator error that occurs in ACL Graph scenarios with expert parallel (ep) < 16. The quickfix addresses the issue to recover CI functionality, with plans for future refactoring. It also disables ACL Graph when testing W8A8 quantization.

## Technical Significance
The bug fix resolves operator errors in ACL Graph mode for MoE models with small expert parallel configurations. By modifying `common_fused_moe.py` and updating test configurations, the PR ensures stable CI operation. The fix temporarily works around ACL Graph compatibility issues with certain MoE configurations while allowing CI to proceed.

## Related
- `technique-aclgraph`
- `technique-moe`
- `technique-quantization`