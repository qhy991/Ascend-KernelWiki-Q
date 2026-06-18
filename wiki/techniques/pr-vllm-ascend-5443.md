---
id: technique-pr-vllm-ascend-5443
title: "PR Insight: vllm-project/vllm-ascend #5443"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - multi-modal
  - attention
  - shape-handling
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5443"
---

# PR Insight: vllm-project/vllm-ascend #5443

**Title:** [Bugfix] Correctly handle the output shape in multimodal attention

## Overview
This PR fixes a bug in `AscendMMEncoderAttention` where the output shape was not consistent with the input shape. The fix ensures proper shape handling for multi-modal attention operations.

## Technical Significance
Consistent tensor shapes are critical for multi-modal models that process both text and vision inputs. This fix ensures encoder attention maintains shape consistency, preventing errors in downstream operations for vision-language models.

## Related
- technique-multi-modal
- technique-attention
- technique-shape-consistency