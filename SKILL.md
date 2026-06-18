---
name: AscendKernelWiki
description: Use when the user asks about optimizing Huawei Ascend NPU kernels — AscendC/AICore programming, Cube/Vector units, NZ format, MTE, pipeline scheduling, Flash/Paged Attention on NPU, aclnn, torch_npu, Catlass, or CUDA→Ascend migration. Do NOT use for generic CUDA/NCU questions unrelated to Ascend.
argument-hint: "[natural-language-question] | [--tag cube-unit --type kernel] | [page-id]"
allowed-tools: "Bash Read Grep Glob"
---

# AscendKernelWiki — Ascend NPU Kernel Optimization Wiki

Query a structured knowledge base of Ascend NPU kernel optimization — hardware features, techniques, kernel case studies, migration guides, and PR references from vllm-ascend, sgl-kernel-npu, catlass, and ascend-samples.

## When To Use This Skill

Trigger when the user asks about:

- **Ascend hardware** — Cube/Vector/Scalar units, UB, L1/L0, MTE, NZ format, HCCS
- **AscendC kernel programming** — pipeline scheduling, tiling, double buffering, format conversion
- **Kernel implementations** — matmul, flash/paged attention, RMSNorm, RoPE, SwiGLU, MoE, quant matmul
- **Languages** — AscendC, TIK, aclnn, AscendCL, torch_npu, MindSpore, Catlass
- **CUDA → Ascend migration** — CUDA runtime→ACL, cuBLAS→aclnn, PyTorch CUDA→NPU, CUTLASS→Catlass
- **Performance patterns** — low Cube utilization, memory-bound, pipeline stalls, host-dispatch-bound, tiling too small
- **PR references** — "how did vllm-ascend/sgl-kernel-npu implement X?"

Do NOT use for NVIDIA CUDA/NCU-specific questions.

## How To Query

All commands run from the skill directory (this `SKILL.md` root).

### Path 1: Unified search (preferred)

```bash
python3 scripts/query.py "how to optimize matmul on Ascend 910B"
python3 scripts/query.py --tag cube-unit --type kernel
python3 scripts/query.py --technique pipeline-scheduling --architecture ascend910b
python3 scripts/query.py --type migration --limit 10
```

Filters: `--type`, `--tag`, `--technique`, `--architecture`, `--limit`, `--verbose`, `--paths-only`.

Type aliases: `hardware`, `technique`, `kernel`, `pattern`, `language`, `migration`, `pr`, `doc`, `blog`.

### Path 2: Fetch a specific page

```bash
python3 scripts/get_page.py kernel-matmul-ascendc
python3 scripts/get_page.py kernel-matmul-ascendc --follow-sources
python3 scripts/get_page.py kernel-matmul-ascendc --body-only
```

### Path 3: Pre-built indices

Auto-generated under `queries/`:

- `queries/by-problem.md` — symptom → pattern → techniques
- `queries/by-technique.md` — optimization techniques
- `queries/by-hardware-feature.md` — hardware features → related pages
- `queries/by-kernel-type.md` — kernel types → pages
- `queries/by-language.md` — language guides
- `queries/by-repo.md` — PR pages by upstream repo

### Path 4: Schema and agent reference

- `CLAUDE.md` — schema, controlled vocabulary, query guide

## Output Pattern

When answering from this KB:

1. **Cite specific pages** with paths (e.g., `wiki/kernels/matmul-ascendc.md`) and IDs.
2. **Follow `sources:` fields** to trace claims back to docs/blogs/PRs.
3. **Respect confidence levels** — `verified` > `source-reported` > `inferred` > `experimental`.
4. **Include code snippets** from wiki pages when available.
5. **Map CUDA concepts** to Ascend equivalents when relevant (Cube≈Tensor Core, UB≈Shared Memory, msprof≈NCU).

## Architecture Mapping (CUDA → Ascend)

| CUDA | Ascend |
|------|--------|
| Tensor Core | Cube Unit |
| CUDA Core | Vector Unit |
| Shared Memory | Unified Buffer |
| CUTLASS | Catlass |
| NCCL | HCCL |
| Nsight (NCU) | msprof |
