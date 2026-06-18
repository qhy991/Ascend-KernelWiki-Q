---
id: code-sgl-kernel-npu-assign-cache
title: SGL Kernel NPU Assign Cache Operator
type: source-code
repo: sgl-project/sgl-kernel-npu
path: csrc/assign_cache_op
url: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/assign_cache_op
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- sglang
- kv-cache
- cache
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

# SGL Kernel NPU Assign Cache Operator

SGL Kernel NPU assign-cache operator providing code evidence for KV-cache write and placement logic around attention-serving pipelines.

## Code Location

- Repository: `sgl-project/sgl-kernel-npu`
- Path: `csrc/assign_cache_op`
- URL: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/assign_cache_op


## Fetched Source


### `csrc/assign_cache_op/op_host/assign_cache.cpp`
```cpp
#include <iostream>
#include "acl/acl.h"
#include "kernel_tiling/kernel_tiling.h"
#include "tiling/platform/platform_ascendc.h"
#include "tiling_data.h"
#include "defines.h"
#include "torch_helper.h"
#include "aclrtlaunch_assign_cache_op.h"

namespace sglang {
namespace npu_kernel {
using namespace custom_assign;

#define OP_CHECK(expression, error_msg, action)                                                                \
    do {                                                                                                       \
        if (!expression) {                                                                                     \
            std::cerr << "[ERROR] " << (error_msg) << " [" << __FILE__ << ":" << __LINE__ << "]" << std::endl; \
            action;                                                                                            \
        }                                                                                                      \
    } while (0)

HOST_API at::Tensor GetTilingTensor(CustomAssignTilingData &tilingData, size_t tilingSize)
{
    auto buffer = at::empty({static_cast<int64_t>(tilingSize)}, at::kByte);
    tilingData.SetToBuffer(buffer.data_ptr<uint8_t>(), tilingSize);
    auto tilingTensor = TorchNpuHelper::CopyTensorHostToDevice(buffer);
    return tilingTensor;
}

HOST_API size_t GetElementByteSize(const at::Tensor &tensor)
{
    at::ScalarType dtype = tensor.scalar_type();
    return at::elementSize(dtype);
}

HOST_API bool assign_cache_op(at::Tensor &dstTensor, const at::Tensor &srcTensor, const at::Tensor &dstStartIdx,
                              const at::Tensor &dstEndIdx, const at::Tensor &srcStartIdx, const at::Tensor &srcEndIdx)
{
    OP_CHECK(dstTensor.defined() && dstTensor.dim() >= 1, "dstTensor is invalid or 0-dimensional", return false);
    OP_CHECK(srcTensor.defined() && srcTensor.dim() >= 1, "srcTensor is invalid or 0-dimensional", return false);
    OP_CHECK(dstStartIdx.defined() && dstStartIdx.dim() >= 1, "dstStartIdx is invalid or 0-dimensional", return false);
    OP_CHECK(dstEndIdx.defined() && dstEndIdx.dim() >= 1, "dstEndIdx is invalid or 0-dimensional", return false);
    OP_CHECK(srcStartIdx.defined() && srcStartIdx.dim() >= 1, "srcStartIdx is invalid or 0-dimensional", return false);
    OP_CHECK(srcEndIdx.defined() && srcEndIdx.dim() >= 1, "srcEndIdx is invalid or 0-dimensional", return false);
    auto dstShape = dstTensor.sizes(), dstStartShape = dstStartIdx.sizes(), dstEndShape = dstEndIdx.sizes();
    auto srcShape = srcTensor.sizes(), srcStartShape = srcStartIdx.sizes(), srcEndShape = srcEndIdx.sizes();
    OP_CHECK(dstShape[0] == srcShape[0] && dstStartShape[0] == srcStartShape[0] && dstEndShape[0] == srcEndShape[0],
             "batch size is not same between srcTensor and dstTensor", return false);
    OP_CHECK(dstShape[0] == dstStartShape[0] && dstShape[0] == dstEndShape[0],
             "batch size is not same between srcTensor and dstTensor", return false);

    auto ascendcPlatform = platform_ascendc::PlatformAscendCManager::GetInstance();
    uint32_t blockDim = static_cast<uint32_t>(ascendcPlatform->GetCoreNumAiv());
    uint64_t ubSize;
    ascendcPlatform->GetCoreMemSize(platform_ascendc::CoreMemType::UB, ubSize);
    uint32_t eleBytes = GetElementByteSize(dstTensor);
    uint32_t syncWorkspaceSize = blockDim * 32 + blockDim * 32 + 32;
    struct CustomAssignTilingData tilingData = {.batchSize = static_cast<uint32_t>(dstShape[0]),
                                                .tokenPoolLength = static_cast<uint32_t>(dstShape[1]),
                                                .typeBytes = eleBytes,
                                                .syncWorkspaceSize = syncWorkspaceSize,
                                                .ubSize = static_cast<uint32_t>(ubSize)};
    at::Tensor tiling = GetTilingTensor(tilingData, sizeof(tilingData));

    auto sync = at::zeros({syncWorkspaceSize, 1}, at::kByte);
    auto syncDevice = TorchNpuHelper::CopyTensorHostToDevice(sync);
    EXEC_KERNEL_CMD(assign_cache_op, blockDim, dstTensor, srcTensor, dstStartIdx, dstEndIdx, srcStartIdx, srcEndIdx,
                    syncDevice, tiling);
    return true;
}
}  // namespace npu_kernel

}  // namespace sglang

```

