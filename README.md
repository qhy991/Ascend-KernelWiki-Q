# Ascend-KernelWiki-Q

Knowledge base for Huawei Ascend NPU kernel optimization, covering AICore hardware, AscendC programming, and CUDA→AscendC migration.

## Structure

```
Ascend-KernelWiki-Q/
├── data/           # Schema and controlled vocabulary
│   ├── schemas.yaml      # 9 page type definitions
│   ├── tags.yaml         # Ascend-specific controlled vocabulary
│   ├── aliases.yaml      # Term alias mappings
│   └── refresh-cutoff.yaml
├── sources/        # Raw data (docs, blogs, PRs)
│   ├── docs/             # Official documentation (17)
│   ├── blogs/            # Community posts and tutorials (9)
│   └── prs/              # PR analysis (7: ascend-pytorch, ascend-samples, sgl-kernel-npu, vllm-ascend, catlass)
├── wiki/           # Synthesized knowledge
│   ├── hardware/         # Hardware features (Cube, Vector, Scalar, UB, L1/L0, MTE, NZ, HCCS)
│   ├── techniques/       # Optimization techniques
│   ├── kernels/          # Kernel case studies (AscendC, TIK, aclnn, CATLASS)
│   ├── languages/        # Programming guides (AscendC, TIK, aclnn, AscendCL, torch_npu, MindSpore, TBE)
│   ├── migration/        # CUDA/Triton/CUTLASS → Ascend migration guides
│   └── patterns/         # Problem→solution diagnosis patterns
├── queries/        # Auto-generated indices
├── scripts/        # Tooling
│   ├── validate.py       # Schema validation
│   ├── generate-indices.py  # Index generation
│   └── query.py          # Knowledge base search
└── CLAUDE.md       # Agent reference (schema + query guide)
```

## Quick Start

```bash
# Validate all pages
python3 scripts/validate.py

# Generate query indices
python3 scripts/generate-indices.py

# Search the knowledge base
python3 scripts/query.py "cube unit matrix"
python3 scripts/query.py --type kernel
python3 scripts/query.py --technique pipeline-scheduling
```

## Coverage

| Category | Count | Key Topics |
|----------|-------|------------|
| Hardware | 10 | Cube, Vector, Scalar units, UB, L1/L0, MTE, NZ format, Instruction queues, HCCS, Memory hierarchy |
| Techniques | 15 | Pipeline scheduling, Double buffering, NZ tiling, Cube/Vector overlap, Format conversion, Bank conflicts, Data reuse, HCCL, Tiling strategy, Online softmax, Atomic accumulation, Workspace mgmt, KV-cache paging, Tensor-parallel overlap, INT8 quant |
| Kernels | 19 | Matmul, Grouped/CATLASS GEMM, Flash & Paged Attention, Softmax, MoE, Layer/RMSNorm, RoPE, SwiGLU, Top-K, Quant matmul (W8A8), Reduction, Elementwise/Embedding/Conv, TIK add, aclnn add |
| Patterns | 7 | Memory-bound, Low Cube util, NZ traps, Pipeline stall, Host-dispatch-bound, Format-conversion overhead, Tiling too small |
| Languages | 7 | AscendC, TBE-DSL, TIK (Python), aclnn (C++), AscendCL host (C/C++), PyTorch torch_npu, MindSpore |
| Migration | 9 | CUDA→AscendC, Memory mapping, API equivalents, Triton→AscendC, TBE→AscendC, CUTLASS→Catlass, CUDA runtime→AscendCL, cuBLAS/cuDNN→aclnn, PyTorch CUDA→NPU |
| Sources | 33 | Official docs (17) + Community blogs (9) + PR sources (7: ascend-pytorch, ascend-samples, sgl-kernel-npu, vllm-ascend ×2, catlass) |
| **Total** | **100** | **All 9 page types populated, 0 validation errors / 0 warnings** |

### Languages covered (operator authoring + host orchestration)

| Language | Pages | Representative content |
|----------|-------|------------------------|
| AscendC (C/C++ kernel) | 28 | Matmul, attention, norms, RoPE, SwiGLU, quant matmul |
| Python (`torch_npu`, MindSpore, TIK, vLLM) | 12 | torch_npu custom ops, MindSpore AOT, W8A8, paged attention |
| C++ host (aclnn, AscendCL, CATLASS) | 11 | Two-phase aclnn calls, ACL runtime, template GEMM |
| TIK (low-level Python) | 3 | Vector add & softmax operators, TIK API reference |
| TBE-DSL (deprecated) | 1 | Legacy high-level DSL |

## Architecture Mapping (CUDA → Ascend)

| CUDA | Ascend | Notes |
|------|--------|-------|
| Tensor Core | Cube Unit | Matrix multiply, requires NZ format |
| CUDA Core | Vector Unit | SIMD operations |
| Shared Memory | Unified Buffer | ~1-2 MB per AICore |
| PTX ISA | CCE Instructions | Not publicly documented |
| CUDA C++ | AscendC | C/C++ based, pipeline model |
| CUTLASS | Catlass | Modular GEMM framework |
| NCCL | HCCL | Collective communication |
| Nsight | msprof | Profiling |

## Dependencies

- Python 3.8+
- PyYAML >= 6.0
