---
id: code-vllm-ascend-ops
title: vLLM Ascend Operator Wrappers
type: source-code
repo: vllm-project/vllm-ascend
path: vllm_ascend/ops
url: https://github.com/vllm-project/vllm-ascend/tree/main/vllm_ascend/ops
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
- operator
- python
- torch-npu
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- global-memory
techniques:
- format-conversion
- kv-cache-paging
- pipeline-scheduling
kernel_types:
- matmul
- attention
- rope
- moe
languages:
- python
- cpp
---

# vLLM Ascend Operator Wrappers

vLLM Ascend operator wrapper source. It is evidence for Python-side dispatch to torch_npu and custom kernels, including format preparation, attention/MoE wrappers, and operator availability gates.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `vllm_ascend/ops`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/vllm_ascend/ops


## Fetched Source


### `vllm_ascend/ops/mm_encoder_attention.py`
```python
#
# Copyright (c) 2025 Huawei Technologies Co., Ltd. All Rights Reserved.
# This file is a part of the vllm-ascend project.
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
#

"""Ascend implementation of upstream :class:`MMEncoderAttention`.

Eager and ACL-graph capture both use Fused Infer Attention (``npu_fused_infer_attention_score``)
with ``graph_task_group_begin/end`` so replay-time host metadata can be rebound from the update stream,
matching the LLM full-graph pattern in :mod:`vllm_ascend.attention.attention_v1`.
"""

from __future__ import annotations

import einops
import numpy as np
import torch
import torch.nn.functional as F
import torch_npu
from vllm.model_executor.layers.attention.mm_encoder_attention import MMEncoderAttention  # type: ignore
from vllm.v1.attention.backends.registry import AttentionBackendEnum

from vllm_ascend.utils import weak_ref_tensors
from vllm_ascend.worker.encoder_acl_graph import (
    get_encoder_forward_context,
    get_encoder_graph_params,
    update_encoder_graph_workspace,
)

MIN_PAD_SIZE: int = 64
MAX_PAD_SIZE: int = 128
SWA_INT_MAX: int = 2147483647
FIA_BLOCK_SIZE: int = 128


class AscendMMEncoderAttention(MMEncoderAttention):
    def __init__(
        self,
        num_heads: int,
        head_size: int,
        scale: float | None = None,
        num_kv_heads: int | None = None,
        prefix: str = "",
    ) -> None:
        """
        Args:
            num_heads: number of attention heads per partition.
            head_size: hidden_size per attention head.
            scale: scale factor.
            num_kv_heads: number of kv heads.
            prefix: This has no effect, it is only here to make it easier to
                    swap between Attention and MMEncoderAttention.
            multimodal_config: configs for multi-modal.
        """
        super().__init__(
            num_heads=num_heads,
            head_size=head_size,
            scale=scale,
            num_kv_heads=num_kv_heads,
            prefix=prefix,
        )

        self.enable_pad = self.head_size > MIN_PAD_SIZE and self.head_size < MAX_PAD_SIZE
        self.scale_value = self.head_size**-0.5

    @classmethod
    def maybe_compute_seq_lens(
        cls,
        attn_backend: AttentionBackendEnum,
        cu_seqlens: np.ndarray,
        device: torch.device,
    ) -> np.ndarray | None:
        if cu_seqlens is None:
            return None

        seq_lens = cu_seqlens[1:] - cu_seqlens[:-1]
        seq_lens = torch.from_numpy(seq_lens).to("cpu", non_blocking=True)

        return seq_lens

    def _maybe_compute_actual_seq_lengths(
        self,
        bsz: int,
        q_len: int,
        cu_seqlens: torch.Tensor | None,
        sequence_lengths: torch.Tensor | None,
    ) -> tuple[list[int], list[int]]:
        """Build FIA ``actual_seq_lengths`` as cumulative host-side ``list[int]``."""
        if sequence_lengths is not None:
            seq_lens_cpu = sequence_lengths
            if seq_lens_cpu.device.type != "cpu":
                seq_lens_cpu = seq_lens_cpu.to("cpu")
            actual = seq_lens_cpu.cumsum(0).to(torch.int64).tolist()
        else:
            cu = self._maybe_compute_cu_seqlens(bsz, q_len, cu_seqlens)
            if cu.device.type != "cpu":
                cu = cu.to("cpu")
            actual = cu[1:].to(torch.int64).tolist()

        return actual, actual

    def _reshape_qkv_to_3d(
        self,
        query: torch.Tensor,
        key: torch.Tensor,
        value: torch.Tensor,
        bsz: int,
        q_len: int,
        kv_len: int,
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """
        Reshape query, key, value to 3D tensors:
        (batch_size * seq_len, num_heads, head_size)
        """
        query = query.view(bsz * q_len, self.num_heads, self.head_size)
        key = key.view(bsz * kv_len, self.num_kv_heads, self.head_size)
        value = value.view(bsz * kv_len, self.num_kv_heads, self.head_size)
        self.num_queries_per_kv = self.num_heads // self.num_kv_heads
        if (num_repeat := self.num_queries_per_kv) > 1:
            # Handle MQA and GQA
            key = torch.repeat_interleave(key, num_repeat, dim=1)
            value = torch.repeat_interleave(value, num_repeat, dim=1)

        return query, key, value

    def _maybe_compute_cu_seqlens(
        self,
        bsz: int,
        q_len: int,
        cu_seqlens: torch.Tensor | None = None,
    ) -> torch.Tensor:
        if cu_seqlens is not None:
            re
// ... (truncated due to length) ...

```

