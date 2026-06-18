---
id: technique-pr-mindspeed-2622
title: "PR Insight: Ascend/MindSpeed #2622"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - attention
  - rotary
  - configuration
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2622"
---

# PR Insight: Ascend/MindSpeed #2622

**Title:** fix: use_fused_rotary_pos_emb with param control

## Overview
This PR fixes the parameter control for `use_fused_rotary_pos_emb`, the configuration flag that enables fused rotary position embedding operations. The change ensures proper handling of this setting across different model architectures and training configurations.

## Technical Significance
Fused rotary position embeddings can improve performance by combining multiple position embedding operations. Proper parameter control is essential for users to enable or disable this feature based on their needs. This fix ensures configuration settings are respected and applied correctly.

## Related
- `kernel-attention`
- `technique-operator-fusion`