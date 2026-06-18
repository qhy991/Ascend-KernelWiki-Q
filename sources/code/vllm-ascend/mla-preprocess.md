---
id: code-vllm-ascend-mla-preprocess
title: vLLM Ascend MLA Preprocess Operator
type: source-code
repo: vllm-project/vllm-ascend
path: csrc/mla_preprocess
url: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/mla_preprocess
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
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

# vLLM Ascend MLA Preprocess Operator

vLLM Ascend MLA preprocess operator with host tiling and kernel code, useful for mapping attention preprocessing to vector and memory-transfer behavior.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `csrc/mla_preprocess`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/mla_preprocess


## Fetched Source


### `csrc/mla_preprocess/mla_preprocess_torch_adpt.h`
```cpp
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2026. All rights reserved.
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
#ifndef MLA_PREPROCESS_TORCH_ADPT_H
#define MLA_PREPROCESS_TORCH_ADPT_H


#include "op_host/mla_preprocess.h"

namespace vllm_ascend {
std::tuple<at::Tensor &, at::Tensor &, at::Tensor &, at::Tensor &, at::Tensor &> mla_preprocess(
    const at::Tensor &hiddenState, const at::Tensor &wdqkv,
    const c10::optional<at::Tensor> &descale0, const at::Tensor &gamma1, const c10::optional<at::Tensor> &beta1, const at::Tensor &wuq,
    const c10::optional<at::Tensor> &descale1, const at::Tensor &gamma2, const at::Tensor &cos, const at::Tensor &sin,
    const at::Tensor &wuk, const at::Tensor &kv_cache, const at::Tensor &kv_cache_rope, const at::Tensor &slotmapping,
    const c10::optional<at::Tensor> &quant_scale0, const c10::optional<at::Tensor> &quant_offset0, const c10::optional<at::Tensor> &bias0,
    const c10::optional<at::Tensor> &quant_scale1, const c10::optional<at::Tensor> &quant_offset1, const c10::optional<at::Tensor> &bias1,
    const c10::optional<at::Tensor> &ctkv_scale, const c10::optional<at::Tensor> &q_nope_scale,
    c10::optional<c10::string_view> cache_mode, c10::optional<c10::string_view> quant_mode, c10::optional<bool> enable_inner_out, at::Tensor &q_out0,
    at::Tensor &kv_cache_out0, at::Tensor &q_out1, at::Tensor &kv_cache_out1, at::Tensor &inner_out)
{
    at::Tensor Descale0 =
        descale0.has_value()
            ? descale0.value()
            : at::empty({1}, at::TensorOptions().dtype(at::kHalf).device(hiddenState.options().device()));
    at::Tensor Descale1 =
        descale1.has_value()
            ? descale1.value()
            : at::empty({1}, at::TensorOptions().dtype(at::kHalf).device(hiddenState.options().device()));
    at::Tensor Beta1 =
        beta1.has_value()
            ? beta1.value()
            : at::empty({1}, at::TensorOptions().dtype(at::kHalf).device(hiddenState.options().device()));
    at::Tensor Quant_scale0 =
        quant_scale0.has_value()
            ? quant_scale0.value()
            : at::empty({1}, at::TensorOptions().dtype(at::kHalf).device(hiddenState.options().device()));
    at::Tensor Quant_scale1 =
        quant_scale1.has_value()
            ? quant_scale1.value()
            : at::empty({1}, at::TensorOptions().dtype(at::kHalf).device(hiddenState.options().device()));
    at::Tensor Quant_offset0 =
        quant_offset0.has_value()
            ? quant_offset0.value()
            : at::empty({1}, at::TensorOptions().dtype(at::kHalf).device(hiddenState.options().device()));
    at::Tensor Quant_offset1 =
        quant_offset1.has_value()
            ? quant_offset1.value()
            : at::empty({1}, at::TensorOptions().dtype(at::kHalf).device(hiddenState.options().device()));
    at::Tensor Bias0 =
        bias0.has_value()
            ? bias0.value()
            : at::empty({1}, at::TensorOptions().dtype(at::kHalf).device(hiddenState.options().device()));
    at::Tensor Bias1 =
        bias1.has_value()
            ? bias1.value()
            : at::empty({1}, at::TensorOptions().dtype(at::kHalf).device(hiddenState.options().device()));
    at::Tensor CtkvScale =
        ctkv_scale.has_value()
            ? ctkv_scale.value()
            : at::empty({1}, at::TensorOptions().dtype(at::kHalf).device(hiddenState.options().device()));
    at::Tensor QnopeScale =
        q_nope_scale.has_value()
            ? q_nope_scale.value()
            : at::empty({1}, at::TensorOptions().dtype(at::kHalf).device(hiddenState.options().device()));
    bool enableInnerOut =
        enable_inner_out.has_value()
            ? enable_inner_out.value()
            : false;
    
    auto [workspace_tensor, tiling, block_dim] = mlapo::mla_preprocess_tiling(
        hiddenState,
        wdqkv,
        wuk,
        gamma1,
        kv_cache_rope,
        cache_mode,
        quant_mode,
        enableInnerOut
    );

    void *hidden_state_ptr = hiddenState.data_ptr();
    void *quant_scale0_ptr = Quant_scale0.data_ptr();
    void *quant_offset0_ptr = Quant_offset0.data_ptr();
    void *wdqkv_ptr = wdqkv.data_ptr();
    void *bias0_ptr = Bias0.data_ptr();
    void *gamma1_ptr = gamma1.data_ptr();
    void *beta1_ptr = Beta1.data_ptr();
    void *quant_scale1_ptr = Quant_scale1.data_ptr();
    void *quant_offset1_ptr = Quant_offset1.data_ptr();
    void *gamma2_ptr = gamma2.data_ptr();
    void *sin_ptr = sin.data_ptr();
    void *cos_ptr = cos.data
// ... (truncated due to length) ...

```

