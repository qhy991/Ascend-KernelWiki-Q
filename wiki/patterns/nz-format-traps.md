---
id: pattern-nz-format-traps
title: "FRACTAL_NZ Format Traps — Common Pitfalls and Solutions"
type: wiki-pattern
architectures: [ascend910, ascend910b]
tags: [nz-format, pitfalls, data-format, diagnosis, pattern]
confidence: inferred
sources: [blog-nz-format-explained, doc-ascend-memory-hierarchy]
symptoms: ["Cube produces garbage output", "Matrix dimensions not aligned to 16", "Unexpected format conversion overhead >15%", "NZ reshape errors"]
techniques: [nz-tiling, format-conversion]
related: [technique-nz-tiling, technique-format-conversion, hw-cube-unit]
---

# FRACTAL_NZ Format Traps

FRACTAL_NZ (also called NZ format) is the mandatory data layout for Ascend's Cube unit matmul operations. This format introduces several non-intuitive behaviors that can cause subtle bugs and performance issues.

## Common Pitfalls

### 1. Dimension Alignment

**Problem**: NZ format requires all matrix dimensions (M, N, K) to be multiples of 16.

**Symptom**: Cube matmul produces incorrect results or runtime errors.

**Solution**: Always pad dimensions to 16× alignment before format conversion:
```ascendc
// Pad M from 512 → 512 (already aligned)
// Pad N from 4096 → 4096 (already aligned)
// Pad K from 128 → 128 (already aligned)
// For K=129, pad to K=144 before NZ conversion
```

### 2. Silent Format Mismatches

**Problem**: Passing ND-format data to Cube matmul without explicit format conversion.

**Symptom**: Cube executes without error but produces completely wrong output (no validation!).

**Solution**: Always use `DataCopy` with format parameter:
```ascendc
DataCopy(ND_input, NZ_output, size, ND_TO_NZ);  // Explicit conversion
Matmul(NZ_A, NZ_B, NZ_C, M, N, K);             // Safe
```

### 3. NZ Reshape Confusion

**Problem**: Assuming NZ 5D layout (C1, H, C0, Ni, No) behaves like simple row-major reshape.

**Reality**: NZ layout includes 16×16 block structure + additional permutation:
- C0 and No are the 16-element block dimensions
- Reshaping requires understanding block-level addressing

**Solution**: Use AscendC's `Reshape` API instead of manual indexing; avoid low-level NZ layout manipulation.

### 4. Memory Overhead

**Problem**: NZ format uses ~1.06× more memory than ND due to block padding.

**Impact**: For large matrices in UB, this can cause allocation failures or force smaller tiles.

**Solution**: Account for NZ expansion in UB budget calculations:
```
UB_required = ceil(M/16) * ceil(N/16) * 256 * sizeof(T)  // 256 = 16×16 block
```

## Diagnostics with msprof

**Low Cube instruction count**: If Cube matmul instruction count is much lower than expected (e.g., 50-100 instructions for a large matmul), suspect format mismatch — the kernel may be operating on wrong memory regions.

**High format conversion overhead**: If `ND_TO_NZ` or `NZ_TO_ND` takes >15% of kernel time, consider keeping data in NZ format throughout pipeline and only converting at boundaries.

## Best Practices

1. **Validate dimensions** before any NZ conversion
2. **Keep data in NZ format** internally; convert only at input/output boundaries
3. **Use NZ-aware tiling** in [NZ Tiling](technique-nz-tiling) pattern
4. **Profile format conversion** separately to identify bottlenecks
5. **Test with small known matrices** to verify correctness before optimization

## Debugging Checklist

- [ ] Are M, N, K all multiples of 16?
- [ ] Did I explicitly call `DataCopy` with format parameter?
- [ ] Does UB budget account for NZ expansion factor?
- [ ] Are reshape operations using AscendC APIs, not manual indexing?
- [ ] Did I verify output with a small test case first?

## Related Patterns

- [NZ Tiling](technique-nz-tiling) — proper tiling strategy for NZ data
- [Format Conversion](technique-format-conversion) — conversion patterns and performance
- [Cube Unit](hw-cube-unit) — hardware requirements and constraints
