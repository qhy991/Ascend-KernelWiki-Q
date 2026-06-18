---
id: code-vllm-ascend-matmul-allreduce-rmsnorm
title: vLLM Ascend Matmul AllReduce Add RMSNorm Operator
type: source-code
repo: vllm-project/vllm-ascend
path: csrc/mc2/matmul_allreduce_add_rmsnorm
url: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/mc2/matmul_allreduce_add_rmsnorm
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
- matmul
- allreduce
- rmsnorm
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
- cube-vector-overlap
kernel_types:
- matmul
- gemm
- rmsnorm
languages:
- cpp
- ascendc
---

# vLLM Ascend Matmul AllReduce Add RMSNorm Operator

vLLM Ascend MC2 operator fusing matmul, communication, residual add, and RMSNorm; it is source evidence for tensor-parallel overlap around NPU GEMM.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `csrc/mc2/matmul_allreduce_add_rmsnorm`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/mc2/matmul_allreduce_add_rmsnorm


## Fetched Source


### `csrc/mc2/matmul_allreduce_add_rmsnorm/matmul_allreduce_add_rmsnorm_torch_adpt.h`
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
#ifndef MATMUL_ALLREDUCE_ADD_RMSNORM_TORCH_ADPT_H
#define MATMUL_ALLREDUCE_ADD_RMSNORM_TORCH_ADPT_H
namespace vllm_ascend {

std::tuple<at::Tensor, at::Tensor> matmul_allreduce_add_rmsnorm(
    const at::Tensor &x1,
    const at::Tensor &x2,
    const at::Tensor &residual,
    const at::Tensor &gamma,
    c10::string_view group_tp,
    int64_t tp_rank_size,
    int64_t tp_rank_id,
    double epsilon,
    bool is_trans_b,
    bool is_gather_add_out)
    {
        at::Tensor output = at::empty_like(residual);
        at::Tensor add_out = at::empty_like(residual);

        std::string group_tp_str(group_tp);

        char *group_tp_ptr = group_tp_str.data();

        float epsilon_f = static_cast<float>(epsilon);
        EXEC_NPU_CMD(aclnnMatmulAllreduceAddRmsnorm,
            // input
            x1, x2, residual, gamma,
            // attr
            group_tp_ptr, tp_rank_size, tp_rank_id, epsilon_f, is_trans_b, is_gather_add_out,
            // output
            output, add_out);

        return {output, add_out};
    }
}
#endif
```

### `csrc/mc2/matmul_allreduce_add_rmsnorm/op_host/matmul_allreduce_add_rmsnorm_def.cpp`
```cpp
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2025. All rights reserved.
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

#include "register/op_def_registry.h"

namespace ops{
class MatmulAllreduceAddRmsnorm : public OpDef {
public:
    explicit MatmulAllreduceAddRmsnorm(const char* name) : OpDef(name)
    {
        this->Input("x1")
            .ParamType(REQUIRED)
            .DataType({ge::DT_BF16, ge::DT_FLOAT16})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND})
            .UnknownShapeFormat({ge::FORMAT_ND, ge::FORMAT_ND});
        this->Input("x2")
            .ParamType(REQUIRED)
            .DataType({ge::DT_BF16, ge::DT_FLOAT16})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND})
            .UnknownShapeFormat({ge::FORMAT_ND, ge::FORMAT_ND});
        this->Input("residual")
            .ParamType(REQUIRED)
            .DataType({ge::DT_BF16, ge::DT_FLOAT16})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND})
            .UnknownShapeFormat({ge::FORMAT_ND, ge::FORMAT_ND});
        this->Input("gamma")
            .ParamType(REQUIRED)
            .DataType({ge::DT_BF16, ge::DT_FLOAT16})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND})
            .UnknownShapeFormat({ge::FORMAT_ND, ge::FORMAT_ND});
        this->Output("y")
            .ParamType(REQUIRED)
            .DataType({ge::DT_BF16, ge::DT_FLOAT16})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND})
            .UnknownShapeFormat({ge::FORMAT_ND, ge::FORMAT_ND});
        this->Output("add_out")
            .ParamType(REQUIRED)
            .DataType({ge::DT_BF16, ge::DT_FLOAT16})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND})
            .UnknownShapeFormat({ge::FORMAT_ND, ge::FORMAT_ND});

        this->Attr("group_tp").String();
        this->Attr("tp_rank_size").Int();
        this->Attr("tp_rank_id").Int();
        this->Attr("epsilon").AttrType(OPTIONAL).Float(1e-6);
        this->Attr("is_trans_b").AttrType(OPTIONAL).Bool(false);
        this->Attr("is_gather_add_out").AttrType(OPTIONAL).Bool(false);

        this->MC2().HcclGroup({"group_tp"});
        this->AICore().AddConfig("ascend910b");
    }
};

