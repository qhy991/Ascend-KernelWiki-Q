---
id: code-cann-ops-adv-fused-infer-attention-score
title: "CANN Ops Adv \u2014 Fused Infer Attention Score"
type: source-code
repo: Ascend/cann-ops-adv
path: src/transformer/fused_infer_attention_score
url: https://gitee.com/ascend/cann-ops-adv/tree/master/src/transformer/fused_infer_attention_score
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- attention
- fusion
- inference
- ascendc
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
- pipeline-scheduling
- data-reuse
kernel_types:
- attention
- flash-attention
languages:
- ascendc
- cpp
---

# CANN Ops Adv — Fused Infer Attention Score

Advanced fused attention-score operator path. This is code evidence for fusing attention score computation, masking, scaling, softmax, and output staging in inference workloads.

## Code Location

- Repository: `Ascend/cann-ops-adv`
- Path: `src/transformer/fused_infer_attention_score`
- URL: https://gitee.com/ascend/cann-ops-adv/tree/master/src/transformer/fused_infer_attention_score


## Fetched Source


### `src/transformer/fused_infer_attention_score/fused_infer_attention_score.cpp`
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
 * \file fused_infer_attention_score.cpp
 * \brief
 */

#include "kernel_operator.h"
#include "kernel_operator_list_tensor_intf.h"
// ifa must include before pfa
#define FIA_ENABLE_MLA
#include "../incre_flash_attention/incre_flash_attention.cpp"
#include "../prompt_flash_attention/prompt_flash_attention.cpp"

