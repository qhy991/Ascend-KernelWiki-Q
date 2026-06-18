---
id: code-vllm-ascend-csrc
title: vLLM Ascend C++/AscendC Extension Source
type: source-code
repo: vllm-project/vllm-ascend
path: csrc
url: https://github.com/vllm-project/vllm-ascend/tree/main/csrc
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
- ascendc
- cpp
- inference
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- vector-unit
- unified-buffer
- mte
- global-memory
techniques:
- pipeline-scheduling
- kv-cache-paging
kernel_types:
- attention
- rope
- elementwise
languages:
- cpp
- ascendc
- python
---

# vLLM Ascend C++/AscendC Extension Source

vLLM Ascend native extension source tree. It is code evidence for binding custom NPU kernels into vLLM, including C++ extension build logic, torch operator registration, and AscendC kernel integration.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `csrc`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/csrc


## Fetched Source


### `csrc/utils.h`
```cpp
#pragma once

#include "kernels/types.h"
#include <c10/core/ScalarType.h>
#include <Python.h>

#define _CONCAT(A, B) A##B
#define CONCAT(A, B) _CONCAT(A, B)

#define _STRINGIFY(A) #A
#define STRINGIFY(A) _STRINGIFY(A)

// A version of the TORCH_LIBRARY macro that expands the NAME, i.e. so NAME
// could be a macro instead of a literal token.
#define TORCH_LIBRARY_EXPAND(NAME, MODULE) TORCH_LIBRARY(NAME, MODULE)

// A version of the TORCH_LIBRARY_IMPL macro that expands the NAME, i.e. so NAME
// could be a macro instead of a literal token.
#define TORCH_LIBRARY_IMPL_EXPAND(NAME, DEVICE, MODULE) \
  TORCH_LIBRARY_IMPL(NAME, DEVICE, MODULE)

// REGISTER_EXTENSION allows the shared library to be loaded and initialized
// via python's import statement.
#define REGISTER_EXTENSION(NAME)                                               \
  PyMODINIT_FUNC CONCAT(PyInit_, NAME)() {                                     \
    static struct PyModuleDef module = {PyModuleDef_HEAD_INIT,                 \
                                        STRINGIFY(NAME), nullptr, 0, nullptr}; \
    return PyModule_Create(&module);                                           \
  }

class TrochBindException : public std::exception
{
private:
    std::string message = {};

public:
    explicit TrochBindException(const char *name, const char *file, const int line, const std::string &error)
    {
        message = std::string("Failed: ") + name + " error " + file + ":" + std::to_string(line) +
                  " error message or error code is '" + error + "'";
    }

    const char *what() const noexcept override
    {
        return message.c_str();
    }
};

#define TORCH_BIND_ASSERT(cond)                                           \
    ;                                                                  \
    do {                                                               \
        if (not(cond)) {                                               \
            throw TrochBindException("Assertion", __FILE__, __LINE__, #cond); \
        }                                                              \
    } while (0)

```

