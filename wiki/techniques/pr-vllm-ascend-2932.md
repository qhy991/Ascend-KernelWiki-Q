---
id: technique-pr-vllm-ascend-2932
title: "PR Insight: vllm-project/vllm-ascend #2932"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - mtp
  - spec-decoding
  - mla
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2932"
---

# PR Insight: vllm-project/vllm-ascend #2932

**Title:** [Feat][Graph] Support MTP for ACL Graph

## Overview
This PR adapts the ACL Graph functionality to support Multi-Token Proposal (MTP) for speculative decoding. It updates MLA v1 implementation, MTP proposer, TorchAir model runner, and adds corresponding test cases.

## Technical Significance
Enabling MTP within ACL Graph mode improves speculative decoding performance on Ascend by reducing Python overhead. MTP generates multiple candidate tokens in a single forward pass, accelerating the verification process. The integration with ACL Graph ensures compatibility with graph-based execution optimization.

## Related
- `technique-spec-decoding`, `kernel-mtp-ascendc`, `technique-aclgraph`