---
id: technique-pr-vllm-ascend-3153
title: "PR Insight: vllm-project/vllm-ascend #3153"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - lora
  - logits-processor
  - mro
  - shape-mismatch
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3153"
---

# PR Insight: vllm-project/vllm-ascend #3153

**Title:** [Bugfix][LoRA] Fix forward error and shape mismatch when using LoRA

## Overview
This PR fixes LoRA forward errors and shape mismatches caused by Method Resolution Order (MRO) issues. When LogitsProcessorWithLoRA calls AscendLogitsProcessor.forward by bypassing MRO, the super().forward() call raises errors. The fix directly invokes LogitsProcessor.forward.

## Technical Significance
MRO bypass issues can cause subtle bugs in object-oriented Python code. The fix ensures correct method invocation in the inheritance hierarchy, preventing runtime errors and shape mismatches in LoRA logits processing. This is critical for correct LoRA functionality.

## Related
- `technique-lora`, `pattern-mro-handling`, `kernel-lora-ascendc`