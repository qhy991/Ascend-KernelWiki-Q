---
id: code-catlass-conv-bias
title: CATLASS Conv Bias Example
type: source-code
repo: Ascend/catlass
path: examples/24_conv_bias
url: https://gitee.com/ascend/catlass/tree/master/examples/24_conv_bias
source_category: upstream-code
architectures:
- ascend910b
tags:
- catlass
- convolution
- bias
- cube
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- l1-buffer
- l0-buffer
techniques:
- data-reuse
- tiling-strategy
- cube-vector-overlap
kernel_types:
- conv
- elementwise
languages:
- cpp
- ascendc
---

# CATLASS Conv Bias Example

CATLASS convolution-plus-bias example anchoring non-GEMM Cube workloads and fused vector epilogue patterns in the Ascend code corpus.

## Code Location

- Repository: `Ascend/catlass`
- Path: `examples/24_conv_bias`
- URL: https://gitee.com/ascend/catlass/tree/master/examples/24_conv_bias


## Fetched Source


### `examples/24_conv_bias/gen_data.py`
```python
# Copyright (c) 2025 Huawei Technologies Co., Ltd.
# This file is a part of the CANN Open Software.
# Licensed under CANN Open Software License Agreement Version 1.0 (the "License").
# Please refer to the License for details. You may not use this file except in compliance with the License.
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
# See LICENSE in the root of the software repository for the full text of the License.

import os
import sys
import numpy as np
import torch
import torch.nn.functional as F
from ml_dtypes import bfloat16

def main():
    # Example parameters
    N = int(sys.argv[1])
    Cin = int(sys.argv[2])
    d = int(sys.argv[3])
    h = int(sys.argv[4])
    w = int(sys.argv[5])
    Cout = int(sys.argv[6])
    kd = int(sys.argv[7])
    kh = int(sys.argv[8])
    kw = int(sys.argv[9])
    sD = int(sys.argv[10])
    sH = int(sys.argv[11])
    sW = int(sys.argv[12])
    dD = int(sys.argv[13])
    dH = int(sys.argv[14])
    dW = int(sys.argv[15])
    pD = int(sys.argv[16])
    pH = int(sys.argv[17])
    pW = int(sys.argv[18])
    dtype_str = sys.argv[19]   # Dtype: bfloat16 or float16

    # Parameter analysis
    c0 , n0 = 16, 16
    if dtype_str == "float16":
        np_dtype = np.float16
        torch_dtype = torch.float16
        bias_dtype = np.float16
    elif dtype_str == "bfloat16":
        np_dtype = bfloat16
        torch_dtype = torch.bfloat16
        bias_dtype = np.float32

    c1 = (Cin + c0 - 1) // c0
    cout1 = (Cout + c0 - 1) // c0
    n1 = (Cout +  n0 - 1) // n0
    tensorDtype = torch.float32

    # Calculate the output size
    d_out = (d + 2 * pD - dD * (kd - 1) - 1) // sD + 1
    h_out = (h + 2 * pH - dH * (kh - 1) - 1) // sH + 1
    w_out = (w + 2 * pW - dW * (kw - 1) - 1) // sW + 1

    # Generate normal shape data
    fmap_tensor = torch.randn((N, Cin, d, h, w)).to(torch_dtype).to(tensorDtype)
    weight_tensor = torch.randn((Cout, Cin, kd, kh, kw)).to(torch_dtype).to(tensorDtype)
    bias = np.random.uniform(-0.1, 0.1, (Cout,)).astype(bias_dtype)

    fmap = fmap_tensor.numpy().astype(np_dtype)
    weight = weight_tensor.numpy().astype(np_dtype)
    bias_tensor = torch.from_numpy(bias).to(tensorDtype)

    # Conv3D
    golden = F.conv3d(
        fmap_tensor,
        weight_tensor,
        bias_tensor,
        stride=(sD, sH, sW),
        padding=(pD, pH, pW),
        dilation=(dD, dH, dW)
    )

    golden_np = golden.numpy().astype(np_dtype)

    # Reshape the data according to the specified memory layout
    # fmap: N, Cin, d, h, w --> (N, c1, c0, d, h, w) --> N * d * c1 * h * w * c0
    num_2_padding_in_cin = c1 * c0 - Cin
    zero_padding_array = np.zeros((N, num_2_padding_in_cin, d, h, w), dtype=np_dtype)
    fmap_data = np.concatenate((fmap, zero_padding_array), axis=1)
    fmap_data = fmap_data.reshape((N, c1, c0, d, h, w)).transpose(0, 3, 1, 4, 5, 2)
    print(f"fmap_reshaped dtype:{fmap_data.dtype}")

    # weight:(Cout, Cin, kd, kh, kw) --> (kd * c1 * kh * kw) * n1 * n0 * c0
    num_padding_in_n = n1 * n0 - Cout
    zero_padding_n_array = np.zeros((num_padding_in_n, Cin, kd, kh, kw), dtype=np_dtype)
    weight_data = np.concatenate((weight, zero_padding_n_array), axis=0)
    zero_padding_cin_array = np.zeros((n1 * n0, num_2_padding_in_cin, kd, kh, kw), dtype=np_dtype)
    weight_data = np.concatenate((weight_data, zero_padding_cin_array), axis=1)
    weight_data = weight_data.reshape(n1, n0, c1, c0, kd, kh, kw)
    weight_data = weight_data.transpose(4, 2, 5, 6, 0, 1, 3)
    weight_data = weight_data.reshape(kd*c1*kh*kw, n1, n0, c0) # (kdC1KhKw) * n1 * n0 * c0
    print(f"weight_reshaped dtype:{weight_data.dtype}")

    # golden: (NCoutDHW)  --> (N,n1,n0,d,h,w) ---> N * d_out * n1 * h_out * w_out * n0
    num_2_padding_in_cin = cout1 * c0 - Cout
    zero_padding_array = np.zeros((N, num_2_padding_in_cin, d_out, h_out, w_out), dtype=np_dtype)
    golden_np_data = np.concatenate((golden_np, zero_padding_array), axis=1)
    golden_np_data = golden_np_data.reshape((N, cout1, c0, d_out, h_out, w_out)).transpose(0, 3, 1, 4, 5, 2).astype(np.float32)
    print(f"golden_reshaped dtype:{golden_np_data.dtype}")

    print(f"fmap_reshaped shape:{fmap_data.shape}")
    print(f"weight_reshaped shape:{weight_data.shape}")
    print(f"golden_reshaped shape:{golden_np_data.shape}")
    # Create an output directory
    os.makedirs("data", exist_ok=True)

    # Save the data as a binary file
    fmap_data.tofile("data/fmap.bin")
    weight_data.tofile("data/weight.bin")
    bias.tofile("data/bias.bin")
    golden_np_data.tofile("data/golden.bin")
   
    print(f"Data generated successfully! Output saved in 'data' directory.")

if __name__ == "__main__":
    if len(sys.argv) != 20:
        print("Usage: python gen_data.py n Cin d h w Cout kd kh kw sD sH sW dD dH dW pD pH pW dtype")
        print("Example: python gen
// ... (truncated due to length) ...

```

