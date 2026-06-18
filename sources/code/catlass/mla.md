---
id: code-catlass-mla
title: CATLASS MLA Example
type: source-code
repo: Ascend/catlass
path: examples/19_mla
url: https://gitee.com/ascend/catlass/tree/master/examples/19_mla
source_category: upstream-code
architectures:
- ascend910b
tags:
- catlass
- mla
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
- matmul
- flash-attention
languages:
- cpp
- ascendc
---

# CATLASS MLA Example

CATLASS MLA example providing code evidence for attention-style matmul pipelines used in inference, including mixed Cube/Vector work and cache-aware data movement.

## Code Location

- Repository: `Ascend/catlass`
- Path: `examples/19_mla`
- URL: https://gitee.com/ascend/catlass/tree/master/examples/19_mla


## Fetched Source


### `examples/19_mla/mla_kernel.cpp`
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

#include "kernel_common.hpp"

using namespace Catlass;

/*
This example demonstrates how to compute mla.
*/
template <
    class BlockMmadQK,
    class BlockMmadPV,
    class EpilogueMLASoftmax,
    class EpilogueMLARescaleO,
    class EpilogueMLAFDRescaleO>
class MLAKernel {
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

    using ElementMask = half;

    using ElementO = typename EpilogueMLARescaleO::ElementOutput;
    using LayoutO = typename EpilogueMLARescaleO::LayoutOutput;

    using ElementOTmp = typename EpilogueMLARescaleO::ElementInput;
    using LayoutOTmp = typename EpilogueMLARescaleO::LayoutInput;

    using ElementUpdate = typename EpilogueMLARescaleO::ElementUpdate;
    using LayoutUpdate = typename EpilogueMLARescaleO::LayoutUpdate;

    static constexpr uint32_t KV_SPLIT_MAX = EpilogueMLAFDRescaleO::KV_SPLIT_MAX;
    static constexpr uint32_t HEADS_PROCESS_MAX = EpilogueMLAFDRescaleO::HEADS_PROCESS_MAX;
    static constexpr uint32_t COMPUTE_ELE_NUM = EpilogueMLAFDRescaleO::COMPUTE_ELE_NUM;

    /// Parameters structure
    struct Params {
        // Data members
        GM_ADDR q;
        GM_ADDR qRope;
        GM_ADDR k;
        GM_ADDR kRope;
        GM_ADDR blockTables;
        GM_ADDR o;
        GM_ADDR s;
        GM_ADDR p;
        GM_ADDR oTmp;
        GM_ADDR oUpdate;
        GM_ADDR oCoreTmp;
        GM_ADDR l;
        GM_ADDR tiling;

        // Methods
        CATLASS_DEVICE
        Params() {}

        CATLASS_DEVICE
        Params(GM_ADDR q_, GM_ADDR qRope_, GM_ADDR k_, GM_ADDR kRope_, GM_ADDR blockTables_,
               GM_ADDR o_, GM_ADDR s_, GM_ADDR p_, GM_ADDR oTmp_, GM_ADDR oUpdate_,
               GM_ADDR oCoreTmp_, GM_ADDR l_, GM_ADDR tiling_)
            : q(q_), qRope(qRope_), k(k_), kRope(kRope_), blockTables(blockTables_), o(o_),
              s(s_), p(p_), oTmp(oTmp_), oUpdate(oUpdate_), oCoreTmp(oCoreTmp_), l(l_), tiling(tiling_) {}
    };

    // Methods
    CATLASS_DEVICE
    MLAKernel() {}

    template <int32_t CORE_TYPE = g_coreType>
    CATLASS_DEVICE void operator()(Params const &params);

