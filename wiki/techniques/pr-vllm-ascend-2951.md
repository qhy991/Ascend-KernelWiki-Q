---
id: technique-pr-vllm-ascend-2951
title: "PR Insight: vllm-project/vllm-ascend #2951"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - spec-decoding
  - torchair
  - pd-separation
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2951"
---

# PR Insight: vllm-project/vllm-ascend #2951

**Title:** [Bugfix] Fix mtp torchair in pd Disaggregation scenario

## Overview
This PR fixes two bugs: MTP TorchAir issues in Prefill-Decode disaggregation scenarios, and MLA bugs in speculative decoding scenarios where num_decodes != num_decode_tokens. It modifies TorchAir MLA and model runner implementations.

## Technical Significance
The fixes address correctness issues in complex inference scenarios. The MLA bug fix ensures proper token count handling in speculative decoding, while the TorchAir MTP fix ensures proper execution in distributed disaggregated environments where prefills and decodes run on separate nodes.

## Related
- `technique-spec-decoding`, `kernel-mtp-ascendc`, `kernel-mla-ascendc`