### `csrc/torch_binding.cpp`
```cpp
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2024. All rights reserved.
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

#include <torch/extension.h>
#include <torch/library.h>
#include <torch/version.h>
#include <torch/torch.h>
#include <ATen/core/Formatting.h>
#include "acl/acl.h"
#include "acl/acl_rt.h"
#include <torch_npu/csrc/core/npu/NPUStream.h>
#include <torch_npu/csrc/framework/OpCommand.h>
#include <torch_npu/csrc/framework/utils/OpPreparation.h>
#include "torch_npu/csrc/core/npu/NPUGuard.h"
#include <torch_npu/csrc/npu/Module.h>
#include "ops.h"
#include "utils.h"
#include "aclnn_torch_adapter/op_api_common.h"
#include "moe/add_rms_norm_bias/add_rms_norm_bias_torch_adpt.h"
#include "moe/apply_top_k_top_p_custom/apply_top_k_top_p_custom_torch_adpt.h"
#ifdef VLLM_ENABLE_ATB_AND_DIRECT_KERNELS
#include "batch_matmul_transpose/batch_matmul_transpose_torch_adpt.h"
#include "mla_preprocess/mla_preprocess_torch_adpt.h"
#endif
#include "mc2/dispatch_ffn_combine/dispatch_ffn_combine_torch_adpt.h"
#include "mc2/dispatch_gmm_combine_decode/dispatch_gmm_combine_decode_torch_adpt.h"
#include "gmm/grouped_matmul_swiglu_quant_weight_nz_tensor_list/grouped_matmul_swiglu_quant_torch_adpt.h"
#include "gmm/grouped_matmul_swiglu_quant_v2/grouped_matmul_swiglu_quant_v2_torch_adpt.h"
#include "attention/lightning_indexer/lightning_indexer_torch_adpt.h"
#include "mc2/matmul_allreduce_add_rmsnorm/matmul_allreduce_add_rmsnorm_torch_adpt.h"
#include "moe/moe_gating_top_k/moe_gating_top_k_torch_adpt.h"
#include "moe/moe_init_routing_custom/moe_init_routing_custom_torch_adpt.h"
#include "attention/sparse_flash_attention/sparse_flash_attention_torch_adpt.h"
#include "attention/lightning_indexer_quant/lightning_indexer_quant_torch_adpt.h"
#include "attention/ngram_spec_decode/ngram_spec_decode_torch_adpt.h"
#include "moe/causal_conv1d_v310/causal_conv1d_310_torch_adpt.h"
#include "attention/recurrent_gated_delta_rule/recurrent_gated_delta_rule_torch_adpt.h"
#include "attention/recurrent_gated_delta_rule_v310/recurrent_gated_delta_rule_310_torch_adpt.h"
#include "attention/store_kv_block/store_kv_block_torch_adpt.h"
#include "attention/fused_gdn_gating/fused_gdn_gating_torch_adpt.h"
#include <c10/core/Device.h>
#include <c10/core/Scalar.h>
#include <c10/util/Exception.h>
#include <c10/util/Logging.h>
#include <array>
#include <cmath>
#include <iostream>
#include <memory>
#include <mutex>
#include <sstream>
#include <unordered_map>
#include <vector>

namespace vllm_ascend {

namespace {

struct DevicePrintPayload {
    std::string message;
    at::Tensor host_tensor_snapshot;
};

std::mutex& get_device_print_mutex()
{
    static std::mutex device_print_mutex;
    return device_print_mutex;
}

void device_print_callback(void* args)
{
    // device_print is a debug-only helper. We intentionally do not reclaim the
    // callback payload here because aclgraph replay may re-execute the same host
    // callback payload multiple times. Freeing it on first execution would make
    // later replays dereference a dangling pointer.
    auto* payload = static_cast<DevicePrintPayload*>(args);
    if (payload == nullptr) {
        return;
    }

    std::lock_guard<std::mutex> guard(get_device_print_mutex());
    if (!payload->message.empty()) {
        std::cout << payload->message;
    }

    if (payload->host_tensor_snapshot.defined()) {
        if (!payload->message.empty()) {
            std::cout << std::endl;
        }
        at::print(std::cout, payload->host_tensor_snapshot.contiguous(), 120);
    }

    std::cout << std::endl;
    std::cout.flush();
}

void enqueue_device_print(std::unique_ptr<DevicePrintPayload> payload,
                          aclrtStream stream)
{
    auto* raw_payload = payload.release();
    const aclError ret = aclrtLaunchHostFunc(stream, device_print_callback,
                                             raw_payload);
    if (ret != ACL_SUCCESS) {
        delete raw_payload;
    }
    TORCH_CHECK(ret == ACL_SUCCESS, "aclrtLaunchHostFunc failed, error code: ", ret);
}

}

void swap_blocks_batch(const torch::Tensor& src_ptrs,
                       const torch::Tensor& dst_ptrs,
                       const torch::Tensor& sizes,
                       int64_t direction) {

    TORCH_CHECK(src_ptrs.device().is_cpu(), "src_ptrs must be on CPU");
    TORCH_CHECK(dst_ptrs.device().is_cpu(), "dst_ptrs must be on CPU");
    TORCH_CHECK(sizes.device().is_cpu(), "sizes must be on CPU");
    TORCH_CHECK(src_p
// ... (truncated due to length) ...

```

### `csrc/camem_allocator.cpp`
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

#include <iostream>
#include <stdexcept>
#include <string>

