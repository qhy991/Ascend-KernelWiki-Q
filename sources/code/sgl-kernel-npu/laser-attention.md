---
id: code-sgl-kernel-npu-laser-attention
title: SGL Kernel NPU Laser Attention Operator
type: source-code
repo: sgl-project/sgl-kernel-npu
path: csrc/attentions/csrc/ops/laser_attention
url: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/attentions/csrc/ops/laser_attention
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- sglang
- laser-attention
- attention
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
- data-reuse
- pipeline-scheduling
kernel_types:
- attention
- flash-attention
languages:
- cpp
- ascendc
---

# SGL Kernel NPU Laser Attention Operator

SGL Kernel NPU laser attention operator directory anchoring an attention variant with custom host and kernel code for serving workloads.

## Code Location

- Repository: `sgl-project/sgl-kernel-npu`
- Path: `csrc/attentions/csrc/ops/laser_attention`
- URL: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/attentions/csrc/ops/laser_attention


## Fetched Source


### `csrc/attentions/csrc/ops/laser_attention/op_host/laser_attention_proto.cpp`
```cpp
/**
 * Copyright (c) Huawei Technologies Co., Ltd. 2025-2025. All rights reserved.
 *
 * You can use this software according to the terms and conditions of the Mulan PSL v2.
 * You may obtain a copy of Mulan PSL v2 at:
 *          http://license.coscl.org.cn/MulanPSL2
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
 * EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
 * MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
 * See the Mulan PSL v2 for more details.
 */

#include "register/op_def_registry.h"
#include "graph/utils/type_utils.h"

namespace ops {

static ge::graphStatus LaserAttentionInferShape(gert::InferShapeContext *context)
{
    if (context == nullptr) {
        return ge::GRAPH_FAILED;
    }
    const gert::Shape *queryShape = context->GetInputShape(0);
    if (queryShape == nullptr) {
        return ge::GRAPH_FAILED;
    }
    gert::Shape *softmaxOut = context->GetOutputShape(0);
    if (softmaxOut == nullptr) {
        return ge::GRAPH_FAILED;
    }
    int32_t queryDimNum = static_cast<int32_t>(queryShape->GetDimNum());
    if (queryDimNum < 4) {  // query dim num is 4
        return ge::GRAPH_FAILED;
    }
    softmaxOut->SetDimNum(queryDimNum - 1);
    softmaxOut->SetDim(0, queryShape->GetDim(0));
    softmaxOut->SetDim(1, queryShape->GetDim(1));
    softmaxOut->SetDim(2, queryShape->GetDim(2));  // index is 2

    gert::Shape *attnOut = context->GetOutputShape(1);
    if (attnOut == nullptr) {
        return ge::GRAPH_FAILED;
    }
    attnOut->SetDimNum(queryDimNum);
    attnOut->SetDim(0, queryShape->GetDim(0));
    attnOut->SetDim(1, queryShape->GetDim(1));
    attnOut->SetDim(2, queryShape->GetDim(2));  // index is 2
    attnOut->SetDim(3, queryShape->GetDim(3));  // index is 3

    return ge::GRAPH_SUCCESS;
}

static ge::graphStatus LaserAttentionInferDtype(gert::InferDataTypeContext *context)
{
    if (context == nullptr) {
        return ge::GRAPH_FAILED;
    }
    const ge::DataType queryDtype = context->GetInputDataType(0);
    context->SetOutputDataType(0, ge::DT_FLOAT);
    context->SetOutputDataType(1, ge::DT_FLOAT);
    return ge::GRAPH_SUCCESS;
}

IMPL_OP_INFERSHAPE(LaserAttention).InferShape(LaserAttentionInferShape).InferDataType(LaserAttentionInferDtype);

}  // namespace ops

```

### `csrc/attentions/csrc/ops/laser_attention/op_host/laser_attention_def.cpp`
```cpp
/**
 * Copyright (c) Huawei Technologies Co., Ltd. 2025-2025. All rights reserved.
 *
 * You can use this software according to the terms and conditions of the Mulan PSL v2.
 * You may obtain a copy of Mulan PSL v2 at:
 *          http://license.coscl.org.cn/MulanPSL2
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
 * EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
 * MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
 * See the Mulan PSL v2 for more details.
 */

#include "register/op_def_registry.h"

namespace {
constexpr size_t MAX_TOKEN = 2147483647;
}

namespace ops {
class LaserAttention : public OpDef
{
public:
    explicit LaserAttention(const char *name) : OpDef(name)
    {
        this->Input("query")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT16, ge::DT_BF16})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND});
        this->Input("key")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT16, ge::DT_BF16})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND});
        this->Input("value")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT16, ge::DT_BF16})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND});
        this->Input("atten_mask")
            .ParamType(OPTIONAL)
            .DataType({ge::DT_FLOAT16, ge::DT_BF16})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND});
        this->Input("alibi_mask")
            .ParamType(OPTIONAL)
            .DataType({ge::DT_FLOAT16, ge::DT_BF16})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND});
        this->Input("drop_mask")
            .ParamType(OPTIONAL)
            .DataType({ge::DT_UINT8, ge::DT_UINT8})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND});
        // （qseqlen，1）
        this->Output("softmax_log_max_sum")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT, ge::DT_FLOAT})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND});
        this->Output("attention_out")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT, ge::DT_FLOAT})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND});
        this->Attr("scale_value").AttrType(REQUIRED).Float();
        this->Attr("head_num").AttrType(REQUIRED).Int();
        this->Attr("input_layout").AttrType(REQUIRED).String();
        this->Attr("keep_prob").AttrType(OPTIONAL).Float(1.0);
        this->Attr("pre_tokens").AttrType(OPTIONAL).Int(MAX_TOKEN);
        this->Attr("next_tokens").AttrType(OPTIONAL).Int(1);
        this->Attr("is_highPrecision").AttrType(OPTIONAL).Bool(true);

        this->AICore().AddConfig("ascend910");
        this->AICore().AddConfig("ascend910b");
        this->AICore().AddConfig("ascend910_93");
    }
};

OP_ADD(LaserAttention);
}  // namespace ops

```

