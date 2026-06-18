---
id: kernel-topk-ascendc
title: "AscendC Top-K — Expert Routing and Sampling Reduction"
type: wiki-kernel
architectures: [ascend910, ascend910b]
tags: [topk, reduce, moe, vector-unit, ascendc]
confidence: inferred
kernel_types: [reduce, moe]
languages: [ascendc]
sources: [doc-ascendc-api-reference, blog-ascendc-performance-tips]
related: [kernel-moe-ascendc, kernel-reduction-ascendc, hw-vector-unit]
techniques: [data-reuse, bank-conflict-avoidance]
reproducibility: pseudocode
---

# AscendC Top-K — Expert Routing and Sampling Reduction

## Overview

Top-K selects the `k` largest values from an array and returns both the values and their original indices. On Ascend NPU it runs on the Vector unit and shows up in two hot paths: MoE expert routing, where it picks the top-k experts from per-token router logits, and sampling, where it truncates a vocabulary distribution to the k most likely tokens. There is no single canonical Top-K API across CANN versions, so this page describes the common construction patterns rather than one fixed kernel; treat it as inferred and reproducible at the pseudocode level. The companion routing logic is covered in kernel-moe-ascendc, and the underlying reduction primitives in kernel-reduction-ascendc.

## Why Top-K Is Awkward on a Vector Unit

The Vector unit is built for dense, regular elementwise and reduction work (see hw-vector-unit). Top-K is neither: it is a partial sort that must also carry an index alongside every value. Two facts drive the design:

- **Index tracking.** A bare `ReduceMax` returns the maximum *value* but not *where* it came from. Top-K consumers need the argmax (the expert id, or the token id), so a companion index tensor must be threaded through every comparison.
- **k is usually tiny.** In MoE routing k is typically 1, 2, or 8 over a small set of experts (8-256). At that scale a full sort is wasteful, and an iterative max-and-mask loop wins. Sampling top-k over a vocabulary (k up to a few hundred over tens of thousands of logits) is the regime where a real partial sort pays off.

The result is two distinct implementations selected by k and array length.

## Approach 1: Iterative ReduceMax + Mask-Out (small k, the MoE case)

For small k this is the dominant pattern. Keep the logits in UB, and run k rounds; each round finds the current maximum, records its index, then writes `-inf` into that slot so the next round finds the next-largest value.

```ascendc
// Small-k Top-K via iterative max-and-mask.
// logits_ub : [n]   router logits for one token (n = num_experts)
// idx_ub    : [n]   companion index tensor, idx_ub[i] = i
// out_val   : [k]   selected values
// out_idx   : [k]   selected expert indices
void TopKSmallK(LocalTensor<float>& logits_ub,
                LocalTensor<int32_t>& idx_ub,
                LocalTensor<float>& out_val,
                LocalTensor<int32_t>& out_idx,
                int n, int k) {
    LocalTensor<float> max_ub = BufferPool::Alloc();   // [1] running max value
    LocalTensor<float> mask_ub = BufferPool::Alloc();  // [n] equality mask

    for (int r = 0; r < k; ++r) {
        // 1. Reduce to the current maximum value.
        ReduceMax(max_ub, logits_ub, n);
        out_val[r] = max_ub[0];

        // 2. Build a mask where logits == max, then read off the argmax index.
        //    Compare yields 1.0 at the winning lane(s), 0.0 elsewhere.
        Compare(mask_ub, logits_ub, max_ub, CMPMODE::EQ, n);
        out_idx[r] = SelectFirstIndex(mask_ub, idx_ub, n);  // argmax = idx at first set lane

        // 3. Mask out the winner so the next round skips it: set it to -inf.
        Duplicate(max_ub, -3.4e38f /* -FLT_MAX as -inf proxy */, 1);
        Select(logits_ub, mask_ub, max_ub, logits_ub, n);   // where mask: -inf, else keep
    }

    BufferPool::Dealloc(max_ub);
    BufferPool::Dealloc(mask_ub);
}
```

The primitives here are all standard AscendC Vector APIs: `ReduceMax` for the per-round maximum (the same primitive used in kernel-reduction-ascendc), `Compare` to produce the equality mask, `Select` to overwrite the winning lane with `-inf`, and `Duplicate` to broadcast the `-inf` sentinel. The cost is `k` passes over `n` elements, so `O(k * n)` — cheap when both k and n are small, which is exactly the MoE routing regime.

### Ties and stability

Because `Compare` with `EQ` can light up more than one lane when duplicate logit values exist, the argmax extraction must commit to a single lane (here, the first set lane). Selecting the first lane gives a deterministic, lowest-index tie-break, which keeps routing reproducible across runs. Masking only that one lane (rather than all equal lanes) ensures a true duplicate value can still be selected in a later round if k allows.

## Approach 2: Bitonic / Partial Sort (larger k, sampling)

When k grows — for example top-k sampling over a vocabulary — the `O(k * n)` iterative loop becomes the bottleneck and a sort-based path wins. Stage the logits (paired with their indices) into UB and run a **bitonic sort**, which is attractive on the Vector unit because its comparison network is data-independent: the same sequence of compare-and-swap stages runs regardless of input, so there are no divergent branches and the schedule is fully static.

