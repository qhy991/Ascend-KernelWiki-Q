---
id: technique-pr-modellink-3376
title: "PR Insight: ascend/ModelLink #3376"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - recompute
  - memory
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/3376"
---

# PR Insight: ascend/ModelLink #3376 - Fix Recompute Valid Actual Sequence Length

## Overview
This PR addresses an issue with activation recomputation (checkpointing) in the PyTorch model implementation of ModelLink. Specifically, it targets the handling and validation of `actual_seq_len` during the recompute phase.

## Technical Details

### Issue Context
In LLM training frameworks like ModelLink (which builds upon Megatron-LM architectures for Ascend NPUs), activation recomputation is heavily utilized to optimize memory usage by dropping activations during the forward pass and recalculating them during the backward pass.

When training with variable sequence lengths, packed datasets, or padding, an `actual_seq_len` value is necessary to track the true, valid length of the sequence. This ensures:
1. Proper masking in attention layers.
2. Correct handling of boundary conditions.

If `actual_seq_len` is not properly validated or maintained when the forward pass is recomputed, the model may experience:
- Inconsistent states between the initial forward pass and the recomputed forward pass.
- Shape mismatches or index out-of-bounds errors.
- Incorrect masking, leading to flawed gradient calculations and model divergence.

### The Fix
The patch `[pytorch][model] fix recompute_valid_actual_seq_len` guarantees that the valid actual sequence length is accurately captured and passed along during the recompute phases. This ensures memory-efficient training does not compromise the correctness of the backward pass when processing variable-length sequences.
