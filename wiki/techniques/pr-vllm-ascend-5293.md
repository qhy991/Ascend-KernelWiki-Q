---
id: technique-pr-vllm-ascend-5293
title: "PR Insight: vllm-project/vllm-ascend #5293"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mtp
  - moe
  - quantization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5293"
---

# PR Insight: vllm-project/vllm-ascend #5293

**Title:** [BugFix]Disable dispatch_gmm_combine_decode operator when mtp drafter model uses non-w8a8 while main model uses w8a8, or drafter model is eagle series

## Overview
This PR disables the `dispatch_gmm_combine_decode` operator in specific MTP configurations: when the drafter model uses non-W8A8 while the main model uses W8A8, or when the drafter model is from the Eagle series. This prevents incompatibility issues with mixed quantization schemes.

## Technical Significance
The dispatch_gmm_combine_decode operator has specific quantization requirements. Disabling it in incompatible configurations ensures correct MoE operations during MTP inference, preventing correctness issues when mixing different quantization schemes between drafter and main models.

## Related
- technique-mtp
- technique-moe
- technique-quantization