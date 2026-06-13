---
id: migration-triton-to-ascendc
title: "Triton → AscendC Migration Guide"
type: wiki-migration
tags: [triton, migration, ascendc, porting]
confidence: inferred
sources: [doc-ascendc-api-reference, blog-ascendc-programming-guide]
from_concept: "Triton Kernel"
to_concept: "AscendC Kernel"
difficulty: hard
related: [migration-cuda-to-ascendc, lang-ascendc-guide]
---

# Triton to AscendC Migration Guide

Migrating from Triton to AscendC requires understanding both the conceptual mapping between the two programming models and the architectural differences of their target platforms.

## Concept Mapping

### Kernel Entry Point

**Triton:**
```python
@triton.jit
def kernel_fn(x_ptr, y_ptr, OUTPUT_PTR, ...):
```

**AscendC:**
```cpp
class MyKernel {
public:
    __aicore__ void Process(GM_ADDR x, GM_ADDR y, GM_ADDR output) {
        // Kernel implementation
    }
};
```

- `@triton.jit` → AscendC class with `__aicore__ Process()` method
- `tl.program_id()` → `GetBlockIdx()` (AICore ID within the AICore cluster)

### Memory Operations

**Triton:**
```python
# Load from DRAM to SRAM
x = tl.load(x_ptr + offsets)
# Store from SRAM to DRAM
tl.store(output_ptr + offsets, result)
```

**AscendC:**
```cpp
// Load from GM to UB
LocalTensor<T> x_ub = UbAllocator::Alloc();
DataCopy(x_ub, GM_ADDR(x + offset));
// Store from UB to GM
DataCopy(GM_ADDR(output + offset), result_ub);
```

- `tl.load()` → `DataCopy()` (GM → UB)
- `tl.store()` → `DataCopy()` (UB → GM)
- **Key difference**: Triton auto-manages shared memory; AscendC requires explicit UB allocation

### Compute Operations

**Matrix Multiplication**

**Triton:**
```python
# Automatic dot product handling
acc = tl.dot(a_block, b_block, acc)
```

**AscendC:**
```cpp
// Requires NZ format for Cube unit
LocalTensor<T> a_nz, b_nz;
// Convert to NZ first
FormatTransfer::Convert(a_ub, a_nz);
FormatTransfer::Convert(b_ub, b_nz);
// Then compute with Cube
Matmul::Compute(a_nz, b_nz, c_nz);
```

- `tl.dot()` → `Matmul::Compute()` (Cube unit, needs NZ format)
- **Key difference**: Triton has no data format concept; AscendC requires NZ for Cube ops

**Reductions**

**Triton:**
```python
sum_result = tl.sum(tensor, axis=0)
```

**AscendC:**
```cpp
// Vector unit reduction
LocalTensor<T> sum_result = ReduceSum::Compute(tensor, axis);
```

- `tl.sum()` → `ReduceSum()` (Vector unit)
- `tl.max()` / `tl.min()` → `ReduceMax()` / `ReduceMin()`

### Index Generation

**Triton:**
```python
offsets = tl.arange(0, BLOCK_SIZE)
```

**AscendC:**
```cpp
// Compute offsets on Scalar unit
for (int i = 0; i < BLOCK_SIZE; ++i) {
    offset = i * element_size;
}
```

- `tl.arange` → Manual offset computation (Scalar unit)

## Architectural Differences

### Memory Hierarchy

| Concept | Triton (GPU) | AscendC (NPU) |
|---------|--------------|---------------|
| Shared memory | Auto-managed SRAM | Unified Buffer (UB), explicit allocation |
| Global memory | DRAM | Global Memory (GM) |
| Transfer units | LD/ST units | Memory Transfer Engine (MTE) |

### Compute Units

| Concept | Triton (GPU) | AscendC (NPU) |
|---------|--------------|---------------|
| Matrix compute | Tensor cores | Cube unit (requires NZ format) |
| Vector compute | CUDA cores | Vector unit |
| Control | SIMT front-end | Scalar unit |

## Side-by-Side Example: Matrix Multiplication

### Triton Version

```python
@triton.jit
def matmul_kernel(a_ptr, b_ptr, c_ptr, M, N, K, BLOCK_SIZE: tl.constexpr):
    # Get program ID
    pid = tl.program_id(axis=0)

    # Compute block offsets
    a_block_ptr = a_ptr + pid * BLOCK_SIZE * K
    b_block_ptr = b_ptr + pid * BLOCK_SIZE * K

    # Load blocks
    a = tl.load(a_block_ptr)
    b = tl.load(b_block_ptr)

    # Compute matmul
    acc = tl.dot(a, b)

    # Store result
    c_block_ptr = c_ptr + pid * BLOCK_SIZE * N
    tl.store(c_block_ptr, acc)
```

### AscendC Version

```cpp
class MatmulKernel {
public:
    __aicore__ void Process(GM_ADDR a_gm, GM_ADDR b_gm, GM_ADDR c_gm,
                           uint32_t M, uint32_t N, uint32_t K) {
        // Get AICore ID
        uint32_t block_idx = GetBlockIdx();

        // Allocate UB buffers
        LocalTensor<half> a_ub = ub_allocator.Alloc();
        LocalTensor<half> b_ub = ub_allocator.Alloc();
        LocalTensor<half> c_ub = ub_allocator.Alloc();

        // Allocate NZ buffers for Cube
        LocalTensor<half> a_nz = nz_allocator.Alloc();
        LocalTensor<half> b_nz = nz_allocator.Alloc();
        LocalTensor<half> c_nz = nz_allocator.Alloc();

        // Load from GM to UB
        uint32_t a_offset = block_idx * BLOCK_SIZE * K * sizeof(half);
        uint32_t b_offset = block_idx * BLOCK_SIZE * K * sizeof(half);
        DataCopy(a_ub, GM_ADDR(a_gm + a_offset));
        DataCopy(b_ub, GM_ADDR(b_gm + b_offset));

        // Convert to NZ format
        FormatTransfer::C1ToNZ(a_ub, a_nz);
        FormatTransfer::C1ToNZ(b_ub, b_nz);

        // Compute matmul on Cube unit
        Matmul::Compute(a_nz, b_nz, c_nz);

        // Convert back from NZ
        FormatTransfer::NZToC1(c_nz, c_ub);

        // Store result to GM
        uint32_t c_offset = block_idx * BLOCK_SIZE * N * sizeof(half);
        DataCopy(GM_ADDR(c_gm + c_offset), c_ub);
    }
};
```

## Key Takeaways

1. **Explicit memory management**: AscendC requires manual UB allocation and GM↔UB transfers
2. **Data format matters**: Cube operations require NZ format; add conversion steps
3. **Queue-based execution**: Use independent queues for Cube/Vector overlap
4. **Scalar unit for control**: Use Scalar unit for loops and index computation
5. **Hardware awareness**: AscendC exposes NPU-specific units (Cube, Vector, MTE, Scalar)

## Difficulty Assessment: Hard

This migration is rated **hard** because:
- Significant conceptual differences between the programming models
- AscendC exposes hardware architecture more explicitly
- Format conversion requirements add complexity
- Queue-based pipeline programming is new concept for Triton developers

## Related Guides

- [CUDA to AscendC Migration](/migration-cuda-to-ascendc.md)
- [AscendC Language Guide](/lang-ascendc-guide.md)
