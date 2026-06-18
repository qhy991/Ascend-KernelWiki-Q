---
id: technique-pr-modellink-2323
title: "PR Insight: Ascend/ModelLink #2323"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - qwen25
  - pack-mode
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2323"
---

# PR Insight: Ascend/ModelLink #2323

**Title:** 添加Qwen2.5 pack模式0.5B/1.5B/72B pack模式微调脚本

## Overview
This PR adds fine-tuning scripts for Qwen2.5 models in pack mode across multiple sizes (0.5B, 1.5B, 72B). Pack mode is a training optimization that batches multiple sequences into a single training sample for improved throughput.

## Technical Significance
Pack mode training significantly improves GPU/NPU utilization by packing variable-length sequences into fixed-length contexts, reducing padding overhead. For Qwen2.5 models ranging from 0.5B to 72B parameters, this enables efficient fine-tuning with varied sequence lengths. The scripts support ModelLink's distributed training on Ascend clusters with proper tensor parallelism and data parallelism configuration for each model size.

## Related
- `technique-packing-optimization`
- `technique-distributed-training`