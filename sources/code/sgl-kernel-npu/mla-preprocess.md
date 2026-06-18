---
id: code-sgl-kernel-npu-mla-preprocess
title: SGL Kernel NPU MLA Preprocess Operator
type: source-code
repo: sgl-project/sgl-kernel-npu
path: csrc/mla_preprocess
url: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/mla_preprocess
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- sglang
- mla
- attention
- preprocessing
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
- rope
- elementwise
languages:
- cpp
- ascendc
---

# SGL Kernel NPU MLA Preprocess Operator

SGL Kernel NPU MLA preprocess source directory, anchoring attention preprocessing and cache-shaping code for serving workloads.

## Code Location

- Repository: `sgl-project/sgl-kernel-npu`
- Path: `csrc/mla_preprocess`
- URL: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/mla_preprocess


## Fetched Source


### `csrc/mla_preprocess/op_host/mla_preprocess.cpp`
```cpp
// Adapted from
//   https://gitee.com/ascend/ascend-transformer-boost.git
//   https://gitee.com/ascend/op-plugin.git
//
// Copyright (c) Huawei Technologies Co., Ltd. 2025. All rights reserved.
// This file is a part of the CANN Open Software.
// Licensed under CANN Open Software License Agreement Version 1.0 (the "License").
// Please refer to the License for details. You may not use this file except in compliance with the License.
// THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
// INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
// See LICENSE in the root of the software repository for the full text of the License.
//

#include <fstream>
#include <iostream>
#include <math.h>
#include <stdexcept>
#include "acl/acl.h"
#include "defines.h"
#include "torch_helper.h"
#include "tiling/platform/platform_ascendc.h"
#include "tiling/mla_preprocess_tiling.h"

#include "aclrtlaunch_mla_preprocess.h"

namespace sglang {
namespace npu_kernel {

constexpr uint32_t DIM_2 = 2;

constexpr uint32_t AXES_ALIGN_SIZE = 512;
constexpr uint32_t BASE_BLOCK_STEP = 2;
constexpr uint32_t CONST_16 = 16;
constexpr uint32_t CONST_32 = 32;
constexpr uint32_t CONST_128 = 128;
constexpr uint32_t CONST_256 = 256;
constexpr uint32_t CONST_512 = 512;
constexpr uint32_t L1_BUFFER_SIZE = 524288;
constexpr uint32_t L1_PINGPONG_BUFFER_LEN = 262144;
constexpr uint32_t L0AB_PINGPONG_BUFFER_LEN = 131072;
constexpr uint32_t L1_SCALE_SIZE = 4096;
constexpr uint32_t L1_BIAS_SIZE = 2048;
constexpr uint32_t L0C_SIZE = 128 * 1024;
constexpr uint32_t CONCAT_SIZE = 512;

constexpr uint32_t HIDDEN_STRATE_ROPE = 192;
constexpr uint32_t HIDDEN_STRATE_MM = 2112;
constexpr uint32_t HIDDEN_STRATE_RMS = 1536;
constexpr uint32_t UB_SIZE = 196352;
constexpr uint32_t HEADDIM = 64;
constexpr uint32_t FP32_REPEAT_MASK = 64;
constexpr uint32_t FP16_REPEAT_MASK = 128;

constexpr int32_t NUM1 = 1;
constexpr int32_t NUM2 = 2;
constexpr int32_t NUM3 = 3;
constexpr int32_t NUM4 = 4;
constexpr int32_t NUM8 = 8;
constexpr uint32_t INDEX_WDQKV = 5;
constexpr uint32_t INDEX_WUQ = 18;
constexpr uint32_t INDEX_WUK = 20;

constexpr uint32_t MAX_SUPPORT_TOKEN_NUMS = 1024;
constexpr uint32_t MAX_CACHE_MODE_NUMS = 3;

inline uint32_t CeilDiv(const uint32_t dividend, const uint32_t divisor)
{
    if (divisor == 0) {
        return UINT32_MAX;
    }
    return (dividend + divisor - 1) / divisor;
}

inline uint32_t RoundUp(const uint32_t val, const uint32_t align = 16)
{
    if (align == 0) {
        return 0;
    }
    return (val + align - 1) / align * align;
}

inline uint32_t RoundDown(const uint32_t val, const uint32_t align = 16)
{
    if (align == 0) {
        return 0;
    }
    return val / align * align;
}

template <typename T = uint32_t>
inline T Max(const T a, const T b)
{
    return a > b ? a : b;
}

template <typename T = uint32_t>
inline T Min(const T a, const T b)
{
    return a < b ? a : b;
}

struct MlaPreprocess {
    enum class QuantMode : int32_t {
        PER_TENSOR_ASYMM_QUANT = 0,
        PER_TOKEN_SYMM_QUANT,
        PER_TOKEN_ASYMM_QUANT,
        NO_QUANT
    };
};
using QuantMode = MlaPreprocess::QuantMode;

struct PlatformInfo {
    uint32_t coreNum;
    uint32_t coreNumAic;
    uint32_t coreNumAiv;
    uint64_t ubSize;
    uint64_t l1Size;
    uint64_t l2Size;
    uint64_t l0aSize;
    uint64_t l0bSize;
    uint64_t l0cSize;
};

struct OpParam {
    uint32_t hiddenStateDim;
    uint32_t N;
    uint32_t headNum;
    int32_t cacheMode;
    QuantMode quantMode;
    caffe2::TypeMeta inDtype;
};

class PpMatmulTilingApi
{
public:
    PpMatmulTilingApi(struct PlatformInfo &platformInfo, uint32_t numBatch, uint32_t m, uint32_t k, uint32_t n,
                      bool transA, bool transB, bool enDequant, bool deqOnTheFly)
        : platformInfo_(platformInfo),
          numBatch_(numBatch),
          m_(m),
          k_(k),
          n_(n),
          transA_(transA),
          transB_(transB),
          enDequant_(enDequant),
          deqOnTheFly_(deqOnTheFly)
    {
        inDataSize_ = enDequant ? sizeof(uint8_t) : sizeof(uint16_t);
    }
    void GetTilingData(PpMatmulTilingData &tiling);

private:
    void GetTileSize();
    float GetCost(const uint32_t m0, const uint32_t n0);
    void UpdateTileSize(const uint32_t m0, const uint32_t n0);
    void Swizzle();
    uint32_t ComputeL1AbSize();
    uint32_t ComputeK0ForABpingpong(uint32_t l1AbSize);
    bool IsLoadAllAmat(uint32_t l1AbSize);
    uint32_t ComputeK0ForOnlyBpingpong(uint32_t l1AbSize);

private:
    uint32_t numBatch_{0};
    uint32_t m_{0};
    uint32_t k_{0};
    uint32_t n_{0};
    uint32_t m0_{0};
    uint32_t k0_{0};
    uint32_t n0_{0};
    uint32_t mLoop_{0};
    uint32_t kLoop_{0};
    uint32_t nLoop_{0};
    uint32_t coreLoop_{0};
    uint32_t swizzleCount_{0};
    uint32_t blockDim_{0};
    uint32_t swizzleDirect_{0};
    uint32_t inDataSize_{0};
    uint32_t b0matPingPongBuff
// ... (truncated due to length) ...

```

