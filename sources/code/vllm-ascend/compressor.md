---
id: code-vllm-ascend-compressor
title: vLLM Ascend Attention Compressor Operator
type: source-code
repo: vllm-project/vllm-ascend
path: csrc/attention/compressor
url: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/attention/compressor
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
- attention
- compressor
- inference
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- vector-unit
- unified-buffer
- global-memory
techniques:
- kv-cache-paging
- data-reuse
- pipeline-scheduling
kernel_types:
- attention
- elementwise
languages:
- cpp
- ascendc
---

# vLLM Ascend Attention Compressor Operator

vLLM Ascend compressor custom operator with host and kernel directories, useful as code evidence for attention-side compression and cache preprocessing.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `csrc/attention/compressor`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/attention/compressor


## Fetched Source


### `csrc/attention/compressor/op_host/compressor_proto.cpp`
```cpp
/**
 * Copyright (c) 2026 Huawei Technologies Co., Ltd.
 * This program is free software, you can redistribute it and/or modify it under the terms and conditions of
 * CANN Open Software License Agreement Version 2.0 (the "License").
 * Please refer to the License for details. You may not use this file except in compliance with the License.
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
 * See LICENSE in the root of the software repository for the full text of the License.
 */

#include <graph/utils/type_utils.h>
#include <register/op_impl_registry.h>
#include "log/ops_log.h"

using namespace ge;

namespace ops {
    // INPUT
    constexpr uint32_t TOKEN_X_INPUT_INDEX = 0;
    constexpr uint32_t WEIGHT_KV_INPUT_INDEX = 1;
    constexpr uint32_t WEIGHT_WGATE_INPUT_INDEX = 2;

    constexpr uint32_t STATE_CACHE_INPUT_INDEX = 3;

    constexpr uint32_t APE_INPUT_INDEX = 4;
    constexpr uint32_t NORM_WEIGHT_INPUT_INDEX = 5;
    constexpr uint32_t ROPE_SIN_INPUT_INDEX = 6;
    constexpr uint32_t ROPE_COS_INPUT_INDEX = 7;

    // INPUT(OPTION)
    constexpr uint32_t STATE_BLOCK_TABLE_INPUT_INDEX = 8;

    constexpr uint32_t CU_SEQ_LEN_INPUT_INDEX = 9;
    constexpr uint32_t SEQ_USED_INPUT_INDEX = 10;
    constexpr uint32_t START_POS_INPUT_INDEX = 11;

    // ATTR
    constexpr uint32_t ROPE_HEAD_DIM_ATTR_INDEX = 0;
    constexpr uint32_t CMP_RATIO_ATTR_INDEX = 1;
    constexpr uint32_t COFF_ATTR_INDEX = 2;
    constexpr uint32_t NORM_EPS_ATTR_INDEX = 3;
    constexpr uint32_t ROTARY_MODE_ATTR_INDEX = 4;
    constexpr uint32_t CACHE_MODE_ATTR_INDEX = 5;
    constexpr uint32_t STATE_CACHE_STRIDE_DIM0_ATTR_INDEX = 6;

    // OUTPUT
    constexpr uint32_t CMP_KV_OUTPUT_INDEX = 0;

    // ATTR DEFAULT VALUE
    constexpr uint32_t CMP_RATIO_VALUE = 4;
    constexpr uint32_t COFF_VALUE = 1;

struct CompressorProtoShapeParam {
    bool isBsMerge { false };
    int64_t B { 0 };
    int64_t T { 0 };
    int64_t S { 0 };
    int64_t Sr { 0 };
    int64_t H { 0 };
    int64_t D { 0 };
};

// tmp
constexpr uint32_t DIM_NUM_1 = 1;
constexpr uint32_t DIM_NUM_2 = 2;
constexpr uint32_t DIM_NUM_3 = 3;
constexpr uint32_t DIM_NUM_4 = 4;
constexpr uint32_t DIM_INDEX_0 = 0;
constexpr uint32_t DIM_INDEX_1 = 1;
constexpr uint32_t DIM_INDEX_2 = 2;
constexpr uint32_t DIM_INDEX_3 = 3;

ge::graphStatus GetCompressorShapeDim(const gert::InferShapeContext* context, CompressorProtoShapeParam &shapeParam)
{
    auto xShape = context->GetRequiredInputShape(TOKEN_X_INPUT_INDEX);      // (B, S, H) | (T, H)
    OPS_LOG_E_IF_NULL(context, xShape, return ge::GRAPH_FAILED)
    auto wkvShape = context->GetRequiredInputShape(WEIGHT_KV_INPUT_INDEX);  // (coff * D, H)
    OPS_LOG_E_IF_NULL(context, wkvShape, return ge::GRAPH_FAILED)
    auto wgateShape = context->GetRequiredInputShape(WEIGHT_WGATE_INPUT_INDEX);  // (coff * D, H)
    OPS_LOG_E_IF_NULL(context, wgateShape, return ge::GRAPH_FAILED)

    auto stateCacheShape = context->GetRequiredInputShape(STATE_CACHE_INPUT_INDEX);    // (block_num, block_size, 2 * coff * D) | (B, tokrn_size, 2 * coff * D)
    OPS_LOG_E_IF_NULL(context, stateCacheShape, return ge::GRAPH_FAILED)

    auto apeShape = context->GetRequiredInputShape(APE_INPUT_INDEX);    // (r, coff * D)
    OPS_LOG_E_IF_NULL(context, apeShape, return ge::GRAPH_FAILED)
    auto normWeightShape = context->GetRequiredInputShape(NORM_WEIGHT_INPUT_INDEX);    // (D)
    OPS_LOG_E_IF_NULL(context, normWeightShape, return ge::GRAPH_FAILED)
    auto ropeSinShape = context->GetRequiredInputShape(ROPE_SIN_INPUT_INDEX);    // (B, ceil(S / r), rD) | (min(T, T/r + B), rD)
    OPS_LOG_E_IF_NULL(context, ropeSinShape, return ge::GRAPH_FAILED)
    auto ropeCosShape = context->GetRequiredInputShape(ROPE_COS_INPUT_INDEX);    // (B, ceil(S / r), rD) | (min(T, T/r + B), rD)
    OPS_LOG_E_IF_NULL(context, ropeCosShape, return ge::GRAPH_FAILED)

    auto stateBlockTableShape = context->GetRequiredInputShape(STATE_BLOCK_TABLE_INPUT_INDEX);    // (B, sMax/block_size) | (B, )
    OPS_LOG_E_IF_NULL(context, stateBlockTableShape, return ge::GRAPH_FAILED)

    auto cuSeqlensShape = context->GetRequiredInputShape(CU_SEQ_LEN_INPUT_INDEX);    // (B+1,)
    OPS_LOG_E_IF_NULL(context, cuSeqlensShape, return ge::GRAPH_FAILED)
    auto seqUsedShape = context->GetRequiredInputShape(SEQ_USED_INPUT_INDEX);    // (B,)
    OPS_LOG_E_IF_NULL(context, seqUsedShape, return ge::GRAPH_FAILED)
    auto startPosShape = context->GetRequiredInputShape(START_POS_INPUT_INDEX);    // (B,)
    OPS_LOG_E_IF_NULL(context, startPosShape, return ge::GRAPH_FAILED)

    if (xShape->GetDimNum() == DIM_NUM_3) {                // BS
        shapeParam.isBsMerge = false;
        shapeParam.B = xShape->GetDim(DIM_INDEX_0);
        shapeParam.S = xShape->GetDim(DIM_INDEX_1);
        shapeParam.H = xShape->GetDim(DIM_INDEX_2);
        shapeParam.T
// ... (truncated due to length) ...

```

