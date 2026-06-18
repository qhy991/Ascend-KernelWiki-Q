---
id: code-catlass-fp8-matmul
title: CATLASS FP8 Matmul Example
type: source-code
repo: Ascend/catlass
path: examples/29_a2_fp8_e4m3_matmul
url: https://gitee.com/ascend/catlass/tree/master/examples/29_a2_fp8_e4m3_matmul
source_category: upstream-code
architectures:
- ascend910b
tags:
- catlass
- fp8
- quantization
- matmul
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- l1-buffer
- l0-buffer
techniques:
- quantization-int8
- tiling-strategy
- pipeline-scheduling
kernel_types:
- quant-matmul
- matmul
- gemm
languages:
- cpp
- ascendc
---

# CATLASS FP8 Matmul Example

CATLASS FP8 E4M3 matmul example documenting low-precision GEMM structure and scale-aware data preparation for Ascend accelerator kernels.

## Code Location

- Repository: `Ascend/catlass`
- Path: `examples/29_a2_fp8_e4m3_matmul`
- URL: https://gitee.com/ascend/catlass/tree/master/examples/29_a2_fp8_e4m3_matmul


## Fetched Source


### `examples/29_a2_fp8_e4m3_matmul/fp8_matmul.cpp`
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

#include <cmath>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <vector>

#include "helper.hpp"
#include "golden.hpp"

#include "catlass/catlass.hpp"
#include "catlass/arch/arch.hpp"
#include "catlass/gemm/block/block_mmad.hpp"
#include "catlass/gemm/block/block_swizzle.hpp"
#include "catlass/gemm/dispatch_policy.hpp"
#include "catlass/gemm/gemm_type.hpp"
#include "catlass/layout/layout.hpp"
#include "catlass/gemm/kernel/fp8_matmul.hpp"

#include "catlass/status.hpp"
#include "catlass/gemm/device/device_gemm.hpp"

using namespace Catlass;

bool ReadFileToVector(const std::string &filePath, std::vector<float> &data)
{
    std::ifstream file(filePath, std::ios::binary);
    if (!file.is_open()) {
        std::cerr << "Failed to open file: " << filePath << std::endl;
        return false;
    }
    file.read(reinterpret_cast<char *>(data.data()), data.size() * sizeof(float));
    file.close();
    return true;
}

struct Options {
    const std::string HELPER = "29_a2_fp8_e4m3_matmul m n k [device_id]";

    GemmCoord problemShape{128, 128, 128};
    int32_t deviceId{0};

    Options() = default;