    template <>
    CATLASS_DEVICE void operator()<AscendC::AIC>(Params const &params)
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
        AscendC::SetFlag<Asc
// ... (truncated due to length) ...

```

### `examples/19_mla/mla_tiling.cpp`
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

#include <cmath>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

#include "catlass/detail/alignment.hpp"
#include "mla_tiling.h"

using namespace std;
namespace MLATiling {
    using AddrOffsets = struct AddressOffsetInfo {
    uint64_t addrQSeqOffset = 0;
    uint64_t addrQSeqRopeOffset = 0;
    uint64_t addrMaskBatchOffset = 0;
    uint64_t addrOFdSeqOffset = 0;
    uint64_t addrLSeqOffset = 0;
};

inline uint32_t GetHigh32Bit(uint64_t v) { return static_cast<uint32_t>(v >> NUM32); }
inline uint32_t GetLow32Bit(uint64_t v) { return static_cast<uint32_t>(v); }

void GetAddrOffsetMLA(uint32_t *tilingHost, const AddrOffsets addrOffsets, const int32_t tilingOffset)
{
    // Calculate address offset
    tilingHost[tilingOffset + NUM4] = GetHigh32Bit(addrOffsets.addrQSeqOffset);
    tilingHost[tilingOffset + NUM5] = GetLow32Bit(addrOffsets.addrQSeqOffset);
    tilingHost[tilingOffset + NUM6] = GetHigh32Bit(addrOffsets.addrQSeqRopeOffset);
    tilingHost[tilingOffset + NUM7] = GetLow32Bit(addrOffsets.addrQSeqRopeOffset);
    tilingHost[tilingOffset + NUM8] = GetHigh32Bit(addrOffsets.addrMaskBatchOffset);
    tilingHost[tilingOffset + NUM9] = GetLow32Bit(addrOffsets.addrMaskBatchOffset);
}

void GetMLATilingCommon(const MLAInfo &mlaInfo, uint32_t &blockDim, uint32_t *tilingHost)
{
    // Calculate the batch-related tiling parameters
    int32_t maxKVSeqlen = 0;
    int32_t maxQSeqlen = 0;
    AddrOffsets addrOffsets{};
    for (int32_t seqIdx = 0; seqIdx < mlaInfo.batch; seqIdx++) {
        int32_t qSeqLen = *(mlaInfo.qSeqLen + seqIdx);
        qSeqLen = (*(mlaInfo.kvSeqLen + seqIdx) == 0) ? 0 : qSeqLen;
        maxQSeqlen = std::max(maxQSeqlen, qSeqLen);
        int32_t kvSeqlen = *(mlaInfo.kvSeqLen + seqIdx);
        maxKVSeqlen = std::max(maxKVSeqlen, kvSeqlen);
        int32_t tilingOffset = TILING_HEAD_SIZE + TILING_PARA_SIZE * seqIdx;
        tilingHost[tilingOffset] = static_cast<uint32_t>(qSeqLen);
        tilingHost[tilingOffset + NUM1] = static_cast<uint32_t>(kvSeqlen);
        tilingHost[tilingOffset + NUM3] = static_cast<uint32_t>(mlaInfo.blockSize);
        GetAddrOffsetMLA(tilingHost, addrOffsets, tilingOffset);
        uint64_t addressOffset = static_cast<uint64_t>(mlaInfo.numHeads * mlaInfo.embeddingSize * qSeqLen);
        uint64_t addressMaskOffset = static_cast<uint64_t>(mlaInfo.maxKvSeqlen * qSeqLen);
        uint64_t addressOffsetRope = static_cast<uint64_t>(mlaInfo.numHeads * mlaInfo.embeddingSizeRope * qSeqLen);
        addrOffsets.addrQSeqOffset += addressOffset;
        addrOffsets.addrQSeqRopeOffset += addressOffsetRope;
        addrOffsets.addrMaskBatchOffset += addressMaskOffset;
    }
    tilingHost[TILING_MAX_KVSEQLEN] = maxKVSeqlen;
    tilingHost[TILING_MAX_QSEQLEN] = maxQSeqlen;
}

void GetMLATilingSpec(const MLAInfo &mmInfo, uint32_t &blockDim, uint32_t *tilingHost)
{
    // Tp1 senario specialization
    // Treat every Q token with 128 heads as one process, regardless of the mtp depth
    int32_t prevTaskNum = 0;
    int32_t maxKVSeqlen = 0;
    for (int32_t seqIdx = 0; seqIdx < mmInfo.batch; seqIdx++) {
        int32_t qSeqLen = mmInfo.qSeqLen == nullptr ? 1 : *(mmInfo.qSeqLen + seqIdx);
        int32_t kvSeqlen = *(mmInfo.kvSeqLen + seqIdx);
        maxKVSeqlen = std::max(maxKVSeqlen, kvSeqlen);
        for (int32_t qSeq = 0; qSeq < qSeqLen; qSeq++) {
            int32_t tilingOffset = TILING_HEAD_SIZE + PARA_TILING_ELENUM_SPEC * prevTaskNum;
            tilingHost[tilingOffset] = seqIdx;
            tilingHost[tilingOffset + NUM1] = prevTaskNum;
            tilingHost[tilingOffset + NUM2] = kvSeqlen;
            prevTaskNum++;
        }
    }
    tilingHost[TILING_MAX_KVSEQLEN] = maxKVSeqlen;
}

int32_t GetQNBlockTile(const MLAInfo &mlaInfo, int32_t qSeqLen, uint32_t specStrategyFlag)
{
    int32_t tokenNum = qSeqLen;
    if (specStrategyFlag) {
        tokenNum = NUM1;
    }
    int32_t tileListIdx = static_cast<int32_t>(std::ceil(std::log2(tokenNum)));
    tileListIdx = (tileListIdx > NUM5) ? NUM5 : tileListIdx;
    int32_t qNBlockTile = QN_TILE_LIST[tileListIdx];
    int32_t group = mlaInfo.numHeads / mlaInfo.kvHeads;
    qNBlockTile = (qNBlockTile > group) ? group : qNBlockTile;
    return qNBlockTile;
}

void GetTilingHead(const MLAInfo &mlaInfo, uint32_t *tilingHost, const uin
// ... (truncated due to length) ...

```

### `examples/19_mla/mla_kernel_tp1_spec.cpp`
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

#include "kernel_common.hpp"

using namespace Catlass;
/*
This example demonstrates how to compute mla.
*/
template <class BlockMmadQK, class BlockMmadPV, class EpilogueMLASoftmax, class EpilogueMLARescaleO,
          class EpilogueMLAFDRescaleO>
class MLAKernelTp1Spec {
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

