---
id: code-vllm-ascend-kv-quant-sparse-attn
title: vLLM Ascend KV Quant Sparse Attention Operator
type: source-code
repo: vllm-project/vllm-ascend
path: csrc/attention/kv_quant_sparse_attn_sharedkv
url: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/attention/kv_quant_sparse_attn_sharedkv
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
- sparse-attention
- kv-cache
- quantization
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- unified-buffer
- global-memory
techniques:
- kv-cache-paging
- quantization-int8
- online-softmax
kernel_types:
- attention
- paged-attention
- quant-matmul
languages:
- cpp
- ascendc
---

# vLLM Ascend KV Quant Sparse Attention Operator

vLLM Ascend sparse attention operator over quantized shared KV data, anchoring code evidence for compressed cache reads and quantized attention execution.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `csrc/attention/kv_quant_sparse_attn_sharedkv`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/attention/kv_quant_sparse_attn_sharedkv


## Fetched Source


### `csrc/attention/kv_quant_sparse_attn_sharedkv/op_host/kv_quant_sparse_attn_sharedkv_proto.cpp`
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
 * \file sparse_attn_sharedkv_proto.cpp
 * \brief
 */

#include <graph/utils/type_utils.h>
#include <register/op_impl_registry.h>
#include "error/ops_error.h"

using namespace ge;

namespace ops {
constexpr uint32_t QUERY_INPUT_INDEX = 0;
constexpr uint32_t RETURN_SOFTMAX_LSE_INDEX = 8;

ge::graphStatus InferShapeKvQuantSparseAttnSharedkv(gert::InferShapeContext *context)
{
    OPS_ERR_IF(context == nullptr, OPS_LOG_E("KvQuantSparseAttnSharedkv", "InferShapeContext is nullptr"),
               return ge::GRAPH_FAILED);
    const gert::Shape *queryShape = context->GetInputShape(QUERY_INPUT_INDEX);
    OPS_LOG_E_IF_NULL(context, queryShape, return ge::GRAPH_FAILED)
    gert::Shape *attentionOutShape = context->GetOutputShape(0);
    OPS_LOG_E_IF_NULL(context, attentionOutShape, return ge::GRAPH_FAILED)
    *attentionOutShape = *queryShape;

    gert::Shape *softmaxLseShape = context->GetOutputShape(1);
    OPS_LOG_E_IF_NULL(context, attentionOutShape, return ge::GRAPH_FAILED)
    auto attr = context->GetAttrs();
    const bool *returnSoftmaxLsePtr = attr->GetAttrPointer<bool>(RETURN_SOFTMAX_LSE_INDEX);
    bool returnSoftmaxLse = (returnSoftmaxLsePtr != nullptr) ? *returnSoftmaxLsePtr : false;
    if (returnSoftmaxLse) {
        *softmaxLseShape = *queryShape;
        auto lastDimIdx = softmaxLseShape->GetDimNum() - 1;
        softmaxLseShape->SetDim(lastDimIdx, 1);
    } else {
        softmaxLseShape->SetDimNum(1);
        softmaxLseShape->SetDim(0, 0);
    }
    return GRAPH_SUCCESS;
}

ge::graphStatus InferDataTypeKvQuantSparseAttnSharedkv(gert::InferDataTypeContext *context)
{
    OPS_ERR_IF(context == nullptr, OPS_LOG_E("KvQuantSparseAttnSharedkv", "InferShapeContext is nullptr"),
               return ge::GRAPH_FAILED);
    const auto inputDataType = context->GetInputDataType(QUERY_INPUT_INDEX);
    context->SetOutputDataType(0, inputDataType);
    return ge::GRAPH_SUCCESS;
}

IMPL_OP(KvQuantSparseAttnSharedkv).InferShape(InferShapeKvQuantSparseAttnSharedkv).InferDataType(InferDataTypeKvQuantSparseAttnSharedkv);
} // namespace ops

