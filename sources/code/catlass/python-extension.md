---
id: code-catlass-python-extension
title: CATLASS Python Extension Example
type: source-code
repo: Ascend/catlass
path: examples/python_extension
url: https://gitee.com/ascend/catlass/tree/master/examples/python_extension
source_category: upstream-code
architectures:
- ascend910b
tags:
- catlass
- python-extension
- binding
- operator
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- global-memory
techniques:
- workspace-management
- pipeline-scheduling
kernel_types:
- matmul
- gemm
languages:
- python
- cpp
- ascendc
---

# CATLASS Python Extension Example

CATLASS Python extension example showing how generated or templated Ascend kernels are surfaced through Python bindings for benchmark and application integration.

## Code Location

- Repository: `Ascend/catlass`
- Path: `examples/python_extension`
- URL: https://gitee.com/ascend/catlass/tree/master/examples/python_extension


## Fetched Source


### `examples/python_extension/setup.py`
```python
# Copyright (c) 2025 Huawei Technologies Co., Ltd.
# This file is a part of the CANN Open Software.
# Licensed under CANN Open Software License Agreement Version 1.0 (the "License").
# Please refer to the License for details. You may not use this file except in compliance with the License.
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
# See LICENSE in the root of the software repository for the full text of the License.

import logging
import os
import subprocess
import sys
import time

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=""):
        super().__init__(name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


class CMakeBuild(build_ext):
    def run(self):
        for ext in self.extensions:
            self.build_cmake(ext)
            self.generate_pyi(ext)

    def build_cmake(self, ext):
        extdir = os.path.abspath(os.path.dirname(
            self.get_ext_fullpath(ext.name)))
        cmake_args = [
            "-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=" + extdir + "/torch_catlass",
            "-DPython3_EXECUTABLE=" + sys.executable,
            "-DBUILD_PYBIND=True"
        ]

        build_args = []
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)

        subprocess.check_call(["cmake", os.path.join(ext.sourcedir, "../../")] +
                              cmake_args, cwd=self.build_temp)
        subprocess.check_call(
            ["cmake", "--build", ".", "--target", "_C", "-j"] + build_args, cwd=self.build_temp)

    def generate_pyi(self, ext):
        extdir = os.path.abspath(os.path.dirname(
            self.get_ext_fullpath(ext.name)))
        module_name = ext.name.split(".")[-1]
        stubgen_args = [module_name, "--output-dir", extdir]
        stubgen_bin = os.path.join(os.path.dirname(
            sys.executable), "pybind11-stubgen")
        try:
            subprocess.check_call([stubgen_bin] + stubgen_args, cwd=extdir)
        except FileNotFoundError as e:
            logging.warning("No pybind11-stubgen found")
        except subprocess.CalledProcessError as e:
            logging.warning("pybind11-stubgen exited abnormally")


version = f"0.1.0.{time.strftime('%Y%m%d%H%M%S')}"

setup(
    name="torch_catlass",
    version=version,
    author="Huawei Technologies Co., Ltd.",
    description="A PyTorch extension for AscendC Tenplates with pybind11 bindings",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=["torch_catlass"],
    ext_modules=[CMakeExtension("torch_catlass")],
    cmdclass={"build_ext": CMakeBuild},
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=[],
    include_package_data=True,
)

```

### `examples/python_extension/torch_catlass/__init__.py`
```python
# Copyright (c) 2025 Huawei Technologies Co., Ltd.
# This file is a part of the CANN Open Software.
# Licensed under CANN Open Software License Agreement Version 1.0 (the "License").
# Please refer to the License for details. You may not use this file except in compliance with the License.
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
# See LICENSE in the root of the software repository for the full text of the License.

import os
import sysconfig
import torch
import torch_npu

__all__ = []

def _load_depend_libs():
    PYTHON_PKG_PATH=sysconfig.get_paths()['purelib']
    TORCH_LIB_PATH=os.path.join(PYTHON_PKG_PATH,"torch/lib")
    TORCH_NPU_LIB_PATH=os.path.join(PYTHON_PKG_PATH,"torch_npu/lib")
    os.environ['LD_LIBRARY_PATH'] = f"{os.environ['LD_LIBRARY_PATH']}:{TORCH_LIB_PATH}:{TORCH_NPU_LIB_PATH}"
    
_load_depend_libs()

from torch_catlass._C import *
```

