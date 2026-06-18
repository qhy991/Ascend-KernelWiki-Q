---
id: technique-pr-modellink-2758
title: "PR Insight: Ascend/ModelLink #2758"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - moe
  - performance
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2758"
---

# PR Insight: Ascend/ModelLink #2758

**Title:** support moe_unperm2_mem_optim

## Overview
This PR adds support for MoE unpermuted-2 memory optimization. The optimization targets memory usage patterns in MoE models during training, reducing the memory footprint required for expert activation routing.

## Technical Significance
MoE models have high memory requirements due to storing activations for multiple experts. This memory optimization enables training larger MoE models or using larger batch sizes on Ascend NPUs by optimizing how expert activations are stored and accessed.

## Related
- technique-data-reuse
- technique-nz-tiling