    using ElementMask = half;

    using ElementO = typename EpilogueMLARescaleO::ElementOutput;
    using LayoutO = typename EpilogueMLARescaleO::LayoutOutput;

    using ElementOTmp = typename EpilogueMLARescaleO::ElementInput;
    using LayoutOTmp = typename EpilogueMLARescaleO::LayoutInput;

    using ElementUpdate = typename EpilogueMLARescaleO::ElementUpdate;
    using LayoutUpdate = typename EpilogueMLARescaleO::LayoutUpdate;

    static constexpr uint32_t KV_SPLIT_MAX = EpilogueMLAFDRescaleO::KV_SPLIT_MAX;
    static constexpr uint32_t HEADS_PROCESS_MAX = EpilogueMLAFDRescaleO::HEADS_PROCESS_MAX;
    static constexpr uint32_t COMPUTE_ELE_NUM = EpilogueMLAFDRescaleO::COMPUTE_ELE_NUM;

    /// Parameters structure
    struct Params {
        // Data members
        GM_ADDR q;
        GM_ADDR qRope;
        GM_ADDR k;
        GM_ADDR kRope;
        GM_ADDR blockTables;
        GM_ADDR o;
        GM_ADDR s;
        GM_ADDR p;
        GM_ADDR oTmp;
        GM_ADDR oUpdate;
        GM_ADDR oCoreTmp;
        GM_ADDR l;
        GM_ADDR tiling;

        // Methods
        CATLASS_DEVICE
        Params() {}

        CATLASS_DEVICE
        Params(GM_ADDR q_, GM_ADDR qRope_, GM_ADDR k_, GM_ADDR kRope_, GM_ADDR blockTables_, GM_ADDR o_, GM_ADDR s_,
               GM_ADDR p_, GM_ADDR oTmp_, GM_ADDR oUpdate_, GM_ADDR oCoreTmp_, GM_ADDR l_, GM_ADDR tiling_)
            : q(q_), qRope(qRope_), k(k_), kRope(kRope_), blockTables(blockTables_), o(o_), s(s_), p(p_), oTmp(oTmp_),
              oUpdate(oUpdate_), oCoreTmp(oCoreTmp_), l(l_), tiling(tiling_)
        {
        }
    };

    // Methods
    CATLASS_DEVICE
    MLAKernelTp1Spec() {}

    template <int32_t CORE_TYPE = g_coreType> CATLASS_DEVICE void operator()(Params const &params);

    template <> CATLASS_DEVICE void operator()<AscendC::AIC>(Params const &params)
    {
        AscendC::SetFlag<AscendC::HardEvent::M_MTE1>(EVENT_ID0);
        AscendC::SetFlag<AscendC::HardEvent::M_MTE1>(EVENT_ID1);
        AscendC::SetFlag<AscendC::HardEvent::M_MTE1>(EVENT_ID2);
        AscendC::SetFlag<AscendC::HardEvent::M_MTE1>(EVENT_ID3);

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

        // Get the memory offset address of the input on Global Memory
        AscendC::GlobalTensor<ElementQ> gQ;
        gQ.SetGlobalBuffer((__gm__ ElementQ *)params.q);
        AscendC::GlobalTensor<ElementQ> gQRope;
        gQRope.SetGlobalBuffer((__gm__ ElementQ *)params.qRope);
    
// ... (truncated due to length) ...

```
