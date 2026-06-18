---
id: code-sgl-kernel-npu-block-sparse-attention
title: SGL Kernel NPU Block Sparse Attention Operator
type: source-code
repo: sgl-project/sgl-kernel-npu
path: csrc/attentions/csrc/ops/block_sparse_attention
url: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/attentions/csrc/ops/block_sparse_attention
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- sglang
- block-sparse-attention
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
- kv-cache-paging
- pipeline-scheduling
kernel_types:
- attention
- paged-attention
- flash-attention
languages:
- cpp
- ascendc
---

# SGL Kernel NPU Block Sparse Attention Operator

SGL Kernel NPU block sparse attention implementation, providing production-style evidence for sparse attention tiling and cache-aware inference kernels.

## Code Location

- Repository: `sgl-project/sgl-kernel-npu`
- Path: `csrc/attentions/csrc/ops/block_sparse_attention`
- URL: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/attentions/csrc/ops/block_sparse_attention


## Fetched Source


### `csrc/attentions/csrc/ops/block_sparse_attention/op_host/data_copy_transpose_tiling.h`
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

#ifndef DATA_COPY_TRANSPOSE_TILING_H
#define DATA_COPY_TRANSPOSE_TILING_H

#pragma once

#include <vector>
#include <graph/tensor.h>
#include "data_copy_transpose_tiling_def.h"

namespace optiling {

inline void GetDataCopyTransposeTiling(const ge::Shape &dstShape, const ge::Shape &srcShape, const uint32_t typeSize,
                                       optiling::CopyTransposeTiling &tiling)
{
    std::vector<int64_t> dstShapeInfo = dstShape.GetDims();
    std::vector<int64_t> srcShapeInfo = srcShape.GetDims();

    tiling.set_dstShapeB(dstShapeInfo[0]);
    tiling.set_dstShapeN(dstShapeInfo[1]);
    tiling.set_dstShapeS(dstShapeInfo[2]);  // 2 is dim2
    tiling.set_dstShapeH(dstShapeInfo[3]);  // 3 is dim3
    tiling.set_dstShapeHN(tiling.get_dstShapeH() / tiling.get_dstShapeN());

    tiling.set_srcShapeB(srcShapeInfo[0]);
    tiling.set_srcShapeN(srcShapeInfo[1]);
    tiling.set_srcShapeS(srcShapeInfo[2]);   // 2 is dim2
    tiling.set_srcShapeHN(srcShapeInfo[3]);  // 3 is dim3
    tiling.set_originalShapeNLen(tiling.get_srcShapeHN() * typeSize);
    tiling.set_shapeSHValue(tiling.get_dstShapeS() * tiling.get_dstShapeH());
    tiling.set_shapeNsValue(tiling.get_dstShapeN() * tiling.get_dstShapeS());
    tiling.set_shapeNsnValue(tiling.get_dstShapeN() * tiling.get_srcShapeS() * tiling.get_srcShapeN());
    tiling.set_shapeBHValue(tiling.get_dstShapeB() * tiling.get_dstShapeH());
}

}  // namespace optiling
#endif  // DATA_COPY_TRANSPOSE_TILING__H

