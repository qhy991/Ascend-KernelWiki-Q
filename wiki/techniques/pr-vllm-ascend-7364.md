---
id: technique-pr-vllm-ascend-7364
title: "PR Insight: vllm-project/vllm-ascend #7364"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - qwen3.5
  - pd-disaggregation
  - mtp
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7364"
---

# PR Insight: vllm-project/vllm-ascend #7364

**Title:** [BugFix]A2 MOE method&& layerwise MTP bugfix && Mamba gdn_metadata bugfix

## Overview
This PR fixes multiple bugs: (1) A2 MoE communication method selection when experts exceed 256, (2) layerwise connector sending KV-cache multiple times when num_spec_tokens > 1, and (3) Qwen3.5 MTP accuracy issue with PD disaggregation due to incorrect gdn_metadata handling during first inference.

## Technical Significance
These fixes matter for Ascend MoE and multi-tenant deployment. The A2 communication fix prevents incorrect MC2 method selection for large expert counts. The KV-cache fix reduces unnecessary data transfer. The MTP accuracy fix ensures correct metadata handling when spec_tokens are generated during first inference, preventing prefill length misclassification in PD disaggregation scenarios.

## Related
- technique-moe
- technique-pd-disaggregation
- technique-mtp