extern "C" __global__ __aicore__ void fused_infer_attention_score(__gm__ uint8_t* query, __gm__ uint8_t* key, __gm__ uint8_t* value,
                                                             __gm__ uint8_t* pse_shift, __gm__ uint8_t* attenMask,
                                                             __gm__ uint8_t* actualSeqLengths, __gm__ uint8_t* actualSeqLengthsKV,
                                                             __gm__ uint8_t* deq_scale1, __gm__ uint8_t* quant_scale1,
                                                             __gm__ uint8_t* deq_scale2, __gm__ uint8_t* quant_scale2,
                                                             __gm__ uint8_t* quant_offset2, __gm__ uint8_t* antiquantScale,
                                                             __gm__ uint8_t* antiquantOffset, __gm__ uint8_t* blocktable,
                                                             __gm__ uint8_t* queryPaddingSize, __gm__ uint8_t* kvPaddingSize,
                                                             __gm__ uint8_t* keyAntiquantScale, __gm__ uint8_t* keyAntiquantOffset,
                                                             __gm__ uint8_t* valueAntiquantScale, __gm__ uint8_t* valueAntiquantOffset,
                                                             __gm__ uint8_t* keySharedPrefix, __gm__ uint8_t* valueSharedPrefix, __gm__ uint8_t* actualSharedPrefixLen,
                                                             __gm__ uint8_t* queryRope, __gm__ uint8_t* keyRope, __gm__ uint8_t* keyRopeAntiquantScale, __gm__ uint8_t* dequantScaleQuery,
                                                             __gm__ uint8_t* attentionOut, __gm__ uint8_t* softmaxLse, __gm__ uint8_t* workspace,
                                                             __gm__ uint8_t* tiling) {
  // judge ifa or pfa by range of tilingKey
  if(TILING_KEY_VAR >= 1000000000000000000) {
    #if (__CCE_AICORE__ == 310) || (defined __DAV_310R6__)
      prompt_flash_attention_FIAS(query, key, value, pse_shift, attenMask, actualSeqLengths, 
                                  actualSeqLengthsKV, deq_scale1, quant_scale1,
                                  deq_scale2, quant_scale2, quant_offset2, antiquantScale, 
                                  antiquantOffset, blocktable, queryPaddingSize, kvPaddingSize, 
                                  keyAntiquantScale, keyAntiquantOffset, valueAntiquantScale, 
                                  valueAntiquantOffset, keySharedPrefix, valueSharedPrefix, 
                                  actualSharedPrefixLen, queryRope, keyRope, attentionOut,
                                  softmaxLse, workspace, tiling);
    #else //__CCE_AICORE__ > 200
      prompt_flash_attention_FIAS(query, key, value, pse_shift, attenMask, actualSeqLengths, 
                                  actualSeqLengthsKV, deq_scale1, quant_scale1,
                                  deq_scale2, quant_scale2, quant_offset2, antiquantScale, 
                                  antiquantOffset, blocktable, queryPaddingSize, kvPaddingSize, 
                                  keyAntiquantScale, keyAntiquantOffset, valueAntiquantScale, 
                                  valueAntiquantOffset, keySharedPrefix, valueSharedPrefix, 
                                  actualSharedPrefixLen, queryRope, keyRope, attentionOut,
                                  softmaxLse, workspace, tiling);
    #endif
  } else {
    incre_flash_attention_FIAS(query, key, value, pse_shift, attenMask, actualSeqLengths,
                          actualSeqLengthsKV, deq_scale1, quant_scale1, deq_scale2, quant_scale2,
                          quant_offset2, antiquantScale, antiquantOffset, blocktable, queryPaddingSize, kvPaddingSize,
                          keyAntiquantScale, keyAntiquantOffset, valueAntiquantScale, valueAntiquantOffset,
                          keySharedPrefix, valueSharedPrefix, actualSharedPrefixLen, queryRope, keyRope, keyRopeAntiquantScale, dequantScaleQuery,
                          atte
// ... (truncated due to length) ...

```

### `src/transformer/fused_infer_attention_score/ophost/fused_infer_attention_score_tiling_input_index.h`
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
 * \file fused_infer_attention_score_tiling_input_index.h
 * \brief
 */

#ifndef FUSED_INFER_ATTENTION_SCORE_TILING_INPUT_INDEX_H
#define FUSED_INFER_ATTENTION_SCORE_TILING_INPUT_INDEX_H
#include "prompt_flash_attention_tiling.h"
#include "incre_flash_attention_tiling.h"
#include "register/tilingdata_base.h"

namespace optiling {
// Inputs Index
constexpr uint32_t QUERY_INDEX = 0;
constexpr uint32_t KEY_INDEX = 1;
constexpr uint32_t VALUE_INDEX = 2;
constexpr uint32_t PSE_SHIFT_INDEX = 3;
constexpr uint32_t ATTEN_MASK_INDEX = 4;
constexpr uint32_t ACTUAL_SEQ_Q_INDEX = 5;
constexpr uint32_t ACTUAL_SEQ_KV_INDEX = 6;
constexpr uint32_t DEQUANT_SCALE1_INDEX = 7;
constexpr uint32_t QUANT_SCALE1_INDEX = 8;
constexpr uint32_t DEQUANT_SCALE2_INDEX = 9;
constexpr uint32_t QUANT_SCALE2_INDEX = 10;
constexpr uint32_t QUANT_OFFSET2_INDEX = 11;
constexpr uint32_t ANTIQUANT_SCALE_INDEX = 12;
constexpr uint32_t ANTIQUANT_OFFSET_INDEX = 13;
constexpr uint32_t BLOCK_TABLE_INDEX = 14;
constexpr uint32_t QUERY_PADDING_SIZE_INDEX = 15;
constexpr uint32_t KV_PADDING_SIZE_INDEX = 16;
constexpr uint32_t KEY_ANTIQUANT_SCALE_INDEX = 17;
constexpr uint32_t KEY_ANTIQUANT_OFFSET_INDEX = 18;
constexpr uint32_t VALUE_ANTIQUANT_SCALE_INDEX = 19;
constexpr uint32_t VALUE_ANTIQUANT_OFFSET_INDEX = 20;
constexpr uint32_t KEY_SHARED_PREFIX_INDEX = 21;
constexpr uint32_t VALUE_SHARED_PREFIX_INDEX = 22;
constexpr uint32_t ACTUAL_SHARED_PREFIX_LEN_INDEX = 23;
constexpr uint32_t QUERY_ROPE_INDEX = 24;
constexpr uint32_t KEY_ROPE_INDEX = 25;
constexpr uint32_t KEY_ROPE_ANTIQUANT_SCALE_INDEX = 26;
constexpr uint32_t DEQUANT_SCALE_QUERY_INDEX = 27;
} // namespace optiling

#endif // FUSED_INFER_ATTENTION_SCORE_TILING_INPUT_INDEX_H

```

### `src/transformer/fused_infer_attention_score/ophost/aclnn_fused_infer_attention_score_v2.h`
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

#ifndef ACLNN_FUSED_INFER_ATTENTION_SCORE_V2_H_
#define ACLNN_FUSED_INFER_ATTENTION_SCORE_V2_H_
#include "aclnn/acl_meta.h"

#ifdef __cplusplus
extern "C" {
#endif

/**
 * @brief The first interface of aclnnFusedInferAttentionScoreV2 calculates the workspace size based on the specific calculation process.
 * @domain aclnn_ops_infer
 */
__attribute__((visibility("default"))) aclnnStatus aclnnFusedInferAttentionScoreV2GetWorkspaceSize(
    const aclTensor *query, const aclTensorList *key, const aclTensorList *value, const aclTensor *pseShiftOptional,
    const aclTensor *attenMaskOptional, const aclIntArray *actualSeqLengthsOptional,
    const aclIntArray *actualSeqLengthsKvOptional, const aclTensor *deqScale1Optional,
    const aclTensor *quantScale1Optional, const aclTensor *deqScale2Optional, const aclTensor *quantScale2Optional,
    const aclTensor *quantOffset2Optional, const aclTensor *antiquantScaleOptional,
    const aclTensor *antiquantOffsetOptional, const aclTensor *blockTableOptional,
    const aclTensor *queryPaddingSizeOptional, const aclTensor *kvPaddingSizeOptional,
    const aclTensor *keyAntiquantScaleOptional, const aclTensor *keyAntiquantOffsetOptional,
    const aclTensor *valueAntiquantScaleOptional, const aclTensor *valueAntiquantOffsetOptional,
    const aclTensor *keySharedPrefixOptional, const aclTensor *valueSharedPrefixOptional,
    const aclIntArray *actualSharedPrefixLenOptional, int64_t numHeads, double scaleValue, int64_t preTokens,
    int64_t nextTokens, char *inputLayout, int64_t numKeyValueHeads, int64_t sparseMode, int64_t innerPrecise,
    int64_t blockSize, int64_t antiquantMode, bool softmaxLseFlag, int64_t keyAntiquantMode, int64_t valueAntiquantMode,
    const aclTensor *attentionOut, const aclTensor *softmaxLse, uint64_t *workspaceSize, aclOpExecutor **executor);

/**
 * @brief The second interface of aclnnFusedInferAttentionScoreV2 is used to perform calculations.
 */
__attribute__((visibility("default"))) aclnnStatus aclnnFusedInferAttentionScoreV2(void *workspace,
                                                                                   uint64_t workspaceSize,
                                                                                   aclOpExecutor *executor,
                                                                                   const aclrtStream stream);


#ifdef __cplusplus
}
#endif

#endif
```
