---
id: code-sgl-kernel-npu-sparse-block-estimate
title: SGL Kernel NPU Sparse Block Estimate Operator
type: source-code
repo: sgl-project/sgl-kernel-npu
path: csrc/attentions/csrc/ops/sparse_block_estimate
url: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/attentions/csrc/ops/sparse_block_estimate
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- sglang
- sparse-attention
- block-estimate
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
- tiling-strategy
- pipeline-scheduling
kernel_types:
- attention
- reduce
languages:
- cpp
- ascendc
---

# SGL Kernel NPU Sparse Block Estimate Operator

SGL Kernel NPU sparse block estimation source for attention pruning and block selection, useful as evidence for auxiliary attention kernels.

## Code Location

- Repository: `sgl-project/sgl-kernel-npu`
- Path: `csrc/attentions/csrc/ops/sparse_block_estimate`
- URL: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/attentions/csrc/ops/sparse_block_estimate


## Fetched Source


### `csrc/attentions/csrc/ops/sparse_block_estimate/op_host/sparse_block_estimate_tiling.cpp`
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

#include <queue>
#include <vector>
#include <string>
// #include <iostream>  // 必须引入 std::cout/std::endl 头文件

#include <unordered_map>
#include "tiling/tiling_api.h"
#include "tiling/platform/platform_ascendc.h"
#include "register/op_def_registry.h"
#include "register/tilingdata_base.h"
#include "sparse_block_estimate_tiling.h"

#include <cstdint>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <cstdlib>
#include <dlfcn.h>
#include <unistd.h>
#include <cstdio>
#include <numeric>
#include <algorithm>
#include <graph/utils/type_utils.h>

using std::string;

using namespace matmul_tiling;

