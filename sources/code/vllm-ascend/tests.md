---
id: code-vllm-ascend-tests
title: vLLM Ascend Kernel and Backend Tests
type: source-code
repo: vllm-project/vllm-ascend
path: tests
url: https://github.com/vllm-project/vllm-ascend/tree/main/tests
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
- tests
- inference
- python
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- global-memory
techniques:
- kv-cache-paging
- format-conversion
kernel_types:
- attention
- matmul
- moe
- rope
languages:
- python
---

# vLLM Ascend Kernel and Backend Tests

vLLM Ascend test suite source. These tests provide executable evidence for NPU backend behavior, custom kernel correctness, model execution, and regression coverage around serving workloads.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `tests`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/tests


## Fetched Source


### `tests/__init__.py`
```python

```

### `tests/ut/test_utils.py`
```python
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# This file is a part of the vllm-ascend project.
#

import math
import os
from unittest import mock

import pytest
import torch

from tests.ut.base import TestBase
from vllm_ascend import utils
from vllm_ascend.utils import REGISTERED_ASCEND_OPS


class TestUtils(TestBase):
    def setUp(self):
        import importlib

        from vllm_ascend import platform

        importlib.reload(platform)
        utils.enable_dsa_cp_with_layer_shard.cache_clear()
        utils.enable_dsa_cp_with_o_proj_tp.cache_clear()

    def test_nd_to_nz_2d(self):
        # can be divided by 16
        input_tensor = torch.randn(32, 64)
        output = utils.nd_to_nz_2d(input_tensor)
        self.assertEqual(output.shape[0], 1)
        self.assertEqual(output.shape[1], 64 // 16)
        self.assertEqual(output.shape[2], 32)
        self.assertEqual(output.shape[3], 16)

        # cannot be divided by 16
        input_tensor = torch.randn(30, 62)
        output = utils.nd_to_nz_2d(input_tensor)
        self.assertEqual(output.shape[0], 1)
        self.assertEqual(output.shape[1], math.ceil(62 / 16))
        self.assertEqual(output.shape[2], 32)
        self.assertEqual(output.shape[3], 16)

        # pad to 16
        input_tensor = torch.randn(8, 12)
        output = utils.nd_to_nz_2d(input_tensor)
        self.assertEqual(output.shape[0], 1)
        self.assertEqual(output.shape[1], 1)  # 12->16, 16//16=1
        self.assertEqual(output.shape[2], 16)  # 8->16
        self.assertEqual(output.shape[3], 16)

        # check if the output is contiguous
        input_tensor = torch.randn(32, 64)
        output = utils.nd_to_nz_2d(input_tensor)
        self.assertTrue(output.is_contiguous())

        # check if the output values are preserved
        input_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
        output = utils.nd_to_nz_2d(input_tensor)
        expected = torch.tensor(
            [
                [
                    [
                        [1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    ]
                ]
            ]
        )
        self.assertTrue(torch.allclose(output, expected))

    def test_aligned_16(self):
        # align to 16
        input_tensor = torch.randn(15, 64)
        output_tensor = utils.aligned_16(input_tensor)
        self.assertEqual(output_tensor.shape[0], 16)

        # align to 16
        input_tensor = torch.randn(16, 64)
        output_tensor = utils.aligned_16(input_tensor)
        self.assertEqual(output_tensor.shape[0], 16)
        self.assertTrue(torch.equal(input_tensor, output_tensor))

        # align to 32
        input_tensor = torch.randn(17, 64)
        output_tensor = utils.aligned_16(input_tensor)
        self.assertEqual(output_tensor.shape[0], 32)

    @pytest.mark.skip("Skip as register_kernels has NPU SocName checking in CANN 8.5.0.")
    def test_enable_custom_op(self):
        result = utils.enable_custom_op()
        self.assertTrue(result)

        utils._CUSTOM_OP_ENABLED = None

        with mock.patch("builtins.__import__") as mock_import_module:
            mock_import_module.side_effect = ImportError("import error")
            self.assertFalse(utils.enable_custom_op())

    def test_find_hccl_library(self):
        with mock.patch.dict(os.environ, {"HCCL_SO_PATH": "/path/to/hccl/libhccl.so"}):
           
// ... (truncated due to length) ...

```