    int Parse(int argc, const char **argv)
    {
        enum ArgsIndex { M_INDEX = 1, N_INDEX, K_INDEX, DEVICE_ID_INDEX, ARGS_MAX };

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

void Run(Options const &options)
{
    aclrtStream stream{nullptr};
    ACL_CHECK(aclInit(nullptr));
    ACL_CHECK(aclrtSetDevice(options.deviceId));
    ACL_CHECK(aclrtCreateStream(&stream));

    // Get the number of cube cores of the current hardware
    auto aicCoreNum = platform_ascendc::PlatformAscendCManager::GetInstance()->GetCoreNumAic();

    uint32_t m = options.problemShape.m();
    uint32_t n = options.problemShape.n();
    uint32_t k = options.problemShape.k();
    constexpr uint32_t mScalar = 2;
    constexpr uint32_t nScalar = 2;
    constexpr uint32_t splitkLength = 1024;

    size_t lenA = static_cast<size_t>(m) * k;
    size_t lenB = static_cast<size_t>(k) * n;
    size_t lenC = static_cast<size_t>(m) * n;
    size_t lenWA = static_cast<size_t>(splitkLength) * 128 * mScalar;
    size_t lenWB = static_cast<size_t>(splitkLength) * 256 * nScalar;
    size_t lenWC = static_cast<size_t>(128 * mScalar) * 256 * nScalar;

    size_t sizeA = lenA * sizeof(int8_t);
    size_t sizeB = lenB * sizeof(int8_t);
    size_t sizeC = lenC * sizeof(half);
    size_t sizeWA = aicCoreNum * lenWA * sizeof(half) * 2;  // 双缓冲
    size_t sizeWB = aicCoreNum * lenWB * sizeof(half) * 2;  // 双缓冲
    size_t sizeWC = aicCoreNum * lenWC * sizeof(float);

    size_t sizeWorkspace;

    using LayoutA = layout::RowMajor;
    using LayoutB = layout::RowMajor;
    using LayoutC = layout::RowMajor;
    LayoutA layoutA{m, k};
    LayoutB layoutB{k, n};
    LayoutC layoutC{m, n};

    // input init
    half scalar = 1.0;
    half zeroPoint = 0;

    std::vector<int8_t> hostA(lenA);
    std::vector<int8_t> hostB(lenB);
    std::string inFileAName = "../../examples/29_a2_fp8_e4m3_matmul/input/a_8.bin";
    std::ifstream inFileA(inFileAName, std::ios::binary);
    if (!inFileA.is_open()) {
        std::cerr << "Failed to open inFileA: " << inFileAName << std::endl;
    } else {
        inFileA.read(reinterpret_cast<char *>(hostA.data()), sizeA);
        inFileA.close();
    }
    std::string inFileBName = "../../examples/29_a2_fp8_e4m3_matmul/input/b_8.bin";
    std::ifstream inFileB(inFileBName, std::ios::binary);
    if (!inFileB.is_open()) {
        std::cerr << "Failed to open inFileB: " << inFileBName << std::endl;
    } else {
        inFileB.read(reinterpret_cast<char *>(hostB.data()), sizeB);
        inFileB.close();
    }

    uint8_t *deviceA{nullptr};
    ACL_CHECK(aclrtMalloc(reinterpret_cast<void **>(&de
// ... (truncated due to length) ...

```

### `examples/29_a2_fp8_e4m3_matmul/gen_data.py`
```python
# Copyright (c) 2025 Huawei Technologies Co., Ltd.
# This file is a part of the CANN Open Software.
# Licensed under CANN Open Software License Agreement Version 1.0 (the "License").
# Please refer to the License for details. You may not use this file except in compliance with the License.
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
# See LICENSE in the root of the software repository for the full text of the License.


import os
import argparse
import torch
import numpy as np


def gen_data_fp8(row, col):
    data = torch.randn((row, col), dtype=torch.float32)
    data_e4m3 = data.to(torch.float8_e4m3fn)
    return data_e4m3


def gen_data(m, n, k, trans_a, trans_b):
    os.makedirs('./input', exist_ok=True)
    os.makedirs('./output', exist_ok=True)

    a_fp8 = gen_data_fp8(m, k)
    b_fp8 = gen_data_fp8(k, n)

    if(trans_a == 1):
        a_fp8 = a_fp8.t()
    if(trans_b == 1):
        b_fp8 = b_fp8.t()

    a_np = torch.tensor(a_fp8.flatten().untyped_storage(), dtype=torch.int8).numpy()
    b_np = torch.tensor(b_fp8.flatten().untyped_storage(), dtype=torch.int8).numpy()
    a_np.tofile('./input/a_8.bin')
    b_np.tofile('./input/b_8.bin')

    a_fp16 = a_fp8.to(torch.float16)
    b_fp16 = b_fp8.to(torch.float16)
    if(trans_a == 1):
        a_fp16 = a_fp8.t().to(torch.float16)
    if(trans_b == 1):
        b_fp16 = b_fp16.t().to(torch.float16)

    c_fp32 = a_fp16.to(torch.float32) @ b_fp16.to(torch.float32)
    c_np = c_fp32.numpy()
    c_np.tofile('./output/expected_data.bin')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('m', type=int)
    parser.add_argument('n', type=int)    
    parser.add_argument('k', type=int)
    parser.add_argument('trans_a', type=int)
    parser.add_argument('trans_b', type=int)
    args = parser.parse_args()
    gen_data(args.m, args.n, args.k, args.trans_a, args.trans_b)

```
