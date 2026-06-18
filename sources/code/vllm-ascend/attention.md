---
id: code-vllm-ascend-attention
title: vLLM Ascend Attention Backend
type: source-code
repo: vllm-project/vllm-ascend
path: vllm_ascend/attention
url: https://github.com/vllm-project/vllm-ascend/tree/main/vllm_ascend/attention
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
- attention
- paged-attention
- inference
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- global-memory
- unified-buffer
techniques:
- kv-cache-paging
- online-softmax
- pipeline-scheduling
kernel_types:
- attention
- paged-attention
- flash-attention
languages:
- python
- cpp
- ascendc
---

# vLLM Ascend Attention Backend

vLLM Ascend attention backend source. It anchors evidence for how vLLM's paged attention abstractions map onto Ascend NPU operators and custom kernels in serving workloads.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `vllm_ascend/attention`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/vllm_ascend/attention


## Fetched Source


### `vllm_ascend/attention/abstract.py`
```python
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

from abc import abstractmethod
from typing import Generic, TypeVar

import torch
from vllm.v1.attention.backend import AttentionImpl, AttentionLayer


class AttentionMetadata:
    pass


T = TypeVar("T", bound=AttentionMetadata)


class DSAAttentionImpl(AttentionImpl[T], Generic[T]):
    @abstractmethod
    def __init__(
        self,
        dim: int,
        n_heads: int,
        scale: float,
        n_local_heads: int,
        q_lora_rank: int,
        o_lora_rank: int,
        head_dim: int,
        rope_head_dim: int | None,
        nope_head_dim: int,
        n_groups: int,
        n_local_groups: int,
        window_size: int,
        compress_ratio: int,
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    def forward(
        self,
        layer: AttentionLayer,
        hidden_states_or_cq: torch.Tensor,
        kv_c_normed: torch.Tensor,
        k_pe: torch.Tensor,
        kv_cache: torch.Tensor,
        attn_metadata: T,
        output: torch.Tensor | None = None,
        output_scale: torch.Tensor | None = None,
        output_block_scale: torch.Tensor | None = None,
    ) -> torch.Tensor:
        raise NotImplementedError

```

