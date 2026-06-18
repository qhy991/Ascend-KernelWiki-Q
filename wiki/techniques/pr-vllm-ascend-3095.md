---
id: technique-pr-vllm-ascend-3095
title: "PR Insight: vllm-project/vllm-ascend #3095"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - lora
  - upstream-sync
  - compatibility
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3095"
---

# PR Insight: vllm-project/vllm-ascend #3095

**Title:** [Bugfix][LoRA] Fix bug introduced by upstream vllm#25249

## Overview
This PR fixes a LoRA compatibility issue caused by upstream vLLM PR #25249. The upstream change introduced breaking changes that affected the LoRA implementation in vllm-ascend, requiring fixes to maintain compatibility.

## Technical Significance
Keeping up with upstream vLLM changes is critical for maintaining feature parity and benefiting from community improvements. This fix ensures that LoRA functionality continues to work correctly after upstream changes, preventing service disruption for users relying on LoRA.

## Related
- `technique-lora`, `pattern-upstream-sync`, `kernel-lora-ascendc`