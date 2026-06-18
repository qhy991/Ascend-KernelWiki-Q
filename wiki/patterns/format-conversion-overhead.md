---
id: pattern-format-conversion-overhead
title: "Format-Conversion Overhead — Excess ND<->NZ Transposes"
type: wiki-pattern
architectures: [ascend910, ascend910b]
tags: [format-conversion, nz-format, diagnosis, performance, pattern]
confidence: source-reported
symptoms: ["repeated ND->NZ conversion every step", "Vector unit busy transposing not computing", "weights re-converted each forward pass", "high MTE traffic for layout change"]
techniques: [format-conversion, nz-tiling]
related: [technique-format-conversion, hw-nz-format, pattern-nz-format-traps]
sources: [blog-nz-format-explained, doc-catlass-framework, pr-vllm-ascend-002]
---

# Format-Conversion Overhead Pattern

The Cube unit only consumes data in `FRACTAL_NZ` layout, so every matmul implies a layout change from the row-major `ND` tensors that frameworks hand over. When that conversion is paid *repeatedly* — re-transposing the same weights on every forward pass, or round-tripping NZ→ND→NZ between fused Cube ops — the Vector and MTE pipes spend cycles shuffling bytes instead of feeding compute. Reported overhead lands in the 10-15% range and can climb higher in inference loops where weights are static but converted anyway.

## Diagnostic Flowchart

```text
matmul kernel slower than its theoretical Cube bound
            │
            ▼
   msprof: do TransData / format ops appear in the timeline?
            │
      ┌─────┴─────┐
     NO          YES
      │            │
      ▼            ▼
 look elsewhere   Is the Vector pipe busy on
 (see pattern-     transpose while Cube is idle?
  pipeline-stall)        │
                   ┌─────┴─────┐
                  NO          YES
                   │            │
                   ▼            ▼
            one-time boundary   FORMAT-CONVERSION OVERHEAD
            conversion (OK)            │
                                       ▼
                   Are weights/activations re-converted
                   on every step (not persisted in NZ)?
                          │
                    ┌─────┴─────┐
                   YES          NO
                    │            │
                    ▼            ▼
            Persist NZ at load   Keep NZ across fused
            (skip per-step       Cube ops; pick op
             TransData)          variants that take NZ
```

## Diagnostic Symptoms (via msprof)

- **`TransData` ops dominate the timeline**: layout-conversion ops appear once per step, sometimes once per layer, rather than only at kernel boundaries.
- **Vector pipe busy transposing, not computing**: the Vector queue is saturated with format work while the Cube queue shows gaps waiting for its NZ inputs.
- **Weights re-converted each forward pass**: in inference, the same static weight tensor is converted from `ND` to `FRACTAL_NZ` on every call.
- **High MTE traffic for layout change**: extra `DataCopy` traffic that exists only to move data through the conversion, not to do useful compute.

## Root Causes

### 1. Per-Step Weight Conversion

A framework stores weights in `ND`. If the operator converts them to `FRACTAL_NZ` inside the hot path, that cost is paid on every invocation even though the weights never change. This is the single most common and most wasteful source of overhead because it is pure repetition.

### 2. Round-Tripping Between Fused Cube Ops

When two Cube operations are chained (for example, two GEMMs in an MLP block), an intermediate that is written back to `ND` only to be re-converted to `NZ` for the next GEMM pays the conversion twice. Each `NZ → ND → NZ` round trip burns Vector/MTE cycles with zero compute value.

### 3. Op Variants That Only Accept ND

Selecting a kernel variant whose interface expects `ND` forces an implicit conversion at the call site even when an NZ-native variant exists. The cost is hidden inside the operator wrapper and easy to miss in profiling unless you look for `TransData`.

## Solutions

### Persist Weights in NZ at Load Time

Convert each weight tensor to `FRACTAL_NZ` once, at model/weight load, and keep the NZ buffer resident for the lifetime of the model. Every subsequent forward pass reads the already-converted buffer, eliminating per-step `TransData` entirely. This is the approach taken in `pr-vllm-ascend-002`, which pre-converts and caches weights in NZ so the inference loop never re-transposes static parameters.

