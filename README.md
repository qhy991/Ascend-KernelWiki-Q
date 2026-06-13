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
│   ├── docs/             # Official documentation
│   ├── blogs/            # Community posts and tutorials
│   └── prs/              # PR analysis (future)
├── wiki/           # Synthesized knowledge
│   ├── hardware/         # Hardware features (Cube, Vector, UB, ...)
│   ├── techniques/       # Optimization patterns
│   ├── kernels/          # Kernel case studies
│   ├── languages/        # Programming guides (AscendC, TBE)
│   ├── migration/        # CUDA→AscendC migration guides
│   └── patterns/         # Problem→solution patterns (future)
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
| Hardware | 5 | Cube unit, Vector unit, UB, Memory hierarchy, Instruction queues |
| Techniques | 8 | Pipeline scheduling, Double buffering, NZ tiling, Cube/Vector overlap, Format conversion, Bank conflicts, Data reuse, HCCL |
| Kernels | 10 | Matmul, Grouped GEMM, Flash Attention, Softmax, MoE, LayerNorm/RMSNorm, Reduction, Elementwise, Embedding, Conv |
| Patterns | 4 | Memory-bound, Low Cube utilization, NZ format traps, Pipeline stall |
| Languages | 2 | AscendC guide, TBE-DSL (deprecated) |
| Migration | 6 | CUDA→AscendC, Memory mapping, API equivalents, Triton→AscendC, TBE→AscendC, CUTLASS→Catlass |
| Sources | 18 | Official docs (10) + Community blogs (5) + PR sources (3) |
| **Total** | **53** | **All 9 page types populated, 0 validation errors** |

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