### `tests/ut/conftest.py`
```python
#
# Copyright (c) 2025 Huawei Technologies Co., Ltd. All Rights Reserved.
# Copyright 2023 The vLLM team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# This file is a part of the vllm-ascend project.
#
"""Shared UT setup.

NPU vs CPU routing is determined by directory convention, not decorators.
See ``.github/workflows/scripts/select_tests.py`` and
``.github/workflows/scripts/test_config.yaml`` for the routing rules.

Conventions for UT directories:
    tests/ut/<module>/            -> CPU runner (default)
    tests/ut/<module>/a2/         -> A2 NPU x1
    tests/ut/<module>/a2_2/       -> A2 NPU x2
    tests/ut/<module>/a3_2/       -> A3 NPU x2
    tests/ut/<module>/a3_4/       -> A3 NPU x4
    tests/ut/<module>/310p/       -> 310P NPU x1
"""

import importlib.util
import subprocess
import sys
import types
from unittest.mock import MagicMock

try:
    # Note: do not import torch here for cpu env, which will lead to circle import error.
    subprocess.run(["npu-smi", "info"], capture_output=True, check=True)
    _npu_available = True
except (subprocess.CalledProcessError, FileNotFoundError):
    _npu_available = False

if not _npu_available:
    triton_runtime = MagicMock()
    triton_runtime.driver.active.utils.get_device_properties.return_value = {
        "num_aic": 8,
        "num_vectorcore": 8,
    }
    sys.modules["triton.runtime"] = triton_runtime
    torch_npu = types.ModuleType("torch_npu")
    torch_npu.__spec__ = importlib.util.spec_from_loader("torch_npu", loader=None)
    torch_npu.__path__ = []
    torch_npu.npu = MagicMock()  # type: ignore[attr-defined]
    torch_npu.profiler = MagicMock()  # type: ignore[attr-defined]
    torch_npu.npu_fusion_attention = MagicMock()  # type: ignore[attr-defined]
    torch_npu.npu_format_cast = MagicMock(side_effect=lambda weight, fmt: weight)  # type: ignore[attr-defined]
    torch_npu._C = MagicMock()  # type: ignore[attr-defined]
    torch_npu._C._NPUTaskGroupHandle = MagicMock
    sys.modules["torch_npu"] = torch_npu
    sys.modules["torch_npu._C"] = torch_npu._C
    sys.modules["torch_npu._C._distributed_c10d"] = torch_npu._C._distributed_c10d
    acl_rt = types.ModuleType("acl.rt")
    acl_rt.__spec__ = importlib.util.spec_from_loader("acl.rt", loader=None)
    acl_rt.memcpy = MagicMock()  # type: ignore[attr-defined]
    acl_mod = types.ModuleType("acl")
    acl_mod.__spec__ = importlib.util.spec_from_loader("acl", loader=None)
    acl_mod.rt = acl_rt  # type: ignore[attr-defined]
    sys.modules["acl"] = acl_mod
    sys.modules["acl.rt"] = acl_rt
    mooncake_engine = types.ModuleType("mooncake.engine")
    mooncake_engine.__spec__ = importlib.util.spec_from_loader("mooncake.engine", loader=None)
    mooncake_engine.TransferEngine = MagicMock()  # type: ignore[attr-defined]
    sys.modules["mooncake.engine"] = mooncake_engine
    import torch

    try:  # noqa: SIM105
        torch.utils.rename_privateuse1_backend("npu")
    except RuntimeError:
        pass
    torch.npu = MagicMock()
    torch.npu.Stream = MagicMock
    torch.version.cann = None
    torch.distributed.is_hccl_available = MagicMock(return_value=True)

import pytest

mooncake_engine = types.ModuleType("mooncake.engine")
mooncake_engine.__spec__ = importlib.util.spec_from_loader("mooncake.engine", loader=None)
mooncake_engine.TransferEngine = MagicMock()  # type: ignore[attr-defined]
sys.modules.setdefault("mooncake.engine", mooncake_engine)

from vllm_ascend.utils import (  # noqa: E402
    adapt_patch,
    clear_enable_sp,
    register_ascend_customop,
)

# Mock torch_npu AFTER vllm_ascend import to avoid circular import in accelerate
if not _npu_available:
    sys.modules["torch_npu"].npu.current_device = MagicMock(return_value=0)
    sys.modules["torch_npu._inductor"] = MagicMock()
    sys.modules["torch_npu"]._npu_flash_attention = MagicMock()  # type: ignore[attr-defined]
    sys.modules["torch_npu"]._npu_paged_attention_splitfuse = MagicMock()  # type: ignore[attr-defined]
    sys.modules["torch_npu"]._npu_reshape_and_cache = MagicMock()  # type: ignore[attr-defined]
    sys.modules["torch_npu"].npu_moe_gating_top_k_softmax = MagicMock()  # type: ignore[attr-defined]
    sys.modules["torch_npu"].npu_quant_matmul = MagicMock()  # type: ignore[attr-defined]
    sys.modules["torch_npu"].npu_rms_norm = MagicMock()  # type: ignore[attr-defined]
    sys.modules["torch_npu"].npu_swiglu = MagicMock()  # type: ignore[attr-defined]
    sys.modules["torch_npu"].npu_convert_weight_to_int4pack = Ma
// ... (truncated due to length) ...

```
