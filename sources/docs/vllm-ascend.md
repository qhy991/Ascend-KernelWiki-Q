---
id: doc-vllm-ascend
title: "vLLM Ascend Backend — NPU Inference Plugin"
type: source-doc
architectures: [ascend910b]
tags: [vllm, inference, python, ascendc, paged-attention]
date: '2026-05-12'
url: https://docs.vllm.ai/projects/ascend/en/latest/
hardware_features: [cube-unit, vector-unit, global-memory]
techniques: [pipeline-scheduling]
confidence: source-reported
---

`vllm-ascend` (the `vllm-project/vllm-ascend` repository) is the hardware plugin that brings Ascend NPU support to the vLLM inference engine. Rather than forking vLLM, it registers as an out-of-tree platform plugin and runs the model on top of `torch_npu`, reusing vLLM's scheduler, KV-cache manager, and sampler while swapping in NPU-specific device handling, an attention backend backed by PagedAttention with block KV cache, and a small set of custom AscendC kernels. This page documents the plugin as a source-reported reference: what it provides, how its custom kernels are built, and the trade-offs of running vLLM on Ascend 910B.

## Plugin Model: vLLM on torch_npu

vLLM exposes a platform-plugin extension point so accelerators can register themselves without modifying the core engine. `vllm-ascend` claims that point and routes all device work through `torch_npu`, the PyTorch Ascend adapter (see `doc-torch-npu-adapter`). The engine's Python control plane — request scheduling, continuous batching, paged KV-cache bookkeeping, sampling — runs unchanged; only the model-execution and attention layers are replaced with NPU implementations.

```python
import torch
import torch_npu  # registers the "npu" PrivateUse1 backend
from vllm import LLM, SamplingParams

# vllm-ascend is selected automatically once installed; the model
# graph executes on the NPU through torch_npu.
llm = LLM(model="Qwen/Qwen2.5-7B-Instruct", max_model_len=4096)

params = SamplingParams(temperature=0.7, max_tokens=256)
outputs = llm.generate(["Explain paged attention on Ascend."], params)
print(outputs[0].outputs[0].text)
```

Because the plugin sits on `torch_npu`, dense layers (the GEMMs in attention projections and the MLP) dispatch onto the AICore Cube unit, while normalization, activation, and elementwise work runs on the Vector unit — the same operator surface described in `doc-torch-npu-adapter` and behind `kernel-matmul-ascendc`.

## PagedAttention with Block KV Cache

The attention backend implements PagedAttention: the key/value cache for each sequence is split into fixed-size **blocks**, and a per-sequence block table maps logical positions to physical block indices. Physically, these blocks live in non-contiguous device memory in global memory, so the allocator can hand out and reclaim blocks without ever needing a contiguous KV region per sequence.

This block scheme is what gives PagedAttention its near-optimal memory behavior: because allocation granularity is one block rather than a worst-case-padded contiguous buffer, internal fragmentation is bounded to a partially-filled final block per sequence — reported as under 4% waste. The freed capacity translates directly into a larger batch (more concurrent sequences) and therefore higher throughput.

```text
Logical KV positions (one sequence)      Physical blocks (non-contiguous)
[ tok0 tok1 ... tok15 | tok16 ... ]      block #42  -> [ ... ]   in global memory
        block 0       |   block 1        block #7   -> [ ... ]
                                         block #91  -> [ ... ]
block_table = [42, 7, 91, ...]   # logical block -> physical block index
```

The block table is consulted inside the attention kernel so that the QK^T and AV (Cube-unit) matmuls gather KV from the scattered physical blocks. This is the same algorithmic structure as GPU PagedAttention; on Ascend the gather and the score/output matmuls land on the Cube and Vector units via the NPU attention backend.

| Aspect | Contiguous KV cache | PagedAttention (block KV) |
| --- | --- | --- |
| Physical layout | one contiguous buffer per sequence | fixed-size blocks, non-contiguous |
| Allocation granularity | whole sequence (padded to max) | one block |
| Memory waste | high (padding to max length) | low (< 4%, last block only) |
| Concurrency | limited by padded reservations | more sequences per device |

## Continuous Batching

vLLM's scheduler drives **continuous batching** (a.k.a. in-flight batching): instead of waiting for a whole batch to finish, completed sequences are evicted and newly arrived requests are admitted at the next decode step. Combined with the block KV cache, this keeps the AICore pipeline fed and overlaps the prefill of incoming requests with the decode of in-flight ones — a `pipeline-scheduling` pattern at the request level rather than the instruction level. `vllm-ascend` inherits this scheduler as-is; its job is to make each scheduled forward pass execute efficiently on the NPU.

## Custom AscendC Kernels

Where `torch_npu`'s operator coverage is not sufficient or not optimal for the inference hot path, `vllm-ascend` ships its own AscendC kernels. They are compiled from AscendC source with CMake against the CANN toolkit and bound into PyTorch through the `torch.library` / `TORCH_LIBRARY` mechanism (the same registration path documented in `doc-torch-npu-adapter`), so they appear as ordinary `torch.ops` callables on the `npu` backend.

```cpp
#include <torch/library.h>
#include <tuple>

// AscendC-backed implementations compiled via CMake against CANN.
// RoPE rotates both query and key, so the op returns the two rotated tensors.
std::tuple<at::Tensor, at::Tensor> rotary_embedding_npu(
    /* positions, query, key, cos_sin_cache, ... */);

TORCH_LIBRARY(vllm_ascend, m) {
    m.def("rotary_embedding(Tensor positions, Tensor query, Tensor key, "
          "Tensor cos_sin_cache, int head_size, bool is_neox) -> (Tensor, Tensor)");
}

TORCH_LIBRARY_IMPL(vllm_ascend, PrivateUse1, m) {
    m.impl("rotary_embedding", &rotary_embedding_npu);
}
```

