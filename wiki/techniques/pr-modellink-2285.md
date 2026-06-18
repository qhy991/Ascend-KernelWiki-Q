---
id: technique-pr-modellink-2285
title: "PR Insight: Ascend/ModelLink #2285"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - qwen25
  - moe
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2285"
---

# PR Insight: Ascend/ModelLink #2285

**Title:** 增加Qwen2.5-3B|7B|14B|32B和Qwen2-MoE微调脚本

## Overview
This PR adds fine-tuning scripts for multiple Qwen2.5 model sizes (3B, 7B, 14B, 32B) and Qwen2-MoE variants. The scripts provide configuration templates for fine-tuning these models on Ascend hardware.

## Technical Significance
Qwen2.5 across multiple scales and the Qwen2-MoE variant require different tensor parallelism and pipeline parallelism configurations to optimize NPU utilization. The MoE variant specifically needs expert parallelism and load balancing strategies. These scripts enable efficient fine-tuning on Ascend clusters with proper communication overlap, memory management, and distributed training setup for each model architecture.

## Related
- `technique-moe-training`
- `technique-tensor-parallelism`
- `technique-pipeline-scheduling`