### `csrc/attentions/csrc/ops/laser_attention/op_host/laser_attention_tiling.cpp`
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

#include "laser_attention_tiling.h"

#include <string>
#include <cinttypes>

#include "register/op_def_registry.h"
#include "tiling/platform/platform_ascendc.h"

using namespace std;

namespace {
constexpr size_t CONST_ONES_SIZE = 16384 * 2;     // half
constexpr size_t CONST_ZERO_SIZE = 32 * 128 * 4;  // float
constexpr size_t MAX_TOKEN = 2147483647;
const int ALIGNNUM = 16;
inline __attribute__((always_inline)) int32_t CeilDiv(int32_t num, int32_t div)
{
    if (div == 0) {
        return 0;
    }
    return (num + div - 1) / div;
}

inline __attribute__((always_inline)) int32_t Align(int32_t num, int32_t alignNum)
{
    if (alignNum != 0) {
        return (num + alignNum - 1) / alignNum * alignNum;
    } else {
        return num + alignNum - 1;
    }
}

}  // namespace

namespace optiling {
class LaserAttentionTiling
{
public:
    LaserAttentionTilingData tilingData;

    ge::graphStatus Tiling4LaserAttention(gert::TilingContext *context);

    ge::graphStatus DoTiling(gert::TilingContext *context);

    ge::graphStatus CheckTiling(gert::TilingContext *context);
};

ge::graphStatus LaserAttentionTiling::DoTiling(gert::TilingContext *context)
{
    if (context == nullptr) {
        return ge::GRAPH_FAILED;
    }
    const auto platformInfo = context->GetPlatformInfo();
    if (platformInfo == nullptr) {
        return ge::GRAPH_FAILED;
    }
    const auto ascendcPlatform = platform_ascendc::PlatformAscendC(platformInfo);
    const auto aicNum = ascendcPlatform.GetCoreNumAic();

    auto col_size = tilingData.get_kSeqLength();
    if (tilingData.get_sparseMode() == 1) {
        col_size = tilingData.get_windowLen();
    }

    int32_t coreNumPerGroup = 1;
    int32_t factor = 2;
    if (col_size <= 8 * 1024 / factor) {  // value is 8 * 1024
        coreNumPerGroup = 1;
    } else if (col_size > 8 * 1024 / factor && col_size <= 16 * 1024 / factor) {   // value is 8、16、1024
        coreNumPerGroup = 2;                                                       // 2 is coreNumPerGroup
    } else if (col_size > 16 * 1024 / factor && col_size <= 32 * 1024 / factor) {  // value is 16、32、1024
        coreNumPerGroup = 4;                                                       // 4 is coreNumPerGroup
    } else {
        if (aicNum == 20) {       // 20 is aicNum
            coreNumPerGroup = 4;  // 4 is coreNumPerGroup
        } else {
            coreNumPerGroup = 8;  // 8 is coreNumPerGroup
        }
    }

    tilingData.set_coreNumPerGroup(coreNumPerGroup);
    tilingData.set_coreGroupNum(aicNum / coreNumPerGroup);

    return ge::GRAPH_SUCCESS;
}

ge::graphStatus LaserAttentionTiling::CheckTiling(gert::TilingContext *context)
{
    if (context == nullptr) {
        return ge::GRAPH_FAILED;
    }

    if (tilingData.get_batchSize() == 0) {
        cout << context->GetNodeName() << "op [TilingData]: batchSize is 0. " << endl;
        return ge::GRAPH_FAILED;
    }

    if (tilingData.get_headNum() == 0) {
        cout << context->GetNodeName() << "op [TilingData]: headNum is 0. " << endl;
        return ge::GRAPH_FAILED;
    }

    if (tilingData.get_qSeqLength() == 0) {
        cout << context->GetNodeName() << "op [TilingData]: qSeqLength is 0. " << endl;
        return ge::GRAPH_FAILED;
    }

    if (tilingData.get_kSeqLength() == 0) {
        cout << context->GetNodeName() << "op [TilingData]: kSeqLength is 0. " << endl;
        return ge::GRAPH_FAILED;
    }

    if (tilingData.get_vSeqLength() == 0) {
        cout << context->GetNodeName() << "op [TilingData]: vSeqLength is 0. " << endl;
        return ge::GRAPH_FAILED;
    }

    // sparse场景下windowsLength需要是256的倍数
    if (tilingData.get_sparseMode() == 1 && (tilingData.get_windowLen() % 256 != 0)) {
        cout << context->GetNodeName() << "op [TilingData]: windowLen= " << tilingData.get_windowLen() << endl;
        return ge::GRAPH_FAILED;
    }

    return ge::GRAPH_SUCCESS;
}

ge::graphStatus LaserAttentionTiling::Tiling4LaserAttention(gert::TilingContext *context)
{
    if (context == nullptr) {
        return ge::GRAPH_FAILED;
    }
    int32_t inputNum = static_cast<int32_t>(context->GetComputeNodeInputNum());
    if (inputNum < 3) {  // 3 is the number of inputs
        return ge::GRAPH_FAILED;
    }
    const auto queryShape = context->GetInputShape(0);
    const auto keyShape = context->GetInputShape(1);
    const auto valu
// ... (truncated due to length) ...

```
