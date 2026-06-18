---
id: technique-pr-vllm-ascend-700
title: "PR Insight: vllm-project/vllm-ascend #700"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/700"
---

# PR Insight: vllm-project/vllm-ascend #700

**Title:** Add LoRA & Multi-LoRA support for V0.7.3 dev by Cherry Pick

## Overview
This PR is a cherry-pick of LoRA and Multi-LoRA support (from #521) for the v0.7.3 release. Implementation includes punica_npu.py (346 lines) and model runner/worker modifications.

## Technical Significance
Brings LoRA feature parity to v0.7.3, enabling efficient model fine-tuning and multi-adapter serving on the release branch. Follows RFC #396 and roadmap #448.

## Related
- technique-lora
- technique-multi-lora