---
id: technique-pr-vllm-ascend-4751
title: "PR Insight: vllm-project/vllm-ascend #4751"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - spec-decoding
  - moe
  - ffn-combine
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4751"
---

# PR Insight: vllm-project/vllm-ascend #4751

**Title:** [Bugfix] Disable the dispatch_ffn_combine kernel in MTP path

## Overview
This PR fixes a smoking test failure by disabling the dispatch_ffn_combine kernel in the MTP (Multi-Token Prediction) speculative decoding path. It adjusts mtp_proposer and model_runner_v1 to route MTP decoding through the non-fused MoE implementation while keeping the overall inference flow unchanged.

## Technical Significance
Resolves incompatibility between the fused FFN combine kernel and MTP speculative decoding by falling back to the non-fused MoE implementation. This ensures correctness at the cost of potential performance in the MTP decoding path.

## Related
- `technique-mtp`
- `technique-speculative-decoding`
- `technique-ffn-combine`
- `kernel-moe-mlp`