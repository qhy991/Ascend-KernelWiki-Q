---
id: doc-ascendc-tiling-api
title: "Ascend C Host-Side Tiling API Reference"
type: source-doc
architectures: [ascend910, ascend910b, ascend310p]
tags: [tiling, ascendc, cpp, operator, cann]
date: '2026-02-28'
url: https://www.hiascend.com/document/detail/en/canncommercial/800/opdevg/Ascendcopdevg/atlas_ascendc_10_0056.html
hardware_features: [unified-buffer, l1-buffer, global-memory]
techniques: [data-reuse, double-buffering]
confidence: verified
---

# Ascend C Host-Side Tiling API Reference

## Overview

In the Ascend C programming model an operator is split into two cooperating halves: a **host-side tiling function** that runs on the CPU before launch, and a **device kernel** that runs on the AICore. The tiling function decides how the problem is partitioned across cores and how each core slices its share into buffer-sized tiles, then serializes those decisions into a `TilingData` struct that the kernel reads at runtime. This separation lets a single kernel binary adapt to arbitrary input shapes without recompilation, and keeps shape-dependent arithmetic off the critical path of the AICore.

## The TilingData Struct

`TilingData` is the contract between host and device. It is declared with a small set of macros so that both sides agree on field layout and the framework can generate the serialization glue automatically.

```cpp
// Host-side tiling header (e.g. add_custom_tiling.h)
#include "register/tilingdata_base.h"

namespace optiling {
BEGIN_TILING_DATA_DEF(TilingData)
    TILING_DATA_FIELD_DEF(uint32_t, totalLength);  // total elements to process
    TILING_DATA_FIELD_DEF(uint32_t, tileNum);      // tiles per core
END_TILING_DATA_DEF;

REGISTER_TILING_DATA_CLASS(AddCustom, TilingData)
}  // namespace optiling
```

- `BEGIN_TILING_DATA_DEF(TilingData)` / `END_TILING_DATA_DEF` open and close the struct definition.
- `TILING_DATA_FIELD_DEF(type, name)` declares one field. Fields are typically `uint32_t`/`uint64_t` scalars; keep them plain so the struct serializes deterministically.
- `REGISTER_TILING_DATA_CLASS(OpName, TilingData)` binds the struct to the operator named `OpName`, which is how the framework knows which `TilingData` layout to marshal for that operator's kernel.

Field ordering matters: the kernel reads the struct back by name through generated accessors, so the host and device must include the same definition header.

## Host-Side Tiling Function

The tiling function receives a `gert::TilingContext*` and is responsible for three things: computing the partition, filling the `TilingData`, and reporting block dimensions and workspace.

```cpp
namespace optiling {
static ge::graphStatus TilingFunc(gert::TilingContext* context)
{
    TilingData tiling;

    // 1. Read the input shape from the context.
    uint32_t totalLength = context->GetInputShape(0)->GetStorageShape().GetShapeSize();

    // 2. Query the platform for the core count and on-chip buffer sizes.
    auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
    uint32_t coreNum = ascendcPlatform.GetCoreNumAiv();
    uint64_t ubSize;
    ascendcPlatform.GetCoreMemSize(platform_ascendc::CoreMemType::UB, ubSize);

    // 3. Decide block dimension and per-core tiling.
    uint32_t tileNum = 8;                       // tiles each core walks through
    context->SetBlockDim(coreNum);              // number of physical cores to launch
    context->SetTilingKey(1);                   // selects a kernel template branch

    // 4. Populate and serialize the TilingData.
    tiling.set_totalLength(totalLength);
    tiling.set_tileNum(tileNum);
    tiling.SaveToBuffer(context->GetRawTilingData()->GetData(),
                        context->GetRawTilingData()->GetCapacity());
    context->GetRawTilingData()->SetDataSize(tiling.GetDataSize());

    // 5. Declare workspace (system reserved + any operator scratch).
    size_t* workspaces = context->GetWorkspaceSizes(1);
    workspaces[0] = 16 * 1024 * 1024;           // bytes of GM scratch
    return ge::GRAPH_SUCCESS;
}
}  // namespace optiling
```

Key responsibilities:

- **Block dim** — `context->SetBlockDim(n)` tells the runtime how many AICore instances to launch. Each instance later identifies itself with `GetBlockIdx()`.
- **Tiling key** — `context->SetTilingKey(key)` selects which compiled kernel template branch runs, letting one operator carry several code paths (e.g. aligned vs. tail-handling).
- **Serialization** — `SaveToBuffer` writes the `TilingData` into the raw buffer the runtime will copy to the device.
- **Workspace** — `context->GetWorkspaceSizes(1)` returns a slot to report GM scratch the kernel needs.

### Querying the Platform

`platform_ascendc::PlatformAscendC`, constructed from `context->GetPlatformInfo()`, is the authoritative source for hardware sizing so the tiling generalizes across Ascend 910, 910B, and 310P:

