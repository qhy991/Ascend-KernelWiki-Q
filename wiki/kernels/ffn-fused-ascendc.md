---
id: kernel-ffn-fused-ascendc
title: "AscendC FFN Fused Kernel — Dual GEMM + Activation"
type: wiki-kernel
architectures: [ascend910b]
tags: [ffn, swiglu, matmul, activation, cube-unit, vector-unit, ascendc]
confidence: source-reported
kernel_types: [matmul, activation, swiglu]
languages: [ascendc, cpp]
sources: [doc-torch-npu-npu-ffn, doc-ascendc-fused-operator-matmul, doc-ascend-operator-fusion, kernel-swiglu-ascendc, kernel-matmul-ascendc]
related: [kernel-swiglu-ascendc, kernel-matmul-ascendc, lang-ascendc-direct-launch-project, technique-ascendc-multi-dtype, technique-workspace-management]
techniques: [pipeline-scheduling, cube-vector-overlap, data-reuse, workspace-management, operator-fusion]
reproducibility: snippet
operator_recipe:
  operator: ffn
  dtype: [fp16, bf16, fp32]
  layout: [ND]
  shape_class: [decode-small-m, prefill-large-m]
  memory_path:
    global_memory: [x, weight1, weight2, bias1, bias2, output]
    onchip_buffers: [UB, L1, L0A, L0B, L0C]
  parallelism:
    granularity: token tiles over M, split N for GEMM1/GEMM2
    block_dim: AI Cube core count
    sync_scope: per-core independent tiles
  instruction_family: [Matmul, Sigmoid, Mul, Add]
  library_backend: [AscendC Matmul, MultiCoreMatmulTiling]
  tiling:
    tile_axes: [M, N, K]
    tile_granularity: L1 blocks sized to UB budget
    constraints: [N-multiple-of-16-for-cube, UB-capacity]
  pipeline:
    stages: [GEMM1, Activation, GEMM2]
    queues: [MTE, Cube, Vector]
    overlap: activation in Vector while next GEMM1 tile loads
  aicore_mapping:
    block_dim: GetBlockNum()
    scheduling: GetBlockIdx() partitions M dimension
  data_movement:
    apis: [DataCopy, DataCopyPad, LoadData]
    path: "GM -> UB/L1 -> L0 -> UB (activation) -> L0 -> GM"
  compute_path:
    units: [Cube Unit, Vector Unit]
    primitives: [Matmul, Sigmoid, Mul, Add, Relu, Tanh]
---

# AscendC FFN Fused Kernel — Dual GEMM + Activation

Feed-Forward Network (FFN) computes:

```
hidden = activation(x @ W1 + b1)
output = hidden @ W2 + b2
```

For gated activations (SwiGLU, GeGLU, ReGLU), `W1` output width is `2N` and activation splits into gate/up halves. This page documents the **end-to-end fused implementation** path beyond the SwiGLU-only snippet in kernel-swiglu-ascendc.

## Baseline Reference (MKB Level 4)

MultiKernelBench FFN task (`2_ffn`) baseline calls fused aclnn op documented in **doc-torch-npu-npu-ffn**:

```python
torch_npu.npu_ffn(x, weight1, weight2, activation,
                  bias1=bias1, bias2=bias2, inner_precise=inner_precise)
```

**Official formula**: `out = activation(x * W1 + b1) * W2 + b2`

Activations: `fastgelu`, `gelu`, `relu`, `silu`, `geglu`, `swiglu`, `reglu`.

### Official Shape Constraints (doc-torch-npu-npu-ffn)

| Activation type | N1 vs K2 | Expert | dtype notes |
|-----------------|----------|--------|-------------|
| geglu/swiglu/reglu | **N1 = 2 × K2** | No expert only (fp16 high-perf) | Gated: weight1 width doubles |
| gelu/fastgelu/relu/silu | **N1 = K2** | Expert or non-expert | fp16/bf16/quant supported |
| All | K1 = N2; K1,K2 < 65536 | — | M-axis 32B-aligned < int32 max |

**Performance caveat (official)**: For geglu/swiglu/reglu, fused `npu_ffn` is only recommended when decomposed vector ops exceed **30µs and 10%+ network time**. Community benchmarks (cann-ops-adv IAM35G) show npu_ffn ≈ manual matmul+silu at some 910B shapes — custom kernel must beat this fused baseline, not unfused matmul chain.