### `vllm_ascend/ops/layernorm.py`
```python
# Copyright (c) 2025 Huawei Technologies Co., Ltd. All Rights Reserved.
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


import torch
from torch import nn
from vllm.config import get_current_vllm_config
from vllm.model_executor.layers.layernorm import GemmaRMSNorm, RMSNorm, RMSNormGated

from vllm_ascend.device.device_op import DeviceOperator
from vllm_ascend.ops.triton.layernorm_gated import layer_norm_fwd_npu
from vllm_ascend.utils import enable_custom_op, get_weight_prefetch_method


class AscendRMSNorm(RMSNorm):
    def __init__(
        self,
        hidden_size: int,
        eps: float = 1e-6,
        var_hidden_size: int | None = None,
        has_weight: bool = True,
        dtype: torch.dtype | None = None,
    ) -> None:
        super().__init__(hidden_size, eps, var_hidden_size, has_weight, dtype)
        vllm_config = get_current_vllm_config()
        self.bias = None
        self.bias_loaded = False

        # quantization with anti_method m4 will generate none-zero norm bias
        if vllm_config.quant_config is not None and any(
            "norm.bias" in name for name in vllm_config.quant_config.quant_description
        ):
            self.bias = torch.nn.Parameter(torch.zeros(hidden_size), requires_grad=False)
            self.bias.weight_loader = self._bias_weight_loader

    def _bias_weight_loader(self, param: torch.nn.Parameter, loaded_weight: torch.Tensor) -> None:
        if param.numel() == 1 and loaded_weight.numel() == 1:
            # Sometimes scalar values aren't considered tensors with shapes
            # so if both param and loaded_weight are a scalar,
            # "broadcast" instead of copy
            param.data.fill_(loaded_weight.item())
        else:
            assert param.size() == loaded_weight.size(), (
                f"Attempted to load weight ({loaded_weight.size()}) into parameter ({param.size()})"
            )

            param.data.copy_(loaded_weight)
        self.bias_loaded = True

    def forward_oot(
        self,
        x: torch.Tensor,
        residual: torch.Tensor | None = None,
    ) -> torch.Tensor | tuple[torch.Tensor, torch.Tensor]:
        import torch_npu

        if residual is not None:
            residual = torch.ops.vllm.maybe_chunk_residual(x, residual)
            if enable_custom_op():
                x, _, residual = torch.ops._C_ascend.npu_add_rms_norm_bias(
                    x, residual, self.weight, self.bias, self.variance_epsilon
                )
            else:
                x, _, residual = torch_npu.npu_add_rms_norm(x, residual, self.weight, self.variance_epsilon)
                if self.bias is not None:
                    x.add_(self.bias)
            return x, residual

        x, residual = torch_npu.npu_rms_norm(x, self.weight, self.variance_epsilon)
        if self.bias_loaded:
            x.add_(self.bias)

        weight_prefetch_method = get_weight_prefetch_method()
        weight_prefetch_method.maybe_prefetch_mlp_weight_postprocess(x)
        return x


class AscendGemmaRMSNorm(GemmaRMSNorm):
    def forward_oot(
        self,
        x: torch.Tensor,
        residual: torch.Tensor | None = None,
    ) -> torch.Tensor | tuple[torch.Tensor, torch.Tensor]:
        import torch_npu

        if residual is not None:
            residual = torch.ops.vllm.maybe_chunk_residual(x, residual)
            if enable_custom_op():
                x, _, residual = torch.ops._C_ascend.npu_add_rms_norm_bias(
                    x, residual, 1.0 + self.weight, None, self.variance_epsilon
                )
            else:
                x, _, residual = torch_npu.npu_add_rms_norm(x, residual, 1.0 + self.weight, self.variance_epsilon)
            return x, residual

        x = DeviceOperator.npu_gemma_rms_norm(x, self.weight, self.variance_epsilon)

        return x


class LayerNormFn(torch.autograd.Function):
    @staticmethod
    def forward(
        ctx,
        x,
        weight,
        bias,
        z=None,
        eps=1e-6,
        group_size=None,
        norm_before_gate=True,
        is_rms_norm=False,
        activation: str = "swish",
    ):
        """If z is not None, we do norm(x) * silu(z) if norm_before_gate, else norm(x * silu(z))"""

        x_shape_og = x.shape
        # reshape input data into 2D tensor
        x = x.reshape(-1, x.shape[-1])
        if x.stride(-1) != 1:
            x = x.contiguous()
        if z is not None:
            assert z.shape == 
// ... (truncated due to length) ...

```

