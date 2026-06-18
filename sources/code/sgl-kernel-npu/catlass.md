---
id: code-sgl-kernel-npu-catlass
title: SGL Kernel NPU CATLASS Utility Kernels
type: source-code
repo: sgl-project/sgl-kernel-npu
path: csrc/catlass
url: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/catlass
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- sglang
- catlass
- matmul
- fp8
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- l1-buffer
- l0-buffer
techniques:
- quantization-int8
- nz-tiling
- pipeline-scheduling
kernel_types:
- matmul
- gemm
- quant-matmul
languages:
- cpp
- ascendc
---

# SGL Kernel NPU CATLASS Utility Kernels

SGL Kernel NPU CATLASS-backed source tree, including GEMM utility code and low-precision matmul components for production inference.

## Code Location

- Repository: `sgl-project/sgl-kernel-npu`
- Path: `csrc/catlass`
- URL: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/catlass


## Fetched Source


### `csrc/catlass/op_host/catlass_matmul_fp8.cpp`
```cpp
// Licensed under the BSD 3-Clause License (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
#include <map>
#include <torch/torch.h>
#include <torch_npu/csrc/core/npu/DeviceUtils.h>
#include <torch_npu/csrc/core/npu/NPUFormat.h>
#include <torch_npu/csrc/core/npu/NPUFunctions.h>
#include <ATen/ATen.h>
#include <torch/library.h>

#include "tiling/platform/platform_ascendc.h"
#include "defines.h"
#include "torch_helper.h"
#include "catlass_op_utils.h"
#include "aclrtlaunch_catlass_fp8w8a16_matmul_bfloat16_t.h"

namespace sglang {
namespace npu_kernel {
HOST_API at::Tensor softfp8_w8a16_matmul(const at::Tensor &mat1, const at::Tensor &mat2, const at::Tensor &scale,
                                         const std::string &outDType)
{
    constexpr int64_t kBlockSize = 128;
    at::ScalarType scalar_type = mat1.scalar_type();

    TORCH_CHECK(scalar_type == at::kBFloat16, "only support bf16");
    TORCH_CHECK(mat1.dim() == 2, "x should be [M, K]");
    TORCH_CHECK(mat2.scalar_type() == at::kByte, "weight should be uint8 storing fp8 bits");
    TORCH_CHECK(mat2.dim() == 2, "weight should be [K, N]");
    TORCH_CHECK(scale.scalar_type() == at::kFloat, "scale should be float32");
    TORCH_CHECK(scale.dim() == 2, "scale should be [ceil(k/128), ceil(n/128)]");

    int64_t m64 = mat1.size(0);
    int64_t k64 = mat1.size(1);
    int64_t n64 = mat2.size(1);
    int64_t scale_rows = (k64 + kBlockSize - 1) / kBlockSize;
    int64_t scale_cols = (n64 + kBlockSize - 1) / kBlockSize;

    TORCH_CHECK(mat2.size(0) == k64, "weight shape mismatch: expect K dim to equal mat1.size(1)");
    TORCH_CHECK(scale.size(0) == scale_rows && scale.size(1) == scale_cols,
                "scale shape mismatch: expect [ceil(k/128), ceil(n/128)]");

    uint32_t m = static_cast<uint32_t>(m64);
    uint32_t k = static_cast<uint32_t>(k64);
    uint32_t n = static_cast<uint32_t>(n64);

    void *x_ptr = mat1.data_ptr();
    void *w_ptr = mat2.data_ptr();
    void *scale_ptr = scale.data_ptr();

    auto outputDataType = TypeStrToAclDtype(outDType);
    at::Tensor output = GetOutputTensor({m, n}, AclDtypeToTorchDtype(outputDataType));
    void *y_ptr = output.data_ptr();

    aclrtStream stream = c10_npu::getCurrentNPUStream().stream(false);
    uint32_t aicCoreNum = platform_ascendc::PlatformAscendCManager::GetInstance()->GetCoreNumAic();
    uint32_t workspace_size = 4 * 256 * 256 * sizeof(outputDataType) * aicCoreNum;
    auto workspace_tensor =
        at::empty({workspace_size}, at::TensorOptions().dtype(at::kByte).device(mat1.options().device()));
    void *workspace_ptr = workspace_tensor.data_ptr();

    at_npu::native::OpCommand cmd;
    cmd.Name("catlass_fp8w8a16_matmul_bfloat16_t");
    cmd.SetCustomHandler([aicCoreNum, stream, x_ptr, w_ptr, scale_ptr, y_ptr, workspace_ptr, m, n, k]() -> int {
        int device_id = 0;
        int64_t aiv_num = 0;
        TORCH_CHECK(aclGetDeviceCapability(device_id, ACL_DEVICE_INFO_VECTOR_CORE_NUM, &aiv_num) == ACL_SUCCESS);

        ACLRT_LAUNCH_KERNEL(catlass_fp8w8a16_matmul_bfloat16_t)
        (aicCoreNum, stream, x_ptr, w_ptr, scale_ptr, y_ptr, workspace_ptr, m, n, k);
        return 0;
    });
    cmd.Run();

    return output;
}

}  // namespace npu_kernel
}  // namespace sglang

```

