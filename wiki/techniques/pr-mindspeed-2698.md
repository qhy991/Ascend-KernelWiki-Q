---
id: technique-pr-mindspeed-2698
title: "PR Insight: Ascend/MindSpeed #2698"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - bugfix
  - configuration
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2698"
---

# PR Insight: Ascend/MindSpeed #2698

**Title:** use ffn_hidden_size if moe_ffn_hidden_size not set

## Overview
This PR adds fallback logic for MoE (Mixture of Experts) configuration when `moe_ffn_hidden_size` is not explicitly specified. It defaults to using the standard `ffn_hidden_size` parameter, ensuring backward compatibility and simplifying configuration for MoE layers.

## Technical Significance
MoE layers have separate hidden dimension parameters for the expert FFN networks. This fix provides sensible defaults and prevents configuration errors when users migrate from standard transformer to MoE architectures. It ensures robust configuration handling in the MoE feature manager and improves user experience.

## Related
- `kernel-moe`