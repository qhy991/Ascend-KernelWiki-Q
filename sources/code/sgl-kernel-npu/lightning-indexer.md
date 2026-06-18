---
id: code-sgl-kernel-npu-lightning-indexer
title: SGL Kernel NPU Lightning Indexer Operator
type: source-code
repo: sgl-project/sgl-kernel-npu
path: csrc/lightning_indexer
url: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/lightning_indexer
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- sglang
- indexing
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

# SGL Kernel NPU Lightning Indexer Operator

SGL Kernel NPU lightning indexer operator, anchoring code evidence for attention index construction and cache-oriented preprocessing.

## Code Location

- Repository: `sgl-project/sgl-kernel-npu`
- Path: `csrc/lightning_indexer`
- URL: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/lightning_indexer


## Fetched Source


### `csrc/lightning_indexer/op_host/lightning_indexer_def.h`
```cpp
/**
 * This program is free software, you can redistribute it and/or modify it.
 * Copyright (c) 2025 Huawei Technologies Co., Ltd.
 * This file is a part of the CANN Open Software.
 * Licensed under CANN Open Software License Agreement Version 2.0 (the "License").
 * Please refer to the License for details. You may not use this file except in compliance with the License.
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING
 * BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE. See LICENSE in the root of
 * the software repository for the full text of the License.
 */

/*!
 * \file lightning_indexer_def.cpp
 * \brief
 */
#include <cstdint>
#include "ge_helper.h"

namespace sglang {
namespace LIHost {
using namespace ge_helper;
class LightningIndexer : public OpDef
{
public:
    explicit LightningIndexer(const char *name) : OpDef(name)
    {
        this->Input("query")
            .ParamType(REQUIRED)
            .DataType({ge::DT_BF16, ge::DT_FLOAT16})
            .FormatList({ge::FORMAT_ND})
            .AutoContiguous();
        this->Input("key")
            .ParamType(REQUIRED)
            .DataType({ge::DT_BF16, ge::DT_FLOAT16})
            .FormatList({ge::FORMAT_ND})
            .AutoContiguous();
        this->Input("weights")
            .ParamType(REQUIRED)
            .DataType({ge::DT_BF16, ge::DT_FLOAT16})
            .FormatList({ge::FORMAT_ND})
            .AutoContiguous();
        this->Input("actual_seq_lengths_query")
            .ParamType(OPTIONAL)
            .DataType({ge::DT_INT32, ge::DT_INT32})
            .FormatList({ge::FORMAT_ND})
            .AutoContiguous();
        this->Input("actual_seq_lengths_key")
            .ParamType(OPTIONAL)
            .DataType({ge::DT_INT32, ge::DT_INT32})
            .FormatList({ge::FORMAT_ND})
            .AutoContiguous();
        this->Input("block_table")
            .ParamType(OPTIONAL)
            .DataTypeList({ge::DT_INT32})
            .FormatList({ge::FORMAT_ND})
            .AutoContiguous();
        this->Output("sparse_indices").ParamType(REQUIRED).DataTypeList({ge::DT_INT32}).FormatList({ge::FORMAT_ND});
        this->Attr("layout_query").AttrType(OPTIONAL).String("TND");
        this->Attr("layout_key").AttrType(OPTIONAL).String("PA_BSND");
        this->Attr("sparse_count").AttrType(OPTIONAL).Int(2048);  // 2048:默认值，筛选前2048
        this->Attr("sparse_mode").AttrType(OPTIONAL).Int(3);      // 3:默认值，只计算下三角
    }
};
}  // namespace LIHost
}  // namespace sglang

```

