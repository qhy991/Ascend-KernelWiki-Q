---
id: code-vllm-ascend-grouped-matmul-swiglu-quant
title: vLLM Ascend Grouped Matmul SwiGLU Quant Operator
type: source-code
repo: vllm-project/vllm-ascend
path: csrc/gmm/grouped_matmul_swiglu_quant
url: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/gmm/grouped_matmul_swiglu_quant
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
- grouped-gemm
- swiglu
- quantization
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
- cube-vector-overlap
- pipeline-scheduling
kernel_types:
- grouped-gemm
- moe
- swiglu
- quant-matmul
languages:
- cpp
- ascendc
---

# vLLM Ascend Grouped Matmul SwiGLU Quant Operator

vLLM Ascend grouped matmul plus SwiGLU quant operator, serving as code evidence for MoE MLP fusion and low-precision grouped GEMM.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `csrc/gmm/grouped_matmul_swiglu_quant`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/gmm/grouped_matmul_swiglu_quant


## Fetched Source


### `csrc/gmm/grouped_matmul_swiglu_quant/op_host/grouped_matmul_swiglu_quant_def.cpp`
```cpp
/**
 * Copyright (c) 2025 Huawei Technologies Co., Ltd.
 * This program is free software, you can redistribute it and/or modify it under the terms and conditions of
 * CANN Open Software License Agreement Version 2.0 (the "License").
 * Please refer to the License for details. You may not use this file except in compliance with the License.
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
 * See LICENSE in the root of the software repository for the full text of the License.
 */

/*!
 * \file grouped_matmul_swiglu_quant_def.cpp
 * \brief
 */

#include "register/op_def_registry.h"
namespace ops {
class GroupedMatmulSwigluQuant : public OpDef {
public:
    explicit GroupedMatmulSwigluQuant(const char *name) : OpDef(name)
    {
        this->Input("x")
            .ParamType(REQUIRED)
            .DataType({ge::DT_INT8, ge::DT_INT8, ge::DT_INT8, ge::DT_INT8, ge::DT_INT8})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
        this->Input("weight")
            .ParamType(REQUIRED)
            .DataType({ge::DT_INT8, ge::DT_INT8, ge::DT_INT8, ge::DT_INT4, ge::DT_INT4})
            .Format({ge::FORMAT_FRACTAL_NZ, ge::FORMAT_FRACTAL_NZ, ge::FORMAT_FRACTAL_NZ, ge::FORMAT_ND,
                     ge::FORMAT_FRACTAL_NZ});
        this->Input("weight_scale")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT, ge::DT_BF16, ge::DT_FLOAT16, ge::DT_UINT64, ge::DT_UINT64})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
        this->Input("x_scale")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT, ge::DT_FLOAT, ge::DT_FLOAT, ge::DT_FLOAT, ge::DT_FLOAT})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
        this->Input("weight_assistance_matrix")
            .ParamType(OPTIONAL)
            .DataType({ge::DT_FLOAT, ge::DT_FLOAT, ge::DT_FLOAT, ge::DT_FLOAT, ge::DT_FLOAT})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
        this->Input("group_list")
            .ParamType(REQUIRED)
            .DataType({ge::DT_INT64, ge::DT_INT64, ge::DT_INT64, ge::DT_INT64, ge::DT_INT64})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
        this->Output("y")
            .ParamType(REQUIRED)
            .DataType({ge::DT_INT8, ge::DT_INT8, ge::DT_INT8, ge::DT_INT8, ge::DT_INT8})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
        this->Output("y_scale")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT, ge::DT_FLOAT, ge::DT_FLOAT, ge::DT_FLOAT, ge::DT_FLOAT})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
        this->Attr("is_enable_weight_assistance_matrix").AttrType(OPTIONAL).Bool(true);
        this->Attr("dequant_mode").AttrType(OPTIONAL).Int(0);
        this->Attr("limited").AttrType(OPTIONAL).Float(0.0f);

        OpAICoreConfig aicore_config;
        aicore_config.DynamicCompileStaticFlag(true)
            .DynamicFormatFlag(true)
            .DynamicRankSupportFlag(true)
            .DynamicShapeSupportFlag(true)
            .NeedCheckSupportFlag(false)
            .PrecisionReduceFlag(true);

        this->AICore().AddConfig("ascend910b", aicore_config);
        this->AICore().AddConfig("ascend910_93", aicore_config);

        OpAICoreConfig config_kirin = GetKirinCoreConfig();
        this->AICore().AddConfig("kirinx90", config_kirin);
        this->AICore().AddConfig("kirin9030", config_kirin);
    }

private:
    OpAICoreConfig GetKirinCoreConfig() const
    {
        OpAICoreConfig config_kirin;
        config_kirin.DynamicCompileStaticFlag(true)
            .DynamicFormatFlag(true)
            .DynamicRankSupportFlag(true)
            .DynamicShapeSupportFlag(true)
            .NeedCheckSupportFlag(false)
            .PrecisionReduceFlag(true);
        config_kirin.Input("x")
            .ParamType(REQUIRED)
            .DataType({ge::DT_INT8, ge::DT_INT8})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND});
        config_kirin.Input("weight")
            .ParamType(REQUIRED)
            .DataType({ge::DT_INT8, ge::DT_INT8})
            .Format({ge::FORMAT_FRACTAL_NZ, ge::FORMAT_FRACTAL_NZ});
        config_kirin.Input("weight_scale")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT, ge::DT_FLOAT16})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND});
        config_kirin.Input("x_scale")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT, ge::DT_FLOAT})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND});
        config_kirin.Input("weight_assistance_matrix")
            .ParamType(OPTIONAL)
            .Dat
// ... (truncated due to length) ...

```

