---
id: wiki-hardware-nz-format
title: "FRACTAL_NZ — The Cube Unit's 5D Tiled Data Format"
type: wiki-hardware
architectures: [ascend910, ascend910b, ascend310p]
tags: [nz-format, nd-format, data-format, cube-unit, hardware]
confidence: source-reported
hardware_features: [nz-format, nd-format, cube-unit]
related: [hw-cube-unit, technique-nz-tiling, technique-format-conversion]
sources: [blog-nz-format-explained, doc-catlass-framework, doc-ascendc-api-reference]
---

# FRACTAL_NZ — The Cube Unit's 5D Tiled Data Format

FRACTAL_NZ (`ACL_FORMAT_FRACTAL_NZ`) is the native operand layout the Cube unit reads when performing matrix multiplication on Ascend NPUs. A logical 2D matrix is split into 16×16 "fractal" blocks, with each block stored contiguously and the blocks themselves arranged in a zN ordering. Code that feeds the Cube unit (`hw-cube-unit`) must either supply data already in this layout or pay a conversion cost from the standard ND format.

## Why a Special Format Exists

The Cube unit does not consume row-major matrices. Its datapath is wired to ingest fixed 16×16 tiles directly, so the hardware reaches peak utilization only when operands are pre-arranged into those tiles. FRACTAL_NZ delivers three concrete benefits:

- **Native tile reads**: The Cube reads a 16×16 fractal in one shot, with no in-flight reshuffling.
- **Maximized MTE burst**: Because each fractal is contiguous in memory, the MTE (Memory Transfer Engine) moves it as a single aligned burst from Global Memory to L1/L0, instead of gathering scattered rows.
- **L0 reuse**: The zN block ordering keeps the blocks a given Cube pass needs close together, improving operand reuse inside L0.

In short, the format trades a one-time data rearrangement for sustained Cube throughput. See `blog-nz-format-explained` for the dataflow walkthrough.

## ND vs. NZ: The Conceptual Reshape

Standard tensors live in **ND** (N-dimensional) format — for a matrix this is plain row-major `[M, N]`. FRACTAL_NZ reshapes that 2D matrix into a 5D-style fractal layout. Conceptually:

```
ND  [M, N]
        │  split both axes into 16-wide fractals
        ▼
NZ  [ceil(N/16), ceil(M/16), 16, 16]
     └── N1 ──┘ └── M1 ──┘ └inner┘
```

The four logical axes are:

- **N1 = ceil(N / 16)** — number of fractal blocks along the original N (column) axis. This is the **outer-major** axis, which is what makes the layout "n-major".
- **M1 = ceil(M / 16)** — number of fractal blocks along the original M (row) axis.
- **16 × 16** — the inner fractal, stored fully contiguously.

The key property is the **zN block order**: the outer blocks step through N-major-then-M (the N1 axis varies slowest at the block level), while inside each block the 16×16 elements are laid out contiguously. This "n-major outer, contiguous inner" arrangement is exactly what the Cube's tile reader expects.

## Layout Diagram

Consider a small `ND[M=32, N=48]` matrix. It becomes `NZ[N1=3, M1=2, 16, 16]` — six fractal blocks. Memory order (block index in brackets) walks N-major across the outer grid, and each block is a dense 16×16 tile:

```
Logical matrix (ND, M rows × N cols):
        N=0..15   N=16..31   N=32..47
M=0..15 [ blkA ]  [ blkC  ]  [ blkE  ]
M=16..31[ blkB ]  [ blkD  ]  [ blkF  ]

FRACTAL_NZ memory order (n-major outer, zN):
  N1=0 → blkA(M1=0), blkB(M1=1)
  N1=1 → blkC(M1=0), blkD(M1=1)
  N1=2 → blkE(M1=0), blkF(M1=1)

Linear bytes:  [ blkA | blkB | blkC | blkD | blkE | blkF ]
                 each block = 16×16 elements, contiguous
```

Each 16×16 fractal is **32-byte aligned** in memory, which keeps MTE transfers on aligned burst boundaries and avoids partial-line reads.

## Format in Code

Format is an attribute carried on the tensor descriptor, not a different data type. The conversion from ND to NZ is performed with a transcode/transpose on the Vector or MTE path; the Catlass GEMM templates (`doc-catlass-framework`) wrap this so kernel authors usually request the target format rather than hand-rolling the shuffle.

