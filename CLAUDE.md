# Ascend-KernelWiki-Q — Claude Code Agent Reference

This file provides the schema, navigation, and query reference for agents working with this knowledge base.

## Schema Reference

### Required Frontmatter Fields

Every page must have:

```yaml
---
id: <type-prefix>-<slug>            # Unique ID, matches page type
title: Human-readable title
type: <page-type>                   # source-pr | source-doc | source-blog | wiki-hardware | wiki-technique | wiki-kernel | wiki-pattern | wiki-language | wiki-migration
architectures: [ascend910, ascend910b, ...]  # At least one
tags: [list, of, controlled, tags]  # From data/tags.yaml
confidence: <level>                 # verified | source-reported | inferred | experimental
---
```

### Optional Fields by Type

**source-pr**:
```yaml
repo: org/repo
pr: 1234
author: github-handle
date: 'YYYY-MM-DD'
url: https://gitee.com/...
source_category: upstream-code
techniques: [list]
hardware_features: [list]
kernel_types: [list]
languages: [list]
captured_at: 'YYYY-MM-DD'
status: merged | open | closed
inclusion_reason: "why this PR matters"
```

**wiki-kernel**:
```yaml
kernel_types: [matmul, attention, ...]
languages: [ascendc, ...]
related: [list-of-page-ids]
sources: [list-of-source-ids]
performance_claims:
  - gpu: Ascend 910B
    dtype: fp16
    shape: "M=4096, N=4096, K=4096"
    metric: TFLOPS
    value: 256
    utilization: "~80%"
    source_id: doc-xxx
artifact_dir: artifacts/kernels/<name>
reproducibility: concept | pseudocode | snippet | runnable | benchmarked
```

**wiki-hardware**:
```yaml
hardware_features: [cube-unit, vector-unit, unified-buffer, ...]
related: [list-of-page-ids]
sources: [list-of-source-ids]
cuda_equivalent: <cuda-feature-name>  # For cross-referencing
```

**wiki-migration**:
```yaml
from_concept: <name>
to_concept: <name>
difficulty: easy | moderate | hard
```

## Controlled Vocabulary

See `data/tags.yaml` for the full tag registry. Key dimensions:

- **architectures**: ascend910, ascend910b, ascend310p
- **hardware_features**: cube-unit, vector-unit, scalar-unit, mte, unified-buffer, l1-buffer, global-memory, nd-format, nz-format, hccs, instruction-queue, event-sync
- **techniques**: pipeline-scheduling, double-buffering, nz-tiling, cube-vector-overlap, bank-conflict-avoidance, data-reuse, hccl-optimization, format-conversion
- **kernel_types**: matmul, gemm, attention, flash-attention, moe, softmax, layernorm, elementwise, reduce
- **languages**: ascendc, tbe-dsl, tbe-tik, python, cpp

## Navigation Paths

1. **Problem-based**: `queries/by-problem.md` → symptom → pattern → technique
2. **Technique-based**: `queries/by-technique.md` → technique → related hardware/kernels
3. **Hardware-based**: `queries/by-hardware-feature.md` → feature → techniques that use it
4. **Kernel-based**: `queries/by-kernel-type.md` → kernel → implementations + optimizations
5. **Language-based**: `queries/by-language.md` → language → guides + examples

## Query Examples for Agents

```
# Find how to use Cube unit for matrix multiplication
python3 scripts/query.py "cube unit matrix multiplication"

# Find optimization techniques for memory-bound kernels
python3 scripts/query.py --technique double-buffering --architecture ascend910b

# Find all kernel implementations
python3 scripts/query.py --type kernel

# Find CUDA to AscendC migration guides
python3 scripts/query.py "migration cuda ascendc"

# Find all pages related to NZ format
python3 scripts/query.py --tag nz-format
```

## Data Refresh

```bash
# 1. Generate source pages from new PRs/docs

# 2. Author wiki pages citing sources

# 3. Regenerate indices
python3 scripts/generate-indices.py

# 4. Validate
python3 scripts/validate.py
```
