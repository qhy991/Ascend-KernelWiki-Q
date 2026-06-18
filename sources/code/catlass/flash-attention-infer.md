---
id: code-catlass-flash-attention-infer
title: CATLASS Flash Attention Inference Example
type: source-code
repo: Ascend/catlass
path: examples/23_flash_attention_infer
url: https://gitee.com/ascend/catlass/tree/master/examples/23_flash_attention_infer
source_category: upstream-code
architectures:
- ascend910b
tags:
- catlass
- flash-attention
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
- data-reuse
kernel_types:
- attention
- flash-attention
languages:
- cpp
- ascendc
---

# CATLASS Flash Attention Inference Example

CATLASS FlashAttention inference example used as source evidence for streaming attention score/value computation and softmax staging on Ascend.

## Code Location

- Repository: `Ascend/catlass`
- Path: `examples/23_flash_attention_infer`
- URL: https://gitee.com/ascend/catlass/tree/master/examples/23_flash_attention_infer


## Fetched Source


### `examples/23_flash_attention_infer/fai_tiling.cpp`
```cpp
/*
 * Copyright (c) 2025 Huawei Technologies Co., Ltd.
 * This file is a part of the CANN Open Software.
 * Licensed under CANN Open Software License Agreement Version 1.0 (the "License").
 * Please refer to the License for details. You may not use this file except in compliance with the License.
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
 * See LICENSE in the root of the software repository for the full text of the License.
 */

 #include <cstdio>
 #include <cstring>
 #include <fstream>
 #include <iomanip>
 #include <iostream>
 #include <string>
 #include <vector>
 #include <cmath>
 
 using namespace std;
 namespace FAInferTiling {
 const int32_t NUM0 = 0;
 const int32_t NUM1 = 1;
 const int32_t NUM2 = 2;
 const int32_t NUM3 = 3;
 const int32_t NUM4 = 4;
 const int32_t NUM5 = 5;
 const int32_t NUM6 = 6;
 const int32_t NUM7 = 7;
 const int32_t NUM8 = 8;
 const int32_t NUM9 = 9;
 const int32_t NUM10 = 10;
 const int32_t NUM11 = 11;
 const int32_t NUM12 = 12;
 const int32_t NUM13 = 13;
 const int32_t NUM14 = 14;
 const int32_t NUM15 = 15;
 const int32_t NUM16 = 16;
 const int32_t NUM17 = 17;
 const int32_t NUM18 = 18;
 const int32_t NUM19 = 19;
 const int32_t NUM20 = 20;
 const int32_t NUM21 = 21;
 const int32_t NUM32 = 32;
 const int32_t NUM64 = 64;
 const int32_t NUM128 = 128;
 const int32_t NUM256 = 256;
 const int32_t NUM512 = 512;
 const int32_t WORKSPACE_BLOCK_SIZE_DB = 131072;
 
 enum class MaskType{
    NO_MASK = 0, 
    MASK_SPEC = 1, 
    MASK_CAUSUAL = 2
};
 
 struct FAInfo {
     int32_t numTokens = 0;
     int32_t numHeads = 0;
     int32_t embeddingSize = 0;
     int32_t numBlocks = 0;
     int32_t blockSize = 0;
     int32_t kvHeads = 0;
     int32_t batch = 0;
     int64_t *qSeqlenList{nullptr};
     int64_t *kvSeqlenList{nullptr};
     int64_t *qSeqlen{nullptr};
     MaskType maskType = MaskType::MASK_SPEC;
 };
 

 
 void FillBasicTilingData(const FAInfo &faInfo, FATilingData &faTilingData, int64_t maxKvSeqlen)
 {
     uint32_t maxNumBlocksPerBatch = (maxKvSeqlen + faInfo.blockSize - 1) / faInfo.blockSize;
     float scaleValue = static_cast<float>(1.0 / std::sqrt(1.0 * faInfo.embeddingSize));
     faTilingData.batch = static_cast<uint32_t>(faInfo.batch);
     faTilingData.numHeads = static_cast<uint32_t>(faInfo.numHeads);
     faTilingData.kvHeads = static_cast<uint32_t>(faInfo.kvHeads);
     faTilingData.embeddingSize = static_cast<uint32_t>(faInfo.embeddingSize);
     faTilingData.numBlocks = static_cast<uint32_t>(faInfo.numBlocks);
     faTilingData.blockSize = static_cast<uint32_t>(faInfo.blockSize);
     faTilingData.maxKvSeqlen = static_cast<uint32_t>(maxKvSeqlen);
     faTilingData.maxNumBlocksPerBatch = maxNumBlocksPerBatch;
     faTilingData.maskType = static_cast<uint32_t>(faInfo.maskType);
     faTilingData.scaleValue = scaleValue;
 }
 
 uint32_t GetQNBlockTile(int64_t qSeqlen, uint32_t groupSize)
 {
     uint32_t qRowNumCeil = 128;
     // A trick is used to ensure the qN tile is a even number,
     // thus most tasks have balanced workload between two vec cores,
     // and each vec core possess no more than 64 rows when all-rounded row num is no larger than 128,
     // aiding the coding of rescale block
     uint32_t qNBlockTile = (qRowNumCeil / qSeqlen) / 2 * 2;
     qNBlockTile = std::min(qNBlockTile, groupSize);
     qNBlockTile = std::max(qNBlockTile, static_cast<uint32_t>(1));
     return qNBlockTile;
 }
 
 uint32_t GetQSBlockTile(int64_t kvSeqlen)
 {
     uint32_t qSBlockTile = 128;
     return qSBlockTile;
 }
 
 void FillSplitCoreTilingData(const FAInfo &faInfo, FATilingData &faTilingData)
 {
     uint32_t totalTaskNum = 0;
     uint32_t groupSize = faInfo.numHeads / faInfo.kvHeads;
     for (int32_t batchIdx = 0; batchIdx < faInfo.batch; batchIdx++) {
         int64_t qSeqlen = *(faInfo.qSeqlenList + batchIdx);
         int64_t kvSeqlen = *(faInfo.kvSeqlenList + batchIdx);
         uint32_t curQNBlockTile = GetQNBlockTile(qSeqlen, groupSize);
         uint32_t qNBlockNumPerGroup = (groupSize + curQNBlockTile - 1) / curQNBlockTile;
         uint32_t curQNBlockNum = qNBlockNumPerGroup * faInfo.kvHeads;
         uint32_t curQSBlockTile = GetQSBlockTile(kvSeqlen);
         uint32_t curQSBlockNum = (qSeqlen + curQSBlockTile - 1) / curQSBlockTile;
         uint32_t curTaskNum = curQNBlockNum * curQSBlockNum;
         if (batchIdx == 0) {
             faTilingData.firstBatchTaskNum = curTaskNum;
         }
         totalTaskNum += curTaskNum;
     }
     faTilingData.totalTaskNum = totalTaskNum;
 }
 
 void FillWorkSpaceTilingData(uint32_t blockDim, FATilingData &faTilingData)
 {
     uint64_t mm1OutSize = blockDim * WORKSPACE_BLOCK_SIZE_DB * NUM4 * NUM3;
     uint64_t smOnlineOutSize = blockDim * WORKSPACE_BLOCK_SIZE_DB * NUM2 * NUM3;
     uint64_t mm2OutSize = blockDim * WORKSPACE_BLOCK_SIZE_DB * NUM4 * NUM3
// ... (truncated due to length) ...

```

