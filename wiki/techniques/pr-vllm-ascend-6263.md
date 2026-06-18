---
id: technique-pr-vllm-ascend-6263
title: "PR Insight: vllm-project/vllm-ascend #6263"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - eplb
  - w4a8
  - moe
  - quantization
  - fused-mc2
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6263"
---

# PR Insight: vllm-project/vllm-ascend #6263

**Title:** [EPLB][Feature] EPLB Support w4a8

## Overview
This PR adds W4A8 quantization support to the EPLB (Expert Parallel Load Balancer) system for MoE models. The implementation extends the EPLB adaptor and quantization methods to handle W4A8 quantized weights, with the constraint that this feature must be used together with `VLLM_ASCEND_ENABLE_FUSED_MC2=1` because GMM does not support tensor list weight inputs. The changes affect the EPLB adaptor, MoE MLP implementation, W4A8 quantization methods, and model runner.

## Technical Significance
This feature enables EPLB to work with W4A8 quantized MoE models, expanding the quantization options for expert parallel inference. The key constraint is that fused MC2 (MoE Combine) must be enabled, as the GMM operator cannot handle tensor list weight inputs. This limitation is documented for users, ensuring they configure the system correctly. Testing on models like dsv4, qwen3.5, and kimi2.5 confirmed functionality, providing users with more quantization flexibility for large MoE deployments while maintaining performance through the fused operator requirement.

## Related
- `technique-eplb`, `technique-w4a8`, `technique-moe`, `technique-quantization`, `technique-fused-mc2`