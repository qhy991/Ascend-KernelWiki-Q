---
id: code-sgl-kernel-npu-csrc
title: SGL Kernel NPU Native Source
type: source-code
repo: sgl-project/sgl-kernel-npu
path: csrc
url: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- sglang
- npu
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
- pipeline-scheduling
- online-softmax
- kv-cache-paging
kernel_types:
- attention
- matmul
- softmax
- layernorm
languages:
- cpp
- ascendc
- python
---

# SGL Kernel NPU Native Source

SGLang NPU native source directory. It should be mined for production inference kernels and binding code used by SGLang's Ascend backend.

## Code Location

- Repository: `sgl-project/sgl-kernel-npu`
- Path: `csrc`
- URL: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc


## Fetched Source


### `csrc/pytorch_extensions.cpp`
```cpp
// Copyright (c) 2025 Huawei Technologies Co., Ltd
// All rights reserved.
//
// Licensed under the BSD 3-Clause License  (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "version.h"

#include "torch_helper.h"
#include "sgl_kenel_npu_ops.h"
#include "causal_conv1d_update/op_host/causal_conv1d_update.h"
#include "causal_conv1d/op_host/causal_conv1d.h"

namespace {
TORCH_LIBRARY_FRAGMENT(npu, m)
{
    m.def("sgl_kernel_npu_print_version() -> ()", []() { printf("%s\n", LIB_VERSION_FULL); });
    m.def("sgl_kernel_npu_version() -> str", []() { return std::string("") + LIB_VERSION; });

    m.def("helloworld(Tensor x, Tensor y) -> Tensor");

    m.def(
        "alloc_extend(Tensor pre_lens, Tensor seq_lens, Tensor last_loc, Tensor free_pages, int page_size, "
        "Tensor(a!) out_indices, Tensor(b!) values) -> ()");

    m.def(
        "cache_loc_assign(Tensor req_indices, Tensor token_pool, Tensor start_offset, Tensor end_offset, Tensor "
        "out_cache_loc) -> Tensor");

    m.def(
        "cache_loc_update(Tensor req_indices, Tensor token_pool, Tensor start_offset, Tensor end_offset, Tensor "
        "out_cache_loc) -> Tensor");

    m.def(
        "assign_cache_op(Tensor! out, Tensor src, Tensor dst_start_idx, Tensor dst_end_idx, Tensor src_start_idx, "
        "Tensor src_end_idx) -> bool");

    m.def(
        "build_tree_kernel_efficient(Tensor parent_list, Tensor selected_index, Tensor verified_seq_len, "
        "Tensor tree_mask, Tensor positions, Tensor retrive_index, Tensor retrive_next_token, "
        "Tensor retrive_next_sibling, int topk, int depth, int draft_token_num, int tree_mask_mode)->()");

    m.def(
        "mla_preprocess(Tensor hiddenState, Tensor gamma0, Tensor beta0, Tensor wdqkv, "
        "Tensor descale0, Tensor gamma1, Tensor beta1, Tensor wuq, "
        "Tensor descale1, Tensor gamma2, Tensor cos, Tensor sin, Tensor wuk,"
        "Tensor kv_cache, Tensor kv_cache_rope, Tensor slotmapping, "
        "Tensor quant_scale0, Tensor quant_offset0, Tensor bias0, "
        "Tensor quant_scale1, Tensor quant_offset1, Tensor bias1, *, "
        "Tensor? ctkv_scale=None, Tensor? q_nope_scale=None, "
        "str? cache_mode=None, str? quant_mode=None, "
        "Tensor(a!) q_out0, Tensor(b!) kv_cache_out0, Tensor(c!) q_out1, Tensor(d!) kv_cache_out1) "
        "-> (Tensor(a!), Tensor(b!), Tensor(c!), Tensor(d!))");

    m.def(
        "batch_matmul_transpose(Tensor tensor_a, Tensor tensor_b, Tensor(a!) tensor_c, "
        "str? format_mode=None, str? quant_mode=None) -> ()");

    m.def(
        "transfer_kv_dim_exchange(Tensor device_k, Tensor host_k, "
        "Tensor device_v, Tensor host_v, "
        "Tensor device_indices, Tensor host_indices, int page_size, int direct, int flags) -> ()");

    m.def(
        "bgmv_expand(Tensor! x, Tensor! weight, Tensor! indices, Tensor! y,"
        "            int slice_offset, int slice_size) -> Tensor");

    m.def(
        "bgmv_shrink(Tensor! x, Tensor! weight, Tensor! indices, Tensor! y,"
        "            float scale) -> ()");

    m.def(
        "sgmv_expand(Tensor! x, Tensor! weight, Tensor! lora_indices, Tensor! seq_len, Tensor! y,"
        "            int slice_offset, int slice_size) -> Tensor");

    m.def(
        "sgmv_shrink(Tensor! x, Tensor! weight, Tensor! lora_indices, Tensor! seq_len, Tensor! y,"
        " float scale) -> ()");

    m.def(
        "sgemmv_expand(Tensor! x, Tensor! weight, Tensor! lora_indices, Tensor! seq_len, Tensor! lora_ranks,"
        "              Tensor! sliceOffsets, Tensor! y) -> Tensor");

    m.def(
        "sgemmv_shrink(Tensor! x, Tensor! weight, Tensor! lora_indices, Tensor! seq_len, Tensor! lora_ranks,"
        "              Tensor! lora_scales, Tensor! y) -> ()");

    m.def(
        "recurrent_gated_delta_rule(Tensor mix_qkv, Tensor(a!) recurrent_state, Tensor beta, "
        "float scale, Tensor actual_seq_lengths, Tensor ssm_state_indices, "
        "int nk, int nv, "
        "Tensor(b!)? intermediate_state=None, Tensor? cache_indices=None, "
        "Tensor? num_accepted_tokens=None, Tensor? g=None, Tensor? gk=None) -> Tensor");

    m.def(
        "sgemmc_expand(Tensor! x, Tensor! weight, Tensor! lora_indices, Tensor! seq_len, Tensor! lora_ranks,"
        "              Tensor! sliceOffsets, Tensor! y) -> Tensor");

    m.def(
        "sgemmc_shrink(Tensor! x, Tensor! weight, Tensor! lora_indices, Tensor! seq_len, Tensor! lora_ranks,"
        "              Tensor! lora_scales, Tensor! y, int slice_count) -> ()");

    m.def(
        "mega_chunk_gdn(Tensor q, Tensor k, Tens
// ... (truncated due to length) ...

```

