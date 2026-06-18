---
id: technique-pr-vllm-ascend-4224
title: "PR Insight: vllm-project/vllm-ascend #4224"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - communication
  - multicast
  - all-gather
  - refactor
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4224"
---

# PR Insight: vllm-project/vllm-ascend #4224

**Title:** [Refactor] remove moe type of multicast.

## Overview
This PR removes multicast-related code from MoE communication, replacing it with all-gather. The rationale is that multicast performance is worse than all-gather in scenarios like A2 Dual-System Back-to-Back Networking (3 TPS vs 10 TPS after modification). With SP feature and prefill ACL graph support, broadcast communication advantages are diminished.

## Technical Significance
Removing multicast simplifies the codebase by removing a communication method that provides worse performance in current scenarios. All-gather is more consistent with SP patterns and benefits from recent prefill ACL graph optimizations. The performance improvement (3x TPS increase) demonstrates significant benefits for A2 networking scenarios.

## Related
- `technique-moe`, `technique-communication`, `pattern-refactoring`, `technique-all-gather`, `pattern-performance-optimization`