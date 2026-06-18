---
id: technique-pr-vllm-ascend-8734
title: "PR Insight: vllm-project/vllm-ascend #8734"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - rotary-embedding
  - bugfix
  - yarn
  - mtp
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8734"
---

# PR Insight: vllm-project/vllm-ascend #8734

**Title:** [Ops][BugFix] Fix AttributeError in AscendYaRNRotaryEmbedding

## Overview
This PR fixes an AttributeError in `AscendYaRNRotaryEmbedding` where the `use_mtp` attribute was not initialized during class construction. The issue manifests when `forward_oot` delegates to `AscendRotaryEmbedding.forward_oot`, which expects `self.use_mtp` to be defined. The fix adds initialization of this attribute in the AscendYaRNRotaryEmbedding constructor.

## Technical Significance
This is a correctness fix that prevents runtime crashes when using YaRN (Yet another RoPE extension) rotary embeddings with Ascend optimization. The YaRN extension supports extended context windows by modifying RoPE frequency bases. Proper initialization of the `use_mtp` flag is essential for correct delegation to the base RotaryEmbedding implementation, ensuring that MTP-related optimizations are correctly applied when enabled.

## Related
- `kernel-attention-ascendc`
- `technique-kv-cache-paging`