### `csrc/gmm/grouped_matmul_swiglu_quant/op_host/grouped_matmul_swiglu_quant_tiling.h`
```cpp
/**
 * Copyright (c) 2025 Huawei Technologies Co., Ltd.
 * This program is free software, you can redistribute it and/or modify it under the terms and conditions of
 * CANN Open Software License Agreement Version 2.0 (the "License").
 * Please refer to the License for details. You may not use this file except in compliance with the License.
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
 * See LICENSE in the root of the software repository for the full text of the License.
 */

/*!
 * \file grouped_matmul_swiglu_quant_tiling.h
 * \brief
 */
#ifndef AIR_CXX_RUNTIME_V2_OP_IMPL_GROUPED_MATMUL_SWIGLU_QUANT_H
#define AIR_CXX_RUNTIME_V2_OP_IMPL_GROUPED_MATMUL_SWIGLU_QUANT_H

#include <set>
#include "register/tilingdata_base.h"
#include "tiling/tiling_api.h"

namespace optiling {
// GMM 基本信息
BEGIN_TILING_DATA_DEF(GMMSwigluBaseParams)
TILING_DATA_FIELD_DEF(uint32_t, groupNum);
TILING_DATA_FIELD_DEF(uint32_t, coreNum);
TILING_DATA_FIELD_DEF(uint32_t, K);
TILING_DATA_FIELD_DEF(uint32_t, N);
TILING_DATA_FIELD_DEF(uint32_t, M);
TILING_DATA_FIELD_DEF(uint32_t, baseM);
TILING_DATA_FIELD_DEF(uint32_t, baseN);
TILING_DATA_FIELD_DEF(uint32_t, mLimit);
TILING_DATA_FIELD_DEF(uint32_t, workSpaceOffset1);
TILING_DATA_FIELD_DEF(uint32_t, workSpaceOffset2);
TILING_DATA_FIELD_DEF(uint32_t, quantGroupNum);
TILING_DATA_FIELD_DEF(float, limited);
END_TILING_DATA_DEF;
REGISTER_TILING_DATA_CLASS(GMMSwigluBaseParamsOp, GMMSwigluBaseParams)

// SwigluQuant部分tiling 基本信息
BEGIN_TILING_DATA_DEF(GMMSwiglu)
TILING_DATA_FIELD_DEF(uint32_t, maxProcessRowNum);
TILING_DATA_FIELD_DEF(uint32_t, groupListLen);
TILING_DATA_FIELD_DEF(uint32_t, tokenLen);
END_TILING_DATA_DEF;
REGISTER_TILING_DATA_CLASS(GMMSwigluOp, GMMSwiglu)

// 结构体集合
BEGIN_TILING_DATA_DEF(GMMSwigluQuantTilingData)
TILING_DATA_FIELD_DEF_STRUCT(GMMSwigluBaseParams, gmmSwigluBaseParams);
TILING_DATA_FIELD_DEF_STRUCT(GMMSwiglu, gmmSwiglu);
TILING_DATA_FIELD_DEF_STRUCT(TCubeTiling, mmTilingData);
END_TILING_DATA_DEF;

REGISTER_TILING_DATA_CLASS(GroupedMatmulSwigluQuant, GMMSwigluQuantTilingData)
} // namespace optiling

namespace GroupedMatmulSwigluQuantTiling {
constexpr uint32_t X_INDEX = 0;
constexpr uint32_t WEIGHT_INDEX = 1;
constexpr uint32_t WEIGHT_SCALE_INDEX = 2;
constexpr uint32_t GROUPLIST_INDEX = 5;
constexpr uint32_t BATCH_MODE_SCHEDULE = 1;
constexpr uint32_t DIM_0 = 0;
constexpr uint32_t DIM_1 = 1;
constexpr uint32_t DIM_2 = 2;
constexpr uint32_t DIM_3 = 3;
constexpr uint32_t DIM_4 = 4;
constexpr uint32_t NUM_FOUR = 4;
constexpr uint32_t NUM_EIGHT = 8;
constexpr uint32_t SYS_WORKSPACE_SIZE = 16 * 1024 * 1024;
constexpr int64_t USER_WORKSPACE_LIMIT = 64 * 1024 * 1024;
constexpr int64_t DOUBLE_WORKSPACE_SPLIT = 2;
constexpr uint32_t ATTR_INDEX_LIMITED = 2;
constexpr int64_t INT32_DTYPE_SIZE = 4;
constexpr int64_t FP32_DTYPE_SIZE = 4;
constexpr int64_t FP32_BLOCK_SIZE = 8;
constexpr int64_t BLOCK_BYTE = 32;
constexpr int64_t SWIGLU_REDUCE_FACTOR = 2;
constexpr int64_t DOUBLE_BUFFER = 2;
constexpr int64_t ND_WEIGHT_DIM_LIMIT = 3;
constexpr int64_t NZ_WEIGHT_DIM_LIMIT = 5;
constexpr int64_t DOUBLE_ROW = 2;
constexpr int64_t PERCHANNEL_WSCALE_DIM_LIMIT = 2;
constexpr int64_t PERGROUP_WSCALE_DIM_LIMIT = 3;
constexpr int64_t A8W4_MSD_TILING_KEY_MODE = 2;
constexpr int64_t SPLITWORKSPACE_TILING_KEY_MODE = 1;
constexpr int64_t COMMON_TILING_KEY_MODE = 0;
constexpr int64_t A8W4_TOKEN_THRESHOLD = 32;
constexpr int64_t A8W4_BASEM = 128;
constexpr int64_t A8W4_BASEK = 256;
constexpr int64_t A8W4_BASEN = 256;
} // namespace GroupedMatmulSwigluQuantTiling

#endif // AIR_CXX_RUNTIME_V2_OP_IMPL_GROUPED_MATMUL_SWIGLU_QUANT_H
```

