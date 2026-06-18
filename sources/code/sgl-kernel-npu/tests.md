---
id: code-sgl-kernel-npu-tests
title: SGL Kernel NPU Tests
type: source-code
repo: sgl-project/sgl-kernel-npu
path: tests
url: https://github.com/sgl-project/sgl-kernel-npu/tree/main/tests
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- sglang
- tests
- npu
- inference
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- global-memory
techniques:
- pipeline-scheduling
- online-softmax
kernel_types:
- attention
- matmul
- softmax
- layernorm
languages:
- python
---

# SGL Kernel NPU Tests

SGL Kernel NPU test source. This is executable evidence for kernel correctness and backend integration around production NPU inference kernels.

## Code Location

- Repository: `sgl-project/sgl-kernel-npu`
- Path: `tests`
- URL: https://github.com/sgl-project/sgl-kernel-npu/tree/main/tests


## Fetched Source


### `tests/python/deepep/test_fused_deep_moe.py`
```python
import argparse
import os
import random
import sys
import time
from functools import partial

import torch
import torch.distributed as dist
import torch_npu
from deep_ep import Buffer
from utils import bench_kineto, calc_diff, hash_tensor, init_dist

torch_npu.npu.config.allow_internal_format = True

GMM_TILE_N_DIM = 64


# ======================== Weight Initialization ========================
def init_base_weights(
    num_local_experts,
    hidden_in=7168,
    moe_intermediate_size=4096,
):
    """
    Initialize the weights for each local expert.
    `num_local_experts`: Number of experts per rank = `num_experts` // `num_ranks`
    `hidden_in`: Input dimension (default 7168)
    `moe_intermediate_size`: Intermediate moe layer dimension (default 4096)
    """
    hidden_out = moe_intermediate_size // 2
    w13_weight = torch.randint(
        -16, 16, [num_local_experts, moe_intermediate_size, hidden_in], dtype=torch.int8
    )
    w2_weight = torch.randint(
        -16, 16, [num_local_experts, hidden_in, hidden_out], dtype=torch.int8
    )

    w13_weight_scale = (
        torch.rand([num_local_experts, moe_intermediate_size, 1]) * 0.0004 + 0.0015
    ).float()
    w2_weight_scale = (
        torch.rand([num_local_experts, hidden_in, 1]) * 0.0004 + 0.0015
    ).float()

    return w13_weight, w13_weight_scale, w2_weight, w2_weight_scale


def init_baseline_weights(w13_weight, w13_weight_scale, w2_weight, w2_weight_scale):

    w13_weight = w13_weight.data.transpose(1, 2).contiguous()
    w2_weight = w2_weight.data.transpose(1, 2).contiguous()
    w13_weight_scale = w13_weight_scale.data.squeeze(-1).contiguous()
    w2_weight_scale = w2_weight_scale.data.squeeze(-1).contiguous()
    # baseline store as nz
    w13_weight = torch_npu.npu_format_cast(w13_weight, 29)
    w2_weight = torch_npu.npu_format_cast(w2_weight, 29)

    return w13_weight, w13_weight_scale, w2_weight, w2_weight_scale


# ======================== Weight Permutation & Fusion ========================
def permute_weight(w: torch.Tensor, tile_n):

    *dims, n = w.shape
    order = list(range(len(dims))) + [-2, -3, -1]
    return (
        w.reshape(*dims, 2, n // tile_n, tile_n // 2)
        .permute(order)
        .reshape(*dims, n)
        .contiguous()
    )


def reshape_fusion_gmm_weight(weight, dim):
    original_shape = weight.shape
    if dim < 0:
        dim += len(original_shape)

    weight = weight.view(
        *original_shape[:dim], 2, -1, GMM_TILE_N_DIM, *original_shape[dim + 1 :]
    )
    weight = weight.transpose(dim, dim + 1).contiguous()
    weight = weight.view(*original_shape[:dim], -1, *original_shape[dim + 1 :])

    return weight.contiguous()


def init_fused_weights_int8(
    w13_weight,
    w13_weight_scale,
    w2_weight,
    w2_weight_scale,
    device="npu",
    block_m: int = 16,
    block_n: int = 16,
):

    # -------- w13_weight --------
    w13 = w13_weight.transpose(1, 2).contiguous()
    torch_npu.npu_format_cast_(w13, 2)
    cpu_w13 = w13.cpu()
    w13 = reshape_fusion_gmm_weight(cpu_w13, -1).npu()
    torch_npu.npu_format_cast_(w13, 29)
    w13_int8_nz = torch.nn.Parameter(w13, requires_grad=False)

    # -------- w2_weight --------
    w2 = torch_npu.npu_format_cast(w2_weight, 29)
    w2_int8_nz = torch.nn.Parameter(w2, requires_grad=False)

    # -------- w13_weight_scale --------
    w13_scale = permute_weight(w13_weight_scale.squeeze(-1).contiguous(), 128)
    w13_scale_o = torch.nn.Parameter(w13_scale, requires_grad=False)

    # -------- w2_weight_scale --------
    w2_scale = w2_weight_scale.squeeze(-1).contiguous()
    w2_scale_o = torch.nn.Parameter(w2_scale, requires_grad=False)

    return w13_int8_nz, w13_scale_o, w2_int8_nz, w2_scale_o


# ======================== Utility Functions ========================
def make_uniform_topk_idx(
    num_tokens: int, num_experts: int, num_ranks: int, num_topk: int, device="npu"
):
    assert num_experts % num_ranks == 0, "num_experts must be divisible by num_ranks"
    experts_per_rank = num_experts // num_ranks

    topk_idx = torch.full((num_tokens, num_topk), -1, dtype=torch.int64, device=device)

    for t in range(num_tokens):
        for k in range(num_topk):
            rank_id = (t * num_topk + k) % num_ranks
            expert_base = rank_id * experts_per_rank
            expert_id = expert_base + ((t + k) % experts_per_rank)
            topk_idx[t, k] = expert_id
    return topk_idx


def from_inclusive_prefix_sum(pref):
    if isinstance(pref, torch.Tensor):
        if pref.numel() == 0:
            return pref
        return torch.cat([pref[:1], pref[1:] - pref[:-1]])

    if not pref:
        return []
    out = [pref[0]]
    for i in range(1, len(pref)):
        out.append(pref[i] - pref[i - 1])
    return out


# ======================== Baseline Reference ========================
def baseline_test(
    buffer,
    x,
    topk_idx,
    num_tokens,
    num_experts,
    cumulative_local_expert_recv_stats,
    return_recv_hook,
    w13,
   
// ... (truncated due to length) ...

```