### `vllm_ascend/attention/dsa_v1.py`
```python
import math
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar, TypeAlias

import torch
import torch.nn.functional as F
import torch_npu
import vllm.envs as envs_vllm
from vllm.config import VllmConfig, get_current_vllm_config
from vllm.distributed import get_tensor_model_parallel_world_size
from vllm.forward_context import get_forward_context
from vllm.triton_utils import HAS_TRITON
from vllm.v1.attention.backend import AttentionBackend, AttentionCGSupport, AttentionMetadataBuilder
from vllm.v1.kv_cache_interface import AttentionSpec, MLAAttentionSpec

from vllm_ascend.ascend_config import get_ascend_config
from vllm_ascend.attention.abstract import DSAAttentionImpl
from vllm_ascend.attention.attention_mask import AttentionMaskBuilder
from vllm_ascend.attention.attention_v1 import AscendAttentionState
from vllm_ascend.attention.utils import AscendCommonAttentionMetadata, split_decodes_and_prefills
from vllm_ascend.device.device_op import DeviceOperator
from vllm_ascend.ops.cv_linear import CVLinearWrapper
from vllm_ascend.ops.linear import AscendUnquantizedLinearMethod
from vllm_ascend.ops.rope_dsv4 import get_cos_and_sin_dsa
from vllm_ascend.quantization.methods.w8a8_dynamic import AscendW8A8DynamicLinearMethod
from vllm_ascend.utils import (
    AscendDeviceType,
    get_ascend_device_type,
    npu_stream_switch,
    olora_tp_enable,
)
from vllm_ascend.worker.npu_input_batch import NPUInputBatch

if TYPE_CHECKING:
    from vllm.v1.core.sched.output import SchedulerOutput

    from vllm_ascend.ops.triton.rms_norm import triton_q_rms

if HAS_TRITON:
    from vllm_ascend.ops.triton.rms_norm import triton_q_rms  # noqa: F811
else:
    triton_q_rms = None  # type: ignore

BUILD_METADATA_STEP_PREFILL = 0
BUILD_METADATA_STEP_DECODE = 1

_DSV4_DSA_OVERLAP_STREAM = None


def dsv4_dsa_overlap_stream() -> torch.npu.Stream:
    global _DSV4_DSA_OVERLAP_STREAM
    if _DSV4_DSA_OVERLAP_STREAM is None:
        _DSV4_DSA_OVERLAP_STREAM = torch_npu.npu.Stream()
    return _DSV4_DSA_OVERLAP_STREAM


# mypy: disable-error-code="has-type"


def hadamard_transform_ref(
    x: torch.Tensor,
    hadamard: torch.Tensor,
    scale: float = 1.0,
):
    x_shape = x.shape
    dim = x.shape[-1]
    x = x.reshape(-1, dim)
    log_dim = math.ceil(math.log2(dim))
    dim_padded = 2**log_dim
    if dim != dim_padded:
        x = F.pad(x, (0, dim_padded - dim))
    out = F.linear(x, hadamard)
    out = out * scale
    return out[..., :dim].reshape(*x_shape)


def rotate_activation(x: torch.Tensor, hadamard: torch.Tensor) -> torch.Tensor:
    hidden_size = x.size(-1)
    return hadamard_transform_ref(x, hadamard=hadamard, scale=hidden_size**-0.5)


def hadamard_linear(x: torch.Tensor, hadamard: torch.Tensor) -> tuple[torch.Tensor, tuple[int, ...], int]:
    """
    Part 1 of rotate_activation: Execute F.linear (matrix multiplication).
    This runs in main stream, parallel with aux_stream kv_scatter.

    Returns:
        Tuple of (linear_output, original_shape, original_dim)
    """
    x_shape = x.shape
    dim = x.shape[-1]
    x = x.reshape(-1, dim)
    log_dim = math.ceil(math.log2(dim))
    dim_padded = 2**log_dim
    if dim != dim_padded:
        x = F.pad(x, (0, dim_padded - dim))
    out = F.linear(x, hadamard)
    return out, x_shape, dim


def hadamard_scale(out: torch.Tensor, x_shape: tuple[int, ...], dim: int, scale: float = 1.0) -> torch.Tensor:
    """
    Part 2 of rotate_activation: Execute scale multiplication and reshape.
    This runs in main stream after aux_stream completes.
    """
    out = out * scale
    return out[..., :dim].reshape(*x_shape)


def _is_w8a8_dynamic(linear) -> bool:
    """True iff ``linear`` is wired up with ``AscendW8A8DynamicLinearMethod``."""
    qm = getattr(linear, "quant_method", None)
    if qm is None or isinstance(qm, AscendUnquantizedLinearMethod):
        return False
    inner = getattr(qm, "quant_method", None)
    return isinstance(inner, AscendW8A8DynamicLinearMethod)


def pad_to_blocks(x: torch.Tensor, length_list: torch.Tensor, block_size: int = 128):
    """
    Pads a ragged/packed tensor into fixed-size blocks.

    Args:
        x: Input tensor of shape [t, n, d] where t = sum(length_list).
        length_list: Tensor of shape [bs] containing valid sequence lengths.
        block_size: The size of each block (default 128).

    Returns:
        padded_blocks: Tensor of shape [total_blocks, block_size, n, d].
    """
    # 1. Validation
    if x.shape[0] != length_list.sum():
        raise ValueError(f"Input dimension 0 ({x.shape[0]}) does not match sum of length_list ({length_list.sum()})")

    bs = length_list.shape[0]
    n, d = x.shape[1], x.shape[2]

    # 2. Calculate how many blocks are needed for each request
    # Formula: ceil(length / block_size) -> (length + block_size - 1) // block_size
    blocks_per_req = (length_list + block_size - 1) // block_size
    total_blocks = blocks_per_req.sum() + 1

    # 3. Allocate output tensor with ze
// ... (truncated due to length) ...

```

### `vllm_ascend/attention/__init__.py`
```python

```
