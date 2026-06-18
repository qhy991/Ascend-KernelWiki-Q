---
id: technique-pr-cann-ops-adv-287
title: "PR Insight: Ascend/cann-ops-adv #287"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - routing
  - quantization
  - debugging
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/287"
---

# PR Insight: Ascend/cann-ops-adv #287

**Title:** moe_finalize_routing_v2 forward&&backward Alarm clearing

## Overview
This PR clears or resolves alarms in the MoE finalize routing V2 operator for both forward and backward passes. The changes address warning or error conditions that were being triggered during routing finalization in MoE models.

## Technical Significance
Alarm clearing in MoE routing finalization is important for stable training and inference. The finalize routing operation likely handles capacity management, padding, or cleanup after expert assignment. Resolving alarms ensures that edge cases (e.g., overflow, underflow, capacity limits) are handled gracefully without triggering warnings or errors. This improves operator robustness and provides clearer feedback when genuine issues occur, making debugging easier for developers working with complex MoE architectures.

## Related
- `technique-moe-ascendc`
- `technique-routing-optimization`
- `technique-error-handling`
- `technique-quantization`