### `examples/python_extension/src/wrapper/common.cpp`
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

#include <acl/acl.h>

#include <torch/torch.h>
#include <torch_npu/csrc/core/npu/DeviceUtils.h>
#include <torch_npu/csrc/core/npu/NPUFormat.h>
#include <torch_npu/csrc/core/npu/NPUFunctions.h>
#include <torch_npu/csrc/core/npu/NPUStream.h>

#include "wrapper/common.h"

namespace CatlassKernelWrapper {
torch::Tensor GetOutputTensor(const std::vector<int64_t> &shape, const torch::Dtype dtype)
{
    at::TensorOptions options = at::TensorOptions();
    options =
        options.dtype(dtype).layout(at::kStrided).requires_grad(false).device(torch_npu::utils::get_npu_device_type());
    return at_npu::native::empty_with_format(shape, options, ACL_FORMAT_ND);
}

torch::Dtype TypeStrToTorchDtype(const std::string &typeStr)
{
    static const std::unordered_map<std::string, torch::Dtype> mapper = {{"float32", torch::kFloat32},
                                                                         {"float16", torch::kFloat16},
                                                                         {"int8", torch::kInt8},
                                                                         {"int32", torch::kInt32},
                                                                         {"bf16", torch::kBFloat16}};
    auto iter = mapper.find(typeStr);
    return iter != mapper.end() ? iter->second : torch::kFloat16;
}

aclDataType TorchDtypeToAclDtype(const torch::Dtype torchDtype)
{
    static const std::unordered_map<torch::Dtype, aclDataType> mapper = {{torch::kFloat32, ACL_FLOAT},
                                                                         {torch::kFloat16, ACL_FLOAT16},
                                                                         {torch::kInt8, ACL_INT8},
                                                                         {torch::kInt32, ACL_INT32},
                                                                         {torch::kBFloat16, ACL_BF16}};
    auto iter = mapper.find(torchDtype);
    return iter != mapper.end() ? iter->second : ACL_FLOAT16;
};

aclDataType TypeStrToAclDtype(const std::string &typeStr)
{
    return TorchDtypeToAclDtype(TypeStrToTorchDtype(typeStr));
};

torch::Dtype AclDtypeToTorchDtype(const aclDataType aclDtype)
{
    static const std::map<aclDataType, torch::Dtype> mapper = {{ACL_FLOAT16, torch::kFloat16},
                                                               {ACL_FLOAT, torch::kFloat32},
                                                               {ACL_INT32, torch::kInt32},
                                                               {ACL_INT8, torch::kInt8},
                                                               {ACL_BF16, torch::kBFloat16}};
    auto iter = mapper.find(aclDtype);
    return iter != mapper.end() ? iter->second : torch::kFloat16;
};

TransposeStatus GetTransposeStatus(const at::Tensor &mat)
{
    if (mat.is_contiguous()) {
        return TransposeStatus::NO_TRANSPOSE;
    }
    std::vector<int64_t> strides = mat.strides().vec();
    std::vector<int64_t> shape = mat.sizes().vec();
    int64_t dimA = shape.at(shape.size() - 2);
    int64_t dimB = shape.at(shape.size() - 1);
    int64_t strideA = strides.at(strides.size() - 2);
    int64_t strideB = strides.at(strides.size() - 1);
    if (strideB == dimA && strideA == 1) {
        return TransposeStatus::TRANSPOSE;
    }
    return TransposeStatus::NON_CONTINUOUS;
}
} // namespace CatlassKernelWrapper
```
