---
id: technique-pr-modellink-2284
title: "PR Insight: Ascend/ModelLink #2284"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - attention
  - tensor-parallelism
  - distributed
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2284"
---

# PR Insight: Ascend/ModelLink #2284

**Title:** seq_aux and tp support

## Overview
Adds support for sequence auxiliary operations and tensor parallelism integration. This enables better handling of sequence-level operations in distributed training scenarios with tensor parallelism.

## Technical Significance
Improves modellink's tensor parallelism capabilities by adding proper support for sequence-level auxiliary operations. This is important for models that require sophisticated sequence processing across multiple devices.

## Related
- technique-attention
- technique-hccl-optimization