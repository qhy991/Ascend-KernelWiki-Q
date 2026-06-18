---
id: technique-pr-vllm-ascend-7288
title: "PR Insight: vllm-project/vllm-ascend #7288"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - w8a8c8
  - lightning-indexer
  - quantization
  - reversion
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7288"
---

# PR Insight: vllm-project/vllm-ascend #7288

**Title:** Revert "[Perf][1/N] w8a8c8 support in dsv3.2/glm5 (#7029)"

## Overview
This PR reverts commit 7ed9e9de which introduced an issue where the patch doesn't work with recompute scheduler enabled. The reversion affects W8A8C8 quantization support for DeepSeek V3.2 and GLM5 models, specifically the lightning_indexer_quant operator implementation.

## Technical Significance
This reversion matters for Ascend W8A8C8 quantization stability. The original optimization added lightning indexer quantization support but broke compatibility with recompute scheduler, which is critical for memory-efficient inference. The reversion ensures correctness across different execution modes while the quantization feature is refined.

## Related
- technique-quantization
- technique-w8a8c8