```

### `csrc/attention/kv_quant_sparse_attn_sharedkv/op_host/kv_quant_sparse_attn_sharedkv_check_existance.cpp`
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
 * \file kv_quant_sparse_attn_sharedkv_check_existance.cpp
 * \brief
 */

#include "kv_quant_sparse_attn_sharedkv_check.h"

using namespace ge;
using namespace AscendC;
using std::map;
using std::string;
using std::pair;
namespace optiling {

static constexpr uint32_t TopK_SIZE = 512;
static constexpr uint32_t DIM_0 = 0;
static constexpr uint32_t DIM_1 = 1;
static constexpr uint32_t DIM_2 = 2;
static constexpr uint32_t DIM_3 = 3;

ge::graphStatus KvQuantSASTilingCheck::CheckParaExistenceAntiquant() const
{
    if (kvLayout_ == SASLayout::BSND) {
        return ge::GRAPH_SUCCESS;
    }  else if (kvLayout_ == SASLayout::PA_ND) {
        OP_CHECK_IF(opParamInfo_.sequsedKv.tensor == nullptr,
            OP_LOGE(opName_, "when layout_kv is PA_ND, actualSeqLengthsKv must not be null"),
            return ge::GRAPH_FAILED);
        OP_CHECK_IF((opParamInfo_.oriBlockTable.tensor == nullptr) && (opParamInfo_.cmpBlockTable.tensor == nullptr),
            OP_LOGE(opName_, "when layout_kv is PA_ND, oriBlockTable and cmpBlockTable must be one "),
            return ge::GRAPH_FAILED);
    }
    return ge::GRAPH_SUCCESS;
}

ge::graphStatus KvQuantSASTilingCheck::CheckParaExistence()
{
    if (ge::GRAPH_SUCCESS != CheckCmpSparseIndicesExistence() ||
        ge::GRAPH_SUCCESS != CheckSWAExistence() ||
        ge::GRAPH_SUCCESS != CheckCFAExistence() ||
        ge::GRAPH_SUCCESS != CheckSCFAExistence() ||
        ge::GRAPH_SUCCESS != CheckCmpRatioExistence() ||
        ge::GRAPH_SUCCESS != CheckUnrequiredParaExistence() ||
        ge::GRAPH_SUCCESS != CheckParaExistenceAntiquant()) {
        return ge::GRAPH_FAILED;
    }
    return ge::GRAPH_SUCCESS;
}

 ge::graphStatus KvQuantSASTilingCheck::CheckUnrequiredParaExistence() const
{
    OP_CHECK_IF(opParamInfo_.oriSparseIndices.tensor != nullptr || opParamInfo_.oriSparseIndices.desc != nullptr,
                OP_LOGE(opName_, "oriSparseIndices is not supported now, it must be nullptr."),
                return ge::GRAPH_FAILED);
    OP_CHECK_IF(opParamInfo_.cuSeqLensOriKv.tensor != nullptr || opParamInfo_.cuSeqLensOriKv.desc != nullptr,
                OP_LOGE(opName_, "cuSeqLensOriKv is not supported now, it must be nullptr."),
                return ge::GRAPH_FAILED);
    OP_CHECK_IF(opParamInfo_.cuSeqLensCmpKv.tensor != nullptr || opParamInfo_.cuSeqLensCmpKv.desc != nullptr,
                OP_LOGE(opName_, "cuSeqLensCmpKv is not supported now, it must be nullptr."),
                return ge::GRAPH_FAILED);
    return ge::GRAPH_SUCCESS;
}

ge::graphStatus KvQuantSASTilingCheck::CheckCmpSparseIndicesExistence()
{
    if (opParamInfo_.cmpSparseIndices.tensor != nullptr) {
        if (qLayout_ == SASLayout::BSND) {
            if (opParamInfo_.cmpSparseIndices.tensor->GetStorageShape().GetDim(DIM_3) != 512 && opParamInfo_.cmpSparseIndices.tensor->GetStorageShape().GetDim(DIM_3) != 1024) {
                OP_LOGE(opName_, "When qLayout is BNSD, topK should be 512 or 1024, but got %ld", opParamInfo_.cmpSparseIndices.tensor->GetStorageShape().GetDim(3));
                return ge::GRAPH_FAILED;
            }
            if (opParamInfo_.cmpSparseIndices.tensor->GetStorageShape().GetDim(DIM_1) != s1Size_) {
                OP_LOGE(opName_, "When qLayout is BNSD, cmpSparseIndices's S should be eaque to s1Size:%u, but got %ld", s1Size_, opParamInfo_.cmpSparseIndices.tensor->GetStorageShape().GetDim(1));
                return ge::GRAPH_FAILED;
            }
        } else {
            if (opParamInfo_.cmpSparseIndices.tensor->GetStorageShape().GetDim(DIM_2) != 512 && opParamInfo_.cmpSparseIndices.tensor->GetStorageShape().GetDim(DIM_2) != 1024) {
                OP_LOGE(opName_, "When qLayout is TND, topK should be 512 or 1024, but got %ld", opParamInfo_.cmpSparseIndices.tensor->GetStorageShape().GetDim(2));
                return ge::GRAPH_FAILED;
            }
            if (opParamInfo_.cmpSparseIndices.tensor->GetStorageShape().GetDim(DIM_0) != qTSize_) {
                OP_LOGE(opName_, "When qLayout is TND, cmpSparseIndices's T should be eaque to qTSize:%u, but got %ld", qTSize_, opParamInfo_.cmpSparseIndices.tensor->GetStorageShape().GetDim(0));
                return ge::GRAPH_FAILED;
            }
        }
    }
    return ge::GRAPH_SUCCESS;
}

ge::graphStatus KvQuantSASTilingCheck::CheckSWAExistence()
{
    if (perfMode_ != SA
// ... (truncated due to length) ...

```

