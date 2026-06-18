---
id: code-cann-ops-adv-prompt-flash-attention
title: "CANN Ops Adv \u2014 Prompt Flash Attention"
type: source-code
repo: Ascend/cann-ops-adv
path: src/transformer/prompt_flash_attention
url: https://gitee.com/ascend/cann-ops-adv/tree/master/src/transformer/prompt_flash_attention
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- attention
- flash-attention
- ascendc
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
- flash-attention
languages:
- ascendc
- cpp
---

# CANN Ops Adv — Prompt Flash Attention

Advanced CANN transformer operator source for prompt-phase FlashAttention. This path is code evidence for attention tiling, score/softmax/value pipeline organization, and inference-oriented memory handling on Ascend.

## Code Location

- Repository: `Ascend/cann-ops-adv`
- Path: `src/transformer/prompt_flash_attention`
- URL: https://gitee.com/ascend/cann-ops-adv/tree/master/src/transformer/prompt_flash_attention


## Fetched Source


### `src/transformer/prompt_flash_attention/prompt_flash_attention.cpp`
```cpp
/**
 * Copyright (c) Huawei Technologies Co., Ltd. 2024. All rights reserved.
 * This file is a part of the CANN Open Software.
 * Licensed under CANN Open Software License Agreement Version 1.0 (the "License").
 * Please refer to the License for details. You may not use this file except in compliance with the License.
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
 * See LICENSE in the root of the software repository for the full text of the License.
 */

/*!
 * \file prompt_flash_attention.cpp
 * \brief
 */

#include "kernel_operator.h"
#if (__CCE_AICORE__ > 200)
#include "prompt_flash_attention_base.h"
#include "prompt_flash_attention_split_n_s_no_tail.h"
#include "prompt_flash_attention_split_n_s_tail.h"
#include "prompt_flash_attention_bnstilling_n_s_no_tail.h"
#include "prompt_flash_attention_bnstilling_n_s_tail.h"
#include "prompt_flash_attention_bnstilling_n_s_no_tailWBNSD.h"
#include "prompt_flash_attention_bnstilling_n_s_tailWBNSD.h"
#include "prompt_flash_attention_s1s2_bns1_x910.h"
#include "prompt_flash_attention_empty_tensor.h"
#else
#include "prompt_flash_attention_s1s2_bns1_x310_base.h"
#include "prompt_flash_attention_s1s2_bns1_x310.h"
#include "prompt_flash_attention_bnstilling_n_s_no_tailWBNSD_KV_NZ.h"
#endif

#define INVOKE_PFA_GENERAL_OP_IMPL(templateClass, ...)                                                                  \
    TPipe tPipe;                                                                                                        \
    do {                                                                                                                \
        if (query == nullptr) {return;}                                                                                 \
        INVOKE_PFA_TILING_DATA(tiling);                                                                                 \
        templateClass<__VA_ARGS__> op;                                                                                  \
        REGIST_MATMUL_OBJ(&tPipe, GetSysWorkSpacePtr(), op.mm, bmm1tiling, op.bmm2, bmm2tiling);                        \
        op.Init(query, key, value, pseShift, attenMask, actualSeqLengths, actualSeqLengthsKV, blocktable, queryPaddingSize,         \
                kvPaddingSize, keySharedPrefix, valueSharedPrefix, actualSharedPrefixLen, attentionOut, softmaxLse, user, tiling_data, tiling, &tPipe);                                    \
        op.InitMsd(key_antiquant_scale, key_antiquant_offset,value_antiquant_scale, value_antiquant_offset);                     \
        op.Process();                                                                                                   \
    } while (0)
#define INVOKE_PFA_INT8_OP_IMPL(templateClass, ...)                                                                     \
    TPipe tPipe;                                                                                                        \
    do {                                                                                                                \
        if (query == nullptr) {return;}                                                                                 \
        INVOKE_PFA_TILING_DATA(tiling);                                                                                 \
        templateClass<__VA_ARGS__> op;                                                                                  \
        REGIST_MATMUL_OBJ(&tPipe, GetSysWorkSpacePtr(), op.mm, bmm1tiling, op.bmm2, bmm2tiling);                        \
        op.Init(query, key, value, pseShift, attenMask, actualSeqLengths, actualSeqLengthsKV, blocktable, queryPaddingSize,         \
                kvPaddingSize, keySharedPrefix, valueSharedPrefix, actualSharedPrefixLen, attentionOut, softmaxLse, user, tiling_data, tiling, &tPipe);                                    \
        op.InitQuant(deq_scale1, quant_scale1, deq_scale2, quant_scale2, quant_offset2);                                \
        op.InitMsd(key_antiquant_scale, key_antiquant_offset,value_antiquant_scale, value_antiquant_offset);            \
        op.Process();                                                                                                   \
    } while (0)
#define INVOKE_PFA_KVANTIQUANT_OP_IMPL(templateClass, ...)                                                              \
    TPipe tPipe;                                                                                                        \
    do {                                                                                                                \
        if (query == nullptr) {return;}                                                                                 \
        INVOKE_PFA_TILING_DATA(tiling);                                                     
// ... (truncated due to length) ...

```