### `csrc/attention/compressor/op_host/compressor_def.cpp`
```cpp
/**
 * Copyright (c) 2026 Huawei Technologies Co., Ltd.
 * This program is free software, you can redistribute it and/or modify it under the terms and conditions of
 * CANN Open Software License Agreement Version 2.0 (the "License").
 * Please refer to the License for details. You may not use this file except in compliance with the License.
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
 * See LICENSE in the root of the software repository for the full text of the License.
 */

#include "register/op_def_registry.h"

namespace ops {
class Compressor : public OpDef {
public:
    static constexpr uint32_t ROPE_HEAD_DIM_VALUE = 64;
    static constexpr uint32_t CMP_RATIO_VALUE = 4;
    static constexpr uint32_t COFF_VALUE = 1;
    static constexpr uint32_t ROTARY_MODE_VALUE = 1;
    static constexpr uint32_t CACHE_MODE_VALUE = 1;
    static constexpr uint32_t STATE_CACHE_STRIDE_DIM0 = 0;

    explicit Compressor(const char *name) : OpDef(name)
    {
        this->Input("x")
            .ParamType(REQUIRED)
            .DataType({ge::DT_BF16, ge::DT_FLOAT16})
            .FormatList({ge::FORMAT_ND})
            .AutoContiguous();
        this->Input("wkv")
            .ParamType(REQUIRED)
            .DataType({ge::DT_BF16, ge::DT_FLOAT16})
            .FormatList({ge::FORMAT_ND})
            .AutoContiguous();
        this->Input("wgate")
            .ParamType(REQUIRED)
            .DataType({ge::DT_BF16, ge::DT_FLOAT16})
            .FormatList({ge::FORMAT_ND})
            .AutoContiguous();
        this->Input("state_cache")
            .ParamType(REQUIRED)
            .DataTypeList({ge::DT_FLOAT})
            .FormatList({ge::FORMAT_ND})
            .IgnoreContiguous();
        this->Input("ape")
            .ParamType(REQUIRED)
            .DataTypeList({ge::DT_FLOAT})
            .FormatList({ge::FORMAT_ND})
            .AutoContiguous();
        this->Input("norm_weight")
            .ParamType(REQUIRED)
            .DataTypeList({ge::DT_FLOAT})
            .FormatList({ge::FORMAT_ND})
            .AutoContiguous();
        this->Input("rope_sin")
            .ParamType(REQUIRED)
            .DataTypeList({ge::DT_FLOAT})
            .FormatList({ge::FORMAT_ND})
            .AutoContiguous();
        this->Input("rope_cos")
            .ParamType(REQUIRED)
            .DataTypeList({ge::DT_FLOAT})
            .FormatList({ge::FORMAT_ND})
            .AutoContiguous();
        this->Input("state_block_table")
            .ParamType(OPTIONAL)
            .DataTypeList({ge::DT_INT32})
            .FormatList({ge::FORMAT_ND})
            .AutoContiguous();
        this->Input("cu_seqlens")
            .ParamType(OPTIONAL)
            .DataTypeList({ge::DT_INT32})
            .FormatList({ge::FORMAT_ND})
            .AutoContiguous();
        this->Input("seqused")
            .ParamType(OPTIONAL)
            .DataTypeList({ge::DT_INT32})
            .FormatList({ge::FORMAT_ND})
            .AutoContiguous();
        this->Input("start_pos")
            .ParamType(OPTIONAL)
            .DataTypeList({ge::DT_INT32})
            .FormatList({ge::FORMAT_ND})
            .AutoContiguous();
        this->Output("cmp_kv")
            .ParamType(REQUIRED)
            .DataType({ge::DT_BF16, ge::DT_FLOAT16})
            .FormatList({ge::FORMAT_ND});
        this->Output("state_cache")
            .ParamType(REQUIRED)
            .DataTypeList({ge::DT_FLOAT})
            .FormatList({ge::FORMAT_ND});
        this->Attr("rope_head_dim").AttrType(REQUIRED).Int(ROPE_HEAD_DIM_VALUE);
        this->Attr("cmp_ratio").AttrType(REQUIRED).Int(CMP_RATIO_VALUE);
        this->Attr("coff").AttrType(OPTIONAL).Int(COFF_VALUE);
        this->Attr("norm_eps").AttrType(OPTIONAL).Float(1e-6f);
        this->Attr("rotary_mode").AttrType(OPTIONAL).Int(ROTARY_MODE_VALUE);
        this->Attr("cache_mode").AttrType(OPTIONAL).Int(CACHE_MODE_VALUE);
        this->Attr("state_cache_stride_dim0").AttrType(OPTIONAL).Int(STATE_CACHE_STRIDE_DIM0);
        OpAICoreConfig aicore_config;
        aicore_config.DynamicCompileStaticFlag(true)
            .DynamicFormatFlag(true)
            .DynamicRankSupportFlag(true)
            .DynamicShapeSupportFlag(true)
            .NeedCheckSupportFlag(false)
            .PrecisionReduceFlag(true)
            .ExtendCfgInfo("aclnnSupport.value", "support_aclnn");   // set value of aclnn support

        OpAICoreConfig config910;
        config910.Input("x")
            .ParamType(REQUIRED)
            .DataType({ge::DT_BF16, ge::DT_FLOAT16, ge::DT_BF16, ge::DT_FLOAT16})
            .FormatList({ge::FORMAT_ND})
            .AutoContiguous();
        config910.Input("wkv")
            .ParamType(REQUIRED)
            .DataType({ge::DT_BF16, ge::DT_FLOAT16, ge::DT_BF16, ge::DT_FLOAT16})
            .FormatList({ge::FORMAT_ND})
            .AutoContigu
// ... (truncated due to length) ...

```

