---
id: code-sgl-kernel-npu-cache-location-assign
title: SGL Kernel NPU Cache Location Assign Operator
type: source-code
repo: sgl-project/sgl-kernel-npu
path: csrc/cache_location_assign
url: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/cache_location_assign
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- sglang
- kv-cache
- scheduling
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
- tiling-strategy
- pipeline-scheduling
kernel_types:
- attention
- elementwise
languages:
- cpp
- ascendc
---

# SGL Kernel NPU Cache Location Assign Operator

SGL Kernel NPU cache-location assignment operator with tiling metadata, useful for mining serving-side KV-cache placement patterns.

## Code Location

- Repository: `sgl-project/sgl-kernel-npu`
- Path: `csrc/cache_location_assign`
- URL: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/cache_location_assign


## Fetched Source


### `csrc/cache_location_assign/op_host/cache_loc_assign.cpp`
```cpp
// Licensed under the BSD 3-Clause License  (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include <stdexcept>
#include "defines.h"
#include "common.h"
#include "torch_helper.h"
#include "tiling/platform/platform_ascendc.h"
#include "tiling/cache_loc_assign.h"
#include "aclrtlaunch_cache_loc_assign.h"

namespace sglang {
namespace npu_kernel {

at::Tensor getTiling(const at::Tensor &reqPoolIndices, uint64_t rowSize, uint64_t poolSize, uint32_t &blockDim,
                     bool isUpddate)
{
    auto batchSize = reqPoolIndices.sizes()[0];
    auto ascendcPlatform = platform_ascendc::PlatformAscendCManager::GetInstance();
    if (isUpddate) {
        blockDim = 1;  // todo: support mulitcore calculate for update
    } else {
        blockDim = ascendcPlatform->GetCoreNumAiv();
    }

    auto tilingBuffer =
        at::empty({sizeof(AssignCacheTillingData)}, at::TensorOptions().dtype(at::kByte).device(at::kCPU));
    AssignCacheTillingData *tillingData = reinterpret_cast<AssignCacheTillingData *>(tilingBuffer.data_ptr());
    tillingData->vcoreNum = blockDim;
    tillingData->poolSize = poolSize;
    tillingData->batchSize = batchSize;
    tillingData->rowNumNoTail = batchSize / (tillingData->vcoreNum);
    tillingData->tailNum = batchSize % (tillingData->vcoreNum);
    tillingData->rowSize = rowSize;

    if (reqPoolIndices.options().dtype() == at::kInt) {
        tillingData->key = 1;
        tillingData->reqInxBufferCount = host_utils::alinInt32Count(batchSize);
        tillingData->reqInxBufferSize = tillingData->reqInxBufferCount * sizeof(int32_t);
    } else if (reqPoolIndices.options().dtype() == at::kLong) {
        tillingData->key = 2;
        tillingData->reqInxBufferCount = host_utils::alinInt64Count(batchSize);
        tillingData->reqInxBufferSize = tillingData->reqInxBufferCount * sizeof(int64_t);
    }

    tillingData->tokenCountAlignInt32 = host_utils::alinInt32Count(MAX_STEP);
    tillingData->tokenColAlignInt32 = tillingData->tokenCountAlignInt32 * sizeof(int32_t);

    tillingData->offsetCountAlignInt64 = host_utils::alinInt64Count(batchSize);
    tillingData->offsetColAlignInt64 = tillingData->offsetCountAlignInt64 * sizeof(int64_t);

    tillingData->cacheLocSize = batchSize * MAX_STEP;
    tillingData->cacheLocCountAlignInt32 = host_utils::alinInt32Count(tillingData->cacheLocSize);
    tillingData->cacheLocAlignInt32 = tillingData->cacheLocCountAlignInt32 * sizeof(int32_t);

    uint64_t ubSize;
    ascendcPlatform->GetCoreMemSize(platform_ascendc::CoreMemType::UB, ubSize);
    uint64_t ubBufferSizeToUse = tillingData->tokenColAlignInt32 + 3 * tillingData->offsetColAlignInt64 +
                                 3 * batchSize * sizeof(int32_t) + tillingData->cacheLocAlignInt32;
    if (ubBufferSizeToUse > ubSize) {
        throw std::invalid_argument("Batch size is too large, buffer is not enough to do calculate");
    }

    auto tilingTensor = TorchNpuHelper::CopyTensorHostToDevice(tilingBuffer);
    return tilingTensor;
}

HOST_API void checkParams(const at::Tensor &reqPoolIndices, const at::Tensor &tokenPool, const at::Tensor &startOffset,
                          const at::Tensor &endOffset, const at::Tensor &outCacheLoc)
{
    auto reqIdxType = reqPoolIndices.options().dtype();
    if ((reqIdxType != at::kInt && reqIdxType != at::kLong) || tokenPool.options().dtype() != at::kInt ||
        startOffset.options().dtype() != at::kLong || endOffset.options().dtype() != at::kLong ||
        outCacheLoc.options().dtype() != at::kInt) {
        throw std::invalid_argument(
            "Only support inputTensor combo1: int64, int32, int64, int64, int32; combo2: "
            "int32, int32, int64, int64, int32");
    }
}

HOST_API at::Tensor cache_loc_assign(const at::Tensor &reqPoolIndices, const at::Tensor &tokenPool,
                                     const at::Tensor &startOffset, const at::Tensor &endOffset,
                                     const at::Tensor &outCacheLoc)
{
    checkParams(reqPoolIndices, tokenPool, startOffset, endOffset, outCacheLoc);
    uint32_t blockDim;
    uint32_t cacheAssignMode = 0;
    at::Tensor tilingTensor = getTiling(reqPoolIndices, tokenPool.sizes()[1], tokenPool.sizes()[0], blockDim, false);

    EXEC_KERNEL_CMD(cache_loc_assign, blockDim, reqPoolIndices, tokenPool, startOffset, endOffset, outCacheLoc,
                    tilingTensor, cacheAssignMode);
    return tokenPool;
}

HOST_API at::Tensor cache_loc_update(const at::Tensor &reqPoolIndices, const at::Tensor &tokenPool,
                                     const at::Tensor &startOffset, co
// ... (truncated due to length) ...

```