### `tests/python/deepep/test_combine.py`
```python
import argparse
import os
import random

import deep_ep
import torch
import torch.distributed as dist
import torch_npu
from utils import calc_diff, init_dist, per_token_cast_back


def generate_base_inputs(args: argparse.Namespace, rank: int, num_ranks: int):
    num_tokens = args.num_tokens
    hidden = args.hidden
    num_topk = args.num_topk
    num_experts = args.num_experts

    assert num_experts % num_ranks == 0
    experts_per_rank = num_experts // num_ranks
    scores = (
        torch.randn((num_tokens, num_experts), dtype=torch.float32, device="npu").abs()
        + 1
    )
    topk_idx = torch.topk(scores, num_topk, dim=-1, largest=True, sorted=False)[1]

    return {
        "num_tokens": num_tokens,
        "hidden": hidden,
        "num_topk": num_topk,
        "num_experts": num_experts,
        "experts_per_rank": experts_per_rank,
        "topk_idx": topk_idx,
    }


def generate_normal_combine_inputs(args: argparse.Namespace, rank: int, num_ranks: int):
    base_inputs = generate_base_inputs(args, rank, num_ranks)

    topk_weights = (
        torch.ones(
            (base_inputs["num_tokens"], base_inputs["num_topk"]),
            dtype=torch.float32,
            device="npu",
        )
        * rank
    )

    x = (
        torch.ones(
            (base_inputs["num_tokens"], base_inputs["hidden"]),
            dtype=torch.bfloat16,
            device="npu",
        )
        * rank
    )

    aligned_num_tokens = base_inputs["num_tokens"]

    return {
        "x": x,
        "topk_idx": base_inputs["topk_idx"],
        "topk_weights": topk_weights,
        "aligned_num_tokens": aligned_num_tokens,
        "num_tokens": base_inputs["num_tokens"],
        "hidden": base_inputs["hidden"],
        "num_experts": base_inputs["num_experts"],
    }


def generate_low_latency_combine_inputs(
    args: argparse.Namespace, rank: int, num_ranks: int
):
    base_inputs = generate_base_inputs(args, rank, num_ranks)
    num_tokens = base_inputs["num_tokens"]
    hidden = base_inputs["hidden"]
    num_topk = base_inputs["num_topk"]

    topk_weights = torch.randn(
        (num_tokens, num_topk), dtype=torch.float32, device="npu"
    ).abs()

    # Offset rank by 128 to test negative values in bfloat16 tensor
    # Constraint: num_ranks must be < 385 (128 + 257) to keep values in valid range
    rank_offset = 128
    assert (
        num_ranks - rank_offset < 257
    ), "Too many ranks (exceeding bfloat16 precision limit)"
    x = torch.ones((num_tokens, hidden), dtype=torch.bfloat16, device="npu") * (
        rank - rank_offset
    )
    x[:, -128:] = torch.arange(num_tokens, device="npu").to(torch.bfloat16).view(-1, 1)
    local_tokens_tensor = torch.tensor([num_tokens], dtype=torch.int32, device="npu")
    dist.all_reduce(local_tokens_tensor, op=dist.ReduceOp.MAX)
    aligned_num_tokens = local_tokens_tensor.item()

    return {
        "x": x,
        "topk_idx": base_inputs["topk_idx"],
        "topk_weights": topk_weights,
        "aligned_num_tokens": aligned_num_tokens,
        "num_tokens": num_tokens,
        "hidden": hidden,
        "num_experts": base_inputs["num_experts"],
    }


def test_only_normal_combine(
    args: argparse.Namespace,
    rank: int,
    num_ranks: int,
    buffer: deep_ep.Buffer,
    group: dist.ProcessGroup,
):
    print(f"[Rank {rank}] Starting PURE combine test (normal)...", flush=True)

    inputs = generate_normal_combine_inputs(args, rank, num_ranks)
    config = deep_ep.Config(24, 8, 256)

    (
        ref_num_tokens_per_rank,
        send_token_idx,
        ref_num_tokens_per_expert,
        ref_is_token_in_rank,
        _,
    ) = buffer.get_dispatch_layout(inputs["topk_idx"], inputs["num_experts"])

    dispatch_args = {
        "x": inputs["x"],
        "num_tokens_per_rank": ref_num_tokens_per_rank,
        "is_token_in_rank": ref_is_token_in_rank,
        "num_tokens_per_expert": ref_num_tokens_per_expert,
        "config": config,
        "topk_idx": inputs["topk_idx"],
        "topk_weights": inputs["topk_weights"],
    }
    recv_x, _, _, _, handle, _ = buffer.dispatch(**dispatch_args)
    recv_x = per_token_cast_back(*recv_x) if isinstance(recv_x, tuple) else recv_x

    combine_args = {
        "x": recv_x,
        "handle": handle,
        "config": config,
        "async_finish": False,
        "topk_weights": handle[7],
    }
    combined_x, _, _ = buffer.combine(**combine_args)
    check_x = combined_x.float()

    diff = calc_diff(
        check_x,
        inputs["x"]
        * handle[7].masked_fill(inputs["topk_idx"] == -1, 0).sum(dim=1).view(-1, 1),
    )
    assert diff < 5e-5, f"Combine diff too large: {diff}"

    print(f"[Rank {rank}] Normal combine test PASSED (diff: {diff:.6f})")


def test_only_low_latency_combine(
    args: argparse.Namespace,
    rank: int,
    num_ranks: int,
    buffer: deep_ep.Buffer,
    group: dist.ProcessGroup,
    inputs: dict,
):
    print(f"[Rank {rank}] Starting PURE combine test (low latency)...", flus
// ... (truncated due to length) ...

```

