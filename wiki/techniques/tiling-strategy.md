---
id: technique-tiling-strategy
title: "Tiling Strategy — Host-Side Tiling and Auto-Tiling"
type: wiki-technique
architectures: [ascend910, ascend910b, ascend310p]
tags: [tiling-strategy, tiling, optimization, ascendc]
confidence: source-reported
techniques: [tiling-strategy]
hardware_features: [unified-buffer, l1-buffer, cube-unit]
kernel_types: [matmul, gemm, attention]
related: [technique-nz-tiling, technique-workspace-management, pattern-tiling-too-small]
sources: [doc-ascendc-tiling-api, doc-ascendc-api-reference, blog-ascendc-performance-tips]
reproducibility: snippet
---

# Tiling Strategy — Host-Side Tiling and Auto-Tiling

In the Ascend C programming model an operator is split into a **host-side tiling function** that runs on the CPU before launch and a **device kernel** that runs on the AICore. The tiling function decides how the problem is partitioned across cores and how each core slices its share into buffer-sized tiles, serializes those decisions into a `TilingData` struct, and the kernel reads them back at runtime. This separation keeps shape-dependent arithmetic off the AICore critical path and lets a single kernel binary adapt to arbitrary shapes without recompilation.

## The Host/Device Split

The host tiling function is responsible for three quantities:

1. **Block dim** — how many AICore instances to launch, set with `context->SetBlockDim(n)`.
2. **Per-core data partition** — the slice of global memory each core owns, derived on the device from `GetBlockIdx()`.
3. **Tile lengths** — the inner-loop chunk each core copies into on-chip memory, sized to fit the Unified Buffer (UB) or L1 buffer.

These are packed into a `TilingData` struct and marshalled to the device. The kernel unpacks them with `GET_TILING_DATA` and offsets into GM by its block index. Nothing about the input shape is hard-coded into the kernel.

```
Host (CPU)                              Device (AICore, ×blockDim)
──────────                              ──────────────────────────
TilingFunc(context):                    add_custom(x, y, z, tiling):
  query shape, coreNum, ubSize            GET_TILING_DATA(t, tiling)
  compute tileNum, tileLength             offset = GetBlockIdx() * blockLength
  SetBlockDim(coreNum)         ──────►    op.Init(x + offset, ...)
  SetTilingKey(key)            tiling     op.Process()   // loops t.tileNum tiles
  tiling.SaveToBuffer(...)
```

## Defining the TilingData Struct

`TilingData` is the contract between host and device. It is declared once in a shared header with framework macros so both sides agree on field layout and the serialization glue is generated automatically.

```cpp
// add_custom_tiling.h — included by BOTH host and device
#include "register/tilingdata_base.h"

namespace optiling {
BEGIN_TILING_DATA_DEF(TilingData)
    TILING_DATA_FIELD_DEF(uint32_t, totalLength);  // total elements to process
    TILING_DATA_FIELD_DEF(uint32_t, tileNum);      // tiles each core walks through
    TILING_DATA_FIELD_DEF(uint32_t, tileLength);   // elements per tile (fits UB)
    TILING_DATA_FIELD_DEF(uint32_t, tailLength);   // remainder for the last tile
END_TILING_DATA_DEF;

REGISTER_TILING_DATA_CLASS(AddCustom, TilingData)
}  // namespace optiling
```

`BEGIN_TILING_DATA_DEF` / `END_TILING_DATA_DEF` open and close the struct, `TILING_DATA_FIELD_DEF(type, name)` declares one plain scalar field, and `REGISTER_TILING_DATA_CLASS(OpName, TilingData)` binds the layout to the operator. Keep the struct to a handful of `uint32_t`/`uint64_t` fields — large structs inflate the host-to-device copy and per-launch overhead.

## The Host Tiling Function

The tiling function receives a `gert::TilingContext*`, queries the platform for real hardware sizes, computes the partition, and serializes it.