OP_ADD(MatmulAllreduceAddRmsnorm);
}
```

### `csrc/mc2/matmul_allreduce_add_rmsnorm/op_host/matmul_allreduce_add_rmsnorm_workspace.h`
```cpp
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2025. All rights reserved.
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

#ifndef MATMUL_ALLREDUCE_ADD_RMSNORM_WORKSPACE_H
#define MATMUL_ALLREDUCE_ADD_RMSNORM_WORKSPACE_H

#include <cstdint>

#pragma once
const constexpr uint32_t ALIGN_BYTES = 512;
const constexpr int32_t INT8_ELE_SIZE = 1;
const constexpr int32_t FP_BF_16_ELE_SIZE = 2;

enum CoCDataTypeDesc : int {
    COC_DATA_TYPE_UNDEFINED = -1,
    FP16FP16_FP32_FP16 = 0,
    BF16BF16_FP32_BF16 = 1,
    INT8INT8_INT32_FP16 = 2,
    INT8INT8_INT32_BF16 = 3,
    FP16INT8_INT32_FP16 = 4,
    BF16INT8_INT32_BF16 = 5,
    FP16INT8_FP32_FP16 = 6,
    BF16INT8_FP32_BF16 = 7,
    FP16INT4_FP32_FP16 = 8,
    BF16INT4_FP32_BF16 = 9,
    COC_DATA_TYPE_DESC_MAX = 10,
};

const std::map<CoCDataTypeDesc, int32_t> COC_TYPE2ELE_SIZE = {
    {FP16FP16_FP32_FP16, FP_BF_16_ELE_SIZE},
    {BF16BF16_FP32_BF16, FP_BF_16_ELE_SIZE},
    {INT8INT8_INT32_FP16, INT8_ELE_SIZE},
    {INT8INT8_INT32_BF16, INT8_ELE_SIZE},
    {FP16INT8_INT32_FP16, INT8_ELE_SIZE},
    {BF16INT8_INT32_BF16, INT8_ELE_SIZE},
    {FP16INT8_FP32_FP16, FP_BF_16_ELE_SIZE},
    {BF16INT8_FP32_BF16, FP_BF_16_ELE_SIZE},
    {FP16INT4_FP32_FP16, FP_BF_16_ELE_SIZE},
    {BF16INT4_FP32_BF16, FP_BF_16_ELE_SIZE}
};

struct MatMulInfo {
    int64_t batchSize = 1;
    int64_t m = -1;
    int64_t n = -1;
    int64_t k = -1;
    bool transA = false;
    bool transB = false;
    bool withBias = false;
    bool isInt8 = false;
    bool weightNz = false;
};

struct WorkspaceDetail {
    int64_t matrixActivationSize{0};
    int64_t matrixWeightSize{0};
    int64_t matrixIntermediateSize{0};
    int64_t formatDequantParamSize{0};

    int64_t GetSize() const
    {
        return matrixActivationSize + matrixWeightSize + matrixIntermediateSize + formatDequantParamSize;
    }
};

#endif
```
