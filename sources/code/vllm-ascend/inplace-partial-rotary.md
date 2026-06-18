---
id: code-vllm-ascend-inplace-partial-rotary
title: vLLM Ascend In-place Partial Rotary Operator
type: source-code
repo: vllm-project/vllm-ascend
path: csrc/attention/inplace_partial_rotary_mul
url: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/attention/inplace_partial_rotary_mul
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
- rope
- attention
- inference
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- vector-unit
- unified-buffer
- global-memory
techniques:
- data-reuse
- pipeline-scheduling
kernel_types:
- rope
- attention
- elementwise
languages:
- cpp
- ascendc
---

# vLLM Ascend In-place Partial Rotary Operator

vLLM Ascend rotary-position operator used as code evidence for in-place vector transformations on query/key tensors during inference.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `csrc/attention/inplace_partial_rotary_mul`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/attention/inplace_partial_rotary_mul


## Fetched Source


### `csrc/attention/inplace_partial_rotary_mul/op_host/inplace_partial_rotary_mul_def.cpp`
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
 * \file inplace_partial_rotary_mul_def.cpp
 * \brief
 */
#include "register/op_def_registry.h"

namespace ops {
class InplacePartialRotaryMul : public OpDef {
public:
    explicit InplacePartialRotaryMul(const char *name) : OpDef(name)
    {
        this->Input("x")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_BF16, ge::DT_FLOAT16, ge::DT_BF16})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND})
            .UnknownShapeFormat({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND})
            .AutoContiguous();
        this->Input("cos")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_BF16, ge::DT_FLOAT, ge::DT_FLOAT})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND})
            .UnknownShapeFormat({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND})
            .AutoContiguous();
        this->Input("sin")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_BF16, ge::DT_FLOAT, ge::DT_FLOAT})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND})
            .UnknownShapeFormat({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND})
            .AutoContiguous();
        this->Output("x")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_BF16, ge::DT_FLOAT16, ge::DT_BF16})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND})
            .UnknownShapeFormat({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
        this->Attr("mode").AttrType(OPTIONAL).Int(0);
        this->Attr("partial_slice").AttrType(OPTIONAL).ListInt({0, 0});

        this->AICore().AddConfig("ascend910b");
        this->AICore().AddConfig("ascend910_93");

        OpAICoreConfig config950;
        config950.Input("x")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_BF16, ge::DT_FLOAT16, ge::DT_BF16})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND})
            .UnknownShapeFormat({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND})
            .AutoContiguous();
        config950.Input("cos")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_BF16, ge::DT_FLOAT, ge::DT_FLOAT})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND})
            .UnknownShapeFormat({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND})
            .AutoContiguous();
        config950.Input("sin")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_BF16, ge::DT_FLOAT, ge::DT_FLOAT})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND})
            .UnknownShapeFormat({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND})
            .AutoContiguous();
        config950.Output("x")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_BF16, ge::DT_FLOAT16, ge::DT_BF16})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND})
            .UnknownShapeFormat({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
        config950.DynamicCompileStaticFlag(true)
            .DynamicRankSupportFlag(true)
            .DynamicShapeSupportFlag(true)
            .ExtendCfgInfo("opFile.value", "inplace_partial_rotary_mul");
        this->AICore().AddConfig("ascend950", config950);
    }
};