```

### `csrc/attentions/csrc/ops/block_sparse_attention/op_host/block_sparse_attention_tiling.h`
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

#ifndef AIR_CXX_RUNTIME_V2_OP_IMPL_SPARSEBSA_H_
#define AIR_CXX_RUNTIME_V2_OP_IMPL_SPARSEBSA_H_
#include <cstdint>
#include <vector>
#include <queue>
#include <string>
#include "exe_graph/runtime/tiling_context.h"
#include "data_copy_transpose_tiling_def.h"
#include "data_copy_transpose_tiling.h"

#include "register/tilingdata_base.h"
#include "tiling/tiling_api.h"

#include "register/op_def_registry.h"
#ifdef ASCENDC_OP_TEST
#define BSA_EXTERN_C extern "C"
#else
#define BSA_EXTERN_C
#endif

#include "block_sparse_attention_tiling_compile_info.h"
#include "block_sparse_attention_tiling_const.h"
#include "block_sparse_attention_tiling_context.h"
#include "block_sparse_attention_tiling_struct.h"

namespace optiling {
BEGIN_TILING_DATA_DEF(PromptAttentionBaseParams)
TILING_DATA_FIELD_DEF(uint8_t, causal);  // bool(uint8)
TILING_DATA_FIELD_DEF(uint32_t, sparseSize);
TILING_DATA_FIELD_DEF(uint32_t, sparseMaskS1);
TILING_DATA_FIELD_DEF(uint32_t, sparseMaskS2);
TILING_DATA_FIELD_DEF(uint32_t, batchSize);
TILING_DATA_FIELD_DEF(uint32_t, headNumSize);
TILING_DATA_FIELD_DEF(uint32_t, seqSize);
TILING_DATA_FIELD_DEF(uint32_t, headSize);
TILING_DATA_FIELD_DEF(float, scaleValue);
TILING_DATA_FIELD_DEF(int32_t, preTokens);
TILING_DATA_FIELD_DEF(int32_t, nextTokens);
TILING_DATA_FIELD_DEF(int32_t, blockSize);
TILING_DATA_FIELD_DEF(int32_t, blockTableDim2);
TILING_DATA_FIELD_DEF(int32_t, PABlockNumSum);
TILING_DATA_FIELD_DEF(uint32_t, dimNumOfseq);
TILING_DATA_FIELD_DEF(uint32_t, typeByteNum);
TILING_DATA_FIELD_DEF(uint32_t, seqInnerSize);
TILING_DATA_FIELD_DEF(uint32_t, prefixSeqInnerSize);
TILING_DATA_FIELD_DEF(uint32_t, usePseShift);
TILING_DATA_FIELD_DEF(uint32_t, useMask);
TILING_DATA_FIELD_DEF(uint32_t, headNumRatio);
TILING_DATA_FIELD_DEF(uint32_t, attenMaskElemType);
TILING_DATA_FIELD_DEF(uint32_t, pseShiftTypeByteNum);
TILING_DATA_FIELD_DEF(uint32_t, pseMaskMaxSize);
TILING_DATA_FIELD_DEF(uint32_t, maskTypeByteNum);
TILING_DATA_FIELD_DEF(uint32_t, outputTypeByteNum);
TILING_DATA_FIELD_DEF(uint32_t, softmaxTypeByteNum);
TILING_DATA_FIELD_DEF(uint32_t, sparseMode);
TILING_DATA_FIELD_DEF(uint32_t, alignedHeadSize);
TILING_DATA_FIELD_DEF(uint32_t, splitS2);
TILING_DATA_FIELD_DEF(uint32_t, splitD);
TILING_DATA_FIELD_DEF(uint32_t, layoutType);
TILING_DATA_FIELD_DEF(uint32_t, PAlayoutType);
TILING_DATA_FIELD_DEF(uint32_t, pseShiftS1Size);
TILING_DATA_FIELD_DEF(uint32_t, pseShiftS2Size);
TILING_DATA_FIELD_DEF(uint32_t, maskKVsSize);
TILING_DATA_FIELD_DEF(uint32_t, maskQsSize);
TILING_DATA_FIELD_DEF(uint32_t, isLayoutSH);
TILING_DATA_FIELD_DEF(uint32_t, isActualSeqLengthsNull);
TILING_DATA_FIELD_DEF(uint32_t, isActualSeqLengthsKVNull);
TILING_DATA_FIELD_DEF(uint32_t, actualSeqLengthsSize);
TILING_DATA_FIELD_DEF(uint32_t, actualSeqLengthsKVSize);
TILING_DATA_FIELD_DEF(uint32_t, deqScaleFlag);
TILING_DATA_FIELD_DEF(uint32_t, deqScale2Flag);
TILING_DATA_FIELD_DEF(uint32_t, isAntiPerchannel);
TILING_DATA_FIELD_DEF(uint32_t, isRowInvalid);
TILING_DATA_FIELD_DEF(uint32_t, softmaxOuterSize);
TILING_DATA_FIELD_DEF(uint32_t, isQuant2Perchannel);
TILING_DATA_FIELD_DEF(uint32_t, isQuant2BF16);
TILING_DATA_FIELD_DEF(uint32_t, isKvContinuous);
TILING_DATA_FIELD_DEF(uint32_t, fromFused);
TILING_DATA_FIELD_DEF(uint32_t, isBSNDOut);
TILING_DATA_FIELD_DEF(uint32_t, isIFA);
TILING_DATA_FIELD_DEF(uint32_t, isSoftMaxLseEnable);
TILING_DATA_FIELD_DEF(uint32_t, isActualSharedPrefixLenNull);
TILING_DATA_FIELD_DEF(uint32_t, isQHasLeftPadding);
TILING_DATA_FIELD_DEF(uint32_t, isKVHasLeftPadding);
TILING_DATA_FIELD_DEF(int64_t, keyAntiquantMode);
TILING_DATA_FIELD_DEF(int64_t, valueAntiquantMode);
TILING_DATA_FIELD_DEF(uint32_t, hasKeyAntiquantOffset);
TILING_DATA_FIELD_DEF(uint32_t, isMsd);
TILING_DATA_FIELD_DEF(uint32_t, isQuant2FP16);
TILING_DATA_FIELD_DEF(uint32_t, ropeHeadSize);
TILING_DATA_FIELD_DEF(uint32_t, qkHeadSize);
TILING_DATA_FIELD_DEF(uint32_t, vHeadSize);
TILING_DATA_FIELD_DEF(uint32_t, gOfMla);
END_TILING_DATA_DEF;
REGISTER_TILING_DATA_CLASS(PromptAttentionBaseParamsOp, PromptAttentionBaseParams)

BEGIN_TILING_DATA_DEF(PromptAttentionBaseApiBaseParams)
TILING_DATA_FIELD_DEF(uint32_t, batchSize);
TILING_DATA_FIELD_DEF(uint32_t, headNumSize);
TILING_DATA_FIELD_DEF(uint32_t, headSize);
TILING_DATA_FIELD_DEF(uint32_t, maskTypeByteNum);

TILING_DATA_FIELD_DEF(uint32_t, inputLayoutType);
TILING_DATA_FIELD_DEF(uint32_t, kvHeadNumSize);
TILING_DATA_FIELD_DEF(uint32_t, maxSeqLen);
TILING_DATA_FIELD_DEF(uint32_t, maxKvSeqLe
// ... (truncated due to length) ...

```

