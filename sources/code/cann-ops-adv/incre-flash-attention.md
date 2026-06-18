---
id: code-cann-ops-adv-incre-flash-attention
title: "CANN Ops Adv \u2014 Incremental Flash Attention"
type: source-code
repo: Ascend/cann-ops-adv
path: src/transformer/incre_flash_attention
url: https://gitee.com/ascend/cann-ops-adv/tree/master/src/transformer/incre_flash_attention
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- attention
- flash-attention
- kv-cache
- inference
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- global-memory
- unified-buffer
techniques:
- online-softmax
- kv-cache-paging
- pipeline-scheduling
kernel_types:
- attention
- flash-attention
- paged-attention
languages:
- ascendc
- cpp
---

# CANN Ops Adv — Incremental Flash Attention

Advanced CANN source path for decode/incremental FlashAttention. It anchors evidence for KV-cache reads, small-step decode attention, and mixed Cube/Vector work in autoregressive inference.

## Code Location

- Repository: `Ascend/cann-ops-adv`
- Path: `src/transformer/incre_flash_attention`
- URL: https://gitee.com/ascend/cann-ops-adv/tree/master/src/transformer/incre_flash_attention


## Fetched Source


### `src/transformer/incre_flash_attention/incre_flash_attention_split_Bbn2s2_Us2.h`
```cpp
/**
 * Copyright (c) 2024 Huawei Technologies Co., Ltd.
 * This file is a part of the CANN Open Software.
 * Licensed under CANN Open Software License Agreement Version 1.0 (the "License").
 * Please refer to the License for details. You may not use this file except in compliance with the License.
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
 * See LICENSE in the root of the software repository for the full text of the License.
 */

/*!
 * \file incre_flash_attention_split_Bbn2s2_Us2.h
 * \brief
 */
#ifndef INCRE_FLASH_ATTENTION_SPLIT_BBN2S2_US2
#define INCRE_FLASH_ATTENTION_SPLIT_BBN2S2_US2

#include "kernel_operator.h"
#include "kernel_operator_list_tensor_intf.h"
#include "kernel_tiling/kernel_tiling.h"
#include "lib/matmul_intf.h"
#include "lib/matrix/matmul/tiling.h"
#include "ifa_public_define.h"

using namespace matmul;
using AscendC::CacheMode;

template <typename IFAT> class IncreFlashAttentionAttenSplitBbn2s2Us2 {
public:
    __aicore__ inline IncreFlashAttentionAttenSplitBbn2s2Us2(){};
    __aicore__ inline void Init(__gm__ uint8_t *query, __gm__ uint8_t *key, __gm__ uint8_t *value,
                                __gm__ uint8_t *pseShift, __gm__ uint8_t *attenMask, __gm__ uint8_t *actualSeqLengths,
                                __gm__ uint8_t *blockTable, __gm__ uint8_t *kvPaddingSize, __gm__ uint8_t *attentionOut,
                                __gm__ uint8_t *softmaxLse, __gm__ uint8_t *workspace,
                                const IncreFlashAttentionTilingData *__restrict tiling, __gm__ uint8_t *gmTiling,
                                TPipe *tPipe, bool isPrefix = false);
    __aicore__ inline void InitQuant(__gm__ uint8_t *deqScale1, __gm__ uint8_t *quantScale1, __gm__ uint8_t *deqScale2,
                                     __gm__ uint8_t *quantScale2, __gm__ uint8_t *quantOffset2,
                                     __gm__ uint8_t *antiquantScale, __gm__ uint8_t *antiquantOffset,
                                     __gm__ uint8_t *keyAntiquantScale, __gm__ uint8_t *keyAntiquantOffset,
                                     __gm__ uint8_t *valueAntiquantScale, __gm__ uint8_t *valueAntiquantOffset,
                                     __gm__ uint8_t *workspace);
    __aicore__ inline void InitAntiquant(__gm__ uint8_t *antiquantScale, __gm__ uint8_t *antiquantOffset,
                                     __gm__ uint8_t *keyAntiquantScale, __gm__ uint8_t *keyAntiquantOffset,
                                     __gm__ uint8_t *valueAntiquantScale, __gm__ uint8_t *valueAntiquantOffse);
    __aicore__ inline void InitPostQuant(__gm__ uint8_t *deqScale1, __gm__ uint8_t *quantScale1, __gm__ uint8_t *deqScale2,
                                     __gm__ uint8_t *quantScale2, __gm__ uint8_t *quantOffset2);
    __aicore__ inline void Process();

    __aicore__ inline void InitPrefix(__gm__ uint8_t *query, __gm__ uint8_t *key, __gm__ uint8_t *value,
                                      __gm__ uint8_t *pseShift, __gm__ uint8_t *attenMask,
                                      __gm__ uint8_t *actualSeqLengths, __gm__ uint8_t *blockTable,
                                      __gm__ uint8_t *kvPaddingSize, __gm__ uint8_t *attentionOut,
                                      __gm__ uint8_t *softmaxLse, __gm__ uint8_t *workspace,
                                      const IncreFlashAttentionTilingDataPrefix *__restrict tiling,
                                      __gm__ uint8_t *gmTiling, TPipe *tPipe);
    __aicore__ inline void ProcessSysPrefixCombine();

    // 中间计算数据类型为float，高精度模式
    using T = float;

    using Q_T = typename IFAT::queryType;
    using KV_T = typename IFAT::kvType;
    using OUT_T = typename IFAT::outputType;
    using ORIGIN_T = typename IFAT::orginalType;
    static constexpr bool PAGE_ATTENTION = IFAT::pageAttention;
    static constexpr bool FLASH_DECODE = IFAT::flashDecode;
    static constexpr LAYOUT LAYOUT_T = IFAT::layout;
    static constexpr uint8_t PER_CHANNEL_MODE = 0; // 伪量化: K V per-channel
    static constexpr uint8_t PER_TOKEN_MODE = 1; // 伪量化: K V per-token
    static constexpr uint8_t PER_CHANNEL_TOKEN_MODE = 2; // 伪量化: K per-channel and V per-token
    static constexpr uint8_t ANTIQUANT_MODE = IFAT::antiquantMode;
    static constexpr bool SHARED_PREFIX = IFAT::sharedPrefix;

    static constexpr bool ANTIQUANT = !IsSameType<Q_T, KV_T>::value;
    static constexpr bool KVINT4 = IsSameType<KV_T, int4b_t>::value;
    static constexpr bool QUANT = (IsSameType<Q_T, KV_T>::value && IsSameType<KV_T, int8_t>::value);
    static constexpr bool ANTIQUANT_PER_CHANNEL_TOKEN = (ANTIQUANT && (ANTIQUANT_MODE == PER_CHANNEL_TOKEN_MODE));
    static constexpr bool ANTIQUANT_PER_TOKEN = (ANTIQUANT && (ANTIQUANT_MODE == PER_TOKEN_MODE));
    static constexpr bool ANTIQUANT_PER_CHANNEL = (ANTIQUANT && (ANTIQUA
// ... (truncated due to length) ...

```