### `csrc/gmm/grouped_matmul_swiglu_quant/op_host/grouped_matmul_swiglu_quant_tiling.cpp`
```cpp
/**
 * Copyright (c) 2025 Huawei Technologies Co., Ltd.
 * This program is free software, you can redistribute it and/or modify it under the terms and conditions of
 * CANN Open Software License Agreement Version 2.0 (the "License").
 * Please refer to the License for details. You may not use this file except in compliance with the License.
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
 * See LICENSE in the root of the software repository for the full text of the License.
 */

/*!
 * \file grouped_matmul_swiglu_quant_tiling.cpp
 * \brief
 */
#include <climits>
#include <graph/utils/type_utils.h>
#include "register/op_impl_registry.h"
#include "log/log.h"
#include "err/ops_err.h"
#include "tiling_base/tiling_base.h"
#include "grouped_matmul_swiglu_quant_tiling.h"
using namespace ge;
using namespace AscendC;
using namespace GroupedMatmulSwigluQuantTiling;
using namespace Ops::Transformer::OpTiling;
namespace {
template <typename T>
static inline auto AlignUp(T a, T base) -> T
{
    if (base == 0) {
        return 0;
    }
    return (a + base - 1) / base * base;
}
} // namespace

namespace optiling {

struct GMMSwigluCompileInfo {
    uint64_t ubSize_ = 0;
    uint32_t aicNum_ = 0;
    uint32_t baseM_ = 128;
    uint32_t baseN_ = 256;
};

static int64_t CalMaxRowInUb_A8W4(const gert::TilingContext *context, const uint64_t ubSize, const uint64_t n)
{
    const uint64_t ALIGNMENT = 8;
    const float WEIGHT_FACTOR = 8.5;
    const uint64_t ALIGNMENT_TERM_FACTOR = 4;
    const uint64_t LINEAR_TERM_FACTOR = 6;
    const uint64_t CONSTANT_TERM = 64;
    const uint64_t MIN_ROW_THRESHOLD = 1;

    // 表达式：8.5 * row * n + 4 * alignUp(row, 8) + 6n + 64 <= ubSize

    // 忽略对齐项的初始估计
    int64_t maxRowEstimate =
        (ubSize - CONSTANT_TERM - LINEAR_TERM_FACTOR * n) / static_cast<int64_t>(WEIGHT_FACTOR * n);

    // 考虑对齐影响
    uint64_t alignedRow = (maxRowEstimate + ALIGNMENT - 1) / ALIGNMENT * ALIGNMENT;
    uint64_t totalSize = static_cast<uint64_t>(WEIGHT_FACTOR * maxRowEstimate * n) +
                         ALIGNMENT_TERM_FACTOR * alignedRow + LINEAR_TERM_FACTOR * n + CONSTANT_TERM;

    // 如果超过UB大小，逐步减少row直到满足条件
    while (totalSize > ubSize && maxRowEstimate > 0) {
        maxRowEstimate--;
        alignedRow = (maxRowEstimate + ALIGNMENT - 1) / ALIGNMENT * ALIGNMENT;
        totalSize = static_cast<uint64_t>(WEIGHT_FACTOR * maxRowEstimate * n) + ALIGNMENT_TERM_FACTOR * alignedRow +
                    LINEAR_TERM_FACTOR * n + CONSTANT_TERM;
    }

    if (maxRowEstimate < MIN_ROW_THRESHOLD) {
        OP_LOGE(context->GetNodeName(), "GMM_SWIGLU_QUANT TILING: No valid row found for n = %lu, ubSize = %lu\n", n,
                ubSize);
        return 0;
    }
    return maxRowEstimate;
}

static int64_t CalMaxRowInUb(const gert::TilingContext *context, const uint64_t ubSize, const uint64_t n)
{
    uint64_t tmpBufSize = (n / SWIGLU_REDUCE_FACTOR) * FP32_DTYPE_SIZE;
    uint64_t perchannleBufSize = n * FP32_DTYPE_SIZE * DOUBLE_BUFFER;
    uint64_t reduceMaxResBufSize = BLOCK_BYTE;
    uint64_t reduceMaxTmpBufSize = BLOCK_BYTE;
    const uint64_t CONSTANT_TERM = 64;
    int64_t remainUbSize = ubSize - tmpBufSize - perchannleBufSize - reduceMaxResBufSize - reduceMaxTmpBufSize;
    int64_t maxRowInUb =
        remainUbSize / (n * INT32_DTYPE_SIZE + n / SWIGLU_REDUCE_FACTOR + FP32_DTYPE_SIZE) / DOUBLE_BUFFER;
    int64_t curUb = DOUBLE_BUFFER * (maxRowInUb * (INT32_DTYPE_SIZE * n + n / SWIGLU_REDUCE_FACTOR) +
                                     AlignUp(maxRowInUb, FP32_BLOCK_SIZE) * FP32_DTYPE_SIZE);
    if (curUb > remainUbSize) {
        // 64 : make sure ub does not excceed maxUbSize after align up to 8
        maxRowInUb = (remainUbSize - CONSTANT_TERM) /
                     (n * INT32_DTYPE_SIZE + n / SWIGLU_REDUCE_FACTOR + FP32_DTYPE_SIZE) / DOUBLE_BUFFER;
    }
    if (maxRowInUb < 1) {
        // when n > (ubSize - 72) / 19 = 10330, maxRowInUb < 1
        OP_LOGE(context->GetNodeName(), "GMM_SWIGLU_QUANT TILING: n should not be greater than 10240, now is %lu\n", n);
    }
    return maxRowInUb;
}

static void SetTilingKey(gert::TilingContext *context, bool isSplitWorkSpace, bool isA8W4MSD)
{
    if (isA8W4MSD) { // A8W4 MSD tiling_key使用4
        context->SetTilingKey(A8W4_MSD_TILING_KEY_MODE);
        context->SetScheduleMode(BATCH_MODE_SCHEDULE);
    } else if (isSplitWorkSpace) {
        context->SetTilingKey(SPLITWORKSPACE_TILING_KEY_MODE);
        context->SetScheduleMode(BATCH_MODE_SCHEDULE);
    } else {
        context->SetTilingKey(COMMON_TILING_KEY_MODE);
        context->SetScheduleMode(BATCH_MODE_SCHEDULE);
    }
}

ASCENDC_EXTERN_C graphStatus TilingGMMSwigluQuant(gert::TilingContext *context)
{
    // set info
    OP_LOGD(context->GetNodeName(), "Begin Run GMM Swiglu Tiling .");
    auto xDesc = context->GetInputDesc(X_INDEX);
    
// ... (truncated due to length) ...

```