```cpp
namespace optiling {
static ge::graphStatus TilingFunc(gert::TilingContext* context)
{
    TilingData tiling;

    // 1. Problem size from the input shape.
    uint32_t totalLength =
        context->GetInputShape(0)->GetStorageShape().GetShapeSize();

    // 2. Authoritative hardware sizing — never hard-code these.
    auto ascendcPlatform =
        platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
    uint32_t coreNum = ascendcPlatform.GetCoreNumAiv();
    uint64_t ubSize;
    ascendcPlatform.GetCoreMemSize(platform_ascendc::CoreMemType::UB, ubSize);

    // 3. Per-core partition and tile sizing.
    uint32_t blockLength = totalLength / coreNum;
    // Reserve UB for input + output + ping-pong copies (double buffering).
    constexpr uint32_t kBuffers = 2, kTensors = 2, kBytesPerElem = 2; // fp16
    uint32_t tileLength = (ubSize / (kBuffers * kTensors)) / kBytesPerElem;
    uint32_t tileNum    = blockLength / tileLength;
    uint32_t tailLength = blockLength % tileLength;

    // 4. Block dim + tiling key + serialize.
    context->SetBlockDim(coreNum);
    context->SetTilingKey(tailLength == 0 ? 1 : 2);  // aligned vs. tail branch
    tiling.set_totalLength(totalLength);
    tiling.set_tileNum(tileNum);
    tiling.set_tileLength(tileLength);
    tiling.set_tailLength(tailLength);
    tiling.SaveToBuffer(context->GetRawTilingData()->GetData(),
                        context->GetRawTilingData()->GetCapacity());
    context->GetRawTilingData()->SetDataSize(tiling.GetDataSize());

    // 5. Declare GM scratch (see technique-workspace-management).
    size_t* workspaces = context->GetWorkspaceSizes(1);
    workspaces[0] = 16 * 1024 * 1024;
    return ge::GRAPH_SUCCESS;
}
}  // namespace optiling
```

`platform_ascendc::PlatformAscendC`, built from `context->GetPlatformInfo()`, is the source of truth for the core count (`GetCoreNumAic()` / `GetCoreNumAiv()`) and on-chip buffer bytes (`GetCoreMemSize(CoreMemType::UB, ...)`, `GetCoreMemSize(CoreMemType::L1, ...)`). Deriving tile bytes from these queries is what makes one tiling function valid across Ascend 910, 910B, and 310P.

## Choosing Tile Sizes

A correct tile size satisfies several constraints simultaneously:

- **UB capacity.** A tile must fit on-chip. For a double-buffered vector kernel, a safe per-tile budget is `ubSize / (numBuffers * numTensors)` so input, output, and the ping-pong copy all coexist.
- **Double-buffer halving.** Double buffering keeps two tiles in flight to overlap copy with compute, which halves the usable budget per tensor. Size the tile against that halved budget, not the full UB — see `technique-double-buffering`.
- **16×16 fractal alignment.** Cube-unit operands live in FRACTAL_NZ, a 16×16 blocked layout. Tile dimensions feeding the Cube unit should be multiples of 16 (and L1 tiles for matmul typically multiples of the 256-element `16×16` fractal). Misaligned tiles force padding and waste cube cycles; the full layout rules live in `technique-nz-tiling`.

| Constraint | Source | Rule of thumb |
|---|---|---|
| Fits UB | `GetCoreMemSize(UB, ...)` | `tileBytes ≤ ubSize / (buffers × tensors)` |
| Fits L1 (matmul) | `GetCoreMemSize(L1, ...)` | A+B tiles co-resident in L1 |
| Double buffering | technique-double-buffering | budget halves; two tiles in flight |
| NZ alignment | technique-nz-tiling | tile M/N/K multiples of 16 |

Choosing the tile too small under-fills the cube/vector pipelines and wastes launch overhead — the failure mode documented in `pattern-tiling-too-small`. Choosing it too large overflows UB at runtime, which is why the budget is derived from `PlatformAscendC` rather than a literal constant.

## Tail Handling

When `totalLength` is not divisible by `blockDim × tileLength`, the last core or last tile is shorter. Reading a full `tileLength` there walks past the end of GM. Two standard remedies:

1. **Remainder field** — carry a `tailLength` in `TilingData` (as above) and have the kernel process `tileNum` full tiles plus one short tile of `tailLength`.
2. **Tiling-key branch** — emit a distinct `SetTilingKey` value for the unaligned case so a separate, tail-aware kernel template runs.