### `csrc/mla_preprocess/op_host/tiling/mla_preprocess_tiling.h`
```cpp
// Adapted from
//   https://gitee.com/ascend/ascend-transformer-boost
//
// Copyright (c) Huawei Technologies Co., Ltd. 2025. All rights reserved.
// This file is a part of the CANN Open Software.
// Licensed under CANN Open Software License Agreement Version 1.0 (the "License").
// Please refer to the License for details. You may not use this file except in compliance with the License.
// THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
// INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
// See LICENSE in the root of the software repository for the full text of the License.
//

#ifndef MLAPREPROCESS_TILING_H
#define MLAPREPROCESS_TILING_H

#include <cstdint>

struct PpMatmulTilingData {
    uint32_t numBatch{0};
    uint32_t m{0};
    uint32_t k{0};
    uint32_t n{0};
    uint32_t m0{0};
    uint32_t k0{0};
    uint32_t n0{0};
    uint32_t mLoop{0};
    uint32_t kLoop{0};
    uint32_t nLoop{0};
    uint32_t coreLoop{0};
    uint32_t swizzleCount{0};
    uint32_t swizzleDirect{0};
    uint32_t enShuffleK{0};
    uint32_t blockDim{0};
    uint32_t enLoadAllAmat{0};
    uint32_t b0matPingPongBufferLen{0};
};

struct MlaTilingData {
    uint32_t tilingKey{0};
    uint64_t userWorkspaceSize{0};
    uint64_t s1Offset{0};
    uint64_t s2Offset{0};
    uint64_t s3Offset{0};
    uint64_t s4Offset{0};
    uint64_t s5Offset{0};

    uint32_t numCore{0};
    uint32_t n{0};
    uint32_t perTaskNum{0};
    uint32_t resTaskNum{0};

    PpMatmulTilingData mm1;
    PpMatmulTilingData mm2;
    PpMatmulTilingData mm3;
    // rms1
    uint32_t rmsNumCore1{0};
    uint32_t rmsNumCol1{0};
    uint32_t rmsNumRow1{0};
    uint32_t rmsQuantMin1{0};
    // rms2
    uint32_t rmsNumCore2{0};
    uint32_t rmsNumCol2{0};
    uint32_t rmsNumRow2{0};
    uint32_t rmsQuantMin2{0};

    uint32_t hiddenSizeQ{0};
    uint32_t headNumQ{0};
    uint32_t headDim{0};
    uint32_t concatSize{0};
    uint32_t rotaryCoeff{0};
    uint32_t ntokens{0};
    uint32_t realCore{0};
    uint32_t nlCoreRun{0};
    uint32_t lCoreRun{0};
    uint32_t maxNPerLoopForUb{0};
    uint32_t preCoreLoopTime{0};
    uint32_t preCoreLoopNLast{0};
    uint32_t lastCoreLoopTime{0};
    uint32_t lastCoreLoopNLast{0};

    // EinSumQuant
    uint32_t esqFrontCore{0};
    uint32_t esqTailCore{0};
    uint32_t esqFrontCoreBatch{0};
    uint32_t esqTailCoreBatch{0};
    uint32_t esqHeadNum{0};
    uint32_t esqColNum{0};
    uint32_t esqUbHeadLoop{0};
    uint32_t esqHeadPerLoop{0};
    uint32_t esqHeadTail{0};
    uint32_t esqColLoop{0};
    uint32_t esqColTail{0};

    // hidden state dimension
    uint32_t hiddenStateDim{7168};
};

#endif  // MLAPREPROCESS_TILING_H

```

