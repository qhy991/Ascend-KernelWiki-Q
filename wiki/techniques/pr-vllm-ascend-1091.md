---
id: technique-pr-vllm-ascend-1091
title: "PR Insight: vllm-project/vllm-ascend #1091"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - deepseek-v3
  - torchair
  - operator-fusion
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1091"
---

# PR Insight: vllm-project/vllm-ascend #1091

**Title:** Avoid unfused Transpose in DeepSeekV3 EP256 MoE layer

## Overview
This PR addresses a performance issue in DeepSeekV3 MoE layers with 256-way expert parallelism. The torchair view optimization was preventing weight Transpose operations from fusing with later GroupedMatmul operations, which degraded MoE layer performance. The PR adds a configuration option to disable the view optimization when needed.

## Technical Significance
This fix is critical for MoE model performance on Ascend when using extreme expert parallelism (EP256). By allowing control over torchair view optimization through `additional_config.torchair_graph_config.enable_view_optimize`, users can ensure proper operator fusion and avoid performance penalties in high-parallelism scenarios.

## Related
- `technique-operator-fusion`
- `technique-moe`
- `technique-deepseek-v3`