### `csrc/attention/compressor/op_host/arch35/compressor_tiling.h`
```cpp
/**
 * Copyright (c) 2026 Huawei Technologies Co., Ltd.
 * This program is free software, you can redistribute it and/or modify it under the terms and conditions of
 * CANN Open Software License Agreement Version 2.0 (the "License").
 * Please refer to the License for details. You may not use this file except in compliance with the License.
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
 * See LICENSE in the root of the software repository for the full text of the License.
 */

/*!
 * \file compressor_tiling.h
 * \brief
 */

#ifndef COMPRESSOR_TILING_H
#define COMPRESSOR_TILING_H

#include <cstdint>
#include <string>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <sstream>
#include "register/tilingdata_base.h"
#include "tiling/tiling_api.h"
#include "exe_graph/runtime/tiling_context.h"
#include "register/op_def_registry.h"
#include "../../op_kernel/arch35/compressor_template_tiling_key.h"
#include "../../op_kernel/arch35/compressor_tiling_data.h"
#include "platform/platform_info.h"

#ifdef ASCENDC_OP_TEST
#define CMP_EXTERN_C extern "C"
#else
#define CMP_EXTERN_C
#endif

namespace optiling {

// INPUT
constexpr uint32_t TOKEN_X_INPUT_INDEX = 0;
constexpr uint32_t WEIGHT_KV_INPUT_INDEX = 1;
constexpr uint32_t WEIGHT_WGATE_INPUT_INDEX = 2;
constexpr uint32_t STATE_CACHE_INPUT_INDEX = 3;
constexpr uint32_t APE_INPUT_INDEX = 4;
constexpr uint32_t NORM_WEIGHT_INPUT_INDEX = 5;
constexpr uint32_t ROPE_SIN_INPUT_INDEX = 6;
constexpr uint32_t ROPE_COS_INPUT_INDEX = 7;

// INPUT(OPTION)
constexpr uint32_t STATE_BLOCK_TABLE_INPUT_INDEX = 8;
constexpr uint32_t CU_SEQ_LEN_INPUT_INDEX = 9;
constexpr uint32_t SEQ_USED_INPUT_INDEX = 10;
constexpr uint32_t START_POS_INPUT_INDEX = 11;

// ATTR
constexpr uint32_t ROPE_HEAD_DIM_ATTR_INDEX = 0;
constexpr uint32_t CMP_RATIO_ATTR_INDEX = 1;
constexpr uint32_t COFF_ATTR_INDEX = 2;
constexpr uint32_t NORM_EPS_ATTR_INDEX = 3;
constexpr uint32_t ROTARY_MODE_ATTR_INDEX = 4;
constexpr uint32_t CACHE_MODE_ATTR_INDEX = 5;
constexpr uint32_t STATE_CACHE_STRIDE_DIM0_ATTR_INDEX = 6;

// OUTPUT
constexpr uint32_t CMP_KV_OUTPUT_INDEX = 0;

constexpr uint32_t COMPRESSOR_DIM_NUM_1 = 1;
constexpr uint32_t COMPRESSOR_DIM_NUM_2 = 2;
constexpr uint32_t COMPRESSOR_DIM_NUM_3 = 3;
constexpr uint32_t COMPRESSOR_DIM_NUM_4 = 4;
constexpr uint32_t COMPRESSOR_DIM_INDEX_0 = 0;
constexpr uint32_t COMPRESSOR_DIM_INDEX_1 = 1;
constexpr uint32_t COMPRESSOR_DIM_INDEX_2 = 2;
constexpr uint32_t COMPRESSOR_DIM_INDEX_3 = 3;

// CONSTRAINTS
constexpr uint32_t MAX_HIDDEN_SIZE = 10240;
constexpr uint32_t MIN_HIDDEN_SIZE = 1024;
constexpr uint32_t ALIGN_FACTOR_HIDDEN_SIZE = 512;
constexpr uint32_t MIN_BLOCK_SIZE = 1;

constexpr uint32_t BATCH_MODE_SCHEDULE = 1;

static const std::string X_NAME = "query";
static const std::string WKV_NAME = "wkv";
static const std::string WGATE_NAME = "wgate";
static const std::string STATE_CACHE_NAME = "state_cache";
static const std::string APE_NAME = "ape";
static const std::string NORM_WEIGHT_NAME = "norm_weight";
static const std::string ROPE_SIN_NAME = "rope_sin";
static const std::string ROPE_COS_NAME = "rope_cos";
static const std::string STATE_BLOCK_TABLE_NAME = "state_block_table";
static const std::string CU_SEQLENS_NAME = "cu_seqlens";
static const std::string SEQUSED_NAME = "seq_used";
static const std::string START_POS_NAME = "start_pos";
static const std::string ROPE_HEAD_DIM_NAME = "rope_head_dim";
static const std::string CMP_RATIO_NAME = "cmp_ratio";
static const std::string COFF_NAME = "coff";
static const std::string NORM_EPS_NAME = "nrom_eps";
static const std::string ROTARY_MODE_NAME = "rotary_mode";
static const std::string CACHE_MODE_NAME = "cache_mode";
static const std::string CMP_KV_NAME = "cmp_kv";

static std::string DataTypeToSerialString(ge::DataType type);

const std::map<std::string, std::vector<ge::DataType>> DTYPE_SUPPORT_MAP = {
    {X_NAME,                  {ge::DT_BF16, ge::DT_FLOAT16}},
    {WKV_NAME,                {ge::DT_BF16, ge::DT_FLOAT16}},
    {WGATE_NAME,              {ge::DT_BF16, ge::DT_FLOAT16}},
    {STATE_CACHE_NAME,        {ge::DT_FLOAT}},
    {APE_NAME,                {ge::DT_FLOAT}},
    {NORM_WEIGHT_NAME,        {ge::DT_FLOAT}},
    {ROPE_SIN_NAME,           {ge::DT_FLOAT}},
    {ROPE_COS_NAME,           {ge::DT_FLOAT}},
    {STATE_BLOCK_TABLE_NAME,  {ge::DT_INT32}},
    {CU_SEQLENS_NAME,         {ge::DT_INT32}},
    {SEQUSED_NAME,            {ge::DT_INT32}},
    {START_POS_NAME,          {ge::DT_INT32}},
    {CMP_KV_NAME,             {ge::DT_BF16, ge::DT_FLOAT16}}
};

const std::map<std::string, std::vector<uint32_t>> DIM_NUM_MAP = {
    {X_NAME,                  {COMPRESSOR_DIM_NUM_2, COMPRESSOR_DIM_NUM_3}},
    {WKV_NAME,                {COMPRESSOR_DIM_NUM_2}},
    {WGATE_NAME,              {COMPRESSOR_DIM_NUM_2}},
    {STATE_CACHE
// ... (truncated due to length) ...

```