### `src/transformer/prompt_flash_attention/prompt_flash_attention_empty_tensor.h`
```cpp
/**
 * Copyright (c) Huawei Technologies Co., Ltd. 2024. All rights reserved.
 * This file is a part of the CANN Open Software.
 * Licensed under CANN Open Software License Agreement Version 1.0 (the "License").
 * Please refer to the License for details. You may not use this file except in compliance with the License.
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
 * See LICENSE in the root of the software repository for the full text of the License.
 */

/*!
 * \file prompt_flash_attention_empty_tensor.h
 * \brief
 */

#ifndef PROMPT_FLASH_ATTENTION_EMPTY_TENSOR_H
#define PROMPT_FLASH_ATTENTION_EMPTY_TENSOR_H

#include "kernel_tiling/kernel_tiling.h"
#include "kernel_operator.h"
#include "lib/matmul_intf.h"
#include "kernel_data_copy_transpose.h"

template<typename T>
class PromptFlashAttentionEmptyTensor {
public:
    __aicore__ inline PromptFlashAttentionEmptyTensor() {};
    __aicore__ inline void Init(__gm__ uint8_t *attentionOut, const PromptFlashAttentionTilingData *__restrict tiling,
                                TPipe *tPipe);
    __aicore__ inline void Process();

protected:
    TPipe *pipe;
    const PromptFlashAttentionTilingData* __restrict tilingData;
    GlobalTensor<T> attentionOutGm;
};

template<typename T>
__aicore__ inline void PromptFlashAttentionEmptyTensor<T>::Init(__gm__ uint8_t*  attentionOut,
                                                                const PromptFlashAttentionTilingData* __restrict tiling,
                                                                TPipe *tPipe) {
    pipe = tPipe;
    attentionOutGm.SetGlobalBuffer((__gm__ T*)attentionOut);
    tilingData = tiling;
}

template<typename T>
__aicore__ inline void PromptFlashAttentionEmptyTensor<T>::Process() {
    uint32_t tmp_block_idx = GetBlockIdx();
    auto &initParams = tilingData->promptAttentionInitOutputParams;
    int32_t tailSize = (int32_t)initParams.totalOutputSize - tmp_block_idx * (int32_t)initParams.singleCoreSize;
    if (tailSize > 0) {
        uint32_t singleInitOutputSize =
            tailSize < initParams.singleCoreSize ? static_cast<uint32_t>(tailSize) : initParams.singleCoreSize;
        InitOutput<T>(attentionOutGm[tmp_block_idx * (int64_t)initParams.singleCoreSize], singleInitOutputSize, 0);
    }
}
#endif  // PROMPT_FLASH_ATTENTION_EMPTY_TENSOR_H
```

