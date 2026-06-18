---
id: technique-pr-vllm-ascend-5183
title: "PR Insight: vllm-project/vllm-ascend #5183"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mtp
  - cudagraph
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5183"
---

# PR Insight: vllm-project/vllm-ascend #5183

**Title:** [bugfix][ACLGraph][MTP] deletes `cudagraph_batch_sizes` in `MtpProposer`

## Overview
This PR fixes a bug where `cudagraph_batch_sizes` in `MtpProposer` was not synchronized with the adjusted sizes in `NPUModelRunner`. The fix removes the duplicate variable and makes `MtpProposer` directly use the one from `NPUModelRunner`, preventing IndexError during MTP inference.

## Technical Significance
Proper cudagraph batch size management is critical for MTP performance. The synchronization issue caused index out of range errors during AISBench stress testing with DeepSeek-V3.2 across 2P2D deployment. This fix ensures consistent cudagraph configuration across components.

## Related
- technique-mtp
- technique-cudagraph
- technique-aclgraph