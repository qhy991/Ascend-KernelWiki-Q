---
id: code-vllm-ascend-aclnn-adapter
title: vLLM Ascend aclnn Torch Adapter
type: source-code
repo: vllm-project/vllm-ascend
path: csrc/aclnn_torch_adapter
url: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/aclnn_torch_adapter
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
- aclnn
- torch-adapter
- operator
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- global-memory
- cube-unit
- vector-unit
techniques:
- workspace-management
- format-conversion
kernel_types:
- attention
- matmul
- elementwise
languages:
- cpp
---

# vLLM Ascend aclnn Torch Adapter

vLLM Ascend aclnn Torch adapter source, anchoring code evidence for bridging PyTorch extension calls to CANN aclnn operators and workspace semantics.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `csrc/aclnn_torch_adapter`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/aclnn_torch_adapter