### `examples/24_conv_bias/conv_bias.cpp`
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
#include <fstream>
#include <vector>

#include "helper.hpp"
#include "golden.hpp"
#include "fp16_t.h"

#include "catlass/catlass.hpp"
#include "catlass/arch/arch.hpp"
#include "catlass/conv/block/block_conv.hpp"
#include "catlass/conv/block/block_swizzle.hpp"
#include "catlass/conv/dispatch_policy.hpp"
#include "catlass/conv/kernel/conv3d_bias.hpp"
#include "catlass/gemm/gemm_type.hpp"
#include "catlass/layout/layout.hpp"
#include "catlass/conv_coord.hpp"

#include "catlass/status.hpp"
#include "catlass/conv/device/device_conv.hpp"

using namespace Catlass;
using fp16_t = op::fp16_t;

bool ReadFile(const std::string &filePath, void *buffer, size_t bufferSize)
{
    if (buffer == nullptr) {
        printf("Read file %s failed. Buffer is nullptr.\n", filePath.c_str());
        return false;
    }

    // Open file
    std::ifstream fd(filePath, std::ios::binary);
    if (!fd) {
        printf("Open file failed. path = %s.\n", filePath.c_str());
        return false;
    }

    // Load file data in buffer
    std::filebuf *buf = fd.rdbuf();
    size_t size = buf->pubseekoff(0, std::ios::end, std::ios::in);
    if (size == 0) {
        printf("File %s size is 0\n", filePath.c_str());
        return false;
    }
    if (size > bufferSize) {
        printf("File %s size is larger than buffer size.\n", filePath.c_str());
        return false;
    }
    buf->pubseekpos(0, std::ios::in);
    buf->sgetn(static_cast<char*>(buffer), size);
    return true;
}

