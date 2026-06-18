---
id: technique-pr-vllm-ascend-7890
title: "PR Insight: vllm-project/vllm-ascend #7890"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - eplb
  - communication
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7890"
---

# PR Insight: vllm-project/vllm-ascend #7890

**Title:** [V0.18.0][EPLB][BugFix] Fix moe_load precision in allgather

## Overview
This is a cherry-pick of PR #7887 to the v0.18.0 release branch. It fixes the same incorrect reshape usage in EPLB MoE load operations, replacing reshape with squeeze for correct tensor layout handling. The fix improves peak-to-average ratio in communication patterns.

## Technical Significance
Ensuring the fix is available in the v0.18.0 release branch allows production deployments to benefit from improved MoE load balancing without requiring an upgrade. The correct tensor handling in allgather operations is essential for maintaining numerical precision across expert-parallel devices in stable release versions.

## Related
- `kernel-moe`
- `technique-hccl-optimization`
- `pattern-moe-load-balancing`