---
id: technique-pr-vllm-ascend-1023
title: "PR Insight: vllm-project/vllm-ascend #1023"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - graph-mode
  - v1-engine
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1023"
---

# PR Insight: vllm-project/vllm-ascend #1023

**Title:** [MTP][V1] Adapt mtp with graph mode in v1.

## Overview
This PR adapts DeepSeek Multi-Token Propose (MTP) to work with TorchAir graph mode in the V1 engine. The changes affect attention, MLA, model runner, and MTP proposer components.

## Technical Significance
MTP in graph mode provides significant performance improvements by leveraging TorchAir's graph compilation optimizations. This adaptation enables advanced speculative decoding techniques to work efficiently with graph mode, combining the benefits of both features for DeepSeek models.

## Related
- `technique-mtp`
- `technique-graph-mode`
- `kernel-deepseek`