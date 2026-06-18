---
id: technique-pr-vllm-ascend-10308
title: "PR Insight: vllm-project/vllm-ascend #10308"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/10308"
---

# PR Insight: vllm-project/vllm-ascend #10308

**Title:** [BugFix][v0.20.2rc] Sanitize MTP placeholders before model forward

## Overview
This PR is the `releases/v0.20.2rc` backport of the main-branch MTP placeholder sanitization fix. It sanitizes MTP placeholder token IDs before they reach model forward passes, replacing `PLACEHOLDER_TOKEN_ID` (`-1`) with token id `0` in the GPU input buffer after `SpecDecodeMetadata` is built. This prevents embedding kernel crashes while preserving the original placeholders in sampler/rejection metadata for correct rejection sampling behavior. The backport builds on the sampler-side placeholder handling previously backported in #10259.

## Technical Significance
This backport ensures release branch parity with main branch for MTP correctness in distributed PD scenarios. The fix is critical for preventing embedding kernel crashes during graph replay when placeholder tokens are present. By sanitizing only the GPU input buffer while keeping metadata intact, the approach maintains the scheduler's placeholder contract without breaking graph shapes or rejection sampling logic. This is essential for robust MTP operation on the release branch.

## Related
- `technique-mtp`
- `technique-speculative-decoding`
- `technique-graph-mode`