To beat baseline (>1.0x speedup), a custom AscendC kernel must fuse GEMM1 → activation → GEMM2 with minimal GM round-trips.

## Architecture: Three-Phase Pipeline

```
Phase 1 (Cube):  GEMM1  —  x[M,K1] @ W1[K1,N1] → hidden_pre[N1]
Phase 2 (Vector): Act    —  activation(hidden_pre) → hidden[N2]  (N2 = N1 or N1/2 for gated)
Phase 3 (Cube):  GEMM2  —  hidden[M,N2] @ W2[N2,K2] → out[M,K2]
```

| Phase | Unit | UB residency |
|-------|------|--------------|
| GEMM1 | Cube | Tile of x, W1 in L1/L0; partial sum in L0C |
| Activation | Vector | hidden_pre tile in UB; output overwrites or new buffer |
| GEMM2 | Cube | hidden tile + W2 in L1/L0 |

**Fusion win**: keep `hidden` in UB between phase 2 and 3 for the current tile — avoid GM write/read.

## MultiCoreMatmulTiling Setup

Official fusion-operator guide (doc-ascendc-fused-operator-matmul, MatmulLeakyRelu sample):

Host-side tiling before kernel launch:

```cpp
#include "matmul/matmul_intf.h"
#include "platform/platform_ascendc.h"

using namespace matmul;

auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
matmul_tiling::MultiCoreMatmulTiling cubeTiling(ascendcPlatform);

cubeTiling.SetAType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND,
                   matmul_tiling::DataType::DT_FLOAT16);
cubeTiling.SetBType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND,
                   matmul_tiling::DataType::DT_FLOAT16);
cubeTiling.SetCType(matmul_tiling::TPosition::LCM, matmul_tiling::CubeFormat::ND,
                   matmul_tiling::DataType::DT_FLOAT);
cubeTiling.SetBiasType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND,
                       matmul_tiling::DataType::DT_FLOAT);
cubeTiling.SetShape(M, N, K);
cubeTiling.SetOrgShape(M, N, K);

TCubeTiling gemm1Tiling;
if (cubeTiling.GetTiling(gemm1Tiling) == -1) {
    return ge::GRAPH_FAILED;  // tiling failed
}
```

For FFN, run tiling twice (GEMM1: M×N1×K1; GEMM2: M×K2×N2). In MIX mode (Cube+Vector), call `SetDim()` per official multi-core rules.

**Kernel workspace**: non-custom-op direct-launch projects must call `SetSysWorkSpace()` before Matmul init (official fusion guide).

## Device Kernel Skeleton

```cpp
template <typename T, ActivationType ACT>
class FFNKernel {
public:
    __aicore__ inline void Init(GM_ADDR x, GM_ADDR w1, GM_ADDR w2, GM_ADDR out,
                                GM_ADDR bias1, GM_ADDR bias2,
                                FFNTilingData tiling)
    {
        blockIdx = GetBlockIdx();
        // SetGlobalBuffer with block offset: M_block = M / blockDim
        pipe.InitBuffer(/* queues sized from tiling */);
        matmulObj1.SetTensorA(/* ... */);
        matmulObj1.SetTensorB(/* ... */);
    }

    __aicore__ inline void Process()
    {
        for (int mTile = 0; mTile < mTileCount; ++mTile) {
            // --- GEMM1 ---
            CopyInXW1(mTile);
            matmulObj1.template IterateAll<false>(/* ... */);
            LocalTensor<T> hiddenPre = /* L0C -> UB */;

            // --- Activation (Vector) ---
            ApplyActivation<T, ACT>(hiddenPre, hidden, tileLen);

            // --- GEMM2 ---
            matmulObj2.SetTensorA(hidden);
            CopyInW2(mTile);
            matmulObj2.template IterateAll<false>(/* ... */);
            CopyOut(mTile);
        }
    }
private:
    TPipe pipe;
    MatmulImpl<T> matmulObj1, matmulObj2;
    int blockIdx;
};
```

## Seven Activation Implementations (Vector Unit)