```cpp
// Tag the operand descriptor with the Cube-native format.
// ACL_FORMAT_FRACTAL_NZ is the layout the Cube unit reads directly;
// ACL_FORMAT_ND is the plain row-major source layout.
aclTensorDesc *ndDesc =
    aclCreateTensorDesc(ACL_FLOAT16, dimCnt, dims, ACL_FORMAT_ND);
aclTensorDesc *nzDesc =
    aclCreateTensorDesc(ACL_FLOAT16, dimCnt, dims, ACL_FORMAT_FRACTAL_NZ);

// Inside an AscendC kernel, the ND→NZ rearrangement rides on the
// Vector/MTE datapath before the tile reaches the Cube. The
// DataCopy / DataCopyPad MTE moves and Transpose vector op together
// realize the fractal blocking; see technique-format-conversion.
DataCopy(srcGlobal, ubLocal, copyParams);   // GM → UB burst
Transpose(ubNz, ubLocal, transposeParams);  // pack into 16×16 fractals
```

The API names above (`ACL_FORMAT_FRACTAL_NZ`, `ACL_FORMAT_ND`, `aclCreateTensorDesc`, `DataCopy`, `DataCopyPad`, `Transpose`) are real CANN/AscendC entry points; the exact `transposeParams` setup for the fractal packing is documented in `doc-ascendc-api-reference`.

## Conversion Cost

Rearranging ND into FRACTAL_NZ is not free. The shuffle runs on the Vector/MTE units, and the reported overhead is roughly **10–15%** of the affected operation when conversion happens on the hot path. The mitigation strategy is to make the conversion a *one-time* cost rather than a *per-iteration* one.

| Aspect | ND format | FRACTAL_NZ format |
|--------|-----------|-------------------|
| Layout | Row-major `[M, N]` | `[ceil(N/16), ceil(M/16), 16, 16]`, zN order |
| Cube-readable | No (needs conversion) | Yes (native) |
| Fractal block | n/a | 16×16, 32-byte aligned |
| Conversion path | — | Vector/MTE transpose |
| Conversion overhead | — | ~10–15% when on hot path |

## The Persistent-Weights Rule

The single most important practical rule follows directly from the conversion cost: **convert weights to FRACTAL_NZ once and keep them resident in NZ across all forward passes.** Weights are read repeatedly but never change, so paying the 10–15% shuffle on every step is pure waste. This is exactly the optimization applied in `pr-vllm-ascend-002`, where model weights are pre-packed into NZ at load time and the Cube reads them directly for the lifetime of the model.

Activations are the opposite case: they change every step, so the conversion cost cannot be amortized the same way. For activations the format choice is a per-shape decision — see `technique-nz-tiling` for how tiling interacts with the fractal boundaries, and `technique-format-conversion` for placing the transpose where it overlaps with compute.

## Trade-offs and Pitfalls

- **Padding waste on small dims**: When M or N is not a multiple of 16, the final fractal is padded with zeros. A matrix with `N = 17` still consumes `N1 = 2` blocks (32 columns of storage), nearly doubling the column footprint. Pad-aware tiling matters most for skinny matrices.
- **Conversion on the hot path**: Inserting an ND→NZ transpose inside the inner loop reintroduces the 10–15% penalty every iteration. Hoist conversions out of loops; persist where possible.
- **Format mismatch errors**: Handing a Cube API an `ACL_FORMAT_ND` descriptor where it expects `ACL_FORMAT_FRACTAL_NZ` is a common failure; the operand must be tagged with the format it physically holds.
- **INT8 differs**: The 16×16 fractal here describes FP16/BF16 operands. Lower-precision types use different fractal dimensions on the Cube; do not assume 16×16 universally (see `hw-cube-unit`).
- **Confidence note**: The conversion-overhead figure and layout details here are *source-reported* (`blog-nz-format-explained`, `doc-catlass-framework`), not independently re-benchmarked. Treat the 10–15% number as a guideline, not a guarantee for a specific shape.

## Best Practices

1. **Persist weights in NZ** — convert at load time, never per step (`pr-vllm-ascend-002`).
2. **Hoist conversions** out of inner loops; amortize over many Cube passes.
3. **Align dimensions to 16** to eliminate fractal padding waste.
4. **Overlap the transpose** with MTE/compute so the conversion cost is hidden, not added — see `technique-format-conversion`.
5. **Let Catlass handle packing** for standard GEMMs rather than hand-coding the fractal shuffle (`doc-catlass-framework`).