### `src/transformer/incre_flash_attention/incre_flash_attention_allvec_new.h`
```cpp
/**
 * Copyright (c) 2024 Huawei Technologies Co., Ltd.
 * This file is a part of the CANN Open Software.
 * Licensed under CANN Open Software License Agreement Version 1.0 (the "License").
 * Please refer to the License for details. You may not use this file except in compliance with the License.
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
 * See LICENSE in the root of the software repository for the full text of the License.
 */

/*!
 * \file incre_flash_attention_allvec_new.h
 * \brief
 */
#ifndef INCRE_FLASH_ATTENTION_ALLVEC_NEW
#define INCRE_FLASH_ATTENTION_ALLVEC_NEW

#include "kernel_operator.h"
#include "kernel_operator_list_tensor_intf.h"
#include "kernel_tiling/kernel_tiling.h"
#include "lib/matmul_intf.h"
#include "lib/matrix/matmul/tiling.h"
#include "ifa_public_define.h"

using namespace AscendC;
using AscendC::MulAddDst;

// 默认srcGm上有效数据是连续的,srcStride为0
template <typename DATA_T>
__aicore__ inline void CopyIn(LocalTensor<DATA_T> &dstLocal, GlobalTensor<DATA_T> srcGm, uint64_t offset,
                              uint32_t rowCnt, uint32_t columnCntAlign, uint32_t actualColumnCnt)
{
    uint32_t typeElementSize = ONE_BLK_SIZE / sizeof(DATA_T);
    if ((actualColumnCnt % typeElementSize) == 0) {
        DataCopyParams intriParams;
        intriParams.blockCount = rowCnt;
        intriParams.dstStride = (columnCntAlign - actualColumnCnt) / typeElementSize;
        intriParams.blockLen = actualColumnCnt / typeElementSize;
        intriParams.srcStride = 0;
        DataCopy(dstLocal, srcGm[offset], intriParams);
    } else {
        // actualColumnCnt不按32B对齐的拷贝,310P当前不支持
#if (__CCE_AICORE__ > 200)
        DataCopyExtParams intriParams;
        intriParams.blockCount = rowCnt;
        intriParams.dstStride = (columnCntAlign - actualColumnCnt) / typeElementSize;
        intriParams.blockLen = actualColumnCnt * sizeof(DATA_T);
        intriParams.srcStride = 0;

        DataCopyPadExtParams<DATA_T> padParams;
        padParams.leftPadding = 0;
        padParams.rightPadding = (columnCntAlign - actualColumnCnt) % typeElementSize;
        padParams.paddingValue = 0;
        padParams.isPad = (padParams.rightPadding != 0);

        DataCopyPad(dstLocal, srcGm[offset], intriParams, padParams);
#endif
    }
}

template <typename IFAT> class IncreFlashAttentionAttenAllVecNew {
public:
    __aicore__ inline IncreFlashAttentionAttenAllVecNew(){};
    __aicore__ inline void Init(__gm__ uint8_t *query, __gm__ uint8_t *key, __gm__ uint8_t *value,
                                __gm__ uint8_t *pseShift, __gm__ uint8_t *attenMask, __gm__ uint8_t *actualSeqLengths,
                                __gm__ uint8_t *blockTable, __gm__ uint8_t *kvPaddingSize, __gm__ uint8_t *attentionOut,
                                __gm__ uint8_t *softmaxLse, __gm__ uint8_t *workspace,
                                const IncreFlashAttentionTilingData *__restrict tiling, TPipe *tPipe);
    __aicore__ inline void InitQuant(__gm__ uint8_t *deqScale1, __gm__ uint8_t *quantScale1, __gm__ uint8_t *deqScale2,
                                     __gm__ uint8_t *quantScale2, __gm__ uint8_t *quantOffset2,
                                     __gm__ uint8_t *antiquantScale, __gm__ uint8_t *antiquantOffset,
                                     __gm__ uint8_t *workspace);
    __aicore__ inline void Process();
    using ORIGIN_T = typename IFAT::orginalType;
    using OUT_T = typename IFAT::outputType;
    using KV_T = typename IFAT::kvType;
    using Q_T = typename IFAT::queryType;
    using T = float;
    static constexpr LAYOUT LAYOUT_T = IFAT::layout;
    static constexpr bool FLASH_DECODE = IFAT::flashDecode;
    static constexpr bool PAGE_ATTENTION = IFAT::pageAttention;
    static constexpr uint8_t PER_TOKEN_MODE = 1; // 伪量化 K V per-token
    static constexpr uint8_t PER_CHANNEL_MODE = 0; // 伪量化 K V per-channel
    static constexpr uint8_t ANTIQUANT_MODE = IFAT::antiquantMode;
    static constexpr bool ANTIQUANT = !IsSameType<Q_T, KV_T>::value;
    static constexpr bool ANTIQUANT_PER_CHANNEL = (ANTIQUANT && (ANTIQUANT_MODE == PER_CHANNEL_MODE));
    static constexpr bool ANTIQUANT_PER_TOKEN = (ANTIQUANT && (ANTIQUANT_MODE == PER_TOKEN_MODE));
    static constexpr bool QUANT = (IsSameType<Q_T, KV_T>::value && IsSameType<KV_T, int8_t>::value);
    using MM_OUT_T = typename AscendC::Conditional<(ANTIQUANT || QUANT), int32_t, T>::type;
    // define pse datetype
    using pseShiftType = typename AscendC::Conditional<AscendC::IsSameType<Q_T, int8_t>::value, half, Q_T>::type;
    using ANTIQ_PARAMS_T = typename AscendC::Conditional<ANTIQUANT_PER_TOKEN, T, Q_T>::type;

protected:
    const IncreFlashAttentionTilingData *__restrict tilingData = nullptr;
    TPipe *pipe = nullptr;
    GlobalTensor<OUT_T> attentionOutGm;
    GlobalTensor<int32_t> blockTableGm;
    GlobalTensor<f
// ... (truncated due to length) ...

```

