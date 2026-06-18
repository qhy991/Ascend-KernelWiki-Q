---
id: technique-pr-mindspeed-2822
title: "PR Insight: MindSpeed #2822"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ci
  - testing
  - fsdp
  - mindspeed
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2822"
---

## PR Insight: MindSpeed #2822

### Overview
This pull request (PR #2822) to the `ascend/MindSpeed` repository introduces System Tests (ST) for the Fully Sharded Data Parallel (FSDP) feature. The title "**新增fsdp的ST**" directly translates to "Add FSDP ST (System Test)".

### Technical Importance

MindSpeed serves as an important optimization and acceleration library within the Huawei Ascend ecosystem, particularly for training large language models (LLMs). Fully Sharded Data Parallel (FSDP) is a crucial memory optimization technique that shards model parameters, gradients, and optimizer states across data-parallel workers, enabling the training of massive models that would otherwise exceed single-device memory limits.

Adding System Tests (ST) for FSDP ensures:
- **Feature Reliability**: Validates that FSDP functions correctly on Ascend NPU hardware (such as Ascend 910 and 910B).
- **Regression Prevention**: Prevents future code changes from breaking the existing FSDP implementation.
- **CI/CD Integration**: Enhances the overall continuous integration pipeline by automating the testing of core distributed training features.

Although this PR focuses primarily on testing infrastructure rather than introducing a novel algorithmic change, it plays a vital role in maintaining the stability and robustness of the MindSpeed training framework, especially for memory-intensive parallel training setups.
