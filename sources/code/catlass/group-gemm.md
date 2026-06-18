---
id: code-catlass-group-gemm
title: CATLASS Group GEMM Example
type: source-code
repo: Ascend/catlass
path: examples/16_group_gemm
url: https://gitee.com/ascend/catlass/tree/master/examples/16_group_gemm
source_category: upstream-code
architectures:
- ascend910b
tags:
- catlass
- grouped-gemm
- moe
- cpp
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- nz-format
- l1-buffer
- l0-buffer
techniques:
- nz-tiling
- tiling-strategy
- pipeline-scheduling
kernel_types:
- grouped-gemm
- gemm
- moe
languages:
- cpp
- ascendc
---

# CATLASS Group GEMM Example

CATLASS grouped GEMM example used as code evidence for MoE-style grouped matmul on Ascend. It demonstrates template-based per-group GEMM dispatch and Cube-friendly tile/lifecycle organization.

## Code Location

- Repository: `Ascend/catlass`
- Path: `examples/16_group_gemm`
- URL: https://gitee.com/ascend/catlass/tree/master/examples/16_group_gemm


## Fetched Source


### `examples/16_group_gemm/group_gemm.cpp`
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

// By setting the K_MAX_SHAPE_DIM macro, the dimension of the AscendC Tensor's ShapeInfo is configured to 0, 
// optimizing stack space. If you need to use the ShapeInfo of the AscendC Tensor, please undefine this macro.
#ifndef K_MAX_SHAPE_DIM
#define K_MAX_SHAPE_DIM 0
#endif

#include <iostream>
#include <string>
#include <vector>
#include <cstdint>
#include <cstdlib>
#include <cstring>

#include "helper.hpp"
#include "golden.hpp"
#include "fp16_t.h"

#include "catlass/catlass.hpp"
#include "catlass/arch/arch.hpp"
#include "catlass/gemm/block/block_mmad.hpp"
#include "catlass/gemm/kernel/group_gemm.hpp"
#include "catlass/gemm/gemm_type.hpp"
#include "catlass/layout/layout.hpp"
#include "catlass/gemm_coord.hpp"
#include "catlass/matrix_coord.hpp"
#include "catlass/gemm/dispatch_policy.hpp"
#include "catlass/epilogue/dispatch_policy.hpp"
#include "catlass/epilogue/tile/tile_copy.hpp"
#include "catlass/epilogue/tile/tile_elemwise_add.hpp"
#include "catlass/epilogue/tile/tile_elemwise_muls.hpp"
#include "catlass/epilogue/tile/tile_cast.hpp"
#include "catlass/epilogue/block/block_epilogue.hpp"

#include "catlass/status.hpp"
#include "catlass/gemm/device/device_gemm.hpp"

using namespace Catlass;
using ScalarType = float;
using fp16_t = op::fp16_t;

struct Options {
    const std::string HELPER = "16_group_gemm groupCnt mlist nlist klist [deviceId]";
    uint32_t groupCnt = 8;
    std::vector<uint32_t> mList;
    std::vector<uint32_t> nList;
    std::vector<uint32_t> kList;
    int32_t deviceId{0};

    Options() = default;

    int Parse(int argc, const char **argv) {
        enum ArgsIndex {
            GROUPCNT_INDEX = 1,
            MLIST_INDEX,
            NLIST_INDEX,
            KLIST_INDEX,
            DEVICE_ID_INDEX,
            ARGS_MAX
        };

        if (argc > ARGS_MAX || argc <= KLIST_INDEX) 
        {
            std::cerr << HELPER << std::endl;
            return -1;
        }

        groupCnt = std::atoi(argv[GROUPCNT_INDEX]);
        parseList(argv[MLIST_INDEX], mList);
        parseList(argv[NLIST_INDEX], nList);
        parseList(argv[KLIST_INDEX], kList);

        if (mList.size() != groupCnt || nList.size() != groupCnt || kList.size() != groupCnt) 
        {
            std::cerr << "List lengths do not match groupCnt." << std::endl;
            return -1;
        }

        if (argc == ARGS_MAX) 
        {
            deviceId = std::atoi(argv[DEVICE_ID_INDEX]);
        }

        return 0;
    }

private:
    void parseList(const char* str, std::vector<uint32_t>& list) 
    {
        char* copy = strdup(str);
        char* token = std::strtok(copy, ",");
        while (token != nullptr) {
            list.push_back(std::atoi(token));
            token = std::strtok(nullptr, ",");
        }
        free(copy);
    }
};

layout::RowMajor GetWorkspaceLayout(layout::RowMajor layout, uint32_t align)
{
    if (align == 0) 
    {
        return layout;
    }
    return layout::RowMajor(layout.shape(0), layout.shape(1),
        RoundUp(layout.shape(1), align));
}

layout::ColumnMajor GetWorkspaceLayout(layout::ColumnMajor layout, uint32_t align)
{
    if (align == 0) 
    {
        return layout;
    }
    return layout::ColumnMajor(layout.shape(0), layout.shape(1),
        RoundUp(layout.shape(0), align));
}

size_t GetWorkspaceLen(layout::RowMajor layout)
{
    return layout.shape(0) * layout.stride(0);
}

size_t GetWorkspaceLen(layout::ColumnMajor layout)
{
    return layout.shape(1) * layout.stride(1);
}

bool IsSameStride(layout::RowMajor layout1, layout::RowMajor layout2)
{
    return layout1.stride(0) == layout2.stride(0);
}

bool IsSameStride(layout::ColumnMajor layout1, layout::ColumnMajor layout2)
{
    return layout1.stride(1) == layout2.stride(1);
}

template <class Adapter>
void RunAdapter(Adapter matmul_op, typename Adapter::Arguments args, aclrtStream stream,
    uint32_t aicCoreNum, uint64_t fftsAddr)
{
    size_t sizeWorkspace = matmul_op.GetWorkspaceSize(args);
    uint8_t *deviceWorkspace = nullptr;
    if (sizeWorkspace > 0) 
    {
        ACL_CHECK(aclrtMalloc(reinterpret_cast<void **>(&deviceWorkspace), sizeWorkspace, ACL_MEM_MALLOC_HUGE_FIRST));
    }
    matmul_op.Initialize(args, deviceWorkspace);
    matmul_op(stream, aicCoreNum, fftsAddr);
    ACL_CHECK(aclrtSynchronizeStream(stream));
    if (sizeWorkspace > 0) 
    {
        ACL_CHECK(aclrtFree(deviceWorkspace));
    
// ... (truncated due to length) ...

```