### `csrc/assign_cache_op/op_host/tiling_data.h`
```cpp
#ifndef ASSIGN_TILING_DATA_H
#define ASSIGN_TILING_DATA_H
#include <assert.h>
#include <cstring>

namespace custom_assign {
#pragma pack(push, 1)
struct CustomAssignTilingData {
    uint32_t batchSize;
    uint32_t tokenPoolLength;
    uint32_t typeBytes;
    uint32_t syncWorkspaceSize;
    uint32_t ubSize;

    void SetToBuffer(uint8_t *dataPtr, size_t dataLen)
    {
        if (dataPtr == nullptr || dataLen < sizeof(CustomAssignTilingData)) {
            return;
        }
        // Ensure no padding is added by the compiler.
        static_assert(sizeof(CustomAssignTilingData) == 5 * sizeof(uint32_t), "CustomAssignTilingData must be packed.");
        memcpy(dataPtr, this, sizeof(CustomAssignTilingData));
    }
};
#pragma pack(pop)
}  // namespace custom_assign
#endif

```

### `csrc/assign_cache_op/op_kernel/assign_cache_op.cpp`
```cpp
#include "kernel_operator.h"
namespace custom_assign {

constexpr int32_t BLOCK_SIZE = 32;
constexpr int32_t TYPEBYPE_ID = 2;

#define SET_FLAG(trigger, waiter, e) AscendC::SetFlag<AscendC::HardEvent::trigger##_##waiter>((e))
#define WAIT_FLAG(trigger, waiter, e) AscendC::WaitFlag<AscendC::HardEvent::trigger##_##waiter>((e))

template <typename T>
class AssignCacheOp
{
public:
    __aicore__ inline AssignCacheOp(){};
    __aicore__ inline void Init(__gm__ uint8_t *dstPtr, __gm__ uint8_t *srcPtr, __gm__ uint8_t *dstStartIdxPtr,
                                __gm__ uint8_t *dstEndIdxPtr, __gm__ uint8_t *srcStartIdxPtr,
                                __gm__ uint8_t *srcEndIdxPtr, __gm__ uint8_t *sync, __gm__ uint8_t *tilingPtr);
    __aicore__ inline void CopyElement(AscendC::LocalTensor<T> &dstTensor, AscendC::LocalTensor<T> &srcTensor,
                                       uint32_t bytes);
    __aicore__ inline void Process();
    __aicore__ inline void ParseTilingData(__gm__ uint8_t *tilingPtr);

private:
    AscendC::TPipe pipe_;
    AscendC::GlobalTensor<T> dstGM_;
    AscendC::GlobalTensor<T> srcGM_;

    AscendC::GlobalTensor<int64_t> dstStartIdxGm_;
    AscendC::GlobalTensor<int64_t> dstEndIdxGm_;
    AscendC::GlobalTensor<int64_t> srcStartIdxGm_;
    AscendC::GlobalTensor<int64_t> srcEndIdxGm_;

    AscendC::TBuf<AscendC::QuePosition::VECCALC> tmpBuf1_;
    AscendC::TBuf<AscendC::QuePosition::VECCALC> tmpBuf2_;
    AscendC::LocalTensor<T> tmpTensor1_;
    AscendC::LocalTensor<T> tmpTensor2_;

    AscendC::TQue<AscendC::TPosition::VECOUT, 1> vecOut_;
    AscendC::GlobalTensor<int32_t> syncGm_;

    uint32_t batchSize_;
    uint32_t tokenPoolLength_;
    uint32_t syncWorkspaceSize_;
    uint32_t ubSize_;
    uint32_t ubUsedBufSize_;
};

template <typename T>
__aicore__ inline void AssignCacheOp<T>::Init(__gm__ uint8_t *dstPtr, __gm__ uint8_t *srcPtr,
                                              __gm__ uint8_t *dstStartIdxPtr, __gm__ uint8_t *dstEndIdxPtr,
                                              __gm__ uint8_t *srcStartIdxPtr, __gm__ uint8_t *srcEndIdxPtr,
                                              __gm__ uint8_t *sync, __gm__ uint8_t *tilingPtr)
{
    this->ParseTilingData(tilingPtr);
    ubUsedBufSize_ = ubSize_ >> 2;  // make sure not overflow

    dstGM_.SetGlobalBuffer((__gm__ T *)dstPtr);
    srcGM_.SetGlobalBuffer((__gm__ T *)srcPtr);
    dstStartIdxGm_.SetGlobalBuffer((__gm__ int64_t *)dstStartIdxPtr);
    dstEndIdxGm_.SetGlobalBuffer((__gm__ int64_t *)dstEndIdxPtr);
    srcStartIdxGm_.SetGlobalBuffer((__gm__ int64_t *)srcStartIdxPtr);
    srcEndIdxGm_.SetGlobalBuffer((__gm__ int64_t *)srcEndIdxPtr);

    pipe_.InitBuffer(tmpBuf1_, ubUsedBufSize_);
    pipe_.InitBuffer(tmpBuf2_, ubUsedBufSize_);
    tmpTensor1_ = tmpBuf1_.Get<T>();
    tmpTensor2_ = tmpBuf2_.Get<T>();

    syncGm_.SetGlobalBuffer((__gm__ int32_t *)(sync), syncWorkspaceSize_);
    pipe_.InitBuffer(vecOut_, 1, 8 * sizeof(int32_t));
}

template <typename T>
__aicore__ inline void AssignCacheOp<T>::CopyElement(AscendC::LocalTensor<T> &dstTensor,
                                                     AscendC::LocalTensor<T> &srcTensor, uint32_t bytes)
{
    for (uint32_t i = 0; i < bytes / sizeof(T); i++) {
        T tmp = srcTensor.GetValue(i);
        dstTensor.SetValue(i, tmp);
    }
}

template <typename T>
__aicore__ inline void AssignCacheOp<T>::Process()
{
    int32_t vecIdx = AscendC::GetBlockIdx();   // current vector core id
    int32_t coreNum = AscendC::GetBlockNum();  // total vector core number

    for (uint32_t batchId = vecIdx; batchId < batchSize_; batchId += coreNum) {
        uint32_t srcStartIdx = srcStartIdxGm_.GetValue(batchId);
        uint32_t srcEndIdx = srcEndIdxGm_.GetValue(batchId);
        uint32_t dstStartIdx = dstStartIdxGm_.GetValue(batchId);
        uint32_t dstEndIdx = dstEndIdxGm_.GetValue(batchId);
        uint32_t totalBytes = (srcEndIdx - srcStartIdx) * sizeof(T);
        uint32_t ubLoopNum = (totalBytes + ubUsedBufSize_ - 1) / ubUsedBufSize_;
        uint32_t tailBytes = totalBytes % ubUsedBufSize_;
        if (totalBytes > 0 && tailBytes == 0) {
            tailBytes = ubUsedBufSize_;
        }
        uint32_t loopOffset = 0;
        uint32_t ubDataNum = ubUsedBufSize_ / sizeof(T);

        // load src data & dst data from gm to ub, then copy to gm of dst data address
        for (uint32_t loopId = 0; loopId < ubLoopNum; loopId++) {
            uint16_t copyLen = ubDataNum * sizeof(T) / BLOCK_SIZE;
            AscendC::DataCopyParams copyParams = {1, copyLen, 0, 0};
            copyParams.blockLen = (loopId == ubLoopNum - 1) ? (tailBytes + BLOCK_SIZE - 1) / BLOCK_SIZE : copyLen;
            DataCopy(tmpTensor1_, srcGM_[srcStartIdx + loopOffset], copyParams);
            SET_FLAG(MTE2, MTE3, EVENT_ID1);
            WAIT_FLAG(MTE2, MTE3, EVENT_ID1);

            if (loopId == ubLoopNum - 1) {
                DataCopy(tmpTensor2_, dstGM_[batchId * tokenPoolLength_ + dstStartIdx + loop
// ... (truncated due to length) ...

```