Both keep the kernel from over-reading; the remainder-field form is simplest when only the final tile differs.

## Tiling Keys for Shape Specialization

`context->SetTilingKey(key)` selects which compiled kernel template branch runs, letting one operator carry several code paths chosen per shape class. Typical uses:

- aligned vs. tail-handling (above);
- small-shape vs. large-shape partitioning;
- different cube/vector blocking for tall-skinny vs. square GEMM.

The device kernel reads the same key at compile time (via the template instantiation the framework dispatches), so the branch is resolved without runtime overhead inside the inner loop. A worked host-tiling-plus-kernel pairing lives in `kernel-matmul-ascendc`.

## The Device Kernel

On the device the kernel reconstitutes the struct and derives its GM slice from its block index.

```cpp
extern "C" __global__ __aicore__ void add_custom(
    GM_ADDR x, GM_ADDR y, GM_ADDR z, GM_ADDR tiling)
{
    GET_TILING_DATA(t, tiling);                       // unpack fields

    uint32_t blockLength = t.totalLength / AscendC::GetBlockNum();
    uint32_t offset = AscendC::GetBlockIdx() * blockLength;  // this core's slice

    KernelAdd op;
    op.Init(x + offset, y + offset, z + offset, blockLength,
            t.tileNum, t.tileLength, t.tailLength);
    op.Process();                                     // loops t.tileNum + tail
}
```

`GET_TILING_DATA(t, tiling)` expands into accessors that read the marshalled fields by name; `GetBlockIdx()` returns the current core index (`0 .. blockDim-1`), the canonical way to compute a non-overlapping GM offset. The inner `Process()` loop walks `tileNum` tiles plus the tail, copying one tile at a time into UB — the loop that pairs naturally with double buffering.

## Auto-Tiling

Newer CANN releases can derive the partition automatically, trading tuning control for faster bring-up.

| Aspect | Manual tiling | Auto-tiling |
|---|---|---|
| Partition logic | Author writes `TilingFunc` | Framework derives block dim / tile sizes from shape |
| Tiling key | Set explicitly | May be chosen by the framework |
| Workspace | Sized via `GetWorkspaceSizes` | Auto workspace allocation reserves GM scratch |
| Control | Full, shape-specific tuning | Less tuning surface, faster to stand up |

Auto **workspace** allocation removes the need to hand-compute GM scratch for many operators; the framework reserves and frees it around the launch. Manual workspace via `GetWorkspaceSizes(n)` stays available and is preferred when an operator needs a precisely sized or aligned scratch region — see `technique-workspace-management`.

## Trade-offs, Pitfalls, and Notes

- **Struct/field drift.** Host and device must include the *same* `TilingData` header. Add a field on one side only and `GET_TILING_DATA` reads garbage. Keep the definition in one shared header.
- **Tile sized off a constant.** Hard-coding tile bytes instead of querying `GetCoreMemSize` risks overflowing UB on a smaller part (310P) or under-using a larger one (910B). Always derive from `PlatformAscendC`.
- **Block dim vs. AIC/AIV split.** On cube-vector fused operators the meaningful core count is `GetCoreNumAic()` or `GetCoreNumAiv()` depending on which unit dominates; the wrong one under- or over-subscribes the chip.
- **Tail forgotten.** Without a remainder field or tail tiling key, ragged shapes read past the end of GM. Cover the tail explicitly.
- **Tile too small.** Over-partitioning starves the pipelines and amplifies launch overhead; see `pattern-tiling-too-small`.
- **Serialization cost.** Keep `TilingData` to a few scalars; large structs inflate the per-launch host-to-device copy.

These behaviors are reported by the CANN tiling documentation and Ascend C performance guidance (confidence: source-reported); the `BEGIN_TILING_DATA_DEF` / `TILING_DATA_FIELD_DEF` / `REGISTER_TILING_DATA_CLASS` macros, `GET_TILING_DATA`, `SetBlockDim`, `SetTilingKey`, `GetBlockIdx()`, and `platform_ascendc::PlatformAscendC` queries are all part of the supported tiling API.
