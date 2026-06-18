---
id: technique-pr-modellink-3386
title: "PR Insight: ModelLink #3386"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - model-support
  - deepseek2
  - mindspore
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/3386"
---

# PR Insight: ascend/ModelLink #3386

**PR Title**: `[mindspore][master]add deepseek2 sh`

## Overview

This pull request introduces support for the **DeepSeek-V2** model within the MindSpore ecosystem of the Ascend ModelLink (now MindSpeed-LLM) framework. Specifically, it adds the necessary shell (`.sh`) execution and launch scripts to facilitate training, fine-tuning, or evaluation of the DeepSeek-V2 architecture on Ascend hardware using MindSpore.

## Key Contributions

1. **DeepSeek-V2 Launch Scripts**:
   - Added dedicated shell scripts for launching DeepSeek-V2 model tasks.
   - These scripts handle the correct initialization of the model's environment, parallel strategies (such as Tensor Parallelism, Pipeline Parallelism, and Expert Parallelism), and memory allocation crucial for DeepSeek-V2's mixture-of-experts (MoE) scaling.

2. **MindSpore Backend Alignment**:
   - Indicated by the `[mindspore]` prefix, this PR ensures that ModelLink coordinates correctly with MindSpore setups for DeepSeek-V2.
   - It bridges the Ascend model ecosystem to properly execute DeepSeek-V2's unique architectural features (like Multi-head Latent Attention (MLA) and DeepSeekMoE) under the MindSpore backend.

## Architectural and Performance Implications

Deploying an advanced model like DeepSeek-V2 on Ascend requires precise configuration of distributed training topologies:
- **Parallelism Configuration**: The added `.sh` scripts provide out-of-the-box configurations for multi-NPU distributed training, ensuring that developers do not need to manually calculate device mappings.
- **Resource Management**: Ensures that the Ascend 910/910B NPUs are optimally utilized by setting framework-specific environment variables for MindSpore, mitigating out-of-memory (OOM) risks commonly associated with large MoE models.

## Conclusion

PR #3386 is an essential enablement update that provides Ascend users with the standard operating scripts needed to run DeepSeek-V2 using MindSpore within the ModelLink repository. It streamlines the deployment pipeline and guarantees that the complex MoE routing and attention mechanisms of DeepSeek-V2 can be seamlessly tested and trained on Ascend NPUs.
