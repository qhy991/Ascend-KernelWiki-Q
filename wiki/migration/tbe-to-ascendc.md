---
id: migration-tbe-to-ascendc
title: "TBE (DSL/TIK) → AscendC Migration Guide"
type: wiki-migration
tags: [tbe, tbe-dsl, tbe-tik, migration, ascendc]
confidence: source-reported
sources: [doc-cann-architecture-guide, doc-ascendc-api-reference]
from_concept: "TBE Operator"
to_concept: "AscendC Operator"
difficulty: moderate
related: [lang-ascendc-guide, lang-tbe-dsl-guide]
---

# TBE to AscendC Migration Guide

Huawei's recommended migration path from TBE (Tensor Boost Engine) to AscendC involves mapping TBE's DSL and TIK abstractions to AscendC's lower-level APIs. This guide covers both TBE-DSL and TBE-TIK migration paths.

## Background: TBE Variants

### TBE-DSL (Python, TVM-based)
High-level DSL for operator definition, compiled by TVM. Closer to mathematical notation but with performance limitations.

### TBE-TIK (Python, low-level)
Lower-level API with more explicit control. Closer to hardware but still Python-based with runtime overhead.

### AscendC (C/C++)
Recommended replacement: native C++ implementation with direct hardware control, no Python runtime dependency, and better performance.

## API Mapping: TBE-DSL → AscendC

### Tensor Declaration

**TBE-DSL:**
```python
from tbe import tbe
import tvm

# Declare tensor with TVM
a = tvm.placeholder(shape, dtype="float16", name="a")
b = tvm.placeholder(shape, dtype="float16", name="b")
```

**AscendC:**
```cpp
// Declare local tensor in UB
LocalTensor<half> a = ub_allocator.Alloc();
LocalTensor<half> b = ub_allocator.Alloc();
```

- `tvm.placeholder()` → `LocalTensor<T>` with explicit allocator

### Basic Arithmetic Operations

**TBE-DSL:**
```python
# Element-wise addition
c = tbe.vadd(a, b)

# Element-wise multiplication
d = tbe.vmul(a, b)
```

**AscendC:**
```cpp
// Vector unit addition
Add::Compute(a, b, c);

// Vector unit multiplication
Mul::Compute(a, b, d);
```

- `tbe.vadd()` → `Add::Compute()`
- `tbe.vmul()` → `Mul::Compute()`
- `tbe.vsub()` / `tbe.vdiv()` → `Sub::Compute()` / `Div::Compute()`

### Scalar Operations

**TBE-DSL:**
```python
# Tensor-scalar multiplication
c = tbe.vmuls(a, scalar_value)
```

**AscendC:**
```cpp
// Scalar unit operation
Scalar<half> scalar(scalar_value);
Muls::Compute(a, scalar, c);
```

- `tbe.vmuls()` → `Muls::Compute()` with `Scalar<T>`

## API Mapping: TIK → AscendC

### Tensor Operations (TIK)

**TIK:**
```python
from tbe import tik

tik_instance = tik.Tik()
# Declare GM tensor
a_gm = tik_instance.Tensor("float16", (M, N), name="a_gm", scope=tik.scope_gm)
# Declare UB tensor
a_ub = tik_instance.Tensor("float16", (M, N), name="a_ub", scope=tik.scope_ub)
```

**AscendC:**
```cpp
// GM and UB tensors
GM_ADDR a_gm = ...;  // Passed as parameter
LocalTensor<half> a_ub = ub_allocator.Alloc();
```

- `tik.Tensor(scope_gm)` → `GM_ADDR` (raw address)
- `tik.Tensor(scope_ub)` → `LocalTensor<T>` with allocator

### Data Movement

**TIK:**
```python
# GM to UB
tik_instance.data_move(a_ub, a_gm, 0, M, N // 16, 0, 0)
```

**AscendC:**
```cpp
// GM to UB with DataCopy
DataCopy(a_ub, GM_ADDR(a_gm));
```

- `tik_instance.data_move()` → `DataCopy()`
- AscendC automatically handles block size and stride calculations

### Compute Operations

**TIK:**
```python
# Vector addition
tik_instance.vec_add(a_ub, b_ub, c_ub, N)
```

**AscendC:**
```cpp
// Vector unit addition
Add::Compute(a_ub, b_ub, c_ub, N);
```