From Python the registered kernel is then reachable through `torch.ops`:

```python
import torch
import torch_npu
import vllm_ascend  # extension exporting the TORCH_LIBRARY bindings

query, key = torch.ops.vllm_ascend.rotary_embedding(
    positions, query, key, cos_sin_cache, head_size=128, is_neox=True
)
```

The notable custom kernels and the PRs that introduced them:

| Kernel | Purpose | PR | Reported result |
| --- | --- | --- | --- |
| `rotary_embedding` | Rotary position embedding (RoPE) | #371 | up to 9.36x / 8.26x vs. the reference path |
| vocab-parallel embedding | Embedding lookup sharded across vocab dim | #796 | — |
| multi-step prepare-input | Build decode inputs for multiple steps at once | #814 | — |

- **`rotary_embedding` (PR #371)** replaces the elementwise RoPE rotation with a fused AscendC kernel, reported at up to 9.36x and 8.26x over the reference implementation. RoPE is applied to query and key every decode step, so cutting its latency directly shortens the per-token critical path.
- **Vocab-parallel embedding (PR #796)** provides an AscendC embedding lookup that matches vLLM's tensor-parallel vocabulary sharding, so each rank only holds and gathers its slice of the embedding table.
- **Multi-step prepare-input (PR #814)** moves the host-side construction of decode inputs into a kernel that prepares several steps in one shot, reducing per-step host overhead that would otherwise stall the NPU between decode iterations.

## NZ Weight Pre-Conversion for MoE

The Ascend Cube unit consumes operands in the fractal `NZ` layout (`ACL_FORMAT_FRACTAL_NZ`) rather than plain `ND`; feeding `ND` weights to a Cube-bound matmul forces an on-the-fly conversion that costs extra memory traffic and latency (the same NZ-vs-ND consideration in `technique-nz-tiling`). For Mixture-of-Experts models the expert weights are large and reused across every token routed to that expert, so `vllm-ascend` pre-converts them once at load time instead of per call. As of PR #2842 the MoE down-projection weight (`w2_weight`) defaults to `NZ`, so the expert GEMMs run directly on the Cube unit without a repeated format conversion in the decode loop.

## npugraph Capture

To cut Python and dispatch overhead on the steady-state decode path, `vllm-ascend` supports graph capture (`npugraph_ex`): the decode forward pass is captured once and replayed as a single graph launch on subsequent steps, analogous to CUDA Graphs on the GPU side. This removes per-op host launch latency, which matters most in the decode phase where each step does little compute but many small launches. Graph capture is best suited to static decode shapes; dynamic-shape or first-token prefill paths typically run eagerly.

## Trade-offs and Pitfalls

- **Plugin/engine/CANN version coupling.** `vllm-ascend` is pinned to specific vLLM, `torch_npu`, and CANN toolkit versions. As with `doc-torch-npu-adapter`, a CANN mismatch usually surfaces as an opaque runtime error at the first NPU op rather than at import. Keep the four-way set (vLLM ↔ plugin ↔ torch_npu ↔ CANN) aligned.
- **Block size is a tuning knob.** Smaller KV blocks reduce last-block waste but enlarge the block table and increase gather bookkeeping; larger blocks do the reverse. The under-4% waste figure assumes a sensibly chosen block size for the sequence-length distribution.
- **Graph capture freezes shapes.** `npugraph` replay assumes the captured shapes; batch size, sequence length, or block-table extents that fall outside the captured set must fall back to eager execution, so a poorly chosen capture set can leave common request shapes un-accelerated.
- **NZ pre-conversion trades memory for speed.** Storing MoE `w2_weight` as `NZ` avoids per-call conversion but the converted layout occupies device memory; on tightly-provisioned 910B deployments this competes with KV-cache capacity (and therefore batch size).
- **Custom kernels need the CANN build chain.** Building the AscendC kernels (`rotary_embedding`, vocab-parallel embedding, prepare-input) requires the CANN toolkit and its CMake config at build time, compiled against the same CANN version as the installed `torch_npu`.
- **Reported speedups are for the kernel, not end-to-end.** The 9.36x / 8.26x figures for `rotary_embedding` (PR #371) are kernel-level comparisons against the reference path, not whole-model throughput; RoPE is one stage of the decode step.

## Related Pages

- `doc-torch-npu-adapter` — the PyTorch Ascend adapter `vllm-ascend` runs on; custom-op registration path.
- `kernel-matmul-ascendc` — Cube-unit matmul behind the attention and MoE projections.
- `technique-nz-tiling` — NZ fractal layout that the MoE weight pre-conversion targets.

## Status

Source-reported from the `vllm-project/vllm-ascend` documentation and pull requests. The plugin runs on `torch_npu`, implements PagedAttention with a fixed-block, non-contiguous KV cache (reported < 4% memory waste), and inherits vLLM continuous batching. Custom AscendC kernels are registered via CMake + `torch.library`: `rotary_embedding` (PR #371, up to 9.36x / 8.26x vs. reference), vocab-parallel embedding (PR #796), and multi-step prepare-input (PR #814). MoE `w2_weight` defaults to `NZ` (PR #2842), and `npugraph_ex` provides decode-path graph capture.