namespace optiling {
constexpr uint32_t NUM_2 = 2;
int32_t SINGLE_CORE_MBASE = 128;
int32_t SINGLE_CORE_NBASE = 1024;

constexpr uint32_t ACTUAL_SEQ_Q_INDEX = 2;
constexpr uint32_t ACTUAL_SEQ_KV_INDEX = 3;
constexpr uint32_t QUERY_INDEX = 0;
constexpr uint32_t KEY_INDEX = 1;

constexpr uint32_t INPUT_LAYOUT = 0;
constexpr uint32_t STRIDE = 1;
constexpr uint32_t SPARSE_SIZE = 2;
constexpr uint32_t NUM_HEADS_ATTR = 3;
constexpr uint32_t NUM_KV_HEADS_ATTR = 4;
constexpr uint32_t SCALE_VALUE = 5;
constexpr uint32_t THRESHOLD = 6;
constexpr uint32_t CAUSAL = 7;
constexpr uint32_t KEEP_SINK = 8;
constexpr uint32_t KEEP_RECENT = 9;
constexpr uint32_t ATTR_ROW_SPARSE = 10;
constexpr uint32_t DIM0_INDEX = 0;
constexpr uint32_t DIM1_INDEX = 1;
constexpr uint32_t DIM2_INDEX = 2;
constexpr uint32_t DIM3_INDEX = 3;

uint64_t BASE_TILING_KEY = 1000000000000000000;  // 默认 TILING_KEY

void PromptFlashAttentionSplitNSNew(SparseBlockEstimateTilingData &tiling, uint32_t curCoreNum,
                                    std::vector<int64_t> &actualSeqLengths, std::vector<int64_t> &actualSeqLengthsKV,
                                    int64_t actualSharedPrefixLen, bool useBalanceTiling)
{
    SparseBlockEstimateSeqParams *seqParams = &tiling.sparseBlockEstimateSeqParams;

    uint32_t arrayLen = tiling.get_batchSize();  // batch size
    uint32_t sOuterSize = SINGLE_CORE_MBASE * tiling.get_stride();
    uint32_t sInnerSize = SINGLE_CORE_NBASE * tiling.get_stride();

    std::vector<uint32_t> accumSOuterTilingNums(static_cast<size_t>(arrayLen), 0U);
    std::vector<uint32_t> sInnerLoopTimes(static_cast<size_t>(arrayLen), 0U);
    std::vector<uint32_t> sOuterBlockNums(static_cast<size_t>(arrayLen), 0U);

    const size_t tilingElementArrayLen =
        (static_cast<size_t>(curCoreNum) > 64UL) ? static_cast<size_t>(curCoreNum) : 64UL;
    std::vector<uint32_t> coreSposEnd(tilingElementArrayLen, 0U);
    std::vector<uint32_t> coreSposStart(tilingElementArrayLen, 0U);
    std::vector<uint32_t> coreSidEnd(tilingElementArrayLen, 0U);
    std::vector<uint32_t> coreSidStart(tilingElementArrayLen, 0U);
    std::vector<uint32_t> coreNidEnd(tilingElementArrayLen, 0U);
    std::vector<uint32_t> coreNidStart(tilingElementArrayLen, 0U);

    int64_t totalBlockWight = 0;
    int totalOuterBlockNum = 0;
    uint32_t preAccumSOuterNum = 0U;
    uint32_t multiSmaxsInnerLoopTimes = 0U;
    uint32_t sInnerPrefixLoopTimes = (actualSharedPrefixLen + sInnerSize - 1) / sInnerSize;
    bool isSOuterNoTail = true;
    bool isSInnerNoTail = true;
    bool causal = tiling.get_causal();
    for (uint32_t i = 0; i < arrayLen; i++) {
        int seqLen = actualSeqLengths[i];
        int subSeqInnerLen = actualSeqLengthsKV[i];
        sOuterBlockNums[i] = (seqLen + sOuterSize - 1) / sOuterSize;
        sInnerLoopTimes[i] = (subSeqInnerLen + sInnerSize - 1) / sInnerSize + sInnerPrefixLoopTimes;
        accumSOuterTilingNums[i] = (sOuterBlockNums[i] * tiling.get_headNumQ()) + preAccumSOuterNum;
        preAccumSOuterNum = accumSOuterTilingNums[i];

        multiSmaxsInnerLoopTimes = std::max(multiSmaxsInnerLoopTimes, sInnerLoopTimes[i]);

        if (seqLen % sOuterSize != 0) {
            isSOuterNoTail = false;
        }
        if (subSeqInnerLen % sInnerSize != 0) {
            isSInnerNoTail = false;
        }
        totalOuterBlockNum += sOuterBlockNums[i];
        if (causal) {
            totalBlockWight += (static_cast<int64_t>(sOuterBlockNums[i]) + 1) *
                               static_cast<int64_t>(sOuterBlockNums[i]) / NUM_2;  // div 2
        } else {
            totalBlockWight += static_cast<int64_t>(sOuterBlockNums[i]) * static_cast<int64_t>(sInnerLoopTimes[i]);
        }
    }
    if ((!useBalanceTiling)) {
        accumSOuterTilingNums[0] = 0;
    }

    float coreWightTarget = (float(totalBlockWight * tiling.get_
// ... (truncated due to length) ...

```

### `csrc/attentions/csrc/ops/sparse_block_estimate/op_host/sparse_block_estimate_def.cpp`
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

namespace ops {
class SparseBlockEstimate : public OpDef
{
public:
    explicit SparseBlockEstimate(const char *name) : OpDef(name)
    {
        this->Input("query").ParamType(REQUIRED).DataType({ge::DT_FLOAT16, ge::DT_BF16}).FormatList({ge::FORMAT_ND});
        this->Input("key").ParamType(REQUIRED).DataType({ge::DT_FLOAT16, ge::DT_BF16}).FormatList({ge::FORMAT_ND});
        this->Input("actual_seq_lengths")
            .ParamType(OPTIONAL)
            .ValueDepend(OPTIONAL)
            .DataTypeList({ge::DT_INT64})
            .FormatList({ge::FORMAT_ND});
        this->Input("actual_seq_lengths_kv")
            .ParamType(OPTIONAL)
            .ValueDepend(OPTIONAL)
            .DataTypeList({ge::DT_INT64})
            .FormatList({ge::FORMAT_ND});
        this->Output("sparse_mask").ParamType(REQUIRED).DataTypeList({ge::DT_INT8}).FormatList({ge::FORMAT_ND});
        this->Output("sparse_count_table").ParamType(REQUIRED).DataTypeList({ge::DT_INT32}).FormatList({ge::FORMAT_ND});

        this->Attr("input_layout").AttrType(OPTIONAL).String("BNSD");
        this->Attr("stride").AttrType(OPTIONAL).Int(8);         // stride 大小，默认为8
        this->Attr("sparse_size").AttrType(OPTIONAL).Int(128);  // sparse 块大小，默认为128
        this->Attr("num_heads").AttrType(OPTIONAL).Int(1);
        this->Attr("num_key_value_heads").AttrType(OPTIONAL).Int(1);
        this->Attr("scale_value").AttrType(OPTIONAL).Float(1.0);  // 缩放因子
        this->Attr("threshold").AttrType(OPTIONAL).Float(1.0);
        this->Attr("causal").AttrType(OPTIONAL).Bool(false);
        this->Attr("keep_sink").AttrType(OPTIONAL).Bool(true);
        this->Attr("keep_recent").AttrType(OPTIONAL).Bool(true);
        this->Attr("row_sparse").AttrType(OPTIONAL).Float(1.0);  // ROW_SPARSE 强制稀疏率，当设置大于等于 1
                                                                 // 时不生效，0~1之间生效。 0.4 时表示强制保留 top-40%
                                                                 // (即稀疏率60%)

        this->AICore().AddConfig("ascend910b");
        this->AICore().AddConfig("ascend910_93");
    }
};

OP_ADD(SparseBlockEstimate);
}  // namespace ops

```

### `csrc/attentions/csrc/ops/sparse_block_estimate/op_host/sparse_block_estimate_proto.cpp`
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

static ge::graphStatus SparseBlockEstimateInferShape(gert::InferShapeContext *context)
{
    return ge::GRAPH_SUCCESS;
}

static ge::graphStatus SparseBlockEstimateInferDtype(gert::InferDataTypeContext *context)
{
    return ge::GRAPH_SUCCESS;
}

IMPL_OP_INFERSHAPE(SparseBlockEstimate)
    .InferShape(SparseBlockEstimateInferShape)
    .InferDataType(SparseBlockEstimateInferDtype);

}  // namespace ops

```