OP_ADD(InplacePartialRotaryMul);
}  // namespace ops
```

### `csrc/attention/inplace_partial_rotary_mul/op_host/inplace_partial_rotary_mul_tiling.cpp`
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
 * \file rotary_position_embedding.cc
 * \brief
 */
#include "inplace_partial_rotary_mul_tiling.h"
#include "register/op_def_registry.h"
// #include "log/log.h"
#include "tiling/tiling_api.h"
// #include "tiling_base/tiling_templates_registry.h"
#include <vector>
namespace optiling {
constexpr uint32_t MODE_ATTR_IDX = 0;

ge::graphStatus RotaryPosEmbeddingMembaseTilingClass::GetPlatformInfo()
{
    auto platformInfo = context_->GetPlatformInfo();
    if (platformInfo != nullptr) {
        auto ascendcPlatform = platform_ascendc::PlatformAscendC(platformInfo);
        aicoreParams_.blockDim = ascendcPlatform.GetCoreNumAiv();
        uint64_t ubSizePlatForm;
        ascendcPlatform.GetCoreMemSize(platform_ascendc::CoreMemType::UB, ubSizePlatForm);
        socVersion_ = ascendcPlatform.GetSocVersion();
        aicoreParams_.ubSize = ubSizePlatForm;
    } else {
        auto compileInfoPtr = reinterpret_cast<const RotaryPositionEmbeddingCompileInfo *>(context_->GetCompileInfo());
        OPS_ERR_IF(compileInfoPtr == nullptr, OPS_LOG_E(context_, "compile info is null"), return ge::GRAPH_FAILED);
        aicoreParams_.ubSize = compileInfoPtr->ubSize;
        aicoreParams_.blockDim = compileInfoPtr->blockDim;
        socVersion_ = compileInfoPtr->socVersion;
    }
    return ge::GRAPH_SUCCESS;
}

ge::graphStatus RotaryPosEmbeddingMembaseTilingClass::GetShapeAttrsInfo()
{
    auto attrs = context_->GetAttrs();
    OPS_LOG_E_IF_NULL(context_, attrs, return ge::GRAPH_FAILED);
    const uint32_t inputMode = *(attrs->GetAttrPointer<uint32_t>(MODE_ATTR_IDX));
    OPS_LOG_I(context_->GetNodeName(), "[mode]: %d", inputMode);
    inputMode_ = inputMode;
    return ge::GRAPH_SUCCESS;
}

ge::graphStatus Tiling4RotaryPositionEmbedding(gert::TilingContext *context)
{
    OPS_LOG_I(context, "Tiling4RotaryPositionEmbedding start");
    OPS_ERR_IF(context == nullptr, OPS_REPORT_VECTOR_INNER_ERR("Tiling4RotaryPositionEmbedding", "Tiling context is null"),
               return ge::GRAPH_FAILED);

    auto platformInfo = context->GetPlatformInfo();
    OPS_ERR_IF(platformInfo == nullptr, OPS_REPORT_VECTOR_INNER_ERR("Tiling4RotaryPositionEmbedding", "Tiling platformInfo is null"),
               return ge::GRAPH_FAILED);
    auto ascendcPlatform = platform_ascendc::PlatformAscendC(platformInfo);
    auto socVersion = ascendcPlatform.GetSocVersion();
    auto xDesc = context->GetInputDesc(0);
    auto cosDesc = context->GetInputDesc(1);
    auto sinDesc = context->GetInputDesc(2);
    OPS_ERR_IF(xDesc == nullptr || cosDesc == nullptr || sinDesc == nullptr,
               OPS_REPORT_VECTOR_INNER_ERR("Tiling4RotaryPositionEmbedding", "input desc is null"),
               return ge::GRAPH_FAILED);
    bool useFp32Rope = xDesc->GetDataType() != ge::DT_FLOAT &&
                       cosDesc->GetDataType() == ge::DT_FLOAT &&
                       sinDesc->GetDataType() == ge::DT_FLOAT;
    bool supportFp32Rope = socVersion == platform_ascendc::SocVersion::ASCEND910B ||
                           socVersion == platform_ascendc::SocVersion::ASCEND910_93;
    if (useFp32Rope && supportFp32Rope) {
        return Tiling4InplacePartialRotaryMul(context);
    }
    if (socVersion == platform_ascendc::SocVersion::ASCEND950)
    {
        std::vector<std::unique_ptr<RopeRegBaseTilingClass>> regBaseTilingCases;
        regBaseTilingCases.push_back(std::unique_ptr<RopeRegBaseTilingClass>(new RopeRegBaseTilingClassAAndB(context)));
        regBaseTilingCases.push_back(std::unique_ptr<RopeRegBaseTilingClass>(new RopeRegBaseTilingClassAB(context)));
        regBaseTilingCases.push_back(std::unique_ptr<RopeRegBaseTilingClass>(new RopeRegBaseTilingClassABAAndBA(context)));
        regBaseTilingCases.push_back(std::unique_ptr<RopeRegBaseTilingClass>(new RopeRegBaseTilingClassBAB(context)));
        OPS_LOG_I(context, "Using arch35 tiling for ASCEND950");

        for (const auto& ptr : regBaseTilingCases)
        {
            if (ptr)
            {
                ge::graphStatus status = ptr->DoTiling();
                if (status != ge::GRAPH_PARAM_INVALID)
                {
                    OPS_LOG_I(context, "Do general op tiling success priority");
                    return status;
                }
                OPS_LOG_I(context, "Ignore general op tiling priority");
            }
        }
        O
// ... (truncated due to length) ...

```

