---
id: code-vllm-ascend-batch-matmul-transpose
title: vLLM Ascend Batch Matmul Transpose Operator
type: source-code
repo: vllm-project/vllm-ascend
path: csrc/batch_matmul_transpose
url: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/batch_matmul_transpose
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
- matmul
- transpose
- ascendc
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- nz-format
- global-memory
techniques:
- format-conversion
- tiling-strategy
- pipeline-scheduling
kernel_types:
- matmul
- gemm
languages:
- cpp
- ascendc
---

# vLLM Ascend Batch Matmul Transpose Operator

vLLM Ascend batch-matmul-transpose custom operator showing how transposed layouts, tiling metadata, and Cube execution are packaged for serving workloads.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `csrc/batch_matmul_transpose`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/batch_matmul_transpose


## Fetched Source


### `csrc/batch_matmul_transpose/batch_matmul_transpose_torch_adpt.h`
```cpp
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2026. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
#ifndef BATCH_MATMUL_TRANSPOSE_TORCH_ADPT_H
#define BATCH_MATMUL_TRANSPOSE_TORCH_ADPT_H
#include "op_host/batch_matmul_transpose.h"

namespace vllm_ascend {

void batch_matmul_transpose(const at::Tensor &tensor_a, const at::Tensor &tensor_b, at::Tensor &tensor_c,
                                    c10::optional<c10::string_view> format_mode,
                                    c10::optional<c10::string_view> quant_mode)
{
    auto [tiling_tensor, block_dim] = bmm_trans::batch_matmul_transpose_tiling(
        tensor_a,
        tensor_b,
        tensor_c,
        format_mode,
        quant_mode
    );

    void *gm_a = tensor_a.data_ptr();
    void *gm_b = tensor_b.data_ptr();
    void *gm_c = tensor_c.data_ptr();
    void *gm_tiling_data = tiling_tensor.data_ptr();

    aclrtStream stream = c10_npu::getCurrentNPUStream().stream();
    at_npu::native::OpCommand cmd;
    cmd.Name("batch_matmul_transpose");

    cmd.SetCustomHandler([stream, gm_a, gm_b, gm_c, gm_tiling_data,
                          block_dim]() -> int {
        batch_matmul_transpose_impl(stream, gm_a, gm_b, gm_c, gm_tiling_data,
                            block_dim);
        return 0;
    });
    cmd.Run();
    return;
}

}
#endif
```

