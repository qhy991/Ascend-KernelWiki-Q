---
id: technique-pr-vllm-ascend-636
title: "PR Insight: vllm-project/vllm-ascend #636"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - deepseek
  - graph-mode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/636"
---

# PR Insight: vllm-project/vllm-ascend #636

**Title:** [MTP] follow custom deepseek modeling changes to support graph mode

## Overview
This PR updates DeepSeek MTP modeling to follow graph mode changes from #585, adds K>1 spec decode support, and fixes sampling issues. Implementation includes graph mode support (with torchair limitations noted) and comprehensive test updates.

## Technical Significance
Enables MTP speculation with graph mode acceleration on DeepSeek. K>1 support allows speculating multiple tokens when compute is available. The PR brings MTP to production readiness with both eager and graph modes.

## Related
- technique-mtp
- technique-deepseek
- technique-aclgraph