### `csrc/attention/inplace_partial_rotary_mul/op_host/inplace_partial_rotary_mul_a3_tiling.cpp`
```cpp
/**
 * Copyright (c) Huawei Technologies Co., Ltd. 2025. All rights reserved.
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

/*!
 * \file inplace_partial_rotary_mul_tiling.cpp
 * \brief
 */

#include "inplace_partial_rotary_mul_tiling.h"

namespace optiling {
constexpr int64_t TILING_KEY_FLOAT16 = 0;
constexpr int64_t TILING_KEY_BFLOAT16 = 10;
constexpr int64_t TILING_KEY_FLOAT32 = 20;
constexpr int64_t TILING_KEY_UNPAD = 0;
constexpr int64_t TILING_KEY_PAD = 1;
constexpr int64_t TILING_KEY_SPLIT_S = 0;
constexpr int64_t TILING_KEY_SPLIT_BS = 100;
constexpr int64_t TILING_KEY_SPLIT_BSN = 200;
constexpr int64_t FP16_BF16_DTYPE_SIZE = 2;
constexpr int64_t FP32_DTYPE_SIZE = 4;
constexpr int64_t INT32_DTYPE_SIZE = 4;
constexpr int64_t REPEAT_FP32 = 64;
constexpr int64_t TBUF_SIZE = 0;
constexpr int64_t ALIGN_32 = 8;
constexpr int64_t ALIGN_16 = 16;
constexpr int64_t IO_NUM = 3; // sin、cos -> tri
constexpr int64_t BASE_KEY = 2000;
constexpr int64_t CONST_4 = 4;

class InplacePartialRotaryMulTiling
{
public:
    explicit InplacePartialRotaryMulTiling(gert::TilingContext* context) : context_(context){};

    ge::graphStatus Init();
    ge::graphStatus DoTiling();

private:
    ge::graphStatus CheckInput();
    ge::graphStatus CalTilingData();
    ge::graphStatus TilingSplitN(int64_t numHeads, int64_t headDimAlign, int64_t ubSize,
                                 ge::DataType dataDtype);
    ge::graphStatus TilingSplitB(int64_t batchSize, int64_t numHeads, int64_t headDimAlign,
                                 int64_t ubSize, ge::DataType dataDtype);
    ge::graphStatus TilingSplitS();
    ge::graphStatus TilingSplit();
    void FillTilingData();
    void PrintTilingData() const;
    void PrintInfo();

private:
    int64_t coreNum_ = 0;
    int64_t ubSize_=0;
    int64_t dtypeX = 0;
    int64_t repeatNum_ = 0;
    bool isBrc_ = true;
    int64_t dim0_ = 0;
    int64_t dim1_ = 0;
    int64_t dim2_ = 0;
    int64_t end_ =0;
    int64_t tilingKey_ =1;
    bool isAlign_ = false;
    bool isSpecial_ = false;
    bool isFp32Rope_ = false;
    int64_t oneBlockSize_ = 0;
    int64_t dtypeSize_ = 2;
    int64_t xdim0_ = 0;
    int64_t xdim1_ = 0;
    int64_t xdim2_ = 0;
    int64_t xdim3_ = 0;
    int64_t r1dim0_ = 0;
    int64_t r1dim1_ = 0;
    int64_t r1dim2_ = 0;
    int64_t r1dim3_ = 0;

    // tiingdata
    int64_t usedCoreNum_ = 0;
    int64_t numHead_ = 0;
    int64_t headDim_ = 0;
    int64_t allHeadDim_ = 0;
    int64_t coreTUbLoopTime_ = 0;
    int64_t coreBUbLoopTime_ = 0;
    int64_t coreTUbLoopTail_ = 0;
    int64_t coreBUbLoopTail_ = 0;
    int64_t ubFactor_ = 0;
    int64_t start_=0;
    int64_t blockFactor_=0;
    gert::TilingContext* context_ = nullptr;
    RopeRegbaseTilingData tilingData_;
};
int64_t GetCeilInt(int64_t value1, int64_t value2)
{
    if (value2 == 0)
        return value2;
    return (value1 + value2 - 1) / value2;
}

int64_t GetDiv(int64_t value1, int64_t value2)
{
    if (value2 == 0)
        return value2;
    return value1 / value2;
}

int64_t GetDivRem(int64_t value1, int64_t value2)
{
    if (value2 == 0)
        return value2;
    return value1 % value2;
}
void InplacePartialRotaryMulTiling::FillTilingData()
{
    tilingData_.set_usedCoreNum(usedCoreNum_);
    tilingData_.set_numHead(numHead_);
    tilingData_.set_headDim(headDim_);
    tilingData_.set_allHeadDim(allHeadDim_);
    tilingData_.set_coreTUbLoopTime(coreTUbLoopTime_);
    tilingData_.set_coreBUbLoopTime(coreBUbLoopTime_);
    tilingData_.set_coreTUbLoopTail(coreTUbLoopTail_);
    tilingData_.set_coreBUbLoopTail(coreBUbLoopTail_);
    tilingData_.set_ubFactor(ubFactor_);
    tilingData_.set_start(start_);
    tilingData_.set_blockFactor(blockFactor_);
}
void InplacePartialRotaryMulTiling::PrintTilingData() const
{
    OPS_LOG_I(context_->GetNodeName(), "InplacePartialRotaryMulTiling  begin print.");
    OPS_LOG_I(context_->GetNodeName(), "usedCoreNum = %ld.", usedCoreNum_);
    OPS_LOG_I(context_->GetNodeName(), "numHead_ = %ld.", numHead_);
    OPS_LOG_I(context_->GetNodeName(), "headDim_ = %ld.", headDim_);
    OPS_LOG_I(context_->GetNodeName(), "allHeadDim_ = %ld.", allHeadDim_);
    OPS_LOG_I(context_->GetNodeName(), "coreTUbLoopTime_ = %ld.", coreTUbLoopTime_);
    OPS_LOG_I(context_->GetNodeName(), "coreBUbLoopTime_ = %ld.", coreBUbLoopTime_);
    OPS_LOG_I(context_->GetNodeName(), "coreTUbLoopTail_ = %ld.", coreTUbLoopTail_);
    OPS_LOG_I(context_->GetNodeName(), "coreBUbLoopTail_ = %ld.", coreBUbLoopTail_);
  
// ... (truncated due to length) ...

```
