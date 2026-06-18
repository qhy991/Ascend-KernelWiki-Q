---
id: code-vllm-ascend-fused-gdn-gating
title: vLLM Ascend Fused GDN Gating Operator
type: source-code
repo: vllm-project/vllm-ascend
path: csrc/attention/fused_gdn_gating
url: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/attention/fused_gdn_gating
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
- fused-op
- gating
- attention
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- vector-unit
- unified-buffer
- global-memory
techniques:
- data-reuse
- pipeline-scheduling
kernel_types:
- attention
- activation
- elementwise
languages:
- cpp
- ascendc
---

# vLLM Ascend Fused GDN Gating Operator

vLLM Ascend fused gating operator source that combines attention-adjacent activation and gating work in a custom NPU kernel.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `csrc/attention/fused_gdn_gating`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/attention/fused_gdn_gating