- `GetCoreNumAic()` — number of AICore Cube (AIC) cores.
- `GetCoreNumAiv()` — number of AICore Vector (AIV) cores.
- `GetCoreMemSize(CoreMemType::UB, size)` — Unified Buffer bytes per core.
- `GetCoreMemSize(CoreMemType::L1, size)` — L1 buffer bytes per core.

A tile must fit on-chip. For a double-buffered vector kernel, a safe per-tile UB budget is roughly `ubSize / (numBuffers * numTensors)`, leaving room for input, output, and ping-pong copies. The `double-buffering` technique relies on this headroom; see the Unified Buffer notes in `hw-unified-buffer` for the underlying constraint.

## Device-Side Kernel

On the device the kernel reconstitutes the struct with `GET_TILING_DATA` and uses `GetBlockIdx()` to find its slice of global memory.

```cpp
extern "C" __global__ __aicore__ void add_custom(
    GM_ADDR x, GM_ADDR y, GM_ADDR z, GM_ADDR tiling)
{
    GET_TILING_DATA(t, tiling);                 // unpack TilingData fields

    uint32_t blockLength = t.totalLength / AscendC::GetBlockNum();
    uint32_t offset = AscendC::GetBlockIdx() * blockLength;  // this core's GM slice

    KernelAdd op;
    op.Init(x + offset, y + offset, z + offset, blockLength, t.tileNum);
    op.Process();
}
```

`GET_TILING_DATA(t, tiling)` expands into accessors that read `t.totalLength` and `t.tileNum` straight from the marshalled buffer. `GetBlockIdx()` returns the index of the current core (0 .. blockDim-1), which is the canonical way to derive a non-overlapping GM offset. Inside `Process()` the kernel further loops `tileNum` times, copying one tile at a time into UB — the inner loop that pairs naturally with double buffering and the `data-reuse` technique used in `kernel-matmul-ascendc`.

## Auto vs. Manual Tiling and Workspace

Newer CANN releases support two levels of automation:

| Aspect | Manual tiling | Auto tiling |
|---|---|---|
| Partition logic | Author writes `TilingFunc` by hand | Framework derives block dim / tile sizes from shape |
| Tiling key | Set explicitly | May be chosen by the framework |
| Workspace | Author sizes via `GetWorkspaceSizes` | Auto workspace allocation reserves GM scratch |
| Control | Full, shape-specific tuning | Faster bring-up, less tuning surface |

Auto **workspace** allocation, available in newer CANN, removes the need to hand-compute the GM scratch byte count for many operators; the framework reserves and frees it around the kernel launch. Manual workspace via `GetWorkspaceSizes(n)` remains available and is preferred when an operator needs a precisely sized or aligned scratch region. The first workspace entry conventionally also covers the runtime's reserved system area.

## Trade-offs, Pitfalls, and Notes

- **Struct/field drift** — host and device must include the *same* `TilingData` header. If a field is added on one side only, `GET_TILING_DATA` reads garbage. Keep the definition in a shared header.
- **Tile too large for UB/L1** — sizing a tile without consulting `PlatformAscendC` risks overflowing the Unified Buffer at runtime. Always derive tile bytes from `GetCoreMemSize`, not a hard-coded constant, so the same code is valid on 910, 910B, and 310P.
- **Tail handling** — when `totalLength` is not divisible by `blockDim * tileLength`, the last core/tile is shorter. Encode a separate `SetTilingKey` branch or carry a remainder field so the kernel does not read past the end of GM.
- **Block dim vs. AIC/AIV split** — on cube-vector fused operators, the meaningful core count comes from `GetCoreNumAic()` or `GetCoreNumAiv()` depending on which unit dominates; using the wrong one under- or over-subscribes the chip.
- **Workspace lifetime** — manually reported workspace is valid only for the launch; do not assume contents persist across kernel invocations.
- **Serialization cost** — `TilingData` should stay small (a handful of scalars). Large structs inflate the host-to-device copy and the per-launch overhead.

## Learning Resources

- Official Ascend C operator development guide: [Tiling and TilingData](https://www.hiascend.com/document/detail/en/canncommercial/800/opdevg/Ascendcopdevg/atlas_ascendc_10_0056.html)
- Companion device-side API surface: `doc-ascendc-api-reference`
- Worked example pairing host tiling with a device kernel: `kernel-matmul-ascendc`

## Status

Verified against CANN 8.0. The `BEGIN_TILING_DATA_DEF` / `TILING_DATA_FIELD_DEF` / `REGISTER_TILING_DATA_CLASS` macros, `GET_TILING_DATA`, `GetBlockIdx()`, and `platform_ascendc::PlatformAscendC` queries are all part of the supported Ascend C tiling API; auto workspace allocation is available in newer CANN releases.