### `vllm_ascend/ops/bailing_moe_linear_attn.py`
```python
#
# Copyright (c) 2026 Huawei Technologies Co., Ltd. All Rights Reserved.
# This file is a part of the vllm-ascend project.
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
#

"""NPU-friendly OOT replacement for BailingMoELinearAttention.

This module provides ``AscendBailingMoELinearAttention``, an out-of-tree (OOT)
replacement for the upstream ``BailingMoELinearAttention`` class.  It is
registered via the ``PluggableLayer`` mechanism so that the upstream class is
transparently replaced at instantiation time when running on Ascend NPU.
"""

import torch
import torch.nn.functional as F
from vllm.forward_context import get_forward_context
from vllm.model_executor.layers.fla.ops.layernorm_guard import layernorm_fn
from vllm.model_executor.models.bailing_moe_linear import BailingMoELinearAttention
from vllm.v1.attention.backend import AttentionMetadata
from vllm.v1.attention.backends.linear_attn import LinearAttentionMetadata

from vllm_ascend.ops.triton.mamba.lightning_attn import AscendLightningAttentionKernel
from vllm_ascend.utils import vllm_version_is

if vllm_version_is("0.22.1"):
    from vllm.model_executor.layers.mamba.linear_attn import (  # type: ignore[import-not-found]
        clear_linear_attention_cache_for_new_sequences,
        linear_attention_decode,
        linear_attention_prefill_and_mix,
    )
else:
    from vllm.model_executor.layers.mamba.linear.minimax_linear_attn import (  # type: ignore[import-not-found]
        clear_linear_attention_cache_for_new_sequences,
        linear_attention_decode,
        linear_attention_prefill_and_mix,
    )


class AscendBailingMoELinearAttention(BailingMoELinearAttention):
    """NPU-friendly drop-in replacement for BailingMoELinearAttention.

    Registered as an OOT PluggableLayer so that the upstream class is
    transparently replaced when running on Ascend NPU.  Only the three
    platform-specific methods are overridden; everything else (``__init__``,
    ``forward``, weight loading, state shape, etc.) is inherited from the
    upstream implementation.
    """

    def _prefill_and_mix_infer(self, q, k, v, kv_cache, state_indices_tensor, attn_metadata):
        return linear_attention_prefill_and_mix(
            q=q,
            k=k,
            v=v,
            kv_cache=kv_cache,
            state_indices_tensor=state_indices_tensor,
            attn_metadata=attn_metadata,
            slope_rate=self.tp_slope,
            block_size=self.BLOCK,
            decode_fn=self._decode_infer,
            prefix_fn=AscendLightningAttentionKernel.jit_linear_forward_prefix,
            layer_idx=self.layer_id,
        )

    def _decode_infer(self, q, k, v, kv_cache, state_indices_tensor, attn_metadata):
        """Handle decode (single token per sequence)."""
        hidden = linear_attention_decode(
            q,
            k,
            v,
            kv_cache,
            self.tp_slope,
            state_indices_tensor,
            q_start=0,
            q_end=attn_metadata.num_decode_tokens,
            slot_start=0,
            slot_end=attn_metadata.num_decodes,
            block_size=32,
        )
        return hidden

    def _forward(self, hidden_states, output, positions):
        forward_context = get_forward_context()
        attn_metadata: AttentionMetadata = forward_context.attn_metadata
        if attn_metadata is not None:
            assert isinstance(attn_metadata, dict)
            attn_metadata = attn_metadata[self.prefix]
            assert isinstance(attn_metadata, LinearAttentionMetadata)
            num_actual_tokens = attn_metadata.num_prefill_tokens + attn_metadata.num_decode_tokens
        else:
            num_actual_tokens = hidden_states.shape[0]

        # QKV projection
        qkv, _ = self.query_key_value(hidden_states[:num_actual_tokens])

        qkv = qkv.to(torch.float32)
        if self.linear_silu:
            qkv = F.silu(qkv)

        # Split q, k, v
        q, k, v = torch.split(
            qkv,
            [self.q_size_per_rank, self.kv_size_per_rank, self.kv_size_per_rank],
            dim=-1,
        )

        # Apply QK norm if needed
        if self.use_qk_norm:
            q = q.reshape(-1, self.tp_heads, self.head_dim)
            k = k.reshape(-1, self.tp_kv_heads, self.head_dim)
            q = layernorm_fn(
                q,
                self.query_layernorm.weight.data,
                bias=None,
                eps=self.rms_norm_eps,
                is_rms_norm=True,
            )
            k = l
// ... (truncated due to length) ...

```
