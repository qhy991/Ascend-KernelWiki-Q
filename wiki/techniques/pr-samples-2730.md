---
id: technique-pr-samples-2730
title: "PR Insight: Ascend/samples #2730"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - matmul
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2730"
---

# PR Insight: Ascend/samples #2730

**Title:** fix mm leakyrelu sample 24blocks aicore error * fix mm leakyrelu block24 aicore error

## Overview
This PR fixes an AI Core error in the matrix multiplication with LeakyReLU sample when using 24 blocks. The fix addresses hardware resource allocation or scheduling issues.

## Technical Significance
LeakyReLU fused with matmul is a common pattern in neural networks. Fixing AI Core errors for specific block configurations ensures samples work reliably across different resource allocation scenarios.

## Related
- `pattern-operator-fusion`, `aicore-resource-management`