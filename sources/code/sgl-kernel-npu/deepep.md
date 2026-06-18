---
id: code-sgl-kernel-npu-deepep
title: SGL Kernel NPU DeepEP Operators
type: source-code
repo: sgl-project/sgl-kernel-npu
path: csrc/deepep/ops
url: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/deepep/ops
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- sglang
- deepep
- moe
- communication
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- hccs
- global-memory
techniques:
- tensor-parallel-overlap
- hccl-optimization
- pipeline-scheduling
kernel_types:
- moe
- grouped-gemm
- matmul
languages:
- cpp
- ascendc
---

# SGL Kernel NPU DeepEP Operators

SGL Kernel NPU DeepEP operator source, useful as evidence for MoE dispatch/combine kernels and communication-aware inference execution.

## Code Location

- Repository: `sgl-project/sgl-kernel-npu`
- Path: `csrc/deepep/ops`
- URL: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/deepep/ops


## Fetched Source


### `csrc/deepep/ops/quantize_functions.h`
```cpp
/**
 * Copyright (c) 2025 Huawei Technologies Co., Ltd.
 * This program is free software, you can redistribute it and/or modify it under the terms and conditions of
 * CANN Open Software License Agreement Version 2.0 (the "License").
 * Please refer to the License for details. You may not use this file except in compliance with the License.
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
 * See LICENSE in the root of the software repository for the full text of the License.
 */

/*!
 * \file quantize_functions.h
 * \brief
 */

#ifndef QUANTIZE_FUNCTIONS_H
#define QUANTIZE_FUNCTIONS_H

#include "common.h"

namespace quant {

#ifdef __DAV_C310__

constexpr int DIGIT_TWO = 2;
constexpr uint16_t MAX_EXP_FOR_BF16 = 0x7f80;
constexpr uint16_t BF16_EXP_BIAS = 0x7f00;
constexpr uint16_t MAX_EXP_FOR_FP8 = 0x00ff;
constexpr uint16_t NAN_CUSTOMIZATION = 0x7f81;
constexpr uint16_t SPECIAL_EXP_THRESHOLD = 0x0040;
constexpr int16_t SHR_NUM_FOR_BF16 = 7;
constexpr uint16_t FP8_E4M3_MAX_EXP = 0x0400;  // elem_emax右移7位(BF16E8M7)
constexpr uint16_t FP8_E5M2_MAX_EXP = 0x0780;
constexpr int64_t OUT_ELE_NUM_ONE_BLK = 64;
constexpr float FP8_E5M2_MAX_VALUE = 57344.0f;
constexpr float FP8_E4M3_MAX_VALUE = 448.0f;
constexpr float HIFP8_MAX_VALUE = 32768.0f;
constexpr float INT8_MAX_VALUE = 127.0f;

using namespace AscendC;

__aicore__ inline constexpr uint32_t GetUbBlockSizeDispatch()
{
    return 32U;
}

__aicore__ inline constexpr uint32_t GetVRegSizeDispatch()
{
#if __CCE_AICORE__ == 310
    return AscendC::VECTOR_REG_WIDTH;
#else
    return 256U;
#endif
}

template <typename T>
__aicore__ inline void ComputeMaxExp(__ubuf__ T *srcAddr, __ubuf__ uint16_t *maxExpAddr, uint32_t totalCountInUB)
{
    uint32_t vlForHalfNumber = GetVRegSizeDispatch() / sizeof(T);
    uint16_t elementAfterReduce = GetVRegSizeDispatch() / GetUbBlockSizeDispatch();
    uint16_t loopNum = Ceil(totalCountInUB, 2 * vlForHalfNumber);

    __VEC_SCOPE__
    {
        MicroAPI::RegTensor<T> vdExp0;
        MicroAPI::RegTensor<T> vdExp1;
        MicroAPI::RegTensor<bfloat16_t> vdExp0BF16;
        MicroAPI::RegTensor<bfloat16_t> vdExp1BF16;
        MicroAPI::RegTensor<uint16_t> vdExpExtract0;
        MicroAPI::RegTensor<uint16_t> vdExpExtract1;

        MicroAPI::RegTensor<uint16_t> expMaskBF16;
        MicroAPI::Duplicate(expMaskBF16, MAX_EXP_FOR_BF16);

        MicroAPI::RegTensor<uint16_t> vdMaxExp;
        MicroAPI::MaskReg scaleMask1;
        MicroAPI::MaskReg scaleMask2;
        MicroAPI::UnalignReg u1;
        static constexpr MicroAPI::CastTrait castTraitHalf2Bf16 = {
            MicroAPI::RegLayout::UNKNOWN, MicroAPI::SatMode::UNKNOWN, MicroAPI::MaskMergeMode::ZEROING,
            RoundMode::CAST_TRUNC};
        for (uint16_t i = 0; i < loopNum; i++) {
            scaleMask1 = MicroAPI::UpdateMask<T>(totalCountInUB);
            scaleMask2 = MicroAPI::UpdateMask<T>(totalCountInUB);
            MicroAPI::DataCopy<T, MicroAPI::PostLiteral::POST_MODE_UPDATE, MicroAPI::LoadDist::DIST_DINTLV_B16>(
                vdExp0, vdExp1, srcAddr, vlForHalfNumber * DIGIT_TWO);
            if constexpr (Std::IsSame<T, half>::value) {
                MicroAPI::Cast<bfloat16_t, T, castTraitHalf2Bf16>(vdExp0BF16, vdExp0, scaleMask1);
                MicroAPI::Cast<bfloat16_t, T, castTraitHalf2Bf16>(vdExp1BF16, vdExp1, scaleMask1);
                MicroAPI::And(vdExpExtract0, (MicroAPI::RegTensor<uint16_t> &)vdExp0BF16, expMaskBF16, scaleMask1);
                MicroAPI::And(vdExpExtract1, (MicroAPI::RegTensor<uint16_t> &)vdExp1BF16, expMaskBF16, scaleMask1);
            } else {
                MicroAPI::And(vdExpExtract0, (MicroAPI::RegTensor<uint16_t> &)vdExp0, expMaskBF16, scaleMask1);
                MicroAPI::And(vdExpExtract1, (MicroAPI::RegTensor<uint16_t> &)vdExp1, expMaskBF16, scaleMask1);
            }

            MicroAPI::Max(vdMaxExp, vdExpExtract0, vdExpExtract1, scaleMask1);
            MicroAPI::ReduceMaxWithDataBlock(vdMaxExp, vdMaxExp, scaleMask1);

            MicroAPI::DataCopyUnAlign<uint16_t, MicroAPI::PostLiteral::POST_MODE_UPDATE>(maxExpAddr, vdMaxExp, u1,
                                                                                         elementAfterReduce);
        }
        MicroAPI::DataCopyUnAlignPost(maxExpAddr, u1, 0);
    }
}

template <typename T>
__aicore__ inline void ComputeScale(__ubuf__ uint16_t *maxExpAddr, __ubuf__ uint16_t *mxScaleLocalAddr,
                                    __ubuf__ uint16_t *halfScaleLocalAddr, uint32_t totalScaleInUB)
{
    uint32_t vlForHalfNumber = GetVRegSizeDispatch() / sizeof(uint16_t);
    uint16_t f8Emax = std::is_same<T, fp8_e4m3fn_t>::value ? FP8_E4M3_MAX_EXP : FP8_E5M2_MAX_EXP;
    uint16_t loopNumScale = Ceil(totalScaleInUB, vlForHalfNumber);

    __VEC_SCOPE__
    {
        MicroAPI::RegTensor<uint16_t> expMask;
        MicroAPI:
// ... (truncated due to length) ...

```

