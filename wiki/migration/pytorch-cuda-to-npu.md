---
id: migration-pytorch-cuda-to-npu
title: "PyTorch CUDA -> NPU — Porting Models with torch_npu"
type: wiki-migration
tags: [pytorch, torch-npu, cuda, migration, python]
confidence: source-reported
sources: [doc-torch-npu-adapter, doc-vllm-ascend, pr-ascend-pytorch-002]
from_concept: "torch.cuda device backend"
to_concept: "torch_npu (PrivateUse1 'npu') backend"
difficulty: easy
related: [lang-pytorch-npu-guide, migration-cuda-to-ascendc]
---

## Overview

Porting a PyTorch model from CUDA to Ascend NPU is one of the *easiest* migrations in this knowledge base: most code runs unchanged once you import `torch_npu` and swap the device string from `"cuda"` to `"npu"`. The `torch_npu` adapter registers Ascend as a PyTorch `PrivateUse1` backend, so `tensor.npu()`, `.to("npu")`, autograd, and the optimizer loop all behave as on CUDA. The remaining work is mechanical: switch the distributed backend from `nccl` to `hccl`, replace a handful of CUDA-specific fused ops (e.g. flash-attention) with their `torch_npu` equivalents, and watch for a few dtype/format pitfalls. For deeper API-by-API coverage see `lang-pytorch-npu-guide`.

## Concept Mapping Table

| CUDA / `torch.cuda` | torch_npu Equivalent | Migration Notes |
|---------------------|----------------------|-----------------|
| `import torch` | `import torch; import torch_npu` | `torch_npu` registers the `npu` device; must be imported before use |
| device string `"cuda"` | device string `"npu"` | Backed by PyTorch `PrivateUse1` dispatch key |
| `tensor.cuda()` | `tensor.npu()` | Same semantics; moves tensor to NPU |
| `x.to("cuda")` / `x.to("cuda:0")` | `x.to("npu")` / `x.to("npu:0")` | Per-card indexing identical |
| `torch.cuda.is_available()` | `torch.npu.is_available()` | Capability probe |
| `torch.cuda.device_count()` | `torch.npu.device_count()` | Card enumeration |
| `torch.cuda.synchronize()` | `torch.npu.synchronize()` | Stream sync |
| `torch.cuda.amp.autocast()` | `torch.npu.amp.autocast()` | Mixed precision; see AMP section |
| `torch.cuda.amp.GradScaler()` | `torch.npu.amp.GradScaler()` | Loss scaling for fp16 |
| dist backend `"nccl"` | dist backend `"hccl"` | Huawei Collective Communication Library |
| `tensor.contiguous()` | `tensor.contiguous()` | Still valid; NPU also has internal formats (see pitfalls) |

## Migration Steps

### Step 1: Import torch_npu

The single most important change. `torch_npu` must be imported (after `torch`) so the `npu` backend, dispatcher kernels, and fused ops are registered:

```python
import torch
import torch_npu  # registers the 'npu' PrivateUse1 backend and op library
```

Nothing else in your model file usually needs to change at import time. From here, `"npu"` is a valid device string everywhere `"cuda"` was.

### Step 2: Replace Device Placement

Swap every `cuda` placement for `npu`. The three common forms:

```python
# Before (CUDA)
model = model.cuda()
x = x.cuda()
y = batch.to("cuda")

# After (NPU)
model = model.npu()
x = x.npu()
y = batch.to("npu")
```

A robust pattern is to define the device once and route everything through it, which keeps the model code device-agnostic:

```python
device = "npu" if torch.npu.is_available() else "cpu"
model = model.to(device)
inputs = inputs.to(device)
```

### Step 3: Switch Automatic Mixed Precision

`torch.cuda.amp` maps directly to `torch.npu.amp`:

```python
# Before (CUDA)
from torch.cuda.amp import autocast, GradScaler
scaler = GradScaler()
with autocast():
    loss = model(x)

# After (NPU)
from torch.npu.amp import autocast, GradScaler
scaler = GradScaler()
with autocast():
    loss = model(x)
```

Ascend NPUs support both fp16 and bf16 autocast. Prefer `bf16` for training stability where the model and ops support it (see pitfalls on bf16 coverage).

### Step 4: Map CUDA-Specific Fused Ops

Generic ops (`matmul`, `softmax`, `layernorm`, elementwise) dispatch automatically and need no change. CUDA-*specific* fused kernels — most notably `flash-attn` — have no CUDA binary on NPU and must be replaced with `torch_npu` fused ops:

```python
# Before (CUDA): flash-attn package
from flash_attn import flash_attn_func
out = flash_attn_func(q, k, v, causal=True)

# After (NPU): torch_npu fused attention
out = torch_npu.npu_fusion_attention(
    q, k, v,
    head_num,
    input_layout="BNSD",
    scale=1.0 / math.sqrt(head_dim),
    sparse_mode=1,  # causal
)[0]
```

Other common substitutions for transformer / LLM models:

