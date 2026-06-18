---
id: technique-pr-mindspeed-2045
title: "PR Insight: Ascend/MindSpeed #2045"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - megatron
  - architecture
  - refactor
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2045"
---

# PR Insight: Ascend/MindSpeed #2045

**Title:** 重构：新增megatron_adaptor_v2和arguments_v2

## Overview
This PR refactors the Megatron integration by adding megatron_adaptor_v2 and arguments_v2. The change improves compatibility with newer Megatron-LM versions and enhances the adapter architecture.

## Technical Significance
Megatron-LM is the foundation for many large-scale training frameworks on Ascend NPUs. The v2 adapter and arguments improve compatibility with Megatron core updates and provide a cleaner integration layer. Better adapter architecture enables easier maintenance and feature synchronization with upstream Megatron-LM development. This is particularly important for supporting advanced features like MoE, 3D parallelism, and specialized attention optimizations that originate from Megatron-LM.

## Related
- `technique-hccl-optimization`
- `technique-pipeline-scheduling`