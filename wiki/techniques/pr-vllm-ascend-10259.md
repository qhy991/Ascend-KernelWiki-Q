---
id: technique-pr-vllm-ascend-10259
title: "PR Insight: vllm-project/vllm-ascend #10259"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - speculative-decoding
  - sampler
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10259"
---

# PR Insight: vllm-project/vllm-ascend #10259

**Title:** [BugFix][v0.20.2rc] Backport MTP placeholder sampler fix

## Overview
This PR backports the PD kv-consumer MTP placeholder sampling fix from #10043 to the `releases/v0.20.2rc` branch. On the first decode step of the D node in PD scenarios, MTP must keep `PLACEHOLDER_TOKEN_ID` (`-1`) in `spec_token_ids` to preserve the required full-graph decode shape. However, this placeholder value is scheduling metadata, not a real vocabulary token, and the sampler must not use it as an index into target or draft probability tables. The fix rejects placeholder draft tokens directly and uses the recovered token path, avoiding reading probability tables with token id `-1`.

## Technical Significance
This is a critical correctness fix for MTP in distributed PD scenarios. The placeholder token is essential for maintaining correct graph shapes but must be handled carefully to avoid being used as a valid token index. The fix ensures placeholder tokens are rejected during sampling, preventing out-of-bounds access to probability tables in Triton kernels and avoiding Python negative indexing issues. This backport ensures the release branch maintains the same robustness as the main branch for PD kv-consumer MTP workflows.

## Related
- `technique-mtp`
- `technique-speculative-decoding`
- `technique-distributed-inference`