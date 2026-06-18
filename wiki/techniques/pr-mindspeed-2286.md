---
id: technique-pr-mindspeed-2286
title: "PR Insight: Ascend/MindSpeed #2286"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - ulysses
  - ckpt-format
  - sequence
  - parallel
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2286"
---

# PR Insight: Ascend/MindSpeed #2286

**Title:** add ckpt-format arg to ulysses ST

## Overview
This PR adds a checkpoint format argument to Ulysses Sequence Parallelism (ST). Ulysses is a sequence parallelism technique that splits sequences across devices, and this addition allows configuring checkpoint formats for compatibility or optimization.

## Technical Significance
Checkpoint format configuration is important for saving and loading training states efficiently. In sequence parallelism, checkpoint handling can be complex due to distributed sequence data. This addition provides flexibility in checkpoint management for Ulysses parallel training.

## Related
- `technique-sequence-parallelism`
- `technique-ulysses`
- `pattern-checkpoint-management`
- `pattern-distributed-training`