### `csrc/deepep/ops/common.h`
```cpp
/**
 * Copyright (c) 2025 Huawei Technologies Co., Ltd.
 * This program is free software, you can redistribute it and/or modify it under the terms and conditions of
 * CANN Open Software License Agreement Version 2.0 (the "License").
 * Please refer to the License for details. You may not use this file except in compliance with the License.
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
 * See LICENSE in the root of the software repository for the full text of the License.
 */

/*!
 * \file common.h
 * \brief
 */

#ifndef MC2_MOE_DISPATCH_COMM_H
#define MC2_MOE_DISPATCH_COMM_H

constexpr uint32_t NEED_ONE_HUNDRED_AND_TWENTY_SEVEN = 127;
constexpr uint32_t RIGHT_SHIFT_BIT_SEVEN = 7;
constexpr uint32_t NEED_THIRTY_FIRST = 31;
constexpr uint32_t ALIGN_UP_TO_2_MASK = 1;
constexpr uint32_t ALIGN_UP_TO_32_MASK = 31;
constexpr uint32_t ALIGN_UP_TO_64_MASK = 64;
constexpr uint32_t ALIGN_UP_TO_128_MASK = 127;
constexpr uint32_t ALIGN_UP_TO_256_MASK = 255;
constexpr uint32_t ALIGN_UP_TO_512_MASK = 511;
constexpr uint32_t RIGHT_SHIFT_BIT_FIVE = 5;
constexpr uint32_t FIVE_HUNDRED_AND_ELEVEN = 511;
constexpr uint32_t RIGHT_SHIFT_BIT_NINE = 9;

namespace AscendC {
template <typename T1, typename T2>
__aicore__ inline T2 Ceil(T1 x, T1 y)
{
    return (x + y - 1) / y;
}

template <typename T>
__aicore__ inline T Ceil32(T x)
{
    return (x + NEED_THIRTY_FIRST) >> RIGHT_SHIFT_BIT_FIVE;
}

template <typename T>
__aicore__ inline T Ceil128(T x)
{
    return (x + NEED_ONE_HUNDRED_AND_TWENTY_SEVEN) >> RIGHT_SHIFT_BIT_SEVEN;
}

template <typename T>
__aicore__ inline T Ceil512(T x)
{
    return (x + FIVE_HUNDRED_AND_ELEVEN) >> RIGHT_SHIFT_BIT_NINE;
}

template <typename T1, typename T2>
__aicore__ inline T2 Align(T1 x, T1 y)
{
    return Ceil<T1, T2>(x, y) * y;
}

template <typename T>
__aicore__ inline T Align2(T x)
{
    return (x + ALIGN_UP_TO_2_MASK) & (~ALIGN_UP_TO_2_MASK);
}

template <typename T>
__aicore__ inline T Align32(T x)
{
    return (x + ALIGN_UP_TO_32_MASK) & (~ALIGN_UP_TO_32_MASK);
}

template <typename T>
__aicore__ inline T Align64(T x)
{
    return (x + ALIGN_UP_TO_64_MASK) & (~ALIGN_UP_TO_64_MASK);
}

template <typename T>
__aicore__ inline T Align128(T x)
{
    return (x + ALIGN_UP_TO_128_MASK) & (~ALIGN_UP_TO_128_MASK);
}

template <typename T>
__aicore__ inline T Align256(T x)
{
    return (x + ALIGN_UP_TO_256_MASK) & (~ALIGN_UP_TO_256_MASK);
}

template <typename T>
__aicore__ inline T Align512(T x)
{
    return (x + ALIGN_UP_TO_512_MASK) & (~ALIGN_UP_TO_512_MASK);
}

#ifdef __DAV_C310__
template <MicroAPI::HistogramsType htype, typename T, typename U>
static __aicore__ inline void HistogramsVf(__local_mem__ U *dst, __local_mem__ T *src, uint16_t repeatElm,
                                           uint16_t halfRepeat, uint32_t totalElm, uint16_t repeatTimes)
{
    AscendC::MicroAPI::RegTensor<T> srcReg;
    AscendC::MicroAPI::RegTensor<U> dst0Reg;
    AscendC::MicroAPI::RegTensor<U> dst1Reg;
    AscendC::MicroAPI::MaskReg pregOut = AscendC::MicroAPI::CreateMask<T>();
    MicroAPI::Duplicate(dst0Reg, 0);
    MicroAPI::Duplicate(dst1Reg, 0);
    for (uint16_t i = 0; i < repeatTimes; ++i) {
        MicroAPI::MaskReg preg = MicroAPI::UpdateMask<T>(totalElm);
        MicroAPI::DataCopy(srcReg, src + repeatElm * i);
        MicroAPI::Histograms<T, U, MicroAPI::HistogramsBinType::BIN0, htype>(dst0Reg, srcReg, preg);
        MicroAPI::Histograms<T, U, MicroAPI::HistogramsBinType::BIN1, htype>(dst1Reg, srcReg, preg);
    }
    MicroAPI::DataCopy(dst, dst0Reg, pregOut);
    MicroAPI::DataCopy(dst + halfRepeat, dst1Reg, pregOut);
}

__aicore__ inline void GetExpertFreq(LocalTensor<uint16_t> &dstLocal, LocalTensor<uint8_t> &srcLocal, uint32_t totalElm)
{
    uint32_t repeatElm = GetVecLen();
    uint16_t repeatTimes = Ceil<uint32_t, uint16_t>(totalElm, repeatElm);
    __local_mem__ uint8_t *src = (__local_mem__ uint8_t *)srcLocal.GetPhyAddr();
    __local_mem__ uint16_t *dst = (__local_mem__ uint16_t *)dstLocal.GetPhyAddr();
    VF_CALL<HistogramsVf<MicroAPI::HistogramsType::FREQUENCY, uint8_t, uint16_t>>(dst, src, repeatElm, repeatElm >> 1,
                                                                                  totalElm, repeatTimes);
    PipeBarrier<PIPE_V>();
}

__aicore__ inline void GetExpertCumSum(LocalTensor<uint16_t> &dstLocal, LocalTensor<uint8_t> &srcLocal,
                                       uint32_t totalElm)
{
    uint32_t repeatElm = GetVecLen();
    uint16_t repeatTimes = Ceil<uint32_t, uint16_t>(totalElm, repeatElm);
    __local_mem__ uint8_t *src = (__local_mem__ uint8_t *)srcLocal.GetPhyAddr();
    __local_mem__ uint16_t *dst = (__local_mem__ uint16_t *)dstLocal.GetPhyAddr();
    VF_CALL<HistogramsVf<MicroAPI::HistogramsType::ACCUMULATE, uint8_t, uint16_t>>(dst, src, repeatElm, repeatElm >> 1,
                          
// ... (truncated due to length) ...

```

