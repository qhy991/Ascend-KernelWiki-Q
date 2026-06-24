---
id: kernel-flash-attention-grad-tnd-catlass
title: "CATLASS Flash Attention Grad TND — Backward Attention Case Study"
type: wiki-kernel
architectures: [ascend910, ascend910b]
tags: [catlass, attention, flash-attention, flash-attention-grad, tnd, backward, softmax-grad, cube-unit, vector-unit]
confidence: inferred
kernel_types: [attention, flash-attention, gemm, softmax]
languages: [ascendc, cpp]
sources: [pr-catlass-169, doc-catlass-framework, doc-ascendc-api-reference]
related: [kernel-flash-attention-npu, kernel-softmax-ascendc, kernel-gemm-catlass-cpp, kernel-matmul-ascendc, wiki-hardware-cube-unit, wiki-hardware-vector-unit, wiki-hardware-l1-l0-buffer, technique-online-softmax, technique-cube-vector-overlap, technique-pipeline-scheduling, technique-workspace-management, technique-nz-tiling]
techniques: [tiling-strategy, workspace-management, cube-vector-overlap, pipeline-scheduling, online-softmax, nz-tiling]
reproducibility: source-example
---

# CATLASS Flash Attention Grad TND — Backward Attention Case Study

CATLASS PR !169 adds a Flash Attention Grad (FAG) TND example and reusable block components. This page treats it as a backward-attention kernel case study. It is distinct from forward Flash Attention pages: the backward pass must compute `dQ`, `dK`, and `dV`, recompute or reuse softmax statistics, manage several workspaces, and synchronize Cube and Vector phases.

## Problem Scope

Forward attention computes:

```text
O = softmax(mask(Q K^T)) V
```

Backward attention receives tensors such as `Q`, `K`, `V`, `dOut`, forward output, row max/sum statistics, masks, and variable-length sequence metadata. It must produce:

```text
dQ, dK, dV
```

The main challenge is that backward attention is a graph of GEMMs and vector reductions, not one GEMM.

## TND Layout and Variable-Length Inputs

The PR's example path is TND-oriented. Variable-length sequence arrays such as `cu_seq_qlen` and `cu_seq_kvlen` affect address mapping for every tile. Batch, head, group, and head-dim metadata determine which region of GM a tile should read or write.

This is why the PR adds common FAG address helpers under `examples/common/fag_common/`. Address computation is part of correctness; a wrong TND offset corrupts later gradient stages even if the MMAD instructions are correct.

## Backward Math Decomposition

A simplified decomposition is:

```text
S    = Q K^T
dP   = dOut V^T
Sfmg = row_sum(dOut * Out)
P    = softmax(mask(S))
dS   = P * (dP - Sfmg)
dQ   = dS K
dK   = dS^T Q
dV   = P^T dOut
```

CATLASS maps the GEMM-like pieces to Cube MMAD blocks and maps softmax/mask/row reductions to Vector epilogues.

## CATLASS Block Pipeline

PR !169 adds three FAG-specific Cube block families:

- `block_mmad_fag_cube1.hpp` — handles first-stage products such as `Q*K^T` and `dOut*V^T`.
- `block_mmad_fag_cube2.hpp` — handles `dQ = dS*K`.
- `block_mmad_fag_cube3.hpp` — handles `dK = dS^T*Q` and `dV = P^T*dOut`.

The Vector side is represented by FAG epilogue blocks:

- `block_epilogue_fag_pre.hpp` — clears or prepares workspace / gradient accumulators.
- `block_epilogue_fag_sfmg.hpp` — computes the softmax-gradient row term.
- `block_epilogue_fag_op.hpp` — applies mask, recomputes softmax-related values, and produces intermediate `P` / `dS` data.
- `block_epilogue_fag_post.hpp` — reduces or writes final `dQ/dK/dV` outputs from workspace.

## Workspace Layout

Backward attention needs multiple intermediate buffers. The PR uses workspace offsets for regions such as MMAD outputs, probabilities, `dS`, and gradient accumulators. These offsets are not incidental scratch space; they define dependencies between pipeline stages.

A wrong workspace offset can make a later Cube block consume stale or unrelated Vector output. This is why `workspace-management` is a first-class technique for this case study.

## Cube/Vector Handoff

The FAG pipeline coordinates AIC Cube work and AIV Vector epilogues. The PR evidence highlights cross-core synchronization mechanisms such as sync base addresses, cross-core flags, wait events, and global synchronization. The exact names vary by helper, but the design pattern is stable:

1. Cube stage writes intermediate tile/workspace.
2. Vector stage waits for the producer stage.
3. Vector epilogue computes softmax/mask/reduction data.
4. Later Cube stages wait on the epilogue output.

This is more complex than forward attention because backward has several alternating Cube and Vector phases.

## Tiling Strategy

The agent analysis of PR !169 notes different tile shapes across FAG Cube stages, with Cube1/Cube3 and Cube2 using different tile regimes. The reason is structural: the GEMMs are transposed in different directions and consume different intermediate tensors.

Do not treat all backward GEMMs as one generic matmul. `dQ`, `dK`, and `dV` have different operand orientation and workspace dependencies.

## Copy Primitive Changes

The PR also changes GM→L1 and L1→L0A/B copy primitives to support FAG transpose/stride scenarios. This matters for TND and backward GEMM layouts: the memory copy path must match the operand orientation used by the Cube block.

If the copy primitive assumes the forward layout, the Cube block can receive correctly typed but incorrectly strided tiles.

## Correctness Pitfalls

- **Workspace offsets:** each intermediate region must match producer and consumer assumptions.
- **Mask/stat consistency:** row max/sum and mask handling must match the forward attention semantics.
- **GQA/head mapping:** grouped heads change which K/V tiles feed each Q head.
- **TND boundaries:** variable-length batches require correct `cu_seq_*` indexing.
- **Cross-core order:** missing waits or flags create data races between Cube and Vector stages.
- **Transpose-aware copy:** L1/L0 copy overloads must match `dK` / `dV` operand orientation.

## When to Reuse This Pattern

Reuse this pattern for:

- training attention backward kernels;
- multi-stage Cube + Vector fused kernels;
- kernels that recompute softmax probabilities from saved row statistics;
- variable-length TND attention gradients;
- custom CATLASS examples requiring workspace-managed dependencies.

Do not use this page as a template for simple forward inference attention. For forward attention, start with `kernel-flash-attention-npu` and `technique-online-softmax`.
