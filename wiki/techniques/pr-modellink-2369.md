---
id: technique-pr-modellink-2369
title: "PR Insight: Ascend/ModelLink #2369"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - mtp
  - bugfix
  - pytorch
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2369"
---

# PR Insight: Ascend/ModelLink #2369

**Title:** mtp output not detach

## Overview
This PR fixes an issue where the MTP (Multi-Head Latent Attention Processing) output tensor was not being detached from the computation graph, causing unnecessary gradient tracking and potential memory issues during inference or evaluation.

## Technical Significance
Proper tensor detachment is critical for separating inference/evaluation paths from training computation graphs. Undetached outputs retain gradient information that prevents garbage collection and increases memory footprint. This fix ensures that MTP outputs are properly detached when used outside the training loop, improving inference efficiency and preventing memory leaks in ModelLink's DeepSeekV3 implementation.

## Related
- `kernel-attention-mla`
- `technique-memory-optimization`