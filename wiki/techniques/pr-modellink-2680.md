---
id: technique-pr-modellink-2680
title: "PR Insight: Ascend/ModelLink #2680"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2680"
---

# PR Insight: Ascend/ModelLink #2680

**Title:** fix bug of megatron_adaptor

## Overview
This PR fixes bugs in the Megatron adapter module of ModelLink. The Megatron adapter provides compatibility with the Megatron-LM framework, enabling users to leverage Megatron training techniques and checkpoints with ModelLink on Ascend hardware.

## Technical Significance
The Megatron adapter is critical for large-scale distributed training. Bug fixes ensure reliable integration between ModelLink and Megatron-LM, supporting advanced training techniques like tensor parallelism and pipeline parallelism on Ascend NPUs.

## Related
- technique-hccl-optimization