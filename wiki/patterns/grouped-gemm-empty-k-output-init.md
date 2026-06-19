---
id: pattern-grouped-gemm-empty-k-output-init
title: "Grouped GEMM Empty-K Output Init — No Compute Still Needs Semantics"
type: wiki-pattern
architectures: [ascend910, ascend910b]
tags: [catlass, grouped-gemm, split-k, output-init, bugfix, pattern]
confidence: source-reported
sources: [pr-catlass-214]
symptoms: ["grouped GEMM output contains stale values", "only empty expert or Ki=0 group fails", "Slice-K path differs from reference on zero-K groups"]
techniques: [tiling-strategy, atomic-accumulation]
hardware_features: [cube-unit, vector-unit, global-memory]
kernel_types: [grouped-gemm, gemm, matmul]
related: [kernel-grouped-gemm-ascendc, technique-tiling-strategy]
---

# Grouped GEMM Empty-K Output Init — No Compute Still Needs Semantics

## Symptom

A grouped GEMM or Slice-K grouped matmul returns stale output for an expert/group whose K extent is zero. Most normal groups pass, so the issue appears only in sparse routing, empty expert, or irregular grouped-shape cases.

## Root Cause

The kernel treats `Ki = 0` as “no Cube work,” but the output tensor still has defined semantics. If the normal accumulation loop is skipped and no explicit clear is performed, the output region can retain previous memory contents.

## Bad Pattern

```text
if Ki == 0:
    skip matmul loop
    skip output write
result = stale GM/UB content
```

## Fix Pattern

- Detect empty-K groups before entering the normal Slice-K accumulation path.
- Clear the corresponding output region deterministically.
- Keep the clear on the cold boundary path, not in the hot non-empty accumulation loop.
- Test per-group empty K, not only globally empty tensors.

## Evidence

- `pr-catlass-214` — fixes `grouped_matmul_slice_k` so `Ki = 0` groups clear output instead of leaking stale data.