### `examples/23_flash_attention_infer/gen_data.py`
```python
# Copyright (c) 2025 Huawei Technologies Co., Ltd.
# This file is a part of the CANN Open Software.
# Licensed under CANN Open Software License Agreement Version 1.0 (the "License").
# Please refer to the License for details. You may not use this file except in compliance with the License.
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
# See LICENSE in the root of the software repository for the full text of the License.


import os
import sys
import logging
import numpy as np
import random
from ml_dtypes import bfloat16
from dataclasses import dataclass
np.random.seed(1)


WORKSPACE = os.path.dirname(os.path.abspath(__file__))

def gen_seqlen(max_q_seqlen: int, max_kv_seqlen: int, is_varied_len: int, batch: int):
    q_seqlen_list = []
    kv_seqlen_list = []
    if is_varied_len == 0:
        q_seqlen_list = [max_q_seqlen] * batch
        kv_seqlen_list = [max_kv_seqlen] * batch
    else:
        for i in range(batch):
            q_seq = random.randint(1, max_q_seqlen)
            kv_seq = random.randint(1, max_kv_seqlen)
            q_seqlen_list.append(q_seq)
            kv_seqlen_list.append(kv_seq)
    print(q_seqlen_list)
    print(kv_seqlen_list)
    return q_seqlen_list, kv_seqlen_list

class TestFlashAttentionInfer():

    @dataclass
    class AttentionInputs:
        query: any
        key_cache: any
        value_cache: any
        block_tables: any
        q_seqlen_list: any
        k_seqlen_list: any
        global_mask: any
        mask_type: any
        shape_param: any

    @dataclass
    class GenDataParams:
        q_seqlen_list: list
        k_seqlen_list: list
        num_heads: int
        kv_heads: int
        head_size: int
        num_blocks: int
        block_size: int
        mask_type: int
        dtype: any
        kv_dtype: int

    @classmethod
    def check_attr(cls, batch: int, q_seqlen: int, kv_seqlen: int, num_blocks: int, block_size: int):
        if q_seqlen > kv_seqlen:
            logging("[ERROR] q_seqlen cannot exceed kv_seqlen.")
            sys.exit()

    @classmethod
    def group_matmul(cls, head, kv_head, left, right):
        group_num = head // kv_head
        score = None
        for i in range(kv_head):
            group_score = np.matmul(left[i * group_num:(i + 1) * group_num, :, :].astype(np.float32),
                                    right[i:(i + 1), :, :].astype(np.float32))
            if score is None:
                score = group_score
            else:
                score = np.concatenate((score, group_score), 0)
        return score

    @classmethod
    def softmax_numpy(cls, sim):
        row_max = np.max(sim, axis=-1, keepdims=True)
        sim_sub = sim - row_max
        sim_sub = np.exp(sim_sub)
        row_sum = np.sum(sim_sub, axis=-1, keepdims=True)
        soft_res = sim_sub / row_sum
        return soft_res

    def ref_masked_attention(self,
            query,  # (q_seqlen, num_heads, head_size)
            key,    # (k_seqlen, kv_heads, head_size)
            value,
            scale: float,
            mask    # (q_seqlen, k_seqlen)
    ):
        # Q * K.T
        query = query
        query = np.transpose(query, (1, 0, 2))
        key = np.transpose(key, (1, 2, 0))
        sim_high = self.group_matmul(query.shape[0], key.shape[0], query, key)  # (head_num, q_seqlen, k_seqlen)
        sim_high = sim_high * scale
        post_mask_factor = -3e38
        if mask is not None:
            sim_high = sim_high + (
                mask[:sim_high.shape[-2], :sim_high.shape[-1]]
                ).astype(np.float32) * post_mask_factor
        
        # softmax
        p_high = self.softmax_numpy(sim_high)
        p = p_high.astype(query.dtype)
        p_high = p_high.astype(np.float32)
        value = np.transpose(value, (1, 0, 2))
        
        out_high = self.group_matmul(query.shape[0], key.shape[0], p_high, value)
        out = self.group_matmul(query.shape[0], key.shape[0], p, value)
        out_high = np.transpose(out_high, (1, 0, 2))
        out = np.transpose(out, (1, 0, 2))
        out = out.astype(query.dtype)
        return out, out_high

    def ref_single_query_cached_kv_attention(self, attention_inputs: AttentionInputs, output, true_out) -> None:
        num_heads = attention_inputs.shape_param.num_heads
        kv_heads = attention_inputs.shape_param.kv_heads
        head_size_qk = attention_inputs.shape_param.head_size
        head_size_vo = attention_inputs.shape_param.head_size
        block_size = attention_inputs.shape_param.block_size

        batch = len(attention_inputs.shape_param.q_seqlen_list)
        cu_seqlen = 0
        kv_seqlen_now = 0
        for i in range(batch):
            q_seqlen = int(attention_inputs.q_seqlen_list[i])
            k_seqlen = int(attention_inputs.k_seqlen_list[i])
            q = attention_inputs.query[cu_seqlen:(cu_seq
// ... (truncated due to length) ...

```