### `tests/python/deepep/test_dispatch_ffn_combine.py`
```python
import argparse
import os
import random
import sys
import time
from functools import partial

import torch
import torch.distributed as dist
import torch_npu
from deep_ep import Buffer
from utils import bench_kineto, calc_diff, hash_tensor, init_dist

torch_npu.npu.config.allow_internal_format = True

GMM_TILE_N_DIM = 64


# ======================== Weight Initialization ========================
def init_base_weights(
    num_local_experts,
    hidden_in=7168,
    moe_intermediate_size=4096,
):
    """
    Initialize the weights for each local expert.
    `num_local_experts`: Number of experts per rank = `num_experts` // `num_ranks`
    `hidden_in`: Input dimension (default 7168)
    `moe_intermediate_size`: Intermediate moe layer dimension (default 4096)
    """
    hidden_out = moe_intermediate_size // 2
    w13_weight = torch.randint(
        -16, 16, [num_local_experts, moe_intermediate_size, hidden_in], dtype=torch.int8
    )
    w2_weight = torch.randint(
        -16, 16, [num_local_experts, hidden_in, hidden_out], dtype=torch.int8
    )

    w13_weight_scale = (
        torch.rand([num_local_experts, moe_intermediate_size, 1]) * 0.0004 + 0.0015
    ).float()
    w2_weight_scale = (
        torch.rand([num_local_experts, hidden_in, 1]) * 0.0004 + 0.0015
    ).float()

    return w13_weight, w13_weight_scale, w2_weight, w2_weight_scale


def init_baseline_weights(w13_weight, w13_weight_scale, w2_weight, w2_weight_scale):
    w13_weight = w13_weight.data.transpose(1, 2).contiguous()
    w2_weight = w2_weight.data.transpose(1, 2).contiguous()
    w13_weight_scale = w13_weight_scale.data.squeeze(-1).contiguous()
    w2_weight_scale = w2_weight_scale.data.squeeze(-1).contiguous()
    # baseline store as nz
    w13_weight = torch_npu.npu_format_cast(w13_weight, 29)
    w2_weight = torch_npu.npu_format_cast(w2_weight, 29)

    return w13_weight, w13_weight_scale, w2_weight, w2_weight_scale


def scale_from_float_to_int64(scale):
    """Convert float32 scale to int64 representation."""
    import numpy as np

    scale = torch.from_numpy(
        np.frombuffer(
            scale.cpu().to(torch.float32).numpy().tobytes(), dtype=np.int32
        ).astype(np.int64)
    ).to(scale.device)
    return torch.nn.Parameter(scale, requires_grad=False)


def init_fused2_weights_int8(w13_weight, w13_weight_scale, w2_weight, w2_weight_scale):
    w13_weight = w13_weight.data.transpose(1, 2).contiguous()
    w2_weight = w2_weight.data.transpose(1, 2).contiguous()
    # baseline store as nz
    w13_weight = torch_npu.npu_format_cast(w13_weight, 29)
    w2_weight = torch_npu.npu_format_cast(w2_weight, 29)

    w13_int8_nz = torch.nn.Parameter(w13_weight, requires_grad=False)
    w2_int8_nz = torch.nn.Parameter(w2_weight, requires_grad=False)
    w13_scale_o = scale_from_float_to_int64(
        w13_weight_scale.data.squeeze(-1).contiguous()
    )
    w2_scale_o = scale_from_float_to_int64(
        w2_weight_scale.data.squeeze(-1).contiguous()
    )

    return w13_int8_nz, w13_scale_o, w2_int8_nz, w2_scale_o


# ======================== Utility Functions ========================
def make_uniform_topk_idx(
    num_tokens: int, num_experts: int, num_ranks: int, num_topk: int, device="npu"
):
    assert num_experts % num_ranks == 0, "num_experts must be divisible by num_ranks"
    experts_per_rank = num_experts // num_ranks

    topk_idx = torch.full((num_tokens, num_topk), -1, dtype=torch.int64, device=device)

    for t in range(num_tokens):
        for k in range(num_topk):
            rank_id = (t * num_topk + k) % num_ranks
            expert_base = rank_id * experts_per_rank
            expert_id = expert_base + ((t + k) % experts_per_rank)
            topk_idx[t, k] = expert_id
    return topk_idx


def from_inclusive_prefix_sum(pref):
    if isinstance(pref, torch.Tensor):
        if pref.numel() == 0:
            return pref
        return torch.cat([pref[:1], pref[1:] - pref[:-1]])

    if not pref:
        return []
    out = [pref[0]]
    for i in range(1, len(pref)):
        out.append(pref[i] - pref[i - 1])
    return out


# ======================== Baseline Reference ========================
def baseline_test(
    buffer,
    x,
    topk_idx,
    num_max_dispatch_tokens_per_rank,
    num_experts,
    cumulative_local_expert_recv_stats,
    return_recv_hook,
    w13,
    w13_scale,
    w2,
    w2_scale,
    topk_weights,
):
    hidden_states, packed_recv_count, handle, _, _ = buffer.low_latency_dispatch(
        x,
        topk_idx,
        num_max_dispatch_tokens_per_rank,
        num_experts,
        cumulative_local_expert_recv_stats=cumulative_local_expert_recv_stats,
        use_fp8=True,
        async_finish=not return_recv_hook,
        return_recv_hook=return_recv_hook,
    )
    output_dtype = torch.bfloat16
    group_list_type = 1

    per_token_scale = hidden_states[1]
    hidden_states = hidden_states[0]

    group_list = packed_recv_count.to(torch.int64)

    # gmm1: gate_up_proj
    hidden_states = to
// ... (truncated due to length) ...

```