- `tik.vec_add()` → `Add::Compute()`
- Similar mapping for `tik.vec_mul()`, `tik.vec_sub()`, etc.

## Complete Example: Element-wise Addition

### TBE-DSL Version

```python
from tbe import tbe
import tvm

def elewise_add(a, b):
    """
    TBE-DSL element-wise addition
    """
    # Define computation
    c = tbe.vadd(a, b)

    # Schedule with TVM
    s = tvm.create_schedule(c.op)
    return s
```

### AscendC Version

```cpp
class ElewiseAddKernel {
public:
    __aicore__ void Process(GM_ADDR a_gm, GM_ADDR b_gm, GM_ADDR c_gm,
                           uint32_t total_elements) {
        // Allocate UB buffers
        LocalTensor<half> a_ub = ub_allocator.Alloc();
        LocalTensor<half> b_ub = ub_allocator.Alloc();
        LocalTensor<half> c_ub = ub_allocator.Alloc();

        uint32_t offset = 0;
        while (offset < total_elements) {
            uint32_t block_size = std::min(BLOCK_SIZE, total_elements - offset);

            // Load from GM to UB
            DataCopy(a_ub, GM_ADDR(a_gm + offset * sizeof(half)), block_size);
            DataCopy(b_ub, GM_ADDR(b_gm + offset * sizeof(half)), block_size);

            // Compute on Vector unit
            Add::Compute(a_ub, b_ub, c_ub, block_size);

            // Store result to GM
            DataCopy(GM_ADDR(c_gm + offset * sizeof(half)), c_ub, block_size);

            offset += block_size;
        }
    }
};
```

## Advantages of AscendC Over TBE

### 1. Better Performance
- Native C++ execution without Python runtime overhead
- More precise control over hardware queues (Cube/Vector/MTE)
- Optimized memory access patterns

### 2. Type Safety
- Compile-time type checking with C++ templates
- No dtype mismatches common in Python-based TBE

### 3. No Runtime Dependency
- Operators compiled into standalone binaries
- No need for Python interpreter in production deployment

### 4. Direct Hardware Control
- Explicit management of UB allocation
- Independent Cube and Vector queues for pipeline overlap
- Fine-grained control over MTE operations

## Migration Strategy

### Step 1: Analyze TBE Code
- Identify all tensor operations (TIK) or compute definitions (DSL)
- Map data flow from GM to UB to compute
- Note any special format requirements (e.g., NZ for matmul)

### Step 2: Create AscendC Skeleton
- Define kernel class with `__aicore__ Process()` method
- Set up allocators (UB, NZ, SQC)
- Declare GM input/output addresses

### Step 3: Map Operations
- Replace TBE DSL expressions with AscendC API calls
- Convert TIK tensor ops to Vector/Cube operations
- Add explicit data movement with `DataCopy()`

### Step 4: Optimize Pipeline
- Implement double buffering for memory/compute overlap
- Use independent queues for Cube/Vector concurrency
- Add NZ format handling for Cube operations

### Step 5: Validate
- Unit test with known inputs and outputs
- Profile with msprof for bottlenecks
- Compare performance against original TBE implementation

## Common Migration Patterns

### Reduction Operations

**TBE:**
```python
sum_result = tbe.reduce_sum(input_tensor, axis=0)
```

**AscendC:**
```cpp
LocalTensor<half> sum_result = ReduceSum::Compute(input_tensor, axis);
```

### Matrix Multiplication

**TBE:**
```python
# TBE handles format internally
c = tbe.matmul(a, b)
```

**AscendC:**
```cpp
// Explicit NZ conversion required
LocalTensor<half> a_nz, b_nz;
FormatTransfer::C1ToNZ(a_ub, a_nz);
FormatTransfer::C1ToNZ(b_ub, b_nz);
Matmul::Compute(a_nz, b_nz, c_nz);
FormatTransfer::NZToC1(c_nz, c_ub);
```

## Difficulty Assessment: Moderate

This migration is rated **moderate** because:
- TBE and AscendC share similar conceptual models
- API mapping is mostly straightforward
- Python developers need to learn C++ patterns
- Format conversion (NZ) adds some complexity
- Pipeline overlap patterns need to be added manually

## Related Guides

- [AscendC Language Guide](/lang-ascendc-guide.md)
- [TBE DSL Reference](/lang-tbe-dsl-guide.md)
- [CUDA to AscendC Migration](/migration-cuda-to-ascendc.md) (for cross-platform migration)