### `src/transformer/prompt_flash_attention/prompt_flash_attention_bnstilling_n_s_tailWBNSD.h`
```cpp
/**
 * Copyright (c) Huawei Technologies Co., Ltd. 2024. All rights reserved.
 * This file is a part of the CANN Open Software.
 * Licensed under CANN Open Software License Agreement Version 1.0 (the "License").
 * Please refer to the License for details. You may not use this file except in compliance with the License.
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
 * See LICENSE in the root of the software repository for the full text of the License. 
 */

/*!
 * \file prompt_flash_attention_bnstilling_n_s_tailWBNSD.h
 * \brief
 */
#ifndef PROMPT_FLASH_ATTENTION_SCORE_BNSTILLING_N_S_WITHBNSD_TAIL_H
#define PROMPT_FLASH_ATTENTION_SCORE_BNSTILLING_N_S_WITHBNSD_TAIL_H

#include "prompt_flash_attention_base.h"

using namespace matmul;
template<typename T, typename U, CubeFormat FORMAT, typename O, Mode M = Mode::HighPerformance>
class PromptFlashAttentionBNSTillingNSWithBNSDTail : public PromptFlashAttentionBase<T, U, FORMAT, O, M> {
public:
    // define datatype
    using mmInputType = typename PromptFlashAttentionTypeTraits<T, M>::mmInputType;
    using mmBiasType = typename PromptFlashAttentionTypeTraits<T, M>::mmBiasType;
    using mmOutputType = typename PromptFlashAttentionTypeTraits<T, M>::mmOutputType;
    using softmaxType = typename PromptFlashAttentionTypeTraits<T, M>::softmaxType;
    using pseShiftType = typename PromptFlashAttentionTypeTraits<T, M>::pseShiftType;
    using pseShiftCastType = typename PromptFlashAttentionTypeTraits<T, M>::pseShiftCastType;
    __aicore__ inline PromptFlashAttentionBNSTillingNSWithBNSDTail() {};
    __aicore__ inline void Process();

protected:
    __aicore__ inline void AttenMaskCopyIn(uint64_t offset, uint32_t sinnerSize, uint32_t sInnerIdx);

    __aicore__ inline void PseShiftCopyIn(uint64_t offset, uint32_t sinnerSize, uint32_t sInnerLoopIdx);

    __aicore__ inline void PseShiftProcess(int64_t sInnerLoopIdx, uint32_t computeSize, LocalTensor<mmOutputType>& mmResUb);

    __aicore__ inline void Bmm1ResDoVecBmm2Compute(LocalTensor<mmOutputType>& mmResUb, LocalTensor<float>& softmaxMaxUb,
                                            LocalTensor<float>& softmaxSumUb, LocalTensor<softmaxType>& softmaxExpUb,
                                            bool isLast, bool isSecond, event_t eventID, int64_t sInnerLoopIdx);

    __aicore__ inline void Bmm1ResDoVecBmm2ComputeFirst(LocalTensor<mmOutputType>& mmResUb, LocalTensor<float>& softmaxMaxUb,
                                            LocalTensor<float>& softmaxSumUb, bool isLast, event_t eventID, int64_t sInnerLoopIdx);

    __aicore__ inline void ComputeEachCoreSInnerLoop(uint32_t startIndex, uint32_t endIndex);

    __aicore__ inline void SInnerLoopFunc(int32_t startIndex, int32_t endIndex);

    __aicore__ inline void ComputeEachCore(uint32_t coreIdx);

    __aicore__ inline void ComputeEachCoreBalance(uint32_t coreIdx);
};

template<typename T, typename U, CubeFormat FORMAT, typename O, Mode M>
__aicore__ inline void PromptFlashAttentionBNSTillingNSWithBNSDTail<T, U, FORMAT, O, M>::Process() {
    if (this->headNumRatio != 1 || this->tilingData->promptAttentionInitOutputParams.needInit ||
        this->tilingData->promptAttentionBaseParams.batchSize != 1) {
        ComputeEachCore(this->tmp_block_idx);
    }
    else {
        ComputeEachCoreBalance(this->tmp_block_idx);
    }
}

template<typename T, typename U, CubeFormat FORMAT, typename O, Mode M>
__aicore__ inline void PromptFlashAttentionBNSTillingNSWithBNSDTail<T, U, FORMAT, O, M>::PseShiftCopyIn(uint64_t offset, uint32_t sinnerSize,
                                                                           uint32_t sInnerLoopIdx) {
    if (!(this->usePseShift)) {
        return;
    }
    LocalTensor<pseShiftType> pseShiftUb = this->attenMaskQueue.template AllocTensor<pseShiftType>();
    pseShiftUb.SetSize(this->singleProcessSOuterSize * sinnerSize);

    DataCopyExtParams intriParams;
    intriParams.blockCount = this->singleProcessSOuterSize;
    intriParams.blockLen = sinnerSize * sizeof(pseShiftType);
    intriParams.srcStride = (this->pseShiftStride - sinnerSize) * sizeof(pseShiftType);

    if (sInnerLoopIdx == this->maxInnerLoopTimes - 1) {
        intriParams.blockLen = this->unalignSInner * sizeof(pseShiftType);
        intriParams.srcStride = (this->pseShiftStride - this->unalignSInner) * sizeof(pseShiftType);
    }

    intriParams.dstStride = 0;

    DataCopyPadExtParams<pseShiftType> padParams;
    padParams.isPad = true;
    padParams.leftPadding = 0;
    padParams.paddingValue = 1;
    if (sInnerLoopIdx == this->maxInnerLoopTimes - 1) {
        padParams.rightPadding = this->pseShiftPadSize;
    } else {
        padParams.rightPadding = 0;
    }
    DataCopyPad(pseShiftUb, this->pseShiftGm[offset], intriParams, padParams);
    this->attenMaskQueue.EnQue(pseShiftUb);
}

tem
// ... (truncated due to length) ...

```