extern "C" {

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <sys/types.h>
#include "acl/acl.h"

// Global references to Python callables
// NOTE: this is borrowed reference, so we don't need to DECREF them.
// This brings the limitation that the allocator needs to be singleton.
static PyObject* g_python_malloc_callback = nullptr;
static PyObject* g_python_free_callback = nullptr;


// ---------------------------------------------------------------------------
// Helper functions:

void ensure_context(unsigned long long device) {
  aclrtContext pctx;
  aclrtGetCurrentContext(&pctx);
  if (!pctx) {
    // Ensure device context.
    aclrtCreateContext(&pctx, device);
    aclrtSetCurrentContext(pctx);
  }
}

void create_and_map(unsigned long long device, ssize_t size, void* d_mem,
                    aclrtDrvMemHandle* p_memHandle) {
  ensure_context(device);
  // Define memory allocation properties
  aclrtPhysicalMemProp prop = {};
  prop.handleType = ACL_MEM_HANDLE_TYPE_NONE;
  prop.allocationType = ACL_MEM_ALLOCATION_TYPE_PINNED;
  prop.memAttr = ACL_HBM_MEM_HUGE;
  prop.location.id = device;
  prop.location.type = ACL_MEM_LOCATION_TYPE_DEVICE;
  prop.reserve = 0;

  // Allocate memory using aclrtMallocPhysical
  aclError error_code = aclrtMallocPhysical(p_memHandle, size, &prop, 0);
  if (error_code != 0) {
    if (error_code == ACL_ERROR_RT_MEMORY_ALLOCATION) {
      throw std::runtime_error("aclrtMallocPhysical failed with acl error code: " + 
                              std::to_string(error_code) + "(OOM: Out of Memory, allocation failed) " + 
                              __FILE__ + ":" + std::to_string(__LINE__));
    } else {
      throw std::runtime_error("aclrtMallocPhysical failed with acl error code: " +
                              std::to_string(error_code) + " " + __FILE__ + ":" + std::to_string(__LINE__));
    }
  }

  // Map memory
  error_code = aclrtMapMem(d_mem, size, 0, *p_memHandle, 0);
  if (error_code != 0) {
    throw std::runtime_error("aclrtMapMem failed with acl error code: " +
                            std::to_string(error_code) + " " + __FILE__ + ":" + std::to_string(__LINE__));
  }
}

void unmap_and_release(unsigned long long device, ssize_t size,
                       void* d_mem,
                       aclrtDrvMemHandle* p_memHandle) {
  // std::cout << "unmap_and_release: device=" << device << ", size=" << size <<
  // ", d_mem=" << d_mem << ", p_memHandle=" << p_memHandle << std::endl;
  ensure_context(device);
  aclError error_code = aclrtUnmapMem(d_mem);
  if (error_code != 0) {
    throw std::runtime_error("aclrtUnmapMem failed with acl error code: " +
                            std::to_string(error_code) + " " + __FILE__ + ":" + std::to_string(__LINE__));
  }
  error_code = aclrtFreePhysical(*p_memHandle);
  if (error_code != 0) {
    throw std::runtime_error("aclrtFreePhysical failed with acl error code: " +
                            std::to_string(error_code) + " " + __FILE__ + ":" + std::to_string(__LINE__));
  }
}

PyObject* create_tuple_from_c_integers(unsigned long long a,
                                       unsigned long long b,
                                       unsigned long long c,
                                       unsigned long long d) {
  // Create a new tuple of size 4
  PyObject* tuple = PyTuple_New(4);
  if (!tuple) {
    return NULL;  // Return NULL on failure
  }

  // Convert integers to Python objects and set them in the tuple
  PyTuple_SetItem(
      tuple, 0,
      PyLong_FromUnsignedLongLong(a));  // Steals reference to the PyLong
  PyTuple_SetItem(tuple, 1, PyLong_FromUnsignedLongLong(b));
  PyTuple_SetItem(tuple, 2, PyLong_FromUnsignedLongLong(c));
  PyTuple_SetItem(tuple, 3, PyLong_FromUnsignedLongLong(d));

  // Note: PyTuple_SetItem "steals" a reference to each object,
  // so we do not need to Py_DECREF the PyLong objects explicitly.

  return tuple;  // Return the created tuple
}

// ---------------------------------------------------------------------------
// Our exported C functions that call Python:

__attribute__ ((visibility("default"))) void* my_malloc(ssize_t size, int device, aclrtStream stream) {
  ensure_context(device);

  // first allocation, align the size, and reserve an address, and also allocate
  // a aclrtDrvMem
// ... (truncated due to length) ...

```
