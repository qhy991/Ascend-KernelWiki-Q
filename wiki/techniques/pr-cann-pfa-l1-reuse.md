---
id: technique-pr-cann-pfa-l1-reuse
title: "PR Insight: CANN PFA L1 Reuse & Tiling"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - flash-attention
  - memory-optimization
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/84"
  - "https://gitee.com/ascend/cann-ops-adv/pulls/58"
---

# PR Insight: CANN PFA L1 Reuse & Tiling

**Source:** [CANN-Ops-Adv PR #84](https://gitee.com/ascend/cann-ops-adv/pulls/84), [PR #58](https://gitee.com/ascend/cann-ops-adv/pulls/58)

The official Huawei `cann-ops-adv` repository contains the highly optimized native C++ operator implementations for Ascend NPUs. Recent optimizations to the **Prompt Flash Attention (PFA)** operator (used exclusively during the Prefill stage) focus heavily on memory hierarchy squeezing.

## L1 Buffer Reuse

During the massive MatMul operations required in the prefill phase (where both Queries and Keys are long sequences), data must be moved from Global Memory (HBM) -> L1 Buffer -> L0A/L0B -> Cube Unit.

- **The Optimization**: Instead of discarding blocks of $K$ and $V$ from the L1 buffer after a single inner loop of the Flash Attention calculation, the PFA operator now implements aggressive **L1 Reuse**. 
- **Impact**: By carefully synchronizing the `TPipe` data queues, the NPU pins the KV blocks in the L1 buffer, allowing multiple Query blocks to multiply against them without re-triggering Memory Transfer Engine (MTE) reads. This drastically reduces HBM bandwidth consumption during first-token generation.

## Advanced Tiling (`--cce-auto-sync=on`)

Tiling (chunking the $Q, K, V$ matrices into hardware-friendly blocks) is notoriously difficult to tune manually.
- The PR reveals that compiling these operators with `--cce-auto-sync=on` allows the AICore compiler to automatically insert synchronization barriers (`SetFlag`/`WaitFlag`) between the asynchronous DMA engines and the compute units, freeing the developers to focus purely on the mathematical tiling ratios (e.g., $N \times d$ block sizes) rather than manual instruction syncs.
