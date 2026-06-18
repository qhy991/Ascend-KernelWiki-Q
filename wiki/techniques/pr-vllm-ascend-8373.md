---
id: technique-pr-vllm-ascend-8373
title: "PR Insight: vllm-project/vllm-ascend #8373"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pd-separation
  - scheduling
  - recompute
  - balance
  - mc2
  - bugfix
  - feature-gate
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8373"
---

# PR Insight: vllm-project/vllm-ascend #8373

**Title:** [BugFix] Gate recompute/balance/fused_mc2 by PD mode

## Overview
This PR enforces feature gating based on PD (Prefill-Decode) separation mode: recompute scheduling only in PD-disaggregated mode, balance scheduling only in PD-mixed mode, and fused MC2 only on PD-disaggregated D-side (kv_consumer). The changes ensure proper feature enablement based on deployment configuration and add comprehensive unit tests for platform validation.

## Technical Significance
This fix ensures correct behavior of advanced scheduling and communication features based on PD deployment mode. Incorrect feature enablement can cause performance degradation or functional issues in different PD configurations. The PR demonstrates the importance of mode-aware feature gating in complex inference systems with multiple optimization strategies.

## Related
- `technique-pd-separation`
- `technique-scheduling-optimization`
- `technique-feature-gating`