struct Options {
    const std::string HELPER = "24_conv_bias batch di cin1 hi wi cin0 cout kd kh kw sD sH sW dD dH dW pD pH pW [device_id]";

    uint32_t fmapRelated[6] = {1, 1, 1, 2, 9, 16};  // {batch, di, cin1, hi, wi, cin0}
    uint32_t filterRelated[4] = {1, 1, 1, 1};  // {kd, kh, kw, cout}
    uint32_t strides[3] = {1, 1, 1};
    uint32_t pads[3] = {0, 0, 0};
    uint32_t dilations[3] = {1, 1, 1};
    int32_t deviceId{0};

    Options() = default;

    int Parse(int argc, const char **argv)
    {
        enum ArgsIndex {
            BATCH_INDEX = 1,
            DI_INDEX,
            CIN1_INDEX,
            HI_INDEX,
            WI_INDEX,
            CIN0_INDEX,
            COUT_INDEX,
            KD_INDEX,
            KH_INDEX,
            KW_INDEX,
            SD_INDEX,
            SH_INDEX,
            SW_INDEX,
            DD_INDEX,
            DH_INDEX,
            DW_INDEX,
            PD_INDEX,
            PH_INDEX,
            PW_INDEX,
            DEVICE_ID_INDEX,
            ARGS_MAX
        };

        if (argc > ARGS_MAX || argc <= PW_INDEX) {
            std::cerr << HELPER << std::endl;
            return 0;
        }

        fmapRelated[0] = std::atoi(argv[BATCH_INDEX]);
        fmapRelated[1] = std::atoi(argv[DI_INDEX]);
        fmapRelated[2] = std::atoi(argv[CIN1_INDEX]);
        fmapRelated[3] = std::atoi(argv[HI_INDEX]);
        fmapRelated[4] = std::atoi(argv[WI_INDEX]);
        fmapRelated[5] = std::atoi(argv[CIN0_INDEX]);
        filterRelated[0] = std::atoi(argv[KD_INDEX]);
        filterRelated[1] = std::atoi(argv[KH_INDEX]);
        filterRelated[2] = std::atoi(argv[KW_INDEX]);
        filterRelated[3] = std::atoi(argv[COUT_INDEX]);
        strides[0] = std::atoi(argv[SD_INDEX]);
        strides[1] = std::atoi(argv[SH_INDEX]);
        strides[2] = std::atoi(argv[SW_INDEX]);
        dilations[0] = std::atoi(argv[DD_INDEX]);
        dilations[1] = std::atoi(argv[DH_INDEX]);
        dilations[2] = std::atoi(argv[DW_INDEX]);
        pads[0] = std::atoi(argv[PD_INDEX]);
        pads[1] = std::atoi(argv[PH_INDEX]);
        pads[2] = std::atoi(argv[PW_INDEX]);

        if (argc == ARGS_MAX) {
            deviceId = std::atoi(argv[DEVICE_ID_INDEX]);
        }

        return 0;
    }
};

void Run(Options const &options)
{
    aclrtStream stream{nullptr};

    ACL_CHECK(aclInit(nullptr));
    ACL_CHECK(aclrtSetDevice(options.deviceId));
    ACL_CHECK(aclrtCreateStream(&stream));

    Conv3dParams problemShape = Conv3dParams::MakeConvCoord(options.fmapRelated, options.filterRelated, options.pads, options.strides, options.dilations);

    uint32_t n = prob
// ... (truncated due to length) ...

```
