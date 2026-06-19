---
id: doc-torch-npu-npu-ffn
title: "torch_npu.npu_ffn — Fused FFN / MoE FFN Operator"
type: source-doc
architectures: [ascend910b]
tags: [torch-npu, ffn, activation, operator, swiglu]
date: '2026-06-19'
url: https://gitcode.com/Ascend/op-plugin/blob/master/docs/context/torch_npu-npu_ffn.md
kernel_types: [activation, matmul]
languages: [python, cpp]
confidence: verified
---

# torch_npu.npu_ffn

Official op-plugin documentation for the fused FFN operator — baseline for MultiKernelBench Level-4 FFN task.

## Source

- Ascend op-plugin: `docs/context/torch_npu-npu_ffn.md`
- URL: https://gitcode.com/Ascend/op-plugin/blob/master/docs/context/torch_npu-npu_ffn.md
- Also: https://www.hiascend.com/document/detail/zh/Pytorch/60RC1/apiref/apilist/ptaoplist_000744.html

## Formula

```
out = activation(x * W1 + b1) * W2 + b2
```

Without `expert_tokens` → standard FFN. With expert grouping → MoE FFN.

## Function Prototype

```python
torch_npu.npu_ffn(
    x, weight1, weight2, activation, *,
    expert_tokens=None, expert_tokens_index=None,
    bias1=None, bias2=None,
    scale=None, offset=None,
    deq_scale1=None, deq_scale2=None,
    antiquant_scale1=None, antiquant_scale2=None,
    antiquant_offset1=None, antiquant_offset2=None,
    inner_precise=None, output_dtype=None
) -> Tensor
```

## Supported Activations

`fastgelu`, `gelu`, `relu`, `silu`, `geglu`, `swiglu`, `reglu`

## Tensor Shapes

| Tensor | Shape (no expert) | Shape (MoE) | dtype |
|--------|-------------------|-------------|-------|
| x | [M, K1] (2–8D) | same | fp16, bf16, int8 |
| weight1 | [K1, N1] | [E, K1, N1] | fp16, bf16, int8 |
| weight2 | [K2, N2] | [E, K2, N2] | fp16, bf16, int8 |

Notation: M = tokens (BS), K1/N1/K2/N2 = matmul dims, E = experts.

## inner_precise (Official Rules)

| Value | Meaning | Applies to |
|-------|---------|------------|
| 0 | High precision — internal FP32 compute | fp16 only |
| 1 | High performance — internal FP16 compute | fp16 only |

- **bf16** non-quant: must use `inner_precise=0`
- **fp16** non-quant: 0 or 1
- **int8** quant / pseudo-quant: 0 and 1 configurable but **ignored**

## Shape Constraints (Official)

**Gated activations (geglu/swiglu/reglu)**:
- No expert grouping only for fp16 high-performance
- Requires **N1 = 2 * K2**

**Non-gated (gelu/fastgelu/relu/silu)**:
- Expert and non-expert; fp16/bf16/quant/pseudo-quant
- Requires **N1 = K2**

**All scenarios**:
- K1 = N2
- K1 < 65536, K2 < 65536
- M-axis after 32-byte alignment < int32 max

## Performance Note (Official)

For geglu/swiglu/reglu: FFN fusion is only recommended when vector ops in decomposed FFN exceed **30µs and 10%+ of network time** — otherwise fusion may not help. Community issue (cann-ops-adv IAM35G) reports npu_ffn ≈ decomposed matmul+silu at some shapes on 910B.

## Supported Products

- Atlas A2 训练/推理 (910B)
- Atlas A3 训练/推理