### `csrc/lightning_indexer/op_host/lightning_indexer.cpp`
```cpp
#include <cstdio>
#include <string>
#include "acl/acl.h"
#include "kernel_tiling/kernel_tiling.h"
#include "tiling/platform/platform_ascendc.h"
#include "tiling/lightning_indexer_tiling.h"
#include "defines.h"
#include "torch_helper.h"
#include "ge_helper.h"
#include "common_tiling.h"
#include "lightning_indexer_def.h"
#include "common.h"
#include "aclrtlaunch_lightning_indexer.h"

namespace sglang::LIHost {

using namespace ge_helper;
constexpr uint32_t MAX_CAPTURE_NUM = 1024;
constexpr uint32_t MAX_DECODE_BS = 512;
// npu tensor max size
constexpr int SIZE = 8;
constexpr int DIM_0 = 0;
constexpr int DIM_1 = 1;
constexpr int DIM_2 = 2;
constexpr int DIM_3 = 3;

// namespace scope global parameters
uint32_t actualCaptureNum = 0;
static std::unordered_map<uint64_t, uint32_t> captureMap;
// at::Tensor workspace;

inline at::Tensor ConstructLightningIndexerOutputTensor(const at::Tensor &query, const at::Tensor &key,
                                                        const c10::optional<at::Tensor> &actual_seq_lengths_query,
                                                        int64_t sparse_count, std::string query_layout_str,
                                                        std::string key_layout_str)
{
    at::SmallVector<int64_t, SIZE> outputSize;
    for (size_t i = 0; i < query.sizes().size(); i++) {
        TORCH_CHECK(query.size(i) > 0,
                    "All values within query's shape should be greater "
                    "than 0, but shape[",
                    i, "] is ", query.size(i));
    }
    TORCH_CHECK(sparse_count > 0, "sparse count should be greater than 0, but now is ", sparse_count);

    if (query_layout_str == "BSND") {
        outputSize = {query.size(DIM_0), query.size(DIM_1), key.size(DIM_2), sparse_count};
    } else {
        int n_dim_index = 0;
        n_dim_index = (key_layout_str == "TND") ? DIM_1 : DIM_2;
        outputSize = {query.size(DIM_0), key.size(n_dim_index), sparse_count};
    }
    at::Tensor output = at::empty(outputSize, query.options().dtype(at::kInt));

    return output;
}
}  // namespace sglang::LIHost

namespace sglang {
namespace npu_kernel {
HOST_API at::Tensor lightning_indexer(const at::Tensor &query, const at::Tensor &key, const at::Tensor &weights,
                                      const c10::optional<at::Tensor> &actual_seq_lengths_query,
                                      const c10::optional<at::Tensor> &actual_seq_lengths_key,
                                      const c10::optional<at::Tensor> &block_table,
                                      c10::optional<c10::string_view> layout_query,
                                      c10::optional<c10::string_view> layout_key, c10::optional<int64_t> sparse_count,
                                      c10::optional<int64_t> sparse_mode)
{
    using namespace LIHost;
    LightningIndexer indexer("lightning_indexer");
    auto context = std::make_shared<TilingContext>("lightning_indexer");
    TORCH_CHECK(context != nullptr, "TilingContext is null");

    std::string layoutQuery(indexer.GetAttr(ATTR_QUERY_LAYOUT_INDEX).GetString());
    std::string layoutKey(indexer.GetAttr(ATTR_KEY_LAYOUT_INDEX).GetString());
    int64_t sparseCount = std::any_cast<int32_t>(indexer.GetAttr(ATTR_SPARSE_COUNT_INDEX).GetValue());

    if (layout_query.has_value()) {
        layoutQuery = std::string(layout_query.value());
        indexer.SetAttrStr("layout_query", layoutQuery);
    }
    if (layout_key.has_value()) {
        layoutKey = std::string(layout_key.value());
        indexer.SetAttrStr("layout_key", layoutKey);
    }
    if (sparse_count.has_value()) {
        sparseCount = sparse_count.value();
        indexer.SetAttrAny("sparse_count", static_cast<int32_t>(sparseCount));
    }
    if (sparse_mode.has_value()) {
        indexer.SetAttrAny("sparse_mode", static_cast<int32_t>(sparse_mode.value()));
    }

    at::Tensor sparse_indices = ConstructLightningIndexerOutputTensor(query, key, actual_seq_lengths_query, sparseCount,
                                                                      layoutQuery, layoutKey);

    auto qScalarType = query.scalar_type();

    at::Tensor actualSeqLengthsQuery =
        actual_seq_lengths_query.has_value()
            ? actual_seq_lengths_query.value()
            : at::empty({1}, at::TensorOptions().dtype(qScalarType).device(query.options().device()));

    at::Tensor actualSeqLengthsKey =
        actual_seq_lengths_key.has_value()
            ? actual_seq_lengths_key.value()
            : at::empty({1}, at::TensorOptions().dtype(qScalarType).device(query.options().device()));

    at::Tensor blockTable =
        block_table.has_value()
            ? block_table.value()
            : at::empty({1}, at::TensorOptions().dtype(qScalarType).device(query.options().device()));

    indexer.SetToContext(context, qScalarType);
    context->RegisterTensor(query, true);
    context->RegisterTensor(key, true);
    context->RegisterTensor(weights, true);
    conte
// ... (truncated due to length) ...

```

