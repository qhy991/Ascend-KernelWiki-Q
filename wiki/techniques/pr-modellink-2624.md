---
id: technique-pr-modellink-2624
title: "PR Insight: Ascend/ModelLink #2624"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - feature
  - dualpipe
  - mla
  - recompute
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2624"
---

# PR Insight: Ascend/ModelLink #2624

**Title:** 【feature】【master】support dualpipev last chunk no mla up proj recompute

## Overview
This PR adds support for a specific optimization in dual pipeline (dualpipe) parallelism: avoiding MLA (Multi-Head Latent Attention) upstream projection recomputation for the last chunk. This optimization reduces unnecessary computation during the final processing stage on Ascend hardware.

## Technical Significance
Dual pipeline parallelism is an advanced distributed training technique. Avoiding redundant recomputation for the last chunk reduces compute overhead, improving training efficiency. MLA optimizations are particularly important for memory-efficient attention in models like DeepSeek, making training more practical on Ascend NPUs.

## Related
- technique-pipeline-scheduling
- technique-operator-fusion
- technique-attention