### `csrc/mla_preprocess/op_host/mla_preprocess.h`
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
// #include "defines.h"
// #include "torch_helper.h"
#include "tiling/platform/platform_ascendc.h"
#include "tiling/mla_preprocess_tiling.h"

// #include "aclrtlaunch_mla_preprocess.h"

// namespace sglang {
namespace mlapo {

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
    uint32_t isWeightQuantized;
    uint32_t hiddenStateDim;
    uint32_t N;
    uint32_t headNum;
    int32_t cacheMode;
    QuantMode quantMode;
    caffe2::TypeMeta inDtype;
    bool enableInnerOut;
    // MLA dimensions derived from tensor shapes
    uint32_t qLoraRank;
    uint32_t qkNopeHeadDim;
    uint32_t qkRopeHeadDim;
    uint32_t kvLoraRank;
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

    uint32_t isWeightQuantized{1};

    // Model-specific MLA dimensions (derived from tensor shapes)
    uint32_t mm1OutSize{2112};        // q_lora_rank + kv_lora_rank + qk_rope_head_dim
    uint32_t splitSizeOne{576};        // kv_lora_rank + qk_rope_head_dim
    uint32_t splitSizeTwo{1536};       // q_lora_rank
    uint32_t splitRmsNormSizeOne{512}; // kv_lora_rank
    uint32_t splitRmsNormSizeTwo{64};  // qk_rope_head_dim
    uint32_t ropeSplitSizeOne{64};     // qk_rope_head_dim
    uint32_t ropeSplitSizeTwo{128};    // qk_nope_head_dim
    uint32_t hiddenStrideRope{192};    // qk_nope_head_dim + qk_rope_head_dim
    uint32_t qkNopeHeadDim{128};       // for RoPE offset calc
    float avgFactor{0.000651041666f};  // 1/splitSizeTwo (1/qLoraRank), for RmsNorm avg
};

#endif  // MLAPREPROCESS_TILING_H

```
