---
id: code-vllm-ascend-sparse-flash-attention
title: vLLM Ascend Sparse Flash Attention Operator
type: source-code
repo: vllm-project/vllm-ascend
path: csrc/attention/sparse_flash_attention
url: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/attention/sparse_flash_attention
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
- sparse-attention
- flash-attention
- inference
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- unified-buffer
- global-memory
techniques:
- online-softmax
- kv-cache-paging
- pipeline-scheduling
kernel_types:
- attention
- flash-attention
- paged-attention
languages:
- cpp
- ascendc
---

# vLLM Ascend Sparse Flash Attention Operator

vLLM Ascend sparse FlashAttention source directory with host/kernel code and examples, useful for mining sparse attention scheduling and softmax patterns.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `csrc/attention/sparse_flash_attention`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/attention/sparse_flash_attention


## Fetched Source


### `csrc/attention/sparse_flash_attention/sparse_flash_attention_torch_adpt.h`
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
#ifndef SPARSE_FLASH_ATTENTION_TORCH_ADPT_H
#define SPARSE_FLASH_ATTENTION_TORCH_ADPT_H

namespace vllm_ascend {

namespace {

std::tuple<at::Tensor, at::Tensor, at::Tensor> construct_sparse_flash_attention_output_tensor(
    const at::Tensor &query, const at::Tensor &key,
    const std::string &layout_query_str, bool return_softmax_lse)
{
    constexpr int64_t SIZE = 8;
    constexpr int64_t DIM_0 = 0;
    constexpr int64_t DIM_1 = 1;
    constexpr int64_t DIM_2 = 2;
    constexpr int64_t DIM_3 = 3;
    constexpr int64_t DIM_4 = 4;

    TORCH_CHECK(layout_query_str == "BSND" || layout_query_str == "TND",
                "The layout of query only support BSND and TND, but got ",
                layout_query_str);
    for (size_t i = 0; i < query.sizes().size(); i++) {
        TORCH_CHECK(query.size(i) > 0,
                    "All values within query's shape should be greater "
                    "than 0, but shape[",
                    i, "] is ", query.size(i));
    }

    at::SmallVector<int64_t, SIZE> output_size;
    if (layout_query_str == "TND") {
        TORCH_CHECK(query.dim() == DIM_3,
                    "When the layout of query is TND, the query dimension must be 3, but got ",
                    query.dim());
        output_size = {query.size(DIM_0), query.size(DIM_1),
                       query.size(DIM_2)};
    } else {
        TORCH_CHECK(query.dim() == DIM_4,
                    "When the layout of query is BSND, the query dimension must be 4, but got ",
                    query.dim());
        output_size = {query.size(DIM_0), query.size(DIM_1),
                       query.size(DIM_2), query.size(DIM_3)};
    }

    at::Tensor attention_output =
        at::empty(output_size, query.options().dtype(query.dtype()));
    at::SmallVector<int64_t, SIZE> softmax_size;
    if (return_softmax_lse) {
        if (query.dim() == DIM_3) {
            softmax_size = {key.size(DIM_1), query.size(DIM_0),
                            query.size(DIM_1) / key.size(DIM_1)};
        } else {
            softmax_size = {query.size(DIM_0), key.size(DIM_2),
                            query.size(DIM_1),
                            query.size(DIM_2) / key.size(DIM_2)};
        }
    } else {
        softmax_size = {0};
    }

    at::Tensor softmax_max =
        at::empty(softmax_size, query.options().dtype(at::kFloat));
    at::Tensor softmax_sum =
        at::empty(softmax_size, query.options().dtype(at::kFloat));
    return std::tuple<at::Tensor, at::Tensor, at::Tensor>(
        attention_output, softmax_max, softmax_sum);
}

}  // namespace

std::tuple<at::Tensor, at::Tensor, at::Tensor> npu_sparse_flash_attention(
    const at::Tensor &query, const at::Tensor &key, const at::Tensor &value,
    const at::Tensor &sparse_indices, double scale_value,
    const c10::optional<at::Tensor> &block_table,
    const c10::optional<at::Tensor> &actual_seq_lengths_query,
    const c10::optional<at::Tensor> &actual_seq_lengths_kv,
    const c10::optional<at::Tensor> &query_rope,
    const c10::optional<at::Tensor> &key_rope, int64_t sparse_block_size,
    c10::string_view layout_query, c10::string_view layout_kv,
    int64_t sparse_mode, int64_t pre_tokens, int64_t next_tokens,
    int64_t attention_mode, bool return_softmax_lse)
{
    TORCH_CHECK(query.numel() > 0, "Tensor query is empty.");
    TORCH_CHECK(key.numel() > 0, "Tensor key is empty.");
    TORCH_CHECK(value.numel() > 0, "Tensor value is empty.");
    TORCH_CHECK(sparse_indices.numel() > 0, "Tensor sparse_indices is empty.");

    std::string layout_query_str = std::string(layout_query);
    std::string layout_kv_str = std::string(layout_kv);

    auto sparse_flash_attention_output =
        construct_sparse_flash_attention_output_tensor(
            query, key, layout_query_str, return_softmax_lse);
    at::Tensor attention_output = std::get<0>(sparse_flash_attention_output);
    at::Tensor softmax_max = std::get<1>(sparse_flash_attention_output);
    at::Tensor softmax_sum = std::get<2>(sparse_flash_attention_output);

    // convert str
    char *layout_query_ptr = const_cast<char *>(layout_query_str.c_str());
    char *layout_kv_ptr = const_cast<char *>(layout_kv_str.c_str());

    EXEC_NPU_CMD(
        aclnnSparseFlashAttention,
        query,
        key,
        value,
        sparse_indices,
        block_table,
        act
// ... (truncated due to length) ...

```

### `csrc/attention/sparse_flash_attention/op_host/sparse_flash_attention_infershape.cpp`
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
 * \file sparse_flash_attention_proto.cpp
 * \brief
 */

#include <graph/utils/type_utils.h>
#include <register/op_impl_registry.h>
#include "err/ops_err.h"

using namespace ge;

namespace ops {
constexpr size_t QUERY_INPUT_INDEX = 0;
constexpr size_t KEY_INPUT_INDEX = 1;

constexpr uint32_t DIM_NUM_1 = 1;
constexpr uint32_t DIM_NUM_3 = 3;
constexpr uint32_t DIM_NUM_4 = 4;
constexpr uint32_t DIM_INDEX_0 = 0;
constexpr uint32_t DIM_INDEX_1 = 1;
constexpr uint32_t DIM_INDEX_2 = 2;
constexpr uint32_t DIM_INDEX_3 = 3;
constexpr uint32_t LAYOUT_KEY_ATTR_INDEX = 3;
constexpr uint32_t RETURN_SOFTMAX_LSE_INDEX = 8;

constexpr uint32_t OUTPUT_INDEX_0 = 0;
constexpr uint32_t OUTPUT_INDEX_1 = 1;
constexpr uint32_t OUTPUT_INDEX_2 = 2;

ge::graphStatus InferShapeSparseFlashAttention(gert::InferShapeContext *context)
{  
    OP_CHECK_IF(context == nullptr, OP_LOGE("SparseFlashAttention", "InferShapeContext is nullptr"),
               return ge::GRAPH_FAILED);
    const gert::Shape *queryShape = context->GetInputShape(QUERY_INPUT_INDEX);
    OP_CHECK_NULL_WITH_CONTEXT(context, queryShape);

    const gert::Shape *keyShape = context->GetInputShape(KEY_INPUT_INDEX);
    OP_CHECK_NULL_WITH_CONTEXT(context, keyShape);
    
    gert::Shape *attentionOutShape = context->GetOutputShape(0);
    OP_CHECK_NULL_WITH_CONTEXT(context, attentionOutShape);
    *attentionOutShape = *queryShape;

    gert::Shape *softmaxMaxShape = context->GetOutputShape(1);
    OP_CHECK_NULL_WITH_CONTEXT(context, softmaxMaxShape);

    gert::Shape *softmaxSumShape = context->GetOutputShape(2);
    OP_CHECK_NULL_WITH_CONTEXT(context, softmaxSumShape);
    
    auto attrs = context->GetAttrs();
    OP_CHECK_NULL_WITH_CONTEXT(context, attrs);
    const char *inputLayoutKeyPtr = attrs->GetAttrPointer<char>(LAYOUT_KEY_ATTR_INDEX);
    OP_CHECK_NULL_WITH_CONTEXT(context, inputLayoutKeyPtr);
    std::string inputLayoutKeyPtrStr = std::string(inputLayoutKeyPtr);
    const bool *lse_flag = attrs->GetAttrPointer<bool>(RETURN_SOFTMAX_LSE_INDEX);
    OP_CHECK_NULL_WITH_CONTEXT(context, lse_flag);
    bool return_softmax_lse = (lse_flag != nullptr)? *lse_flag : false;

    if(return_softmax_lse){
        if(queryShape->GetDimNum() == DIM_NUM_3){
            if (inputLayoutKeyPtrStr == "PA_BSND") {
                softmaxMaxShape->SetDimNum(DIM_NUM_3);
                softmaxMaxShape->SetDim(DIM_INDEX_0, keyShape->GetDim(DIM_INDEX_2));
                softmaxMaxShape->SetDim(DIM_INDEX_1, queryShape->GetDim(DIM_INDEX_0));
                softmaxMaxShape->SetDim(DIM_INDEX_2, queryShape->GetDim(DIM_INDEX_1) / keyShape->GetDim(DIM_INDEX_2));

                softmaxSumShape->SetDimNum(DIM_NUM_3);
                softmaxSumShape->SetDim(DIM_INDEX_0, keyShape->GetDim(DIM_INDEX_2));
                softmaxSumShape->SetDim(DIM_INDEX_1, queryShape->GetDim(DIM_INDEX_0));
                softmaxSumShape->SetDim(DIM_INDEX_2, queryShape->GetDim(DIM_INDEX_1) / keyShape->GetDim(DIM_INDEX_2));
            } else {
                softmaxMaxShape->SetDimNum(DIM_NUM_3);
                softmaxMaxShape->SetDim(DIM_INDEX_0, keyShape->GetDim(DIM_INDEX_1));
                softmaxMaxShape->SetDim(DIM_INDEX_1, queryShape->GetDim(DIM_INDEX_0));
                softmaxMaxShape->SetDim(DIM_INDEX_2, queryShape->GetDim(DIM_INDEX_1) / keyShape->GetDim(DIM_INDEX_1));

                softmaxSumShape->SetDimNum(DIM_NUM_3);
                softmaxSumShape->SetDim(DIM_INDEX_0, keyShape->GetDim(DIM_INDEX_1));
                softmaxSumShape->SetDim(DIM_INDEX_1, queryShape->GetDim(DIM_INDEX_0));
                softmaxSumShape->SetDim(DIM_INDEX_2, queryShape->GetDim(DIM_INDEX_1) / keyShape->GetDim(DIM_INDEX_1));
            }
        } else {
            softmaxMaxShape->SetDimNum(DIM_NUM_4);
            softmaxMaxShape->SetDim(DIM_INDEX_0, queryShape->GetDim(DIM_INDEX_0));
            softmaxMaxShape->SetDim(DIM_INDEX_1, keyShape->GetDim(DIM_INDEX_2));
            softmaxMaxShape->SetDim(DIM_INDEX_2, queryShape->GetDim(DIM_INDEX_1));
            softmaxMaxShape->SetDim(DIM_INDEX_3, queryShape->GetDim(DIM_INDEX_2) / keyShape->GetDim(DIM_INDEX_2));

            softmaxSumShape->SetDimNum(DIM_NUM_4);
            softmaxSumShape->SetDim(DIM_INDEX_0, queryShape->GetDim(DIM_INDEX_0));
            softmaxSumShape->SetDim(DIM_INDEX_1, keyShape->GetDim(DIM_INDEX_2));
 
// ... (truncated due to length) ...

```

### `csrc/attention/sparse_flash_attention/op_host/sparse_flash_attention_tiling.cpp`
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
 * \file sparse_flash_attention_tiling.cpp
 * \brief
 */

#include <map>
#include <vector>
#include <numeric>
#include <algorithm>
#include <graph/utils/type_utils.h>
#include "err/ops_err.h"
#include "register/op_def_registry.h"
#include "../op_kernel/sparse_flash_attention_template_tiling_key.h"
#include "sparse_flash_attention_tiling.h"

using std::map;
using std::string;
using std::pair;

using namespace ge;
using namespace AscendC;
namespace optiling {

constexpr uint32_t PRE_LOAD_NUM = 2;
constexpr uint32_t BLOCK_TABLE_ELEM_BYTE = 4;
constexpr int32_t SPARSE_MODE_BAND = 4;

static const std::string QUERY_NAME = "query";
static const std::string KEY_NAME = "key";
static const std::string VALUE_NAME = "value";
static const std::string BLOCK_TABLE_NAME = "block_table";
static const std::string SPARSE_INDICES_NAME = "sparse_indices";
static const std::string QUERY_ROPE_NAME = "query_rope";
static const std::string KEY_ROPE_NAME = "key_rope";
static const std::string ATTEN_OUT_NAME = "attention_out";
static const std::string SOFTMAX_MAX_NAME = "softmax_max";
static const std::string SOFTMAX_SUM_NAME = "softmax_sum";

const std::map<std::string, std::vector<ge::DataType>> DTYPE_SUPPORT_MAP = {
    {QUERY_NAME,                  {ge::DT_FLOAT16, ge::DT_BF16}},
    {KEY_NAME,                    {ge::DT_FLOAT16, ge::DT_BF16}},
    {VALUE_NAME,                  {ge::DT_FLOAT16, ge::DT_BF16}},
    {QUERY_ROPE_NAME,             {ge::DT_FLOAT16, ge::DT_BF16}},
    {KEY_ROPE_NAME,               {ge::DT_FLOAT16, ge::DT_BF16}},
    {ATTEN_OUT_NAME,              {ge::DT_FLOAT16, ge::DT_BF16}},
    {SOFTMAX_MAX_NAME,            {ge::DT_FLOAT}},
    {SOFTMAX_SUM_NAME,            {ge::DT_FLOAT}},
    {SPARSE_INDICES_NAME,         {ge::DT_INT32}},
    {BLOCK_TABLE_NAME,            {ge::DT_INT32}},
};

const std::map<std::string, std::vector<SFALayout>> LAYOUT_SUPPORT_MAP = {
    {QUERY_NAME,             {SFALayout::BSND, SFALayout::TND}},
    {KEY_NAME,               {SFALayout::BSND, SFALayout::TND, SFALayout::PA_BSND}},
    {VALUE_NAME,             {SFALayout::BSND, SFALayout::TND, SFALayout::PA_BSND}},
    {ATTEN_OUT_NAME,         {SFALayout::BSND, SFALayout::TND}},
    {SOFTMAX_MAX_NAME,       {SFALayout::BNSG, SFALayout::NTG}},
    {SOFTMAX_SUM_NAME,       {SFALayout::BNSG, SFALayout::NTG}},
};

const std::map<ge::DataType, std::string> DATATYPE_TO_STRING_MAP = {
    {ge::DT_UNDEFINED, "DT_UNDEFINED"},           // Used to indicate a DataType field has not been set.
    {ge::DT_FLOAT, "DT_FLOAT"},                   // float type
    {ge::DT_FLOAT16, "DT_FLOAT16"},               // fp16 type
    {ge::DT_INT8, "DT_INT8"},                     // int8 type
    {ge::DT_INT16, "DT_INT16"},                   // int16 type
    {ge::DT_UINT16, "DT_UINT16"},                 // uint16 type
    {ge::DT_UINT8, "DT_UINT8"},                   // uint8 type
    {ge::DT_INT32, "DT_INT32"},                   // uint32 type
    {ge::DT_INT64, "DT_INT64"},                   // int64 type
    {ge::DT_UINT32, "DT_UINT32"},                 // unsigned int32
    {ge::DT_UINT64, "DT_UINT64"},                 // unsigned int64
    {ge::DT_BOOL, "DT_BOOL"},                     // bool type
    {ge::DT_DOUBLE, "DT_DOUBLE"},                 // double type
    {ge::DT_DUAL, "DT_DUAL"},                     // dual output type
    {ge::DT_DUAL_SUB_INT8, "DT_DUAL_SUB_INT8"},   // dual output int8 type
    {ge::DT_DUAL_SUB_UINT8, "DT_DUAL_SUB_UINT8"}, // dual output uint8 type
    {ge::DT_COMPLEX32, "DT_COMPLEX32"},           // complex32 type
    {ge::DT_COMPLEX64, "DT_COMPLEX64"},           // complex64 type
    {ge::DT_COMPLEX128, "DT_COMPLEX128"},         // complex128 type
    {ge::DT_QINT8, "DT_QINT8"},                   // qint8 type
    {ge::DT_QINT16, "DT_QINT16"},                 // qint16 type
    {ge::DT_QINT32, "DT_QINT32"},                 // qint32 type
    {ge::DT_QUINT8, "DT_QUINT8"},                 // quint8 type
    {ge::DT_QUINT16, "DT_QUINT16"},               // quint16 type
    {ge::DT_RESOURCE, "DT_RESOURCE"},             // resource type
    {ge::DT_STRING_REF, "DT_STRING_REF"},         // string ref type
    {ge::DT_STRING, "DT_STRING"},                 // string type
    {ge::DT_VARIANT, "DT_VARIANT"},               // dt_variant type
    {ge::DT_BF16, "DT_BFLOAT16"},                 
// ... (truncated due to length) ...

```