```python
# RMSNorm: replace a hand-written normalize with the fused op
hidden = torch_npu.npu_rms_norm(hidden, weight, epsilon=1e-6)[0]

# Rotary position embedding
q = torch_npu.npu_rotary_mul(q, cos, sin)

# Quantized matmul (W8A8 / int8) — see pr-ascend-pytorch-002
out = torch_npu.npu_quant_matmul(x_int8, weight_int8, scale=scale, bias=bias)
```

### Step 5: Switch the Distributed Backend

For multi-card / multi-node training and inference, replace the NCCL backend with HCCL:

```python
# Before (CUDA)
torch.distributed.init_process_group(backend="nccl")

# After (NPU)
import torch
import torch_npu
torch.distributed.init_process_group(backend="hccl")
torch.npu.set_device(local_rank)
```

Collective calls (`all_reduce`, `broadcast`, `all_gather`, etc.) keep the same PyTorch API; only the backend string changes. Frameworks such as vLLM (`doc-vllm-ascend`) wire `hccl` in for you when run on Ascend.

## Op Substitution Quick Reference

| CUDA-specific op | torch_npu replacement | Used for |
|------------------|-----------------------|----------|
| `flash_attn_func` (flash-attn) | `torch_npu.npu_fusion_attention` | Fused scaled-dot-product attention |
| custom / fused RMSNorm | `torch_npu.npu_rms_norm` | LLM normalization |
| rotary embedding (custom kernel) | `torch_npu.npu_rotary_mul` | RoPE position encoding |
| int8 / W8A8 GEMM (custom) | `torch_npu.npu_quant_matmul` | Quantized linear layers |
| `nccl` collective backend | `hccl` collective backend | Distributed all-reduce / gather |

## Trade-offs, Pitfalls, and Notes

- **Unsupported ops fall back to CPU.** If an operator has no NPU kernel, PyTorch may silently execute it on CPU, inserting device-to-host copies and crushing throughput. Profile and check for unexpected `aten::*` CPU fallbacks; replace the offending op with a `torch_npu` fused equivalent or restructure the model.
- **bf16 coverage is not universal.** While both fp16 and bf16 autocast are supported, individual fused ops may support only a subset of dtypes. Verify that `npu_fusion_attention`, `npu_rms_norm`, etc. accept your chosen dtype before assuming parity with the CUDA path.
- **Contiguity and internal format.** Beyond the standard `contiguous()` contract, Ascend tensors may carry an internal hardware layout (the ND vs NZ distinction discussed in `migration-cuda-to-ascendc`). Some ops require contiguous ND inputs; an unexpected format can trigger an implicit conversion or a fallback. When in doubt, call `.contiguous()` before a fused op.
- **Import order matters.** `torch_npu` must be imported after `torch` and before any `npu` device use, or the backend will not be registered and `"npu"` will be rejected.
- **Quantization path.** `npu_quant_matmul` (per `pr-ascend-pytorch-002`) expects pre-quantized int8 weights/activations plus a scale; it is not a drop-in for a plain fp16 `matmul`. Quantize weights offline and supply matching `scale`/`bias`.
- **`.cuda()` literals hide in third-party code.** Search the whole tree (including config files and dependencies you vendor) for hard-coded `"cuda"` strings and `.cuda()` calls; a single missed literal forces a tensor onto a non-existent CUDA device and raises at runtime.

## Before / After: Minimal Training Loop

```python
# ---------- Before (CUDA) ----------
import torch
from torch.cuda.amp import autocast, GradScaler

device = "cuda"
model = MyModel().to(device)
scaler = GradScaler()
torch.distributed.init_process_group(backend="nccl")

for x, target in loader:
    x, target = x.to(device), target.to(device)
    with autocast():
        loss = model(x, target)
    scaler.scale(loss).backward()
    scaler.step(optimizer); scaler.update()

# ---------- After (NPU) ----------
import torch
import torch_npu                       # 1. register npu backend
from torch.npu.amp import autocast, GradScaler   # 3. npu AMP

device = "npu"                          # 2. device swap
model = MyModel().to(device)
scaler = GradScaler()
torch.distributed.init_process_group(backend="hccl")  # 5. nccl -> hccl

for x, target in loader:
    x, target = x.to(device), target.to(device)
    with autocast():                    # bf16/fp16 on NPU
        loss = model(x, target)
    scaler.scale(loss).backward()
    scaler.step(optimizer); scaler.update()
```

The diff is four lines for a vanilla model. The effort scales only with how many CUDA-specific fused kernels (Step 4) the model relies on.

## Reference

- `lang-pytorch-npu-guide` — full torch_npu API surface, supported ops, and dtype coverage
- `migration-cuda-to-ascendc` — when you need to drop below the framework and write a custom kernel
- `doc-vllm-ascend` — serving LLMs on Ascend with HCCL and `npu_fusion_attention`
- `pr-ascend-pytorch-002` — quantized matmul (`npu_quant_matmul`) support
