---
id: technique-pr-vllm-ascend-5946
title: "PR Insight: vllm-project/vllm-ascend #5946"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mooncake
  - pd-disaggregation
  - ipv6
  - networking
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5946"
---

# PR Insight: vllm-project/vllm-ascend #5946

**Title:** [P/D] Remove restrictions on mooncake for IPv6

## Overview
This PR removes IPv6 restrictions from the Mooncake connector for PD disaggregation. The change enables Mooncake to work with IPv6 networks, removing limitations that prevented deployment in IPv6-only environments.

## Technical Significance
IPv6 support is essential for modern network deployments where IPv4 addresses are exhausted. Removing IPv6 restrictions enables Mooncake-based PD disaggregation in IPv6-only networks, expanding deployment flexibility. The fix updates the Mooncake transfer engine and documentation, with dependencies on CANN 8.5 and Mooncake v0.3.8.post1.

## Related
- `technique-mooncake`, `technique-pd-disaggregation`, `technique-kv-cache-transfer`