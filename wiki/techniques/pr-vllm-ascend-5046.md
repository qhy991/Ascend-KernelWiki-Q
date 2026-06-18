---
id: technique-pr-vllm-ascend-5046
title: "PR Insight: vllm-project/vllm-ascend #5046"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseekv3
  - fia
  - async-scheduling
  - mtp
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5046"
---

# PR Insight: vllm-project/vllm-ascend #5046

**Title:** [Bugfix]fix dsv3.1 FIA err in async_scheduling with mtp

## Overview
This PR fixes errors in DeepSeekV3.1 FIA when using async_scheduling with MTP. In large EP scenes with async_scheduling enabled, the MTP module enters eagle mode, causing mismatch in seq_lens_list and block_table. The fix adds proper judgment before draft model forward.

## Technical Significance
Resolves mode switching issues between MTP and Eagle speculative decoding when using async scheduling with large expert parallelism, ensuring correct metadata handling.

## Related
- `kernel-deepseekv3`
- `kernel-fia`
- `technique-async-scheduling`
- `technique-mtp`
- `kernel-eagle-proposer`