### `csrc/lightning_indexer/op_host/tiling/lightning_indexer_tiling.cpp`
```cpp
/**
 * This program is free software, you can redistribute it and/or modify it.
 * Copyright (c) 2025 Huawei Technologies Co., Ltd.
 * This file is a part of the CANN Open Software.
 * Licensed under CANN Open Software License Agreement Version 2.0 (the "License").
 * Please refer to the License for details. You may not use this file except in compliance with the License.
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING
 * BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE. See LICENSE in the root of
 * the software repository for the full text of the License.
 */

/*!
 * \file lightning_indexer_tiling.cpp
 * \brief
 */

#include "lightning_indexer_tiling.h"

using namespace ge;
using namespace AscendC;
using std::map;
using std::string;
namespace sglang::LIHost {

#define OPS_LOG_E(opName, logInfo) (std::string(opName) + ": " + logInfo)
// --------------------------LIInfoParser类成员函数定义-------------------------------------
ge::graphStatus LIInfoParser::CheckRequiredInOutExistence() const
{
    TORCH_CHECK(opParamInfo_.query.shape != nullptr, OPS_LOG_E(opName_, "Shape of tensor query is nullptr"));
    TORCH_CHECK(opParamInfo_.query.desc != nullptr, OPS_LOG_E(opName_, "Desc of tensor query is nullptr"));
    TORCH_CHECK(opParamInfo_.key.shape != nullptr, OPS_LOG_E(opName_, "Shape of tensor key is nullptr"));
    TORCH_CHECK(opParamInfo_.key.desc != nullptr, OPS_LOG_E(opName_, "Desc of tensor key is nullptr"));
    TORCH_CHECK(opParamInfo_.weights.shape != nullptr, OPS_LOG_E(opName_, "Shape of tensor weights is nullptr"));
    TORCH_CHECK(opParamInfo_.weights.desc != nullptr, OPS_LOG_E(opName_, "Desc of tensor weights is nullptr"));
    TORCH_CHECK(opParamInfo_.attenOut.shape != nullptr, OPS_LOG_E(opName_, "Shape of tensor attenOut is nullptr"));
    TORCH_CHECK(opParamInfo_.attenOut.desc != nullptr, OPS_LOG_E(opName_, "Desc of tensor attenOut is nullptr"));

    return ge::GRAPH_SUCCESS;
}

ge::graphStatus LIInfoParser::CheckRequiredAttrExistence() const
{
    TORCH_CHECK(opParamInfo_.layOut != nullptr, OPS_LOG_E(opName_, "attr layout_query is nullptr"));
    TORCH_CHECK(opParamInfo_.layOutKey != nullptr, OPS_LOG_E(opName_, "attr layout_key is nullptr"));
    TORCH_CHECK(opParamInfo_.sparseCount != nullptr, OPS_LOG_E(opName_, "attr sparse_count is nullptr"));
    TORCH_CHECK(opParamInfo_.sparseMode != nullptr, OPS_LOG_E(opName_, "attr sparse_mode is nullptr"));

    return ge::GRAPH_SUCCESS;
}

ge::graphStatus LIInfoParser::CheckRequiredParaExistence() const
{
    if (CheckRequiredInOutExistence() != ge::GRAPH_SUCCESS || CheckRequiredAttrExistence() != ge::GRAPH_SUCCESS) {
        return ge::GRAPH_FAILED;
    }

    return ge::GRAPH_SUCCESS;
}

ge::graphStatus LIInfoParser::GetOpName()
{
    TORCH_CHECK(context_ != nullptr, OPS_LOG_E("LightningIndexer", "opName got from TilingContext is nullptr"));
    opName_ = context_->GetNodeName();
    return ge::GRAPH_SUCCESS;
}

ge::graphStatus LIInfoParser::GetNpuInfo()
{
    auto ascendcPlatform = *platform_ascendc::PlatformAscendCManager::GetInstance();
    uint32_t aivNum = ascendcPlatform.GetCoreNumAiv();
    uint32_t aicNum = ascendcPlatform.GetCoreNumAic();
    TORCH_CHECK(aivNum != 0 && aicNum != 0, OPS_LOG_E(opName_, "num of core obtained is 0"));

    socVersion_ = ascendcPlatform.GetSocVersion();
    TORCH_CHECK(socVersion_ == platform_ascendc::SocVersion::ASCEND910B ||
                    socVersion_ == platform_ascendc::SocVersion::ASCEND910_93,
                OPS_LOG_E(opName_, "soc version does not support "), (int32_t)socVersion_);

    TORCH_CHECK(context_->GetWorkspaceSizes(1) != nullptr, OPS_LOG_E(opName_, "workspaceSize got from ge is nullptr"));

    return ge::GRAPH_SUCCESS;
}

void LIInfoParser::GetOptionalInputParaInfo()
{
    opParamInfo_.actualSeqLengthsQ.tensor = context_->GetOptionalInputTensor(ACTUAL_SEQ_Q_INDEX);
    opParamInfo_.actualSeqLengthsQ.desc = context_->GetOptionalInputDesc(ACTUAL_SEQ_Q_INDEX);
    opParamInfo_.actualSeqLengths.tensor = context_->GetOptionalInputTensor(ACTUAL_SEQ_K_INDEX);
    opParamInfo_.actualSeqLengths.desc = context_->GetOptionalInputDesc(ACTUAL_SEQ_K_INDEX);
    opParamInfo_.blockTable.tensor = context_->GetOptionalInputTensor(BLOCK_TABLE_INDEX);
    opParamInfo_.blockTable.desc = context_->GetOptionalInputDesc(BLOCK_TABLE_INDEX);
}

void LIInfoParser::GetInputParaInfo()
{
    opParamInfo_.query.desc = context_->GetInputDesc(QUERY_INDEX);
    opParamInfo_.query.shape = context_->GetInputShape(QUERY_INDEX);
    opParamInfo_.key.desc = context_->GetInputDesc(KEY_INDEX);
    opParamInfo_.key.shape = context_->GetInputShape(KEY_INDEX);
    opParamInfo_.weights.desc = context_->GetInputDesc(WEIGTHS_INDEX);
    opParamInfo_.weights.shape = context_->GetInputShape(WEIGTHS_INDEX);
    GetOptionalInputParaInfo();
}

void LIInfoParser::GetOutputParaInfo()
{
    opParamInfo_.attenOut.desc = context_->GetOutpu
// ... (truncated due to length) ...

```