### `csrc/helloworld/op_host/helloworld.cpp`
```cpp
// Licensed under the BSD 3-Clause License  (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "defines.h"
#include "torch_helper.h"

#include "aclrtlaunch_helloworld.h"

namespace sglang {
namespace npu_kernel {

HOST_API at::Tensor helloworld(const at::Tensor &x, const at::Tensor &y)
{
    /* create a result tensor */
    at::Tensor z = at::empty_like(x);

    /* define the block dim */
    uint32_t blockDim = 8;

    /* memory size */
    uint32_t totalLength = 1;
    for (uint32_t size : x.sizes()) {
        totalLength *= size;
    }

    /* launch the kernel function via torch */
    EXEC_KERNEL_CMD(helloworld, blockDim, x, y, z, totalLength);
    return z;
}

HOST_API void printVersion()
{
    /*
     * dont remove this, this is used to put LIB_VERSION into symbol of the library,
     * then we can get the version and commit id via strings command, i.e.
     * strings libsgl_kernel_npu.so | grep commit
     */
    printf("%s\n", LIB_VERSION_FULL);
}

}  // namespace npu_kernel
}  // namespace sglang

```

### `csrc/helloworld/op_kernel/kernel_helloworld.cpp`
```cpp
// Licensed under the BSD 3-Clause License  (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#ifndef SGL_KERNEL_NPU_KERNEL_HELLOWORLD_H
#define SGL_KERNEL_NPU_KERNEL_HELLOWORLD_H

/* include file of ascendc */
#include "kernel_operator.h"

/* tensor num for each queue */
constexpr int32_t BUFFER_NUM = 2;

class KernalHelloworld
{
public:
    __aicore__ inline KernalHelloworld() {}

    __aicore__ inline void Init(GM_ADDR x, GM_ADDR y, GM_ADDR z, uint32_t totalLength)
    {
        this->blockLength = totalLength / AscendC::GetBlockNum();
        this->tileNum = 8;
        this->tileLength = this->blockLength / this->tileNum / BUFFER_NUM;
        xGm.SetGlobalBuffer((__gm__ half *)x + this->blockLength * AscendC::GetBlockIdx(), this->blockLength);
        yGm.SetGlobalBuffer((__gm__ half *)y + this->blockLength * AscendC::GetBlockIdx(), this->blockLength);
        zGm.SetGlobalBuffer((__gm__ half *)z + this->blockLength * AscendC::GetBlockIdx(), this->blockLength);
        pipe.InitBuffer(inQueueX, BUFFER_NUM, this->tileLength * sizeof(half));
        pipe.InitBuffer(inQueueY, BUFFER_NUM, this->tileLength * sizeof(half));
        pipe.InitBuffer(outQueueZ, BUFFER_NUM, this->tileLength * sizeof(half));
    }

    __aicore__ inline void Process()
    {
        int32_t loopCount = this->tileNum * BUFFER_NUM;
        for (int32_t i = 0; i < loopCount; i++) {
            CopyIn(i);
            Compute(i);
            CopyOut(i);
        }
    }

private:
    __aicore__ inline void CopyIn(int32_t progress)
    {
        AscendC::LocalTensor<half> xLocal = inQueueX.AllocTensor<half>();
        AscendC::LocalTensor<half> yLocal = inQueueY.AllocTensor<half>();
        AscendC::DataCopy(xLocal, xGm[progress * this->tileLength], this->tileLength);
        AscendC::DataCopy(yLocal, yGm[progress * this->tileLength], this->tileLength);
        inQueueX.EnQue(xLocal);
        inQueueY.EnQue(yLocal);
    }

    __aicore__ inline void Compute(int32_t progress)
    {
        AscendC::LocalTensor<half> xLocal = inQueueX.DeQue<half>();
        AscendC::LocalTensor<half> yLocal = inQueueY.DeQue<half>();
        AscendC::LocalTensor<half> zLocal = outQueueZ.AllocTensor<half>();
        AscendC::Add(zLocal, xLocal, yLocal, this->tileLength);
        outQueueZ.EnQue<half>(zLocal);
        inQueueX.FreeTensor(xLocal);
        inQueueY.FreeTensor(yLocal);
    }

    __aicore__ inline void CopyOut(int32_t progress)
    {
        AscendC::LocalTensor<half> zLocal = outQueueZ.DeQue<half>();
        AscendC::DataCopy(zGm[progress * this->tileLength], zLocal, this->tileLength);
        outQueueZ.FreeTensor(zLocal);
    }

private:
    AscendC::TPipe pipe;
    AscendC::TQue<AscendC::TPosition::VECIN, BUFFER_NUM> inQueueX, inQueueY;
    AscendC::TQue<AscendC::TPosition::VECOUT, BUFFER_NUM> outQueueZ;
    AscendC::GlobalTensor<half> xGm;
    AscendC::GlobalTensor<half> yGm;
    AscendC::GlobalTensor<half> zGm;
    uint32_t blockLength;
    uint32_t tileNum;
    uint32_t tileLength;
};

extern "C" __global__ __aicore__ void helloworld(GM_ADDR x, GM_ADDR y, GM_ADDR z, uint32_t totalLength)
{
    KernalHelloworld op;
    op.Init(x, y, z, totalLength);
    op.Process();
}

#endif  // SGL_KERNEL_NPU_KERNEL_HELLOWORLD_H

```