### `csrc/batch_matmul_transpose/op_host/common_tiling.h`
```cpp
/*
 * Copyright (c) 2024 Huawei Technologies Co., Ltd.
 * This file is a part of the CANN Open Software.
 * Licensed under CANN Open Software License Agreement Version 1.0 (the "License").
 * Please refer to the License for details. You may not use this file except in compliance with the License.
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
 * See LICENSE in the root of the software repository for the full text of the License.
 */

#ifndef COMMMON_TILING_H
#define COMMMON_TILING_H

#include <iostream>
#include <cmath>
#include "common.h"
#include "tiling/platform/platform_ascendc.h"

namespace host_utils {

constexpr uint32_t FP16_SIZE = 2;
constexpr uint32_t FP32_SIZE = 4;
constexpr uint32_t BLOCK_SIZE = 16;
constexpr uint32_t BLOCK_SIZE_INT8_K = 32;
constexpr uint32_t BASE_BLOCK_STEP = 2;
constexpr uint32_t AXES_ALIGN_SIZE = 512;
constexpr uint32_t AXES_ALIGN_SIZE_INT8 = 256;
constexpr uint32_t ND_SHAPE_SIZE = 2;
constexpr uint32_t NZ_SHAPE_SIZE = 4;
constexpr uint32_t CUBE_BLOCK_SIZE = 256;
constexpr uint32_t CUBE_BLOCK_SIZE_INT8 = 512;
constexpr uint32_t L1AB_PINGPONG_BUFFER_LEN = 262144;
constexpr uint32_t L0AB_PINGPONG_BUFFER_LEN_INT8 = 131072 * 2;  // 256 KB
constexpr uint32_t L0AB_PINGPONG_BUFFER_LEN_FP16 = 131072;      // 128 KB
constexpr uint32_t L1AB_PINGPONG_BUFFER_LEN_INT8_SPARSE = 160 * 1024;
constexpr uint32_t UB_LIMIT_SIZE_910A = 128 * 1024;

enum class PlatformType { ASCEND_310P, ASCEND_910A, ASCEND_910B, ASCEND_910C, PLATFORM_INVALID };

struct PlatformInfo {
public:
    static const PlatformInfo &Instance()
    {
        static PlatformInfo platformInfo;
        return platformInfo;
    }

    PlatformType socType;
    uint32_t coreNum;
    uint32_t coreNumAic;
    uint32_t coreNumAiv;
    uint64_t ubSize;
    uint64_t l1Size;
    uint64_t l2Size;
    uint64_t l0aSize;
    uint64_t l0bSize;
    uint64_t l0cSize;

private:
    PlatformInfo()
    {
        auto ascendcPlatform = platform_ascendc::PlatformAscendCManager::GetInstance();
        // TODO Hard coding set to 910_93xx, parse using aclrtGetSocName is better
        socType = PlatformType::ASCEND_910C;
        coreNum = ascendcPlatform->GetCoreNum();
        coreNumAic = ascendcPlatform->GetCoreNumAic();
        coreNumAiv = ascendcPlatform->GetCoreNumAiv();
        ascendcPlatform->GetCoreMemSize(platform_ascendc::CoreMemType::UB, ubSize);
        ascendcPlatform->GetCoreMemSize(platform_ascendc::CoreMemType::L1, l1Size);
        ascendcPlatform->GetCoreMemSize(platform_ascendc::CoreMemType::L2, l2Size);
        ascendcPlatform->GetCoreMemSize(platform_ascendc::CoreMemType::L0_A, l0aSize);
        ascendcPlatform->GetCoreMemSize(platform_ascendc::CoreMemType::L0_B, l0bSize);
        ascendcPlatform->GetCoreMemSize(platform_ascendc::CoreMemType::L0_C, l0cSize);
    }

    PlatformInfo(const PlatformInfo &) = delete;
    PlatformInfo &operator=(const PlatformInfo &) = delete;
    PlatformInfo(PlatformInfo &&) = delete;
    PlatformInfo &operator=(PlatformInfo &&) = delete;
};

inline __attribute__((always_inline)) uint32_t GetN0TilingLimit(bool compressFlag, uint32_t tilingN,
                                                                const PlatformType &platformType)
{
    if (compressFlag) {
        return std::min(tilingN * BLOCK_SIZE, AXES_ALIGN_SIZE_INT8);
    } else {
        return (platformType == PlatformType::ASCEND_310P || platformType == PlatformType::ASCEND_910A)
                   ? AXES_ALIGN_SIZE
                   : AXES_ALIGN_SIZE_INT8;
    }
}

template <typename OpShareType>
inline __attribute__((always_inline)) uint32_t GetN0TilingInit(const OpShareType &opShape, bool compressFlag,
                                                               uint32_t tilingN)
{
    const uint32_t rnd = 16;
    return compressFlag
               ? ((tilingN * BLOCK_SIZE > opShape.n) ? RoundUp<uint32_t>(opShape.n, rnd) : tilingN * BLOCK_SIZE)
               : BLOCK_SIZE;
}

template <bool PRI_FLAG>
inline __attribute__((always_inline)) bool IsExceedTilingLimit(uint32_t axes0, uint32_t priAxes0,
                                                               uint32_t n0TilingLimit, PlatformType platformType,
                                                               uint32_t basicBlockSize)
{
    return (PRI_FLAG && axes0 > n0TilingLimit) || (!PRI_FLAG && priAxes0 > n0TilingLimit) ||
           (platformType == PlatformType::ASCEND_910A && basicBlockSize > UB_LIMIT_SIZE_910A);
}

template <bool PRI_FLAG, typename OpShareType>
inline __attribute__((always_inline)) void SetOpShapeAxesInfo(OpShareType &opShape, uint32_t priAxes0, uint32_t axes0)
{
    opShape.m0 = PRI_FLAG ? priAxes0 : axes0;
    opShape.n0 = PRI_FLAG ? axes0 : priAxes0;
}

template <typename HardwareType, typename OpShapeType>
inline __attribute__((always_inline)) float CostFunc(const HardwareT
// ... (truncated due to length) ...

```

### `csrc/batch_matmul_transpose/op_host/common.h`
```cpp

// Licensed under the BSD 3-Clause License  (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#ifndef UTILS_COMMON_H
#define UTILS_COMMON_H

namespace host_utils {

constexpr uint32_t BLK_SIZE_ALIN_FOR_INT64 = 4;
constexpr uint32_t BLK_SIZE_ALIN_FOR_INT32 = 8;

inline uint64_t alinInt64Count(uint64_t count)
{
    return (count + BLK_SIZE_ALIN_FOR_INT64 - 1) / BLK_SIZE_ALIN_FOR_INT64 * BLK_SIZE_ALIN_FOR_INT64;
}

inline uint64_t alinInt32Count(uint64_t count)
{
    return (count + BLK_SIZE_ALIN_FOR_INT32 - 1) / BLK_SIZE_ALIN_FOR_INT32 * BLK_SIZE_ALIN_FOR_INT32;
}

template <typename T>
inline T CeilDiv(const T dividend, const T divisor)
{
    if (divisor == 0) {
        return UINT32_MAX;
    }
    return (dividend + divisor - 1) / divisor;
}

template <typename T>
inline T RoundUp(const T val, const T align = 16)
{
    if (align == 0 || val + align - 1 < val) {
        return 0;
    }
    return (val + align - 1) / align * align;
}

template <typename T>
inline T RoundDown(const T val, const T align = 16)
{
    if (align == 0) {
        return 0;
    }
    return val / align * align;
}
}  // namespace host_utils
#endif  // UTILS_COMMON_H

```
