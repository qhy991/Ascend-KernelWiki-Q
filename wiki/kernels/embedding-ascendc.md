---
id: kernel-embedding-ascendc
title: "Embedding Lookup on Ascend NPU"
type: wiki-kernel
architectures: [ascend910, ascend910b]
tags: [embedding, lookup, gather, ascendc]
confidence: inferred
kernel_types: [embedding]
languages: [ascendc]
related: [kernel-matmul-ascendc, technique-data-reuse]
sources: [doc-ascendc-api-reference]
reproducibility: concept
techniques: [data-reuse]
---

# Embedding Lookup on Ascend NPU

## Overview

Embedding lookup is a fundamental operation in natural language processing, where dense vector representations are retrieved from a learned embedding table based on discrete token indices. This operation appears in language models, recommendation systems, and classification tasks. On Ascend NPU, embedding lookup is implemented using gather operations optimized for sparse access patterns.

## Mathematical Formulation

Given an embedding table W ∈ R^(V×D) where V is vocabulary size and D is embedding dimension, and indices I ∈ Z^N, the embedding lookup produces:

```
E = W[I]  # Shape: [N, D]
```

where E[i] = W[I[i]] retrieves the i-th embedding vector.

## Ascend NPU Implementation

The Ascend implementation follows a three-stage approach:

**Stage 1: Index Processing**
```ascendc
// Copy indices from GM to UB for efficient access
__gm____int32__* indices;  // [batch_size]
LocalTensor<int32_t> indices_ub = BufferPool::Alloc();
DataCopy(indices_ub, indices, batch_size);
```

**Stage 2: Gather Operation**
```ascendc
// For each index, gather corresponding embedding row
__gm____half__* embedding_table;  // [vocab_size, embedding_dim]
LocalTensor<Half> output_ub = BufferPool::Alloc();

for (int i = 0; i < batch_size; ++i) {
    int32_t idx = indices_ub[i];
    // Gather row from embedding table
    DataCopy(output_ub + i * embedding_dim, 
             embedding_table + idx * embedding_dim, 
             embedding_dim);
}
```

**Stage 3: Output Transfer**
```ascendc
// Copy gathered embeddings to GM
__gm____half__* output;  // [batch_size, embedding_dim]
DataCopy(output, output_ub, batch_size * embedding_dim);
```

## Key Optimizations

**Batch Consecutive Indices**: When indices are spatially localized, consecutive DataCopy operations improve memory bandwidth utilization:
```ascendc
// Good: Consecutive indices
indices = [100, 101, 102, 103, 104];

// Less efficient: Strided indices
indices = [100, 5000, 10000, 15000, 20000];
```

**L1 Buffer Caching**: Hot embedding rows can be cached in L1/L2 buffers to reduce GM access:
```ascendc
// Cache frequently accessed embeddings in L1
LocalTensor<Half> l1_cache = BufferPool::Alloc();
// Track cache hits/misses for adaptive caching strategy
```

**DataCopy Coalescing**: Batch multiple embedding lookups into single memory transactions:
```ascendc
// Instead of individual lookups, batch consecutive rows
for (int batch = 0; batch < num_batches; ++batch) {
    int start_idx = indices[batch * batch_size];
    DataCopy(output_ub + batch * batch_size * embedding_dim,
             embedding_table + start_idx * embedding_dim,
             batch_size * embedding_dim);
}
```

## AscendC Implementation Example

```ascendc
extern "C" __global__ void EmbeddingLookupKernel(
    __gm____half__* embedding_table,  // [vocab_size, embedding_dim]
    __gm____int32__* indices,          // [batch_size]
    __gm____half__* output,            // [batch_size, embedding_dim]
    int vocab_size,
    int embedding_dim,
    int batch_size
) {
    LocalTensor<int32_t> indices_ub = BufferPool::Alloc();
    LocalTensor<Half> output_ub = BufferPool::Alloc();
    
    // Copy indices to UB
    DataCopy(indices_ub, indices, batch_size);
    
    // Gather embeddings
    for (int i = 0; i < batch_size; ++i) {
        int32_t idx = indices_ub[i];
        
        // Boundary check
        if (idx >= 0 && idx < vocab_size) {
            // Copy embedding row
            DataCopy(output_ub + i * embedding_dim,
                     embedding_table + idx * embedding_dim,
                     embedding_dim);
        } else {
            // Handle out-of-bounds indices (padding, etc.)
            Muls(output_ub + i * embedding_dim, 0.0_h, embedding_dim);
        }
    }
    
    // Copy output to GM
    DataCopy(output, output_ub, batch_size * embedding_dim);
    
    BufferPool::Dealloc(indices_ub);
    BufferPool::Dealloc(output_ub);
}
```

## Advanced Optimization: Adaptive Caching

For workloads with skewed index distributions, adaptive caching significantly improves performance:

```ascendc
// Frequency-based caching strategy
struct CacheEntry {
    int32_t index;
    LocalTensor<Half> cached_embedding;
    int access_count;
};

// Maintain LRU cache of hot embeddings
LocalTensor<CacheEntry> embedding_cache;
int cache_size = 128;  // Number of cached embeddings

for (int i = 0; i < batch_size; ++i) {
    int32_t idx = indices_ub[i];
    
    // Check cache
    if (is_cached(embedding_cache, idx)) {
        // Cache hit: use cached embedding
        DataCopy(output_ub + i * embedding_dim, 
                 get_cached(embedding_cache, idx),
                 embedding_dim);
    } else {
        // Cache miss: fetch from GM
        DataCopy(output_ub + i * embedding_dim,
                 embedding_table + idx * embedding_dim,
                 embedding_dim);
        
        // Update cache if frequently accessed
        if (should_cache(embedding_cache, idx)) {
            update_cache(embedding_cache, idx, 
                        output_ub + i * embedding_dim,
                        embedding_dim);
        }
    }
}
```

## Performance Characteristics

- **Memory Bandwidth**: Primary bottleneck is GM bandwidth for embedding table access
- **Cache Locality**: Performance improves significantly with index spatial locality
- **Batch Size Benefits**: Larger batch sizes amortize memory access overhead

## Comparison with GPU Implementation

**Similarities**:
- Both use gather-based operations
- Both benefit from index locality
- Both face memory bandwidth constraints

**Differences**:
- **CUDA**: Uses `__ldg()` cache and texture memory for embedding optimization
- **AscendC**: Uses explicit DataCopy with UB buffer management
- **Performance**: Comparable for sequential access, Ascend shows advantages for batched consecutive indices

## Integration with Attention Mechanisms

Embedding lookup is typically followed by attention mechanisms:
```
Indices → Embedding Lookup → Positional Encoding → Attention Layers
```

The embedding kernel output feeds directly into attention computation, making efficient embedding lookup crucial for overall language model performance.

The Ascend embedding implementation demonstrates how sparse gather operations can be optimized through intelligent caching, batching, and buffer management to achieve efficient embedding lookup for large-scale language models.