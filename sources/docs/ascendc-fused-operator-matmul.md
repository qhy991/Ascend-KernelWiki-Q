---
id: doc-ascendc-fused-operator-matmul
title: "AscendC Fused Operator Programming — Matmul + Activation"
type: source-doc
architectures: [ascend910, ascend910b]
tags: [ascendc, matmul, operator-fusion, activation]
date: '2026-06-19'
url: https://www.hiascend.com/document/detail/zh/canncommercial/80RC3/developmentguide/opdevg/Ascendcopdevg/atlas_ascendc_10_0054.html
hardware_features: [cube-unit, vector-unit, unified-buffer]
techniques: [pipeline-scheduling, operator-fusion, tiling-strategy]
kernel_types: [matmul, activation]
languages: [ascendc, cpp]
confidence: verified
---

# AscendC Fused Operator Programming — Matmul + Activation

Official CANN guide for fusion operators combining Matmul (Cube) with Vector activations — reference for FFN and MatmulLeakyRelu patterns.

## Source

- CANN Commercial 8.0.RC3 — Ascend C Operator Development → Fused Operator Programming → Operator Implementation
- URL: https://www.hiascend.com/document/detail/zh/canncommercial/80RC3/developmentguide/opdevg/Ascendcopdevg/atlas_ascendc_10_0054.html
- Complete sample: **MatmulLeakyRelu**

## Fusion Pattern

AscendC Matmul high-level APIs encapsulate tiling, data movement, and compute. Fusion operators combine Matmul with subsequent Vector ops (e.g., LeakyRelu) using the same pipeline paradigm:

1. Host: obtain tiling via `MultiCoreMatmulTiling`
2. Pass tiling to kernel
3. Kernel: Matmul iterate + Vector activation in loop

## Host-Side MultiCoreMatmulTiling (Official)

```cpp
auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
matmul_tiling::MultiCoreMatmulTiling cubeTiling(ascendcPlatform);

cubeTiling.SetAType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND,
                   matmul_tiling::DataType::DT_FLOAT16);
cubeTiling.SetBType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND,
                   matmul_tiling::DataType::DT_FLOAT16);
cubeTiling.SetCType(matmul_tiling::TPosition::LCM, matmul_tiling::CubeFormat::ND,
                   matmul_tiling::DataType::DT_FLOAT);
cubeTiling.SetBiasType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND,
                       matmul_tiling::DataType::DT_FLOAT);

cubeTiling.SetShape(M, N, K);
cubeTiling.SetOrgShape(M, N, K);

MatmulLeakyreluCustomTilingData tiling;
if (cubeTiling.GetTiling(tiling.cubeTilingData) == -1) {
    return ge::GRAPH_FAILED;
}
```

## Multi-Core SetDim Rules (Official)

For MIX mode (Cube + Vector):
- Use `SetDim()` to set Matmul core count
- MIX scheduling rules documented in fusion guide

## Kernel Workspace (Official)

For non-custom-operator and non-`-DHAVE_WORKSPACE` kernel-direct projects:
- Call `SetSysWorkSpace()` before Matmul init

## Kernel Tiling Registration (C++ Standard Syntax)

Official aclnn-style projects use:

```cpp
REGISTER_TILING_DEFAULT(TilingStructType);
// In kernel:
GET_TILING_DATA(tilingData, tilingPointer);
```

Requires `kernel_tiling.h` generated from host tiling struct.

## Applicability to FFN

FFN = GEMM1 → activation → GEMM2 maps to:
- Two `MultiCoreMatmulTiling` passes (or fused single-kernel with UB-resident intermediate)
- Vector unit for activation between GEMMs
- Reference sample MatmulLeakyRelu for single-GEMM+activation fusion pattern