### `csrc/mla_preprocess/op_kernel/mla_preprocess_kernel.cpp`
```cpp
// Adapted from
//   https://gitee.com/ascend/ascend-transformer-boost
//
// Copyright (c) Huawei Technologies Co., Ltd. 2025. All rights reserved.
// This file is a part of the CANN Open Software.
// Licensed under CANN Open Software License Agreement Version 1.0 (the "License").
// Please refer to the License for details. You may not use this file except in compliance with the License.
// THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
// INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
// See LICENSE in the root of the software repository for the full text of the License.
//

#include "kernel_operator.h"

#include "mla_preprocess_mix_fp16.hpp"
#include "mla_preprocess_mix_bf16.hpp"

#include "../op_host/tiling/mla_preprocess_tiling.h"

extern "C" __global__ __aicore__ void mla_preprocess(
    GM_ADDR hiddenState, GM_ADDR gamma1, GM_ADDR beta1, GM_ADDR quantScale1, GM_ADDR quantOffset1, GM_ADDR wdqkv,
    GM_ADDR bias1, GM_ADDR gamma2, GM_ADDR beta2, GM_ADDR quantScale2, GM_ADDR quantOffset2, GM_ADDR gamma3,
    GM_ADDR sin1, GM_ADDR cos1, GM_ADDR sin2, GM_ADDR cos2, GM_ADDR keycache, GM_ADDR slotMapping, GM_ADDR wuq,
    GM_ADDR bias2, GM_ADDR wuk, GM_ADDR descale1, GM_ADDR descale2, GM_ADDR ctkvScale, GM_ADDR qnopeScale, GM_ADDR q,
    GM_ADDR keycacheOut, GM_ADDR q2, GM_ADDR keycacheOut2, GM_ADDR workspace, GM_ADDR tiling)
{
    PRELOAD(2);

    SetAtomicnone();
    SetMasknorm();
#ifdef __DAV_C220_CUBE__
    SetPadding<uint64_t>((uint64_t)0);
    SetNdpara(1, 0, 0);
#endif

    MlaTilingData mlaTilingData;
    __gm__ MlaTilingData *tilingData = reinterpret_cast<__gm__ MlaTilingData *>(tiling);

    mlaTilingData.tilingKey = tilingData->tilingKey;
    mlaTilingData.n = tilingData->n;
    mlaTilingData.hiddenStateDim = tilingData->hiddenStateDim;

    mlaTilingData.mm1.numBatch = tilingData->mm1.numBatch;
    mlaTilingData.mm1.m = tilingData->mm1.m;
    mlaTilingData.mm1.k = tilingData->mm1.k;
    mlaTilingData.mm1.n = tilingData->mm1.n;
    mlaTilingData.mm1.m0 = tilingData->mm1.m0;
    mlaTilingData.mm1.k0 = tilingData->mm1.k0;
    mlaTilingData.mm1.n0 = tilingData->mm1.n0;
    mlaTilingData.mm1.mLoop = tilingData->mm1.mLoop;
    mlaTilingData.mm1.kLoop = tilingData->mm1.kLoop;
    mlaTilingData.mm1.nLoop = tilingData->mm1.nLoop;
    mlaTilingData.mm1.coreLoop = tilingData->mm1.coreLoop;
    mlaTilingData.mm1.swizzleCount = tilingData->mm1.swizzleCount;
    mlaTilingData.mm1.enShuffleK = tilingData->mm1.enShuffleK;
    mlaTilingData.mm1.blockDim = tilingData->mm1.blockDim;
    mlaTilingData.mm1.enLoadAllAmat = tilingData->mm1.enLoadAllAmat;
    mlaTilingData.mm1.b0matPingPongBufferLen = tilingData->mm1.b0matPingPongBufferLen;

    mlaTilingData.mm2.numBatch = tilingData->mm2.numBatch;
    mlaTilingData.mm2.m = tilingData->mm2.m;
    mlaTilingData.mm2.k = tilingData->mm2.k;
    mlaTilingData.mm2.n = tilingData->mm2.n;
    mlaTilingData.mm2.m0 = tilingData->mm2.m0;
    mlaTilingData.mm2.k0 = tilingData->mm2.k0;
    mlaTilingData.mm2.n0 = tilingData->mm2.n0;
    mlaTilingData.mm2.mLoop = tilingData->mm2.mLoop;
    mlaTilingData.mm2.kLoop = tilingData->mm2.kLoop;
    mlaTilingData.mm2.nLoop = tilingData->mm2.nLoop;
    mlaTilingData.mm2.coreLoop = tilingData->mm2.coreLoop;
    mlaTilingData.mm2.swizzleCount = tilingData->mm2.swizzleCount;
    mlaTilingData.mm2.enShuffleK = tilingData->mm2.enShuffleK;
    mlaTilingData.mm2.blockDim = tilingData->mm2.blockDim;
    mlaTilingData.mm2.enLoadAllAmat = tilingData->mm2.enLoadAllAmat;
    mlaTilingData.mm2.b0matPingPongBufferLen = tilingData->mm2.b0matPingPongBufferLen;

    mlaTilingData.mm3.numBatch = tilingData->mm3.numBatch;
    mlaTilingData.mm3.m = tilingData->mm3.m;
    mlaTilingData.mm3.k = tilingData->mm3.k;
    mlaTilingData.mm3.n = tilingData->mm3.n;
    mlaTilingData.mm3.m0 = tilingData->mm3.m0;
    mlaTilingData.mm3.k0 = tilingData->mm3.k0;
    mlaTilingData.mm3.n0 = tilingData->mm3.n0;
    mlaTilingData.mm3.mLoop = tilingData->mm3.mLoop;
    mlaTilingData.mm3.kLoop = tilingData->mm3.kLoop;
    mlaTilingData.mm3.nLoop = tilingData->mm3.nLoop;
    mlaTilingData.mm3.coreLoop = tilingData->mm3.coreLoop;
    mlaTilingData.mm3.swizzleCount = tilingData->mm3.swizzleCount;
    mlaTilingData.mm3.enShuffleK = tilingData->mm3.enShuffleK;
    mlaTilingData.mm3.blockDim = tilingData->mm3.blockDim;

    mlaTilingData.perTaskNum = tilingData->perTaskNum;
    mlaTilingData.resTaskNum = tilingData->resTaskNum;
    mlaTilingData.numCore = tilingData->numCore;

    mlaTilingData.rmsNumCore1 = tilingData->rmsNumCore1;
    mlaTilingData.rmsNumCol1 = tilingData->rmsNumCol1;
    mlaTilingData.rmsNumCore2 = tilingData->rmsNumCore2;
    mlaTilingData.rmsNumCol2 = tilingData->rmsNumCol2;

    mlaTilingData.hiddenSizeQ = tilingData->hiddenSizeQ;
    mlaTilingData.headNumQ = tilingData->headNumQ;
    mlaTilingData.headDim = tilingData->headDim;
    mlaTilingData.concatS
// ... (truncated due to length) ...

```