### `csrc/cache_location_assign/op_host/tiling/cache_loc_assign.h`
```cpp
// Licensed under the BSD 3-Clause License  (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#ifndef CACHE_LOC_ASSIGN_TILING_H
#define CACHE_LOC_ASSIGN_TILING_H

#include <cstdint>

struct AssignCacheTillingData {
    uint64_t key{0};

    uint64_t vcoreNum{0};
    uint64_t poolSize{0};
    uint64_t batchSize{0};
    uint64_t rowNumNoTail{0};
    uint64_t tailNum{0};
    uint64_t rowSize{0};

    uint64_t reqInxBufferCount{0};
    uint64_t reqInxBufferSize{0};

    uint64_t tokenCountAlignInt32{0};
    uint64_t tokenColAlignInt32{0};

    uint64_t offsetCountAlignInt64{0};
    uint64_t offsetColAlignInt64{0};

    uint64_t cacheLocSize{0};
    uint64_t cacheLocCountAlignInt32{0};
    uint64_t cacheLocAlignInt32{0};
};

constexpr uint32_t MAX_STEP = 16;

#endif  // CACHE_LOC_ASSIGN_TILING_H

```

### `csrc/cache_location_assign/op_kernel/cache_loc_assign_kernel.cpp`
```cpp
// Licensed under the BSD 3-Clause License  (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#ifndef SGL_KERNEL_NPU_KERNEL_CACHE_LOC_ASSIGN_H
#define SGL_KERNEL_NPU_KERNEL_CACHE_LOC_ASSIGN_H

/* include file of ascendc */
#include "kernel_operator.h"
#include "../op_host/tiling/cache_loc_assign.h"

/* tensor num for each queue */
constexpr int32_t BUFFER_NUM = 2;

constexpr uint32_t ASSIGN_TO_POOL = 0;
constexpr uint32_t RETRIEVE_FROM_POOL = 1;

template <typename T>
class CacheLocAssignKernel
{
public:
    __aicore__ inline CacheLocAssignKernel() {}

    __aicore__ inline void Init(GM_ADDR reqPoolIndices, GM_ADDR tokenPool, GM_ADDR startOffset, GM_ADDR endOffset,
                                GM_ADDR outCacheLoc, __gm__ AssignCacheTillingData *tempTilingGM)
    {
        this->coreId = AscendC::GetBlockIdx();
        this->batchSize = tempTilingGM->batchSize;
        this->vcoreNum = tempTilingGM->vcoreNum;
        this->rowNumNoTail = tempTilingGM->rowNumNoTail;
        this->tailNum = tempTilingGM->tailNum;
        if (this->coreId < this->tailNum) {
            this->rowNum = this->rowNumNoTail + 1;
            this->tailOffset = this->coreId;
        } else {
            this->rowNum = this->rowNumNoTail;
            this->tailOffset = this->tailNum;
        }
        this->rowSize = tempTilingGM->rowSize;
        this->reqInxBufferCount = tempTilingGM->reqInxBufferCount;
        this->tokenCountAlignInt32 = tempTilingGM->tokenCountAlignInt32;
        this->offsetCountAlignInt64 = tempTilingGM->offsetCountAlignInt64;
        this->cacheLocCountAlignInt32 = tempTilingGM->cacheLocCountAlignInt32;
        this->cacheLocSize = tempTilingGM->cacheLocSize;

        this->rowOffset = this->rowNumNoTail * this->coreId + this->tailOffset;
        this->reqPoolIndicesGM.SetGlobalBuffer((__gm__ T *)reqPoolIndices, this->batchSize);
        this->tokenPoolGM.SetGlobalBuffer((__gm__ int32_t *)tokenPool, tempTilingGM->poolSize * this->rowSize);
        this->startOffsetGm.SetGlobalBuffer((__gm__ int64_t *)startOffset, this->batchSize);
        this->endOffsetGM.SetGlobalBuffer((__gm__ int64_t *)endOffset, this->batchSize);
        this->cacheLocGM.SetGlobalBuffer((__gm__ int32_t *)outCacheLoc, this->cacheLocSize);

        AscendC::TBuf<AscendC::TPosition::VECCALC> tmpBuff1, tmpBuff2, tmpBuff3, tmpBuff4, tmpBuff5, tmpBuff6, tmpBuff7;
        this->pipe.InitBuffer(tmpBuff1, tempTilingGM->reqInxBufferSize);
        this->pipe.InitBuffer(tmpBuff2, tempTilingGM->offsetColAlignInt64);
        this->pipe.InitBuffer(tmpBuff3, tempTilingGM->offsetColAlignInt64);
        uint64_t offsetBufferInt32 = this->batchSize * sizeof(int32_t);
        this->pipe.InitBuffer(tmpBuff4, offsetBufferInt32);
        this->pipe.InitBuffer(tmpBuff5, offsetBufferInt32);
        this->pipe.InitBuffer(tmpBuff6, offsetBufferInt32);
        this->pipe.InitBuffer(tmpBuff7, tempTilingGM->cacheLocAlignInt32);

        this->ubReqPoolIndices = tmpBuff1.Get<T>();
        this->ubStartOffset = tmpBuff2.Get<int64_t>();
        this->ubEndOffset = tmpBuff3.Get<int64_t>();
        this->ubStartOffsetInt32 = tmpBuff4.Get<int32_t>();
        this->ubEndOffsetInt32 = tmpBuff5.Get<int32_t>();

        this->ubCacheLength = tmpBuff6.Get<int32_t>();
        this->ubCacheLoc = tmpBuff7.Get<int32_t>();

        this->pipe.InitBuffer(this->inQueue1, BUFFER_NUM, tempTilingGM->tokenColAlignInt32);
    }

    __aicore__ inline void ProcessForTokenPoolAssign()
    {
        if (this->rowNum > 0) {
            PreProcess();
            for (int32_t i = 0; i < this->rowNum; i++) {
                uint64_t rowIdx = this->rowOffset + i;
                uint64_t reqIdx = this->ubReqPoolIndices.GetValue(rowIdx);
                CopyIn(rowIdx, reqIdx);
                ComputeForTokenPoolAssign(rowIdx, reqIdx);
            }
        }
    }

    __aicore__ inline void ProcessForCacheUpdate()
    {
        if (this->rowNum > 0) {
            PreProcess();
            for (int32_t i = 0; i < this->rowNum; i++) {
                uint64_t rowIdx = this->rowOffset + i;
                uint64_t reqIdx = this->ubReqPoolIndices.GetValue(rowIdx);
                CopyIn(rowIdx, reqIdx);
                ComputeForCacheUpdate(rowIdx);
            }

            int32_t eventIDVTOMTE3 = static_cast<int32_t>(GetTPipePtr()->FetchEventID(AscendC::HardEvent::V_MTE3));
            AscendC::SetFlag<AscendC::HardEvent::V_MTE3>(eventIDVTOMTE3);
            AscendC::WaitFlag<AscendC::HardEvent::V_MTE3>(eventIDVTOMTE3);

            uint32_t cacheBytes = static_cast<uint32_t>(this->cacheLocSize * size
// ... (truncated due to length) ...

```