### `csrc/attention/kv_quant_sparse_attn_sharedkv/op_host/kv_quant_sparse_attn_sharedkv_check.h`
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
 * \file kv_quant_sparse_attn_sharedkv_check.h
 * \brief
 */
#ifndef KV_QUANT_SPARSE_ATTN_SHAREDKV_CHECK_H
#define KV_QUANT_SPARSE_ATTN_SHAREDKV_CHECK_H

#include <graph/utils/type_utils.h>
#include <exe_graph/runtime/tiling_context.h>
#include <tiling/platform/platform_ascendc.h>
#include "register/tilingdata_base.h"
#include "register/op_def_registry.h"
#include "tiling/tiling_api.h"
#include "log/log.h"
#include "log/error_code.h"
#include "err/ops_err.h"
#include "platform/platform_info.h"

namespace optiling {

const std::string ORI_BLOCK_TABLE_NAME = "ori_block_table";
const std::string CMP_BLOCK_TABLE_NAME = "cmp_block_table";
const std::string SINKS_NAME = "sinks";

const std::string QUERY_NAME = "query";
const std::string KEY_NAME = "key";
const std::string VALUE_NAME = "value";

const std::string ORI_KV_NAME = "ori_kv";
const std::string CMP_KV_NAME = "cmp_kv";
const std::string ORI_SPARSE_INDICES_NAME = "ori_sparse_indices";
const std::string CMP_SPARSE_INDICES_NAME = "cmp_sparse_indices";
const std::string ATTEN_OUT_NAME = "attention_out";

const std::string CU_SEQLENS_Q_NAME = "cu_seqlens_q";
const std::string SEQUSED_KV_NAME = "seqused_kv";

// // ------------------公共定义--------------------------
struct SASTilingRequiredParaInfo {
    const gert::CompileTimeTensorDesc *desc;
    const gert::StorageShape *shape;
};

struct SASTilingOptionalParaInfo {
    const gert::CompileTimeTensorDesc *desc;
    const gert::Tensor *tensor;
};

enum class SASLayout : uint32_t {
    BSND = 0,
    TND = 1,
    PA_ND = 2
};

enum class SASAxis : uint32_t {
    B = 0,
    S = 1,
    N = 2,
    D = 3,
    K = 3,  // sparse_indices的K和key的D枚举值相同，表达相同位置, 最后一维
    T = 5,
    Bn = 6, // block number
    Bs = 7 // block size
};

enum class SASTemplateMode : uint32_t {
    SWA_TEMPLATE_MODE = 0,
    CFA_TEMPLATE_MODE = 1,
    SCFA_TEMPLATE_MODE = 2
};

enum class KvStorageMode : uint32_t {
    BATCH_CONTINUOUS = 0,
    TENSOR_LIST = 1,
    PAGE_ATTENTION = 2
};

struct KvQuantSASTilingShapeCompareParam {
    int64_t B = 1;
    int64_t S = 1;
    int64_t N = 1;
    int64_t D = 1;
    int64_t T = 1;
    // PA
    int64_t Bs = 1;
    int64_t Bn = 1;
};

// ------------------算子原型索引常量定义----------------
// Inputs Index
constexpr uint32_t Q_INDEX = 0;
constexpr uint32_t ORI_KV_INDEX = 1;
constexpr uint32_t CMP_KV_INDEX = 2;
constexpr uint32_t ORI_SPARSE_INDICES_INDEX = 3;
constexpr uint32_t CMP_SPARSE_INDICES_INDEX = 4;
constexpr uint32_t ORI_BLOCK_TABLE_INDEX = 5;
constexpr uint32_t CMP_BLOCK_TABLE_INDEX = 6;
constexpr uint32_t CU_SEQLENS_Q_INDEX = 7;
constexpr uint32_t CU_SEQLENS_ORI_KV_INDEX = 8;
constexpr uint32_t CU_SEQLENS_CMP_KV_INDEX = 9;
constexpr uint32_t SEQUSED_Q_INDEX = 10;
constexpr uint32_t SEQUSED_KV_INDEX = 11;
constexpr uint32_t SINKS_INDEX = 12;
constexpr uint32_t METADATA_INDEX = 13;
// Outputs Index
constexpr uint32_t ATTN_OUT_INDEX = 0;

// Attributes Index
constexpr uint32_t ATTR_KV_QUANT_SCALE_INDEX = 0;
constexpr uint32_t ATTR_TILE_SIZE_INDEX = 1;
constexpr uint32_t ATTR_ROPE_HEAD_DIM_INDEX = 2;
constexpr uint32_t ATTR_SOTFMAX_SCALE_INDEX = 3;
constexpr uint32_t ATTR_CMP_RATIO_INDEX = 4;
constexpr uint32_t ATTR_ORI_MASK_MODE_INDEX = 5;
constexpr uint32_t ATTR_CMP_MASK_MODE_INDEX = 6;
constexpr uint32_t ATTR_ORI_WIN_LEFT_INDEX = 7;
constexpr uint32_t ATTR_ORI_WIN_RIGHT_INDEX = 8;
constexpr uint32_t ATTR_LAYOUT_Q_INDEX = 9;
constexpr uint32_t ATTR_LAYOUT_KV_INDEX = 10;
constexpr uint32_t ATTR_ORIKV_STRIDE_INDEX = 11;
constexpr uint32_t ATTR_CMPKV_STRIDE_INDEX = 12;

// Dim Index
constexpr uint32_t DIM_IDX_ONE = 1;
constexpr uint32_t DIM_IDX_TWO = 2;
constexpr uint32_t DIM_IDX_THREE = 3;
constexpr uint32_t DIM_IDX_FOUR = 4;

// Dim Num
constexpr uint32_t DIM_NUM_ONE = 1;
constexpr uint32_t DIM_NUM_TWO = 2;
constexpr uint32_t DIM_NUM_THREE = 3;
constexpr uint32_t DIM_NUM_FOUR = 4;

// 入参限制常量
constexpr uint32_t HEAD_DIM_LIMIT = 128;
constexpr uint32_t SPARSE_LIMIT = 2048;
constexpr uint32_t SPARSE_MODE_LOWER = 3;
constexpr uint32_t MAX_BLOCK_SIZE = 1024;
constexpr uint32_t COPYND2NZ_SRC_STRIDE_LIMITATION = 65535;
constexpr uint32_t NUM_BYTES_FLOAT = 4;
constexpr uint32_t NUM_BYTES_FLOAT16 = 2;
constexpr uint32_t NUM_BYTES_BF16 = 2;
constexpr uint32_t BYTE_BLOCK = 32;
const uint32_t QSFA_MAX_AIC_CORE_NUM = 26; // 25 + 1 保证数组8字节对齐

const std::map<ge::DataType, std::strin
// ... (truncated due to length) ...

```
