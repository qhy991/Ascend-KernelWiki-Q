---
id: technique-pr-modellink-3380
title: "PR Insight: ModelLink #3380"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - scripts
  - qwen
  - mindspore
  - inference
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/3380"
---

# PR Insight: ModelLink #3380 - Add Qwen Shell Scripts

## Overview
This PR introduces MindSpore support scripts for the Qwen model family within the `ModelLink` (now also known as MindSpeed-LLM) repository. Given the title `[mindspore][master]add qwen sh`, it indicates that the core addition is shell (`.sh`) scripts for executing Qwen model tasks on the MindSpore backend.

## Architectural and Technical Context

### Qwen Model Support on Ascend
The Qwen model is one of the most widely used open-source Large Language Models (LLMs). Deploying it efficiently on Ascend NPUs (such as Ascend 910/910B) requires specialized launch scripts that correctly configure parallelization, communication endpoints, and memory usage. 

### Importance of Shell Scripts
Within the ModelLink ecosystem, `.sh` scripts serve as the entry points for:
1. **Weight Conversion:** Migrating model checkpoints from Hugging Face format into a Megatron-compatible or MindSpore format suitable for distributed deployment on Ascend NPUs.
2. **Distributed Training/Fine-Tuning:** Initializing multi-device settings using MindSpore distributed runtimes, configuring tensor parallelism (TP), pipeline parallelism (PP), and data parallelism (DP).
3. **Inference/Evaluation:** Running the model for downstream tasks with proper Ascend configuration environments (e.g., `CANN` variables, `HCCL` communication setups).

### MindSpore Backend
The `[mindspore]` tag specifically highlights that this script implementation is tailored for the MindSpore framework rather than PyTorch. Running LLMs like Qwen on MindSpore relies heavily on MindSpore's specific environment setups, dynamic shapes handling, and Ascend-specific operators (like NPU Fused Operators).

## Key Learnings
- **Ease of Deployment:** By maintaining official launch scripts for models like Qwen, ModelLink drastically reduces the boilerplate code necessary for end-users deploying these models on Huawei Ascend hardware.
- **Framework Diversity:** Adding these scripts directly to the MindSpore ecosystem signifies ongoing support for the native Ascend-first framework, expanding options beyond the more common PyTorch/Megatron approaches. 
- **Standardized Execution:** These scripts follow the community-standard approach for configuring HCCL (Huawei Collective Communication Library) ports, MS_WORKER variables, and dynamic memory allocations on Ascend.
