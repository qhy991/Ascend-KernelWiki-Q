---
id: technique-pr-vllm-ascend-5200
title: "PR Insight: vllm-project/vllm-ascend #5200"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - flashcomm
  - aclgraph
  - incompatibility
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5200"
---

# PR Insight: vllm-project/vllm-ascend #5200

**Title:** [misc][FlashComm1][ACLGraph] Incompatibility between Flashcomm1 and FULL_DECODE_ONLY.

## Overview
This PR documents and prevents the incompatible combination of FlashComm1 and FULL_DECODE_ONLY features by adding assertions with clear error messages. The combination causes graph capture errors and provides minimal TPOT benefit in mixed deployment scenarios.

## Technical Significance
FlashComm1 requires specific graph structure incompatible with FULL_DECODE_ONLY mode. Proper error messaging prevents deployment failures and guides users to correct configurations. A future decode phase reconstruction for FlashComm1 will address this incompatibility.

## Related
- technique-flash-communication
- technique-aclgraph
- technique-cudagraph