### `csrc/attentions/csrc/ops/block_sparse_attention/op_host/block_sparse_attention_def.cpp`
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
class BlockSparseAttention : public OpDef
{
public:
    explicit BlockSparseAttention(const char *name) : OpDef(name)
    {
        this->Input("query")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_BF16,    ge::DT_INT8,    ge::DT_INT8, ge::DT_BF16,
                       ge::DT_INT8,    ge::DT_INT8,    ge::DT_BF16,    ge::DT_INT8,    ge::DT_INT8, ge::DT_FLOAT16,
                       ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_BF16, ge::DT_INT8,
                       ge::DT_INT8,    ge::DT_BF16,    ge::DT_INT8,    ge::DT_INT8,    ge::DT_BF16, ge::DT_INT8,
                       ge::DT_INT8,    ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_BF16, ge::DT_BF16,
                       ge::DT_FLOAT16, ge::DT_FLOAT16})
            .FormatList({ge::FORMAT_ND});
        this->Input("key")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_BF16,    ge::DT_INT8,    ge::DT_INT8, ge::DT_BF16,
                       ge::DT_INT8,    ge::DT_INT8,    ge::DT_BF16,    ge::DT_INT8,    ge::DT_INT8, ge::DT_FLOAT16,
                       ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_BF16, ge::DT_INT8,
                       ge::DT_INT8,    ge::DT_BF16,    ge::DT_INT8,    ge::DT_INT8,    ge::DT_BF16, ge::DT_INT8,
                       ge::DT_INT8,    ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_BF16, ge::DT_BF16,
                       ge::DT_FLOAT16, ge::DT_FLOAT16})
            .FormatList({ge::FORMAT_ND});
        this->Input("value")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_BF16,    ge::DT_INT8,    ge::DT_INT8, ge::DT_BF16,
                       ge::DT_INT8,    ge::DT_INT8,    ge::DT_BF16,    ge::DT_INT8,    ge::DT_INT8, ge::DT_FLOAT16,
                       ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_BF16, ge::DT_INT8,
                       ge::DT_INT8,    ge::DT_BF16,    ge::DT_INT8,    ge::DT_INT8,    ge::DT_BF16, ge::DT_INT8,
                       ge::DT_INT8,    ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_BF16, ge::DT_BF16,
                       ge::DT_FLOAT16, ge::DT_FLOAT16})
            .FormatList({ge::FORMAT_ND});
        this->Input("pse_shift")
            .ParamType(OPTIONAL)
            .DataType({ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_BF16,    ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_BF16,
                       ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_BF16,    ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_FLOAT16,
                       ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_BF16,    ge::DT_FLOAT16,
                       ge::DT_FLOAT16, ge::DT_BF16,    ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_BF16,    ge::DT_FLOAT16,
                       ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_BF16,    ge::DT_BF16,
                       ge::DT_FLOAT16, ge::DT_FLOAT16})
            .FormatList({ge::FORMAT_ND});
        this->Input("atten_mask")
            .ParamType(OPTIONAL)
            .DataType({ge::DT_FLOAT16, ge::DT_BOOL,  ge::DT_BOOL,  ge::DT_BOOL,  ge::DT_BOOL, ge::DT_INT8, ge::DT_INT8,
                       ge::DT_INT8,    ge::DT_UINT8, ge::DT_UINT8, ge::DT_UINT8, ge::DT_BOOL, ge::DT_INT8, ge::DT_UINT8,
                       ge::DT_FLOAT16, ge::DT_BOOL,  ge::DT_BOOL,  ge::DT_BOOL,  ge::DT_BOOL, ge::DT_INT8, ge::DT_INT8,
                       ge::DT_INT8,    ge::DT_UINT8, ge::DT_UINT8, ge::DT_UINT8, ge::DT_BOOL, ge::DT_INT8, ge::DT_UINT8,
                       ge::DT_BOOL,    ge::DT_BOOL,  ge::DT_INT8,  ge::DT_UINT8})
            .FormatList({ge::FORMAT_ND});
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
        this->Input("deq_scale1")
            .ParamType(OPTIONAL)
            .DataType({ge::DT_UINT64, ge::DT_UINT64, ge::DT_UINT64, ge::DT_UINT64, ge::DT_UINT64, ge::DT_UINT64,
                       ge::DT_UINT64, ge::DT_UINT64, ge::DT_UINT64, ge::DT_UINT64, ge::DT_UINT64, ge::DT_UINT64,
  
// ... (truncated due to length) ...

```