### `csrc/catlass/op_host/catlass_matmul_tiling.h`
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

#ifndef KERNEL_CATLASS_MATMUL_TILING_H
#define KERNEL_CATLASS_MATMUL_TILING_H

#include <cstdint>

namespace sglang {
namespace npu_kernel {

typedef enum { WEIGHT_ND = 0, WEIGHT_NZ = 1 } WeightFormatMode;

typedef enum { BF16 = 0, FP16 = 1, FP32 = 2 } DataFormatMode;

struct KernelCatlassMatmulTilingData {
    int32_t m;
    int32_t n;
    int32_t k;

    int64_t weight_format_mode = WEIGHT_ND;
    int64_t data_format_mode = BF16;
};

}  // namespace npu_kernel
}  // namespace sglang

#endif  // KERNEL_CATLASS_MATMUL_TILING_H

```

### `csrc/catlass/op_host/catlass_matmul_basic.cpp`
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
#include <map>

#include "defines.h"
#include "tiling/platform/platform_ascendc.h"
#include "torch_helper.h"
#include "catlass_matmul_tiling.h"
#include "aclrtlaunch_catlass_matmul_basic.h"

namespace sglang {
namespace npu_kernel {

constexpr uint32_t PADDING_BYTE = 32U;

std::map<c10::ScalarType, DataFormatMode> dTypeMap = {{at::ScalarType::Half, DataFormatMode::FP16},
                                                      {at::ScalarType::BFloat16, DataFormatMode::BF16},
                                                      {at::ScalarType::Float, DataFormatMode::FP32}};

std::unordered_map<c10::string_view, uint16_t> weightFormatMap = {{"ND", WeightFormatMode::WEIGHT_ND},
                                                                  {"NZ", WeightFormatMode::WEIGHT_NZ}};

template <typename MapType>
inline int GetModeVal(const MapType &mode_map, c10::optional<c10::string_view> mode_opt, c10::string_view default_mode,
                      const char *mode_name)
{
    std::string modeStr(mode_name);
    c10::string_view mode_str = mode_opt.value_or(default_mode);
    auto it = mode_map.find(mode_str);
    // if input mode is unsupported, use default value
    TORCH_CHECK(it != mode_map.end(), modeStr, c10::str(": Unsupported mode value ", mode_str));
    return it->second;
}

at::Tensor get_tiling(int32_t &m, int32_t &n, int32_t k, int64_t weight_format_mode, int64_t data_format_mode,
                      uint32_t &blockDim)
{
    auto ascendc_platform = platform_ascendc::PlatformAscendCManager::GetInstance();
    blockDim = static_cast<uint32_t>(ascendc_platform->GetCoreNumAiv());

    // align to 32 bytes
    int32_t tiling_size = (sizeof(KernelCatlassMatmulTilingData) + PADDING_BYTE - 1) / PADDING_BYTE * PADDING_BYTE;
    auto tiling_buffer = at::empty({tiling_size}, at::TensorOptions().dtype(at::kByte).device(at::kCPU));

    KernelCatlassMatmulTilingData *tiling_data =
        reinterpret_cast<KernelCatlassMatmulTilingData *>(tiling_buffer.data_ptr());
    tiling_data->m = m;
    tiling_data->n = n;
    tiling_data->k = k;
    tiling_data->weight_format_mode = weight_format_mode;
    tiling_data->data_format_mode = data_format_mode;

    auto tiling_tensor = TorchNpuHelper::CopyTensorHostToDevice(tiling_buffer);
    return tiling_tensor;
}

HOST_API void catlass_matmul_basic(const at::Tensor &input_a, const at::Tensor &input_b, at::Tensor &output_c,
                                   c10::optional<c10::string_view> format_mode)
{
    // ops valid check
    at::ScalarType aType = input_a.scalar_type();
    at::ScalarType bType = input_b.scalar_type();
    at::ScalarType cType = output_c.scalar_type();
    TORCH_CHECK(aType == bType && bType == cType, "tensor type is not the same");
    TORCH_CHECK(
        (aType == at::ScalarType::BFloat16) || (aType == at::ScalarType::Half) || (aType == at::ScalarType::Float),
        "tensor type only support half / bf16 / fp32");

    auto formatMode = static_cast<WeightFormatMode>(GetModeVal(weightFormatMap, format_mode, "ND", "format_mode"));
    TORCH_CHECK(formatMode == WeightFormatMode::WEIGHT_ND, "current ops only support weightFormat ND");

    int32_t m = input_a.size(0);
    int32_t k = input_a.size(1);
    int32_t n = input_b.size(1);
    TORCH_CHECK(input_b.size(0) == k, "input k dim shape mismatch");

    uint32_t blockDim;
    auto tiling_tensor = get_tiling(m, n, k, formatMode, dTypeMap[aType], blockDim);

    // launch the kernel function via torch
    auto workspace_tensor = at::empty({1}, at::TensorOptions().dtype(at::kByte).device(input_a.options().device()));
    EXEC_KERNEL_CMD(catlass_matmul_basic, blockDim, input_a, input_b, output_c, workspace_tensor, tiling_tensor);
}

}  // namespace npu_kernel
}  // namespace sglang

```
