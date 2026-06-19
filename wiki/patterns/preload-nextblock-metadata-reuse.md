---
id: pattern-preload-nextblock-metadata-reuse
title: "Preload nextBlock Metadata Reuse — Current Tile State Leaks into Next Tile"
type: wiki-pattern
architectures: [ascend910, ascend910b]
tags: [catlass, block-mmad, preload, pipeline, tiling, gemm, bugfix, pattern]
confidence: source-reported
sources: [pr-catlass-159]
symptoms: ["wrong result only on tail K blocks", "preload path fails while non-preload path passes", "nonuniform block shapes read wrong GM range"]
techniques: [pipeline-scheduling, tiling-strategy]
hardware_features: [cube-unit, l1-buffer, l0-buffer]
kernel_types: [gemm, matmul]
related: [technique-pipeline-scheduling, technique-tiling-strategy]
---

# Preload nextBlock Metadata Reuse — Current Tile State Leaks into Next Tile

## Symptom

A GEMM/GEMV preload pipeline produces wrong results only for tail K blocks, nonuniform block shapes, or cases where the next block has a different actual K extent. The non-preload path may pass.

## Root Cause

The preload logic computes next-block GM offsets using current-block metadata: K-loop count, tile count, first tile index, or actual K size. This causes the pipeline to prefetch the wrong tile range for the next block.

## Bad State Sharing Pattern

```text
current.actual_k -> current kLoops / kTileCount
preload(next) accidentally reuses current kLoops / kTileCount
next GM offset points to wrong K tile
```

Preload increases the number of live states. Current and next block metadata must be separate.

## Fix Pattern

- Maintain next-block-specific metadata.
- Compute `kLoopsNext`, `kTileCountNext`, and `firstTileIdxNext` from `actualShapeNext`.
- Compute next-block GM offsets from next-block actual K extent.
- Test tail K blocks and nonuniform next-block shapes.

## Tail-Block Test Cases

- K not divisible by tile K.
- Current block full, next block tail.
- Current block tail, next block full.
- GEMM and GEMV preload paths.
- Preload enabled vs disabled comparison.

## Evidence

- `pr-catlass-159` — CATLASS BlockMmad preload fix: adds next-block-specific K loop/tile metadata and uses `actualShapeNext.k()` / `kNextBlockActual` for next-block offsets.
