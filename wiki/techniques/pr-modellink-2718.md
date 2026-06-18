---
id: technique-pr-modellink-2718
title: "PR Insight: Ascend/ModelLink #2718"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - deepseekv3
  - operator-fusion
  - pretrain
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2718"
---

# PR Insight: Ascend/ModelLink #2718

**Title:** deepseekv3权重转换文档修改：不支持qlora-nf4 deepseekv3 pretrain脚本修改：增加coc融合算子

## Overview
This PR makes two key changes: (1) updates weight conversion documentation to indicate that QLoRA-NF4 is not supported for DeepSeekV3, and (2) modifies the pretrain script to add CoC (Compose of Compute) fusion operators for better performance.

## Technical Significance
The CoC fusion operators improve training efficiency by fusing multiple compute operations together, reducing memory access and leveraging Ascend's Cube unit more effectively. This is particularly valuable for large models like DeepSeekV3 on Ascend hardware.

## Related
- technique-operator-fusion
- kernel-matmul