### `csrc/deepep/ops/op_host/dispatch_ffn_combine_def.cpp`
```cpp
/**
 * Copyright (c) 2025 Huawei Technologies Co., Ltd.
 * This file is a part of the CANN Open Software.
 * Licensed under CANN Open Software License Agreement Version 1.0 (the "License").
 * Please refer to the License for details. You may not use this file except in compliance with the License.
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
 * See LICENSE in the root of the software repository for the full text of the License.
 */

/*!
 * \file dispatch_ffn_combine_def.cpp
 * \brief
 */
#include "register/op_def_registry.h"

namespace ops {
class DispatchFFNCombine : public OpDef
{
public:
    explicit DispatchFFNCombine(const char *name) : OpDef(name)
    {
        this->Input("a")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT16, ge::DT_BF16, ge::DT_BF16})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND})
            .UnknownShapeFormat({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
        this->Input("w1")
            .ParamType(REQUIRED)
            .DataType({ge::DT_INT8, ge::DT_INT8, ge::DT_INT8})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_FRACTAL_NZ})
            .UnknownShapeFormat({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_FRACTAL_NZ});
        this->Input("w2")
            .ParamType(REQUIRED)
            .DataType({ge::DT_INT8, ge::DT_INT8, ge::DT_INT8})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_FRACTAL_NZ})
            .UnknownShapeFormat({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_FRACTAL_NZ});
        this->Input("expertIdx")
            .ParamType(REQUIRED)
            .DataType({ge::DT_INT32, ge::DT_INT32, ge::DT_INT32})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND})
            .UnknownShapeFormat({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
        this->Input("scale1")
            .ParamType(REQUIRED)
            .DataType({ge::DT_INT64, ge::DT_INT64, ge::DT_INT64})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND})
            .UnknownShapeFormat({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
        this->Input("scale2")
            .ParamType(REQUIRED)
            .DataType({ge::DT_INT64, ge::DT_INT64, ge::DT_INT64})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND})
            .UnknownShapeFormat({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
        this->Input("probs")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT, ge::DT_FLOAT, ge::DT_FLOAT})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND})
            .UnknownShapeFormat({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});

        // Output
        this->Output("out")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT16, ge::DT_BF16, ge::DT_BF16})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND})
            .UnknownShapeFormat({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
        this->Output("expert_token_nums")
            .ParamType(REQUIRED)
            .DataType({ge::DT_INT32, ge::DT_INT32, ge::DT_INT32})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND})
            .UnknownShapeFormat({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});

        this->Attr("group").AttrType(REQUIRED).String();
        this->Attr("ep_rank_size").Int();
        this->Attr("ep_rank_id").Int();
        this->Attr("M").AttrType(OPTIONAL).Int();  // global_bs
        this->Attr("transB").AttrType(OPTIONAL).Bool(false);
        this->Attr("weightNz").AttrType(OPTIONAL).Bool(false);

        OpAICoreConfig aicore_config;
        aicore_config.DynamicCompileStaticFlag(true)
            .DynamicFormatFlag(true)
            .DynamicRankSupportFlag(true)
            .DynamicShapeSupportFlag(true)
            .NeedCheckSupportFlag(false)
            .PrecisionReduceFlag(true)
            .ExtendCfgInfo("aclnnSupport.value", "support_aclnn")
            .ExtendCfgInfo("jitCompile.flag", "static_false")
            .ExtendCfgInfo("multiKernelSupportDynamicGraph.value", "multi_kernel");
        this->AICore().AddConfig("ascend910_93", aicore_config);
        this->MC2().HcclGroup("group");
    }
};

OP_ADD(DispatchFFNCombine);
}  // namespace ops

```
