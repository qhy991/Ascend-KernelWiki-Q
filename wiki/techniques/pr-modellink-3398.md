---
id: technique-pr-modellink-3398
title: "PR Insight: ascend/ModelLink #3398"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - checkpointing
  - pytorch
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/3398"
---

# [pytorch][bugfix]fix bug of ckpt-v2

## Overview
This PR addresses a bug related to the version 2 checkpointing mechanism (`ckpt-v2`) in PyTorch within the `ascend/ModelLink` repository.

## Technical Details
- **Component**: PyTorch Model Checkpointing (`ckpt-v2`)
- **Nature of Fix**: Resolves an issue affecting the saving or loading of v2 checkpoints on the Ascend NPU. 
- **Impact**: Ensures that model states, including weights and optimizer states, are correctly and reliably serialized/deserialized during training and inference when using the `ckpt-v2` format, preventing potential state corruption or load failures.

## Context
Checkpointing is critical for fault tolerance and resuming training in large-scale LLM training pipelines. ModelLink utilizes optimized checkpointing formats (like `ckpt-v2`) to handle distributed weights and optimizer states effectively on Ascend hardware. Bug fixes in this area typically resolve state dictionary mismatches, missing tensor slices, distributed synchronization issues during save/load, or unpickling errors encountered in distributed execution environments.