Key points for a UB-resident bitonic Top-K:

- Sort *(value, index)* pairs together so the permutation that orders the values simultaneously orders the indices — this is how the argmax information survives the sort.
- You only need the top k, so once the array is bitonically ordered (or partially ordered up to the k-th element) you slice the first k entries; a full descending sort of all n elements is more work than necessary but is the simplest correct version.
- The comparison network maps cleanly onto vectorized `Max`/`Min` + `Select` operations, keeping the Vector unit busy with regular work.

This path trades extra compute (`O(n log^2 n)` compares for a full bitonic sort) for branch-free, predictable execution, which is why it overtakes the iterative loop once k is no longer tiny.

## Hardware-Assisted Path

Some CANN releases expose a fused Top-K vector instruction / library entry that performs the selection in fewer passes than the hand-rolled loop, returning values and indices together. Where available it is the fastest option and removes the manual mask bookkeeping. Because its presence and exact name vary by CANN version, this page does not pin an API name; check the `doc-ascendc-api-reference` for your toolkit version, and fall back to the iterative or bitonic construction when it is absent. This is the main reason the page is marked `reproducibility: pseudocode` rather than `snippet`.

## UB Layout and Bank-Conflict Avoidance

Top-K touches the same arrays repeatedly — the logits every round, the companion index tensor on every argmax read — so UB layout matters (technique-bank-conflict-avoidance). The Unified Buffer is banked, and if the value tensor and the index tensor are laid out so that lane `i` of each lands in the same bank, the paired value/index accesses in each round serialize on that bank.

Guidance:

- **Pad the per-row stride** so that the value buffer and the index buffer start on different banks, letting a `(value, index)` pair be read in parallel rather than back-to-back.
- **Keep logits UB-resident across all k rounds** instead of re-streaming from global memory each round — this is the `data-reuse` win and is what makes the iterative loop cheap.
- For the bitonic path, choose a power-of-two-padded length and align the compare-swap stride to bank boundaries so each stage's strided accesses stay conflict-free.

## Numerical Handling

- **Sentinel choice.** The mask-out step needs a value strictly below every real logit. Use `-FLT_MAX` (shown above as a `-inf` proxy) rather than literal infinity to avoid `NaN` if a later op subtracts or scales the masked slot. Router logits are typically post-softmax-precursor values well within fp32 range, so `-FLT_MAX` is safely below them.
- **Index dtype.** Indices are tracked in an `int32` companion tensor initialized to `0..n-1`. For MoE the index *is* the expert id consumed downstream by kernel-moe-ascendc; for sampling it is the vocabulary token id.
- **Precision.** Routing logits are usually fp32 even when the model runs in fp16, because the ordering of close-valued experts must be stable. Doing the Top-K compares in fp32 avoids fp16 ties that would make routing flap between runs.

## Choosing an Approach

| Regime | Typical k | n | Recommended path | Cost |
|---|---|---|---|---|
| MoE expert routing | 1-8 | 8-256 experts | Iterative ReduceMax + mask | `O(k·n)`, branch-free per round |
| Top-k sampling | up to a few hundred | 10k-200k vocab | Bitonic / partial sort in UB | `O(n log^2 n)` compares |
| Either, on a supporting toolkit | any | any | Hardware-assisted Top-K | fewest passes (version-dependent) |

## Trade-offs, Pitfalls, and Notes

- **Don't mask all equal lanes at once.** A common bug: `Select`-ing `-inf` into every lane where `logits == max` collapses duplicate top values into a single round, so a tensor with repeated maxima returns fewer than k distinct picks. Mask exactly one lane per round.
- **`ReduceMax` gives value, not position.** The argmax must come from a separate `Compare`/`Select` step against the companion index tensor; forgetting this is the most frequent Top-K mistake on the Vector unit.
- **Iterative loop scales badly in k.** At large k the `O(k·n)` passes dominate; switch to the bitonic path. The crossover depends on n and toolkit version — measure rather than assume.
- **Bank conflicts hide in the index reads.** Because every round reads both a value and an index lane, mis-aligned UB layout doubles the effective latency of the inner loop. Pad to separate banks (technique-bank-conflict-avoidance).
- **No single canonical API.** Top-K is assembled from `ReduceMax`, `Compare`, `Select`, and `Duplicate`; the fused hardware path, where present, is version-specific. This is why the page is `confidence: inferred` and `reproducibility: pseudocode`.

## Integration with MoE

In the MoE flow, Top-K is the second half of the router: after computing gate logits (the softmax/gate step in kernel-moe-ascendc), Top-K over those logits produces the `routing_indices` (selected expert ids) and the selected gate values used to form `routing_weights`. With k small and the expert count modest, the iterative ReduceMax + mask-out kernel above is the natural fit, and its UB-resident logits and index tensors keep the routing overhead within the few-percent budget noted for the overall MoE kernel.
