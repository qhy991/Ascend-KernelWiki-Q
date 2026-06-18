---
id: code-catlass-optimized-matmul
title: CATLASS Optimized Matmul Example
type: source-code
repo: Ascend/catlass
path: examples/06_optimized_matmul
url: https://gitee.com/ascend/catlass/tree/master/examples/06_optimized_matmul
source_category: upstream-code
architectures:
- ascend910b
tags:
- catlass
- optimized-gemm
- matmul
- ascendc
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- l1-buffer
- l0-buffer
- unified-buffer
techniques:
- pipeline-scheduling
- double-buffering
- data-reuse
kernel_types:
- matmul
- gemm
languages:
- cpp
- ascendc
---

# CATLASS Optimized Matmul Example

CATLASS optimized matmul example anchoring higher-performance GEMM variants with explicit scheduling, tile reuse, and buffered movement around Cube computation.

## Code Location

- Repository: `Ascend/catlass`
- Path: `examples/06_optimized_matmul`
- URL: https://gitee.com/ascend/catlass/tree/master/examples/06_optimized_matmul


## Fetched Source


### `examples/06_optimized_matmul/optimized_matmul.cpp`
```cpp
/*
 * Copyright (c) 2025 Huawei Technologies Co., Ltd.
 * This file is a part of the CANN Open Software.
 * Licensed under CANN Open Software License Agreement Version 1.0 (the "License").
 * Please refer to the License for details. You may not use this file except in compliance with the License.
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
 * See LICENSE in the root of the software repository for the full text of the License.
 */

// By setting the K_MAX_SHAPE_DIM macro, the dimension of the AscendC Tensor's ShapeInfo is configured to 0, 
// optimizing stack space. If you need to use the ShapeInfo of the AscendC Tensor, please undefine this macro.
#ifndef K_MAX_SHAPE_DIM
#define K_MAX_SHAPE_DIM 0
#endif

#include <iostream>
#include <vector>

#include "helper.hpp"
#include "golden.hpp"
#include "fp16_t.h"

#include "catlass/catlass.hpp"
#include "catlass/arch/arch.hpp"
#include "catlass/layout/layout.hpp"
#include "catlass/gemm/block/block_mmad.hpp"
#include "catlass/gemm/block/block_swizzle.hpp"
#include "catlass/gemm/dispatch_policy.hpp"
#include "catlass/gemm/kernel/optimized_matmul.hpp"
#include "catlass/gemm/gemm_type.hpp"

#include "catlass/status.hpp"
#include "catlass/gemm/device/device_gemm.hpp"

using namespace Catlass;
using fp16_t = op::fp16_t;

template <
    /// Tag indicating architecture
    class ArchTag,
    /// GemmType for A matrix operand
    class AType,
    /// GemmType type for B matrix operand
    class BType,
    /// GemmType type for C matrix operand
    class CType,
    /// GemmType type for Bias operand
    class BiasType = void
>
struct TileCopyOpt : public Catlass::Gemm::Tile::TileCopy<ArchTag, AType, BType, CType, BiasType> {
    using Base = Catlass::Gemm::Tile::TileCopy<ArchTag, AType, BType, CType, BiasType>;
    using ElementA = typename Base::ElementA;
    using ElementB = typename Base::ElementB;
    using ElementAccumulator = typename Base::ElementAccumulator;

    // When matrix A is row-major, if the number of rows in matrix A is less than 16, 
    // using the CopyGmToL1IntervalDataCopy method can improve the transfer efficiency.
    // The situation is similar for matrix B. If the above conditions are met, 
    // please uncomment the following and comment out the original matrix A transfer method

    // using CopyGmToL1A = Gemm::Tile::CopyGmToL1IntervalDataCopy<ArchTag, AType>;

    using CopyGmToL1A = typename Base::CopyGmToL1A;
    using CopyGmToL1B = typename Base::CopyGmToL1B;

    using CopyL1ToL0A = typename Base::CopyL1ToL0A;
    using CopyL1ToL0B = typename Base::CopyL1ToL0B;

    using CopyL0CToGm = typename Base::CopyL0CToGm; 
    using BiasTypeSelector = typename Base::BiasTypeSelector; 
    using CopyGmToL1Bias = typename Base::CopyGmToL1Bias;
    using CopyL1ToBT = typename Base::CopyL1ToBT;
};

constexpr uint32_t alignByByte = 512;
constexpr uint32_t alignByElement = alignByByte / sizeof(fp16_t);

using ArchTag = Arch::AtlasA2;
constexpr bool ENABLE_UNIT_FLAG = true;
constexpr bool ENABLE_SHUFFLE_K = true;
using ElementA = half;
using ElementB = half;
using ElementC = half;
using LayoutA = layout::RowMajor;
using LayoutB = layout::ColumnMajor;
using LayoutC = layout::RowMajor;

using AType = Gemm::GemmType<ElementA, LayoutA>;
using BType = Gemm::GemmType<ElementB, LayoutB>;
using CType = Gemm::GemmType<ElementC, LayoutC>;
using DispatchPolicy = Gemm::MmadAtlasA2Preload<ENABLE_UNIT_FLAG, ENABLE_SHUFFLE_K>;

// if LayoutA and LayoutB is both ColumnMajor,
// L1TileShape using GemmShape<256, 128, 256> can achieve better performance.
using L1TileShape = std::conditional_t<std::is_same_v<LayoutA, layout::ColumnMajor> &&
    std::is_same_v<LayoutB, layout::ColumnMajor>, GemmShape<256, 128, 256>, GemmShape<128, 256, 256>>;
using L0TileShape = std::conditional_t<std::is_same_v<LayoutA, layout::ColumnMajor> &&
    std::is_same_v<LayoutB, layout::ColumnMajor>, GemmShape<256, 128, 64>, GemmShape<128, 256, 64>>;
using BlockScheduler30 = typename Gemm::Block::GemmIdentityBlockSwizzle<3, 0>;
using BlockScheduler31 = typename Gemm::Block::GemmIdentityBlockSwizzle<3, 1>;
using BlockEpilogue = void;

struct Options {
    const std::string HELPER = "06_optimizd_matmul m n k [device_id]";

    GemmCoord problemShape{128, 128, 128};
    int32_t deviceId{0};

    Options() = default;

    int Parse(int argc, const char **argv)
    {
        enum ArgsIndex {
            M_INDEX = 1,
            N_INDEX,
            K_INDEX,
            DEVICE_ID_INDEX,
            ARGS_MAX
        };

        if (argc > ARGS_MAX || argc <= K_INDEX) {
            std::cerr << HELPER << std::endl;
            return -1;
        }

        problemShape.m() = std::atoi(argv[M_INDEX]);
        problemShape.n() = std::atoi(argv[N_INDEX]);
        problemShape.k() = std::atoi(argv[K_INDEX]);
        if (argc == ARGS_MAX) {
      
// ... (truncated due to length) ...

```
