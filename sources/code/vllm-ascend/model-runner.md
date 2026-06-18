---
id: code-vllm-ascend-model-runner
title: vLLM Ascend Model Runner
type: source-code
repo: vllm-project/vllm-ascend
path: vllm_ascend/worker
url: https://github.com/vllm-project/vllm-ascend/tree/main/vllm_ascend/worker
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
- scheduler
- inference
- python
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- global-memory
- cube-unit
- vector-unit
techniques:
- kv-cache-paging
- pipeline-scheduling
- tensor-parallel-overlap
kernel_types:
- attention
- matmul
- moe
languages:
- python
---

# vLLM Ascend Model Runner

vLLM Ascend worker/model-runner source. This path is evidence for request scheduling, execution orchestration, KV-cache management, and how Python control flow invokes NPU kernels in serving.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `vllm_ascend/worker`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/vllm_ascend/worker


## Fetched Source


### `vllm_ascend/worker/worker.py`
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
# Adapted from vllm-project/vllm/vllm/worker/gpu_worker.py
#

import copy
import gc
import logging
from types import NoneType

import torch
import torch.nn as nn
import torch_npu
import vllm.envs as envs_vllm
from torch_npu.op_plugin.atb._atb_ops import _register_atb_extensions
from torch_npu.profiler import dynamic_profile as dp
from vllm.config import CUDAGraphMode, VllmConfig, set_current_vllm_config
from vllm.distributed import ensure_model_parallel_initialized, init_distributed_environment
from vllm.distributed.ec_transfer import ensure_ec_transfer_initialized
from vllm.distributed.kv_transfer import (
    ensure_kv_transfer_initialized,
    ensure_kv_transfer_shutdown,
    get_kv_transfer_group,
    has_kv_transfer_group,
)
from vllm.distributed.kv_transfer.kv_connector.v1.base import KVConnectorHandshakeMetadata
from vllm.distributed.parallel_state import Handle, get_pp_group, get_tp_group
from vllm.logger import logger
from vllm.lora.request import LoRARequest
from vllm.sequence import IntermediateTensors
from vllm.tasks import SupportedTask
from vllm.utils.mem_constants import GiB_bytes
from vllm.utils.mem_utils import MemorySnapshot, format_gib, memory_profiling
from vllm.utils.torch_utils import STR_DTYPE_TO_TORCH_DTYPE
from vllm.v1.core.sched.output import GrammarOutput, SchedulerOutput
from vllm.v1.kv_cache_interface import KVCacheConfig, KVCacheSpec
from vllm.v1.outputs import EMPTY_MODEL_RUNNER_OUTPUT, AsyncModelRunnerOutput, DraftTokenIds, ModelRunnerOutput
from vllm.v1.utils import report_usage_stats
from vllm.v1.worker.gpu_worker import AsyncIntermediateTensors
from vllm.v1.worker.worker_base import CompilationTimes, WorkerBase
from vllm.v1.worker.workspace import init_workspace_manager

import vllm_ascend.envs as envs_ascend
from vllm_ascend.ascend_config import get_ascend_config, init_ascend_config
from vllm_ascend.batch_invariant import init_batch_invariance
from vllm_ascend.cpu_binding import bind_cpus
from vllm_ascend.device_allocator.camem import CaMemAllocator
from vllm_ascend.distributed.parallel_state import init_ascend_model_parallel
from vllm_ascend.ops.triton.triton_utils import init_device_properties_triton
from vllm_ascend.profiler.torch_npu_profiler import TorchNPUProfilerWrapper
from vllm_ascend.utils import (
    AscendDeviceType,
    check_ascend_device_type,
    enable_sp,
    get_ascend_device_type,
    register_ascend_customop,
    setup_ascend_local_comm_res,
    vllm_version_is,
)
from vllm_ascend.worker.model_runner_v1 import NPUModelRunner