```cpp
// At weight load (run once), not in the hot path:
// nd_weight is the framework's row-major ND tensor.
// Convert to FRACTAL_NZ and keep the NZ buffer resident.
TransData(nz_weight_gm, nd_weight_gm, /*srcFormat=*/ND,
          /*dstFormat=*/FRACTAL_NZ, M, N);

// Hot path (per forward pass): read the persisted NZ buffer directly.
// No TransData here — the Cube op consumes nz_weight_gm as-is.
DataCopy(nz_weight_ub, nz_weight_gm, tileSize);   // MTE load, NZ already
Matmul(nz_act_ub, nz_weight_ub, nz_out_ub, M, N, K);
```

### Keep Data in NZ Across Fused Cube Ops

When chaining Cube operations, leave the intermediate in `FRACTAL_NZ` so the next GEMM consumes it without re-conversion. Only convert back to `ND` at the *final* boundary where a non-Cube consumer (or the framework) needs row-major output.

```cpp
// Two chained GEMMs (e.g. MLP up- then down-projection).
// Keep the intermediate in NZ — do NOT round-trip to ND.
Matmul(nz_x_ub, nz_w1_ub, nz_h_ub, M, H, K);   // h stays in FRACTAL_NZ
Matmul(nz_h_ub, nz_w2_ub, nz_y_ub, M, N, H);   // consumes NZ directly

// Convert ONCE, only at the output boundary:
TransData(nd_y_gm, nz_y_ub, /*srcFormat=*/FRACTAL_NZ,
          /*dstFormat=*/ND, M, N);
```

### Choose Op Variants That Accept NZ

Where the operator library offers an NZ-native entry point, call it directly with NZ inputs rather than the `ND` variant that hides a conversion. This keeps the layout change out of the hot path entirely. See `technique-format-conversion` for the conversion-placement guidance and `hw-nz-format` for why the Cube unit mandates the `FRACTAL_NZ` block layout in the first place.

## Cost Comparison

| Strategy | Per-step `TransData` | Vector pipe load | Notes |
|---|---|---|---|
| Convert weights every step | Yes (per pass) | High (transpose-bound) | Worst case; pure repetition |
| `NZ → ND → NZ` between fused ops | Yes (×2 per chain) | High | Wasted round trips |
| Persist NZ weights at load | No | Low | `pr-vllm-ascend-002` approach |
| Keep NZ across fused Cube ops | Convert once at output | Low | Only boundary conversion remains |

Reported format-conversion overhead is roughly **10-15% or more** of kernel time when conversions sit in the hot path; persisting NZ and avoiding round trips drives that toward the one-time boundary cost.

## Trade-offs and Pitfalls

- **Memory footprint**: a resident NZ weight buffer costs extra device memory (the `FRACTAL_NZ` block layout carries padding overhead — see `pattern-nz-format-traps`). For large models this is a real budget item; the savings only pay off when the weights are reused across many steps.
- **Don't over-eagerly persist transient data**: persisting NZ makes sense for *static* tensors (weights). Activations that change every step still need conversion at their producer; the win there is avoiding *round trips*, not caching.
- **Boundary correctness**: when you stop round-tripping to `ND`, make sure every downstream consumer between the Cube ops genuinely accepts `FRACTAL_NZ`. A silent ND-vs-NZ mismatch produces wrong output with no error — this failure mode is detailed in `pattern-nz-format-traps`.
- **Alignment still applies**: keeping data in NZ does not remove the 16× dimension-alignment requirement of the Cube unit; padding rules from `pattern-nz-format-traps` and `hw-nz-format` still hold.
- **Profile to confirm**: always verify with msprof that `TransData` has actually left the hot path after the change — an op variant can re-introduce a hidden conversion.

## Related Patterns

- [Format Conversion](technique-format-conversion) — where to place ND<->NZ conversions and their cost model
- [NZ Format](hw-nz-format) — why the Cube unit requires `FRACTAL_NZ` and the block layout details
- [NZ Format Traps](pattern-nz-format-traps) — alignment, silent mismatch, and memory-overhead pitfalls
