---
id: code-catlass-quant-matmul
title: CATLASS Quantized Matmul Example
type: source-code
repo: Ascend/catlass
path: examples/12_quant_matmul
url: https://gitee.com/ascend/catlass/tree/master/examples/12_quant_matmul
source_category: upstream-code
architectures:
- ascend910b
tags:
- catlass
- quantization
- matmul
- ascendc
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- nz-format
- l0-buffer
techniques:
- quantization-int8
- nz-tiling
- format-conversion
kernel_types:
- quant-matmul
- matmul
- gemm
languages:
- cpp
- ascendc
---

# CATLASS Quantized Matmul Example

CATLASS quantized matmul example for low-precision GEMM flows, including quantized operands, Cube execution, and vector-side scale/dequantization handling.

## Code Location

- Repository: `Ascend/catlass`
- Path: `examples/12_quant_matmul`
- URL: https://gitee.com/ascend/catlass/tree/master/examples/12_quant_matmul


## Fetched Source


### `examples/12_quant_matmul/quant_matmul.cpp`
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
#include <cstdlib>

#include "helper.hpp"
#include "golden.hpp"
#include "fp16_t.h"

#include "catlass/catlass.hpp"
#include "catlass/arch/arch.hpp"
#include "catlass/epilogue/block/block_epilogue.hpp"
#include "catlass/epilogue/dispatch_policy.hpp"
#include "catlass/epilogue/tile/tile_broadcast_mul.hpp"
#include "catlass/epilogue/tile/tile_broadcast_one_blk.hpp"
#include "catlass/epilogue/tile/tile_swizzle.hpp"
#include "catlass/gemm/block/block_mmad.hpp"
#include "catlass/gemm/block/block_swizzle.hpp"
#include "catlass/gemm/dispatch_policy.hpp"
#include "catlass/gemm/kernel/quant_matmul_multistage_workspace.hpp"
#include "catlass/gemm/gemm_type.hpp"
#include "catlass/layout/layout.hpp"
#include "catlass/status.hpp"
#include "catlass/gemm/device/device_gemm.hpp"

using namespace Catlass;
using fp16_t = op::fp16_t;

using L1TileShape = GemmShape<128, 256, 512>;
constexpr uint32_t workspaceStages = 2;


struct Options {
    const std::string HELPER = "12_quant_matmul m n k [device_id]";

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
            deviceId = std::atoi(argv[DEVICE_ID_INDEX]);
        }
        return 0;
    }
};

void Run(Options const & options)
{
    aclrtStream stream{nullptr};
    ACL_CHECK(aclInit(nullptr));
    ACL_CHECK(aclrtSetDevice(options.deviceId));
    ACL_CHECK(aclrtCreateStream(&stream));

    auto aicCoreNum = platform_ascendc::PlatformAscendCManager::GetInstance()->GetCoreNumAic();

    uint32_t m = options.problemShape.m();
    uint32_t n = options.problemShape.n();
    uint32_t k = options.problemShape.k();

    size_t lenA = static_cast<size_t>(m) * k;
    size_t lenB = static_cast<size_t>(k) * n;
    size_t lenScale = static_cast<size_t>(n);
    size_t lenPerTokenScale = static_cast<size_t>(m);
    size_t lenD = static_cast<size_t>(m) * n;

    size_t sizeA = lenA * sizeof(int8_t);
    size_t sizeB = lenB * sizeof(int8_t);
    size_t sizeScale = lenScale * sizeof(fp16_t);
    size_t sizePerTokenScale = lenPerTokenScale * sizeof(fp16_t);
    size_t sizeD = lenD * sizeof(fp16_t);
    size_t sizeWorkspace;

    std::vector<int8_t> hostA(lenA);
    std::vector<int8_t> hostB(lenB);
    std::vector<fp16_t> hostScale(lenScale);
    std::vector<fp16_t> hostPerTokenScale(lenPerTokenScale);
    golden::FillRandomData(hostA, -16, 16); // Fill with random data, ranging from -16 to 16.
    golden::FillRandomData(hostB, -16, 16); // Fill with random data, ranging from -16 to 16.
    golden::FillRandomData(hostScale, 0.0, 1.0); // Fill with random data, ranging from 0.0 to 1.0
    golden::FillRandomData(hostPerTokenScale, 0.0, 1.0); // Fill with random data, ranging from 0.0 to 1.0

    uint8_t *deviceA{nullptr};
    ACL_CHECK(aclrtMalloc(reinterpret_cast<void **>(&deviceA), sizeA, ACL_MEM_MALLOC_HUGE_FIRST));
    ACL_CHECK(aclrtMemcpy(deviceA, sizeA, hostA.data(), sizeA, ACL_MEMCPY_HOST_TO_DEVICE));

    uint8_t *deviceB{nullptr};
    ACL_CHECK(aclrtMalloc(reinterpret_cast<void **>(&deviceB), sizeB, ACL_MEM_MALLOC_HUGE_FIRST));
    ACL_CHECK(aclrtMemcpy(deviceB, sizeB, hostB.data(), sizeB, ACL_MEMCPY_HOST_TO_DEVICE));

    uint8_t *deviceScale{nullptr};
    ACL_CHECK(aclrtMalloc(reinterpret_cast<void **>(&deviceScale), sizeScale, ACL_MEM_MALLOC_HUGE_FIRST));
    ACL_CHECK(aclrtMemcpy(deviceScale, sizeScale, hostScale.data(), sizeScale, ACL_MEMCPY_HOST_TO_DEVICE));

    uint8_t *devicePerTokenScale{nullptr};
    ACL_CHECK(aclrtMalloc(reinterpret_cast<void **>(&devicePerTokenScale), sizePerTokenScale,
        ACL_MEM_MALLOC_H
// ... (truncated due to length) ...

```
