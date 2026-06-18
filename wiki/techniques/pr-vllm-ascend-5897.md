---
id: technique-pr-vllm-ascend-5897
title: "PR Insight: vllm-project/vllm-ascend #5897"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eplb
  - swift-balancer
  - refactor
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5897"
---

# PR Insight: vllm-project/vllm-ascend #5897

**Title:** [EPLB][Bugfix] policy_swift_balancer bugfix and renaming

## Overview
This PR renames and fixes the EPLB (Expert Parallel Load Balancing) policy modules. It renames dynamic_ep to default_eplb, dynamic_ep_v2 to swift_balancer, and removes the unused compose_expert_update_info_bipartite function.

## Technical Significance
The renaming improves code clarity and aligns terminology with the EPLB feature's intent. Swift_balancer is the new name for the advanced EPLB policy, while default_eplb is the basic implementation. Removing unused functions reduces code bloat. The PR also updates documentation and unit tests to reflect the new naming. Testing shows EPLB continues to work correctly with the renamed modules.

## Related
- `technique-eplb`, `technique-expert-parallel`, `technique-load-balancing`