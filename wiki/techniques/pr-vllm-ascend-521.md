---
id: technique-pr-vllm-ascend-521
title: "PR Insight: vllm-project/vllm-ascend #521"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - lora
  - multi-lora
  - fine-tuning
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/521"
---

# PR Insight: vllm-project/vllm-ascend #521

**Title:** [Platform][Worker][ModelRunner] Add LoRA & Multi-LoRA support

## Overview
This PR adds LoRA and Multi-LoRA support following RFC #396 and roadmap #448. Implementation includes punica_npu.py (346 lines), model runner modifications, and worker updates. Enables dynamic LoRA serving via /v1/load_lora_adapter and /v1/unload_lora_adapter APIs.

## Technical Significance
LoRA enables efficient model fine-tuning by adding low-rank adapters. Multi-LoRA support allows serving multiple adapters simultaneously, essential for multi-tenant scenarios. The NPU-specific punica wrapper implements efficient LoRA weight fusion on Ascend.

## Related
- technique-lora
- technique-multi-lora