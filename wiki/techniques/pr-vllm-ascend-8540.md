---
id: technique-pr-vllm-ascend-8540
title: "PR Insight: vllm-project/vllm-ascend #8540"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pd-separation
  - mtp
  - kv-cache
  - mooncake
  - bugfix
  - tp-imbalance
  - connector
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8540"
---

# PR Insight: vllm-project/vllm-ascend #8540

**Title:** [BugFix] [P/D] In scenarios where TP is not equal, the KV cache at the MTP layer is not handled.

## Overview
This PR fixes an issue where the Mooncake connector does not handle the MTP (Multi-Tensor Parallel) layer KV cache when TP is unbalanced. The fix ensures proper KV cache handling for MTP layers in scenarios with uneven tensor parallelism distribution, preventing incorrect inference results or crashes.

## Technical Significance
This fix is critical for correct KV cache management in complex deployment scenarios with MTP and unbalanced TP configurations. The Mooncake connector must properly handle KV cache across all layers and TP ranks to maintain consistency. The PR demonstrates the complexity of KV cache management in advanced parallel deployment scenarios.

## Related
- `technique-pd-separation`
- `technique-kv-pooling`
- `technique-tensor-parallel`