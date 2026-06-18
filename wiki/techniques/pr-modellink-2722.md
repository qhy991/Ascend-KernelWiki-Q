---
id: technique-pr-modellink-2722
title: "PR Insight: Ascend/ModelLink #2722"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - bugfix
  - qlora
  - deepseekv3
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2722"
---

# PR Insight: Ascend/ModelLink #2722

**Title:** fixing torch2.6, DeepSeek-V3 QLoRA loading checkpoint error

## Overview
This PR fixes a checkpoint loading error that occurred when using QLoRA with DeepSeek-V3 models on PyTorch 2.6. The fix resolves compatibility issues between the quantization format and checkpoint loading mechanism.

## Technical Significance
DeepSeek-V3 QLoRA requires precise handling of quantized parameters. This fix ensures that quantized checkpoints can be loaded correctly on Ascend NPUs with PyTorch 2.6, enabling efficient fine-tuning workflows for large models.

## Related
- technique-format-conversion