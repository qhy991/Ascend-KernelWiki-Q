---
id: technique-pr-sgl-kernel-npu-411
title: "PR Insight: sgl-project/sgl-kernel-npu #411"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - speculative-decoding
  - cache-location
  - draft-tokens
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/411"
---

# PR Insight: sgl-project/sgl-kernel-npu #411

**Title:** speculative decoding support 16 draft token

## Overview
This PR adds support for 16 draft tokens in speculative decoding by updating the cache location assignment kernel and tiling logic. The modifications enable larger draft token windows for improved speculative decoding efficiency while maintaining proper cache allocation and management.

## Technical Significance
Supporting 16 draft tokens expands speculative decoding capabilities, allowing more aggressive speculation strategies that can improve inference throughput. The enhanced draft token support enables better utilization of the verification phase in speculative decoding, particularly beneficial for models with strong draft generation capabilities.

## Related
- `technique-speculative-decoding`, `kernel-cache-management`