torch._dynamo.trace_rules.clear_lru_cache()  # noqa: E402
from torch._dynamo.variables import TorchInGraphFunctionVariable  # noqa: E402
from vllm.utils.torch_utils import set_random_seed  # noqa: E402

torch_non_c_binding_in_graph_functions_npu = dict.fromkeys(
    ["torch.npu.current_stream"],
    TorchInGraphFunctionVariable,
)  # noqa: E402
torch_non_c_binding_in_graph_functions_npu["torch.npu.stream"] = TorchInGraphFunctionVariable  # noqa: E402
torch._dynamo.trace_rules.torch_name_rule_map.append(torch_non_c_binding_in_graph_functions_npu)  # noqa: E402


class NPUWorker(WorkerBase):
    def __init__(
        self,
        vllm_config: VllmConfig,
        local_rank: int,
        rank: int,
        distributed_init_method: str,
        is_driver_worker: bool = False,
        # Additional parameters for compatibility with vllm
        **kwargs,
    ):
        """Initialize the worker for Ascend."""
        if not envs_ascend.COMPILE_CUSTOM_KERNELS:
            logger.warning(
                "COMPILE_CUSTOM_KERNELS is set to False. "
                "In most scenarios, without custom kernels, vllm-ascend will not function correctly."
            )

        # register patch for vllm
        from vllm_ascend.utils import adapt_patch

        adapt_patch()

        # Register ops when worker init.
        from vllm_ascend import ops

        ops.register_dummy_fusion_op()
        if get_ascend_device_type() != AscendDeviceType.A5:
            _register_atb_extensions()
        register_ascend_customop(vllm_config)
        # init ascend config and soc version
        init_ascend_config(vllm_config)
        from vllm_ascend.logger import configure_ascend_file_logging

        configure_ascend_file_logging()
        check_ascend_device_type(
// ... (truncated due to length) ...

```

### `vllm_ascend/worker/block_table.py`
```python
import numpy as np
import torch
from vllm.distributed import get_dcp_group, get_pcp_group
from vllm.utils.math_utils import cdiv
from vllm.v1.attention.backends.utils import PAD_SLOT_ID
from vllm.v1.kv_cache_interface import KVCacheGroupSpec, MambaSpec
from vllm.v1.utils import CpuGpuBuffer
from vllm.v1.worker.block_table import _compute_slot_mapping_kernel
from vllm.v1.worker.cp_utils import get_total_cp_world_size


class BlockTable:
    def __init__(
        self,
        block_size: int,
        max_num_reqs: int,
        max_num_blocks_per_req: int,
        max_num_batched_tokens: int,
        pin_memory: bool,
        device: torch.device,
        kernel_sizes: list[int] | None = None,
        cp_kv_cache_interleave_size: int = 1,
        num_speculative_tokens: int = 0,
        kv_cache_group: KVCacheGroupSpec = None,
    ):
        self.max_num_reqs = max_num_reqs
        self.pcp_world_size = get_pcp_group().world_size
        self.pcp_rank = get_pcp_group().rank_in_group if self.pcp_world_size > 1 else 0
        self.dcp_world_size = get_dcp_group().world_size
        self.dcp_rank = get_dcp_group().rank_in_group
        compress_ratio = 1
        if (
            kv_cache_group is not None
            and hasattr(kv_cache_group, "kv_cache_spec")
            and hasattr(kv_cache_group.kv_cache_spec, "compress_ratio")
        ):
            compress_ratio = kv_cache_group.kv_cache_spec.compress_ratio
        if (
            kv_cache_group is not None
            and hasattr(kv_cache_group, "kv_cache_spec")
            and (self.pcp_world_size * self.dcp_world_size > 1)
            and isinstance(kv_cache_group.kv_cache_spec, MambaSpec)
        ):
            max_num_blocks_per_req = max_num_blocks_per_req * self.pcp_world_size * self.dcp_world_size
        max_num_blocks_per_req = max(cdiv(max_num_blocks_per_req, compress_ratio), 1)
        self.max_num_blocks_per_req = max_num_blocks_per_req
        self.max_num_batched_tokens = max_num_batched_tokens
        self.pin_memory = pin_memory
        self.device = device
        self.physical_block_size = block_size
        self.is_mamba_group = (
            kv_cache_group is not None
            and hasattr(kv_cache_group, "kv_cache_spec")
            and isinstance(kv_cache_group.kv_cache_spec, MambaSpec)
        )

        # If kernel_sizes is None or [0], use physical block size (no splitting)
        if kernel_sizes is None or kernel_sizes == [0]:
            self.block_size = block_size
            self.logical_block_size = block_size
            self.blocks_per_phys_block = 1
            self.use_hybrid_blocks = False
        else:
            # Find the first kernel size that divides physical_block_size evenly
            selected_kernel_size = None
            for kernel_size in kernel_sizes:
                if kernel_size > 0 and self.physical_block_size % kernel_size == 0:
                    selected_kernel_size = kernel_size
                    break

            if selected_kernel_size is None:
                raise ValueError(
                    f"None of the kernel sizes {kernel_sizes} can divide "
                    f"physical block size {self.physical_block_size} evenly"
                )

            self.block_size = selected_kernel_size
            self.logical_block_size = selected_kernel_size
            self.blocks_per_phys_block = self.physical_block_size // self.logical_block_size
            if self.blocks_per_phys_block > 1:
                self.use_hybrid_blocks = True
            else:
                self.use_hybrid_blocks = False

        if self.use_hybrid_blocks:
            logical_table_size = max_num_blocks_per_req * self.blocks_per_phys_block
        else:
            logical_table_size = max_num_blocks_per_req

        duplicate_size = 1
        if self.pcp_world_size * self.dcp_world_size > 1:
            duplicate_size += num_speculative_tokens
        self.block_table = self._make_buffer(max_num_reqs * duplicate_size, logical_table_size, dtype=torch.int32)
        self.num_blocks_per_row = np.zeros(max_num_reqs, dtype=np.int32)
        self.slot_mapping = self._make_buffer(
            self.max_num_batched_tokens + 2 * self.pcp_world_size * self.max_num_reqs, dtype=torch.int32
        )

        self.kernel_sizes = kernel_sizes
        self.cp_kv_cache_interleave_size = cp_kv_cache_interleave_size

    def append_row(
        self,
        block_ids,
        row_idx: int,
    ) -> None:
        if not block_ids:
            return
        block_ids = np.array(block_ids)
        if self.use_hybrid_blocks:
            block_ids = self._convert_physical_to_logical_blocks(block_ids)

        num_blocks = len(block_ids)
        start = self.num_blocks_per_row[row_idx]

        self.block_table.np[row_idx, start : start + num_blocks] = block_ids
        self.num_blocks_per_row[row_idx] += num_blocks

    def add_row(self, block_ids: list[int], row_idx: int) -> None:
        self.num_blocks_per_row[row_idx] = 0
  
// ... (truncated due to length) ...

```

### `vllm_ascend/worker/kvcomp_utils.py`
```python
import json
import logging
from collections import defaultdict
from dataclasses import asdict, dataclass, field

import torch
import torch_npu
from vllm.model_executor.layers.attention import Attention
from vllm.model_executor.models.utils import extract_layer_index
from vllm.utils.math_utils import cdiv

from vllm_ascend.ascend_config import get_ascend_config

logger = logging.getLogger(__name__)


# largely follow vllm.v1.worker.utils.bind_kv_cache
def bind_hashk_cache(
    hashk_caches: dict[str, torch.Tensor],
    forward_context: dict[str, Attention],
    runner_hashk_caches: list[torch.Tensor],
    num_attn_module: int = 1,
) -> None:
    """
    Bind the allocated hashk cache to both ModelRunner and forward context so
    that the hashk cache can be used in the forward pass.

    This function:
      1) Fills the ModelRunner's hashk cache list (`runner_hashk_caches`) with
         hashk_caches.
      2) Associates each attention layer in the `forward_context` with its
         corresponding hashk cache in hashk_caches.

    Args:
        hashk_caches: The allocated hashk_caches with layer names as keys.
        forward_context: The global forward context containing all Attention
            layers with layer names as keys.
        runner_hashk_caches: The hashk cache declared by ModelRunner.
    """
    # Bind hashk_caches to ModelRunner; ensure it is empty before binding
    assert len(runner_hashk_caches) == 0

    # Convert hashk_caches dict to a list of tensors in the order of layer_index.
    index2name = defaultdict(list)
    for layer_name in hashk_caches:
        index2name[extract_layer_index(layer_name, num_attn_module)].append(layer_name)

    for layer_index in sorted(index2name.keys()):
        layer_names = index2name[layer_index]
        # TODO: support multiple hashk caches for the same layer index later, e.g., encoder-decoder models.
        layer_name = layer_names[0]
        runner_hashk_caches.append(hashk_caches[layer_name])

    # Bind kv_caches to forward context
    for layer_name, hashk_cache in hashk_caches.items():
        # NOTE: Use list because of v0 PP virtual engine.
        forward_context[layer_name].hashk_cache = [hashk_cache]


def bind_hashk_cache_nope(
    hashk_caches_nope: dict[str, torch.Tensor],
    forward_context: dict[str, Attention],
    runner_hashk_caches_nope: list[torch.Tensor],
    num_attn_module: int = 1,
) -> None:
    """
    Bind the allocated hashk cache for nope in MLA to both ModelRunner and forward context so
    that the hashk cache for nope can be used in the forward pass.

    This function:
      1) Fills the ModelRunner's hashk cache list (`runner_hashk_caches_nope`) with
         hashk_caches_nope.
      2) Associates each attention layer in the `forward_context` with its
         corresponding hashk cache for nope in MLA in hashk_caches_nope.

    Args:
        hashk_caches_nope: The allocated hashk_caches_nope with layer names as keys.
        forward_context: The global forward context containing all Attention
            layers with layer names as keys.
        runner_hashk_caches_nope: The hashk cache for nope declared by ModelRunner.
    """
    # Bind hashk_caches_nope to ModelRunner; ensure it is empty before binding
    assert len(runner_hashk_caches_nope) == 0

    # Convert hashk_caches_nope dict to a list of tensors in the order of layer_index.
    index2name = defaultdict(list)
    for layer_name in hashk_caches_nope:
        index2name[extract_layer_index(layer_name, num_attn_module)].append(layer_name)

    for layer_index in sorted(index2name.keys()):
        layer_names = index2name[layer_index]
        # TODO: support multiple hashk caches for the same layer index later, e.g., encoder-decoder models.
        layer_name = layer_names[0]
        runner_hashk_caches_nope.append(hashk_caches_nope[layer_name])

    # Bind hashk_caches_nope to forward context
    for layer_name, hashk_cache_nope in hashk_caches_nope.items():
        # NOTE: Use list because of v0 PP virtual engine.
        forward_context[layer_name].hashk_cache_nope = [hashk_cache_nope]


def bind_hashk_cache_rope(
    hashk_caches_rope: dict[str, torch.Tensor],
    forward_context: dict[str, Attention],
    runner_hashk_caches_rope: list[torch.Tensor],
    num_attn_module: int = 1,
) -> None:
    """
    Bind the allocated hashk cache for rope in MLA to both ModelRunner and forward context so
    that the hashk cache for rope can be used in the forward pass.

    This function:
      1) Fills the ModelRunner's hashk cache list (`runner_hashk_caches_rope`) with
         hashk_caches_rope.
      2) Associates each attention layer in the `forward_context` with its
         corresponding hashk cache for rope in MLA in hashk_caches_rope.

    Args:
        hashk_caches_rope: The allocated hashk_caches_rope with layer names as keys.
        forward_context: The global forward context containing all Attention
            layers with layer names as keys.
        
// ... (truncated due to length) ...

```
