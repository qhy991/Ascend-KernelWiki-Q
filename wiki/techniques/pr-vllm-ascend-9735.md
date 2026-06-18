---
id: technique-pr-vllm-ascend-9735
title: "PR Insight: vllm-project/vllm-ascend #9735"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decode
  - sampling
  - dflash
  - mtp
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9735"
---

# PR Insight: vllm-project/vllm-ascend #9735

**Title:** [BugFix]Reduce sampling is reconstructed to eliminate all patch behaviors and support DFlash and MTP

## Overview
This PR reconstructs reduce sampling optimization to eliminate patch behaviors and support DFlash and MTP. When sampling optimization is enabled with Eagle3 or DFlash spec decode, sampling can be optimized for both main model and MTP layer. With MTP spec decode, some models can optimize sampling for both layers while others only for the main model.

## Technical Significance
Refactors reduce sampling to work generically across different speculative decoding methods (Eagle3, DFlash, MTP) without requiring per-method patches. Supports sampling optimization at both main model and MTP layer levels where applicable, improving speculative decoding performance and maintainability.

## Related
- `technique-spec-decode`, `technique-mtp`, `technique-dflash`, `pattern-optimization`