---
id: technique-pr-vllm-ascend-10307
title: "PR Insight: vllm-project/vllm-ascend #10307"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - speculative-decoding
  - graph-mode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10307"
---

# PR Insight: vllm-project/vllm-ascend #10307

**Title:** [BugFix][SpecDecode] Sanitize MTP placeholders before model forward

## Overview
This PR sanitizes MTP placeholder token IDs before they reach model forward passes. MTP placeholder token IDs (`PLACEHOLDER_TOKEN_ID = -1`) are valid scheduler/sampler metadata, especially on the PD kv-consumer first step, but they must not reach model forward `input_ids` because embedding kernels reject `-1` token IDs. The fix sanitizes only the current forward GPU input buffer after `SpecDecodeMetadata` has been built, replacing `PLACEHOLDER_TOKEN_ID` with token id `0` while preserving the original placeholders in sampler/rejection metadata.

## Technical Significance
This is a critical correctness fix that prevents embedding kernel crashes during MTP graph replay. The approach is safe because it only mutates the GPU input buffer after metadata is built, keeping CPU token history unchanged and preserving the scheduler's placeholder contract. This complements the sampler-side placeholder handling in #10043 and #10259, ensuring placeholders are handled correctly at multiple stages of the speculative decoding pipeline without breaking the scheduling metadata required for proper graph shapes.

## Related
- `technique-mtp`
- `technique-speculative-decoding`
- `technique-graph-mode`