| Activation | Formula | Vector ops |
|------------|---------|------------|
| `relu` | `max(0, x)` | `Maxs`, `Relu` |
| `silu` | `x * sigmoid(x)` | `Sigmoid`, `Mul` |
| `gelu` | `x * Φ(x)` | `Erf` or polynomial approx + `Mul` |
| `fastgelu` | tanh-based approx | `Tanh`, `Mul`, `Adds` |
| `swiglu` | `silu(gate) * up` | Split `[M, 2N]` → gate/up; see below |
| `geglu` | `gelu(gate) * up` | Split + GELU on gate |
| `reglu` | `relu(gate) * up` | Split + ReLU on gate |

### SwiGLU Split + Gate (Critical Path)

```cpp
template <typename T>
__aicore__ inline void SwiGLU(LocalTensor<T>& in_2n, LocalTensor<T>& out_n, int halfLen)
{
    // in_2n layout: [gate_0..gate_{H-1}, up_0..up_{H-1}] per row tile
    LocalTensor<T> gate = in_2n[0];           // first H elements
    LocalTensor<T> up   = in_2n[halfLen];      // second H elements

    LocalTensor<T> sig = /* temp UB */;
    Sigmoid(sig, gate, halfLen);
    Mul(gate, gate, sig, halfLen);              // silu(gate) in-place
    Mul(out_n, gate, up, halfLen);             // silu(gate) * up
}
```

For row-major `[M, 2N]` input, use offset `DataCopy` to load gate/up halves separately (see kernel-swiglu-ascendc).

## Multi-Core Task Assignment

```cpp
int64_t blockIdx = AscendC::GetBlockIdx();
int64_t blockNum = AscendC::GetBlockNum();  // set at launch: <<<blockDim, ...>>>

int64_t mPerBlock = (M + blockNum - 1) / blockNum;
int64_t mStart = blockIdx * mPerBlock;
int64_t mEnd   = min(mStart + mPerBlock, M);
int64_t mLocal = mEnd - mStart;

// Offset GM pointers
xGm.SetGlobalBuffer((__gm__ T*)x + mStart * K1, mLocal * K1);
```

**Small M (decode, M < 128)**: use fewer blocks to avoid launch overhead; assign multiple m-tiles per core sequentially.

**Large M (prefill)**: maximize `blockDim = min(coreNum, ceil(M / MIN_M_PER_CORE))`.

## UB Memory Budget

```
UB_total ≈ 192 KB – 256 KB (910B, query via PlatformAscendCManager)

Budget allocation:
  GEMM1 ping-pong A/B tiles:  2 × tileM × tileK × sizeof(T)
  GEMM1 output (hidden_pre):   tileM × tileN1 × sizeof(T)
  Activation temps:            tileM × tileN1 × sizeof(T)  (sigmoid buffer)
  GEMM2 B tile:                tileN2 × tileK2 × sizeof(T)

Constraint: sum ≤ UB_total × 0.9 (leave headroom for queue metadata)
```

If OOM: reduce `tileM`, split activation across more passes, or spill hidden to GM (loses fusion benefit).

See **pattern-ub-oom** for diagnosis.

## pybind Entry for MKB

```cpp
torch::Tensor ffn(const torch::Tensor& x,
                  const torch::Tensor& weight1,
                  const torch::Tensor& weight2,
                  const std::string& activation)
{
    // 1. Validate shapes: x[M,K1], w1[K1,N1], w2[N2,K2]
    // 2. calc_ffn_tiling(M, K1, N1, N2, K2)
    // 3. Dispatch activation enum + dtype
    // 4. launch_ffn_kernel<<<blockDim, nullptr, stream>>>(...)
}
```

For first correctness pass, wrap `torch_npu.npu_ffn` in C++ binding; replace with fused AscendC for performance iteration.

## Performance Targets

| Scenario | Strategy | Expected vs npu_ffn |
|----------|----------|---------------------|
| M < 128 (decode) | Single-core or few blocks; fuse all 3 phases | Hard — launch overhead dominates |
| M ≥ 1024 | Full multi-core GEMM tiling + UB-resident activation | 1.0–1.3x achievable |
| Gated (swiglu) | Must fuse split+gate in Vector — unfused 3x GM traffic | Largest fusion win |

## Related Pages

- **kernel-swiglu-ascendc** — Vector-only SwiGLU fusion detail
- **kernel-matmul-ascendc** — Cube GEMM / Catlass patterns
- **technique-ascendc-multi-dtype** — fp16/bf16/fp32 dispatch
- **lang-ascendc-direct-launch-project** — build integration
- **pattern-ascend-performance-decision-tree** — when to fuse vs call aclnn