### `examples/23_flash_attention_infer/fai_kernel.cpp`
```cpp
/*
 * Copyright (c) 2025 Huawei Technologies Co., Ltd.
 * This file is a part of the CANN Open Software.
 * Licensed under CANN Open Software License Agreement Version 1.0 (the "License").
 * Please refer to the License for details. You may not use this file except in compliance with the License.
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
 * See LICENSE in the root of the software repository for the full text of the License.
 */

 #include "catlass/catlass.hpp"
 #include "catlass/arch/arch.hpp"
 #include "catlass/layout/layout.hpp"
 
 #include "catlass/gemm/block/block_mmad.hpp"
 #include "catlass/gemm/dispatch_policy.hpp"
 #include "catlass/gemm/gemm_type.hpp"
 
 #include "catlass/arch/cross_core_sync.hpp"
 #include "catlass/arch/resource.hpp"
 #include "catlass/epilogue/block/block_epilogue.hpp"
 #include "catlass/epilogue/dispatch_policy.hpp"
 #include "catlass/debug.hpp"
 
 #include "kernel_common.hpp"
 #include "kernel_operator.h"
 using namespace Catlass;
 
 
 template <
    class BlockMmadQK,
    class BlockMmadPV,
    class BlockMmadQKTail,
    class BlockMmadPVTail,
    class EpilogueOnlineSoftmax,
    class EpilogueRescaleO,
    bool PAGED_CACHE_FLAG>
class FAInferKernel {
public:
    using ArchTag = typename BlockMmadQK::ArchTag;
    using L1TileShape = typename BlockMmadQK::L1TileShape;
    using ElementQ = typename BlockMmadQK::ElementA;
    using LayoutQ = typename BlockMmadQK::LayoutA;
    using ElementK = typename BlockMmadQK::ElementB;
    using LayoutK = typename BlockMmadQK::LayoutB;
    using ElementS = typename BlockMmadQK::ElementC;
    using LayoutS = typename BlockMmadQK::LayoutC;

    using ElementP = typename BlockMmadPV::ElementA;
    using LayoutP = typename BlockMmadPV::LayoutA;
    using ElementV = typename BlockMmadPV::ElementB;
    using LayoutV = typename BlockMmadPV::LayoutB;

    using ElementMask = typename EpilogueOnlineSoftmax::ElementMask;
    using LayoutMask = typename EpilogueOnlineSoftmax::LayoutMask;

    using ElementO = typename EpilogueRescaleO::ElementOutput;
    using LayoutO = typename EpilogueRescaleO::LayoutOutput;

    using ElementOTmp = typename EpilogueRescaleO::ElementInput;
    using LayoutOTmp = typename EpilogueRescaleO::LayoutInput;

    // Methods
    CATLASS_DEVICE
    FAInferKernel() {}

    template <int32_t CORE_TYPE = g_coreType>
    CATLASS_DEVICE void operator()(FAIKernelParams const &params);

    template <>
    CATLASS_DEVICE void operator()<AscendC::AIC>(FAIKernelParams const &params)
    {
        AscendC::SetFlag<AscendC::HardEvent::M_MTE1>(EVENT_ID0);
        AscendC::SetFlag<AscendC::HardEvent::M_MTE1>(EVENT_ID1);
        AscendC::SetFlag<AscendC::HardEvent::M_MTE1>(EVENT_ID2);
        AscendC::SetFlag<AscendC::HardEvent::M_MTE1>(EVENT_ID3);
        AscendC::SetFlag<AscendC::HardEvent::M_MTE1>(EVENT_ID4);
        AscendC::SetFlag<AscendC::HardEvent::M_MTE1>(EVENT_ID5);
        AscendC::SetFlag<AscendC::HardEvent::M_MTE1>(EVENT_ID6);
        AscendC::SetFlag<AscendC::HardEvent::M_MTE1>(EVENT_ID7);
        AscendC::SetFlag<AscendC::HardEvent::FIX_M>(EVENT_ID0);
        AscendC::SetFlag<AscendC::HardEvent::FIX_M>(EVENT_ID1);
        AscendC::SetFlag<AscendC::HardEvent::MTE1_MTE2>(EVENT_ID0);
        AscendC::SetFlag<AscendC::HardEvent::MTE1_MTE2>(EVENT_ID1);
        AscendC::SetFlag<AscendC::HardEvent::MTE1_MTE2>(EVENT_ID2);
        AscendC::SetFlag<AscendC::HardEvent::MTE1_MTE2>(EVENT_ID3);
        AscendC::SetFlag<AscendC::HardEvent::MTE1_MTE2>(EVENT_ID4);
        AscendC::SetFlag<AscendC::HardEvent::MTE1_MTE2>(EVENT_ID5);
        AscendC::SetFlag<AscendC::HardEvent::MTE1_MTE2>(EVENT_ID6);
        AscendC::SetFlag<AscendC::HardEvent::MTE1_MTE2>(EVENT_ID7);
        static constexpr uint32_t L1_QK_SIZE = BlockMmadQK::L1TileShape::M * BlockMmadQK::L1TileShape::K * sizeof(ElementQ) + 
                                             BlockMmadQK::L1TileShape::N * BlockMmadQK::L1TileShape::K * sizeof(ElementK) * 2;
        BlockMmadQK blockMmadQK(resource);
        BlockMmadPV blockMmadPV(resource, L1_QK_SIZE);

        BlockMmadQKTail blockMmadQKTail(resource);
        BlockMmadPVTail blockMmadPVTail(resource, L1_QK_SIZE);
        __gm__ FATilingData *fATilingData = reinterpret_cast<__gm__ FATilingData *>(params.tiling);
        uint64_t mm1OutSize = fATilingData->mm1OutSize;
        uint64_t smOnlineOutSize = fATilingData->smOnlineOutSize;
        uint32_t batch = fATilingData->batch;
        uint32_t qHeads = fATilingData->numHeads;
        uint32_t kvHeads = fATilingData->kvHeads;
        uint32_t embed = fATilingData->embeddingSize;
        uint32_t pagedBlockSize = fATilingData->blockSize;
        uint32_t maxNumBlocksPerBatch = fATilingData->maxNumBlocksPerBatch;
        uint32_t curTotalTaskNum = fATilingData->firstBatchTaskNum;
        uint32_t totalTaskNum = fATilin
// ... (truncated due to length) ...

```