### `src/transformer/incre_flash_attention/ifa_public_define.h`
```cpp
/**
 * Copyright (c) 2024 Huawei Technologies Co., Ltd.
 * This file is a part of the CANN Open Software.
 * Licensed under CANN Open Software License Agreement Version 1.0 (the "License").
 * Please refer to the License for details. You may not use this file except in compliance with the License.
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
 * See LICENSE in the root of the software repository for the full text of the License.
 */

/*!
 * \file ifa_public_define.h
 * \brief
 */
#ifndef IFA_PUBLIC_DEFINE_H
#define IFA_PUBLIC_DEFINE_H

#include "kernel_operator.h"
#include "lib/matmul_intf.h"
#include "lib/matrix/matmul/tiling.h"

using namespace AscendC;
using AscendC::AIC;
using AscendC::AIV;
using AscendC::GlobalTensor;
using AscendC::LocalTensor;
using AscendC::SetFlag;
using AscendC::ShapeInfo;
using AscendC::SoftmaxConfig;
using AscendC::WaitFlag;
using matmul::Matmul;
using matmul::MatmulType;

#define FLT_MAX 3.402823466e+38F

constexpr MatmulConfig CFG_NORM_EXCEED = GetNormalConfig(true);
constexpr MatmulConfig CFG_MDL_EXCEED = GetMDLConfig(true);

// CFG_NORM_EXCEED_INIT: doNorm, enable intrinsicsCheck and Init
constexpr MatmulConfig CFG_NORM_EXCEED_INIT{.doNorm = true,
                                            .doBasicBlock = false,
                                            .doMultiDataLoad = false,
                                            .basicM = 0,
                                            .basicN = 0,
                                            .basicK = 0,
                                            .intrinsicsCheck = true,
                                            .isNBatch = false,
                                            .enVecND2NZ = false,
                                            .doSpecialBasicBlock = false,
                                            .doMTE2Preload = false,
                                            .singleCoreM = 0,
                                            .singleCoreN = 0,
                                            .singleCoreK = 0,
                                            .stepM = 0,
                                            .stepN = 0,
                                            .baseMN = 0,
                                            .singleCoreMN = 0,
                                            .enUnitFlag = true,
                                            .isPerTensor = false,
                                            .hasAntiQuantOffset = false,
                                            .doIBShareNorm = false,
                                            .doSpecialMDL = false,
                                            .enableInit = false,
                                            .batchMode = BatchMode::NONE,
                                            .enableEnd = false,
                                            .enableGetTensorC = false,
                                            .enableSetOrgShape = true,
                                            .enableSetBias = false,
                                            .enableSetTail = true,
                                            .enableQuantVector = false,
                                            .enableSetDefineData = true,
                                            .iterateMode = IterateMode::ITERATE_MODE_ALL};

// CFG_MDL_EXCEED_INIT: enable MDL, intrinsicsCheck and Init
constexpr MatmulConfig CFG_MDL_EXCEED_INIT{.doNorm = false,
                                           .doBasicBlock = false,
                                           .doMultiDataLoad = true,
                                           .basicM = 0,
                                           .basicN = 0,
                                           .basicK = 0,
                                           .intrinsicsCheck = true,
                                           .isNBatch = false,
                                           .enVecND2NZ = false,
                                           .doSpecialBasicBlock = false,
                                           .doMTE2Preload = false,
                                           .singleCoreM = 0,
                                           .singleCoreN = 0,
                                           .singleCoreK = 0,
                                           .stepM = 0,
                                           .stepN = 0,
                                           .baseMN = 0,
                                           .singleCoreMN = 0,
                                           .enUnitFlag = false,
                                           .isPerTensor = false,
                                           .hasAntiQuantOffset = false,
                                           .doIBShareNorm = false,
                                           .doSpecialMDL = false,
            
// ... (truncated due to length) ...

```
