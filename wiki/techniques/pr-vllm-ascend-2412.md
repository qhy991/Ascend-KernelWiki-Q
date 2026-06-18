---
id: technique-pr-vllm-ascend-2412
title: "PR Insight: vllm-project/vllm-ascend #2412"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - configuration
  - v1-scheduler
  - v0.9.1
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2412"
---

# PR Insight: vllm-project/vllm-ascend #2412

**Title:** [0.9.1][BUGFIX] fix mtp config bug

## Overview
This PR removes validation checks that prevented MTP from working with V1 scheduler, since MTP now supports V1 scheduler. The change removes 16 lines from `vllm_ascend/ascend_config.py` and 4 lines from `vllm_ascend/worker/mtp_proposer_v1.py`.

## Technical Significance
This cleanup removes outdated validation code that was blocking MTP functionality with V1 scheduler. After the V1 scheduler support was added in PR #2371, these validation checks became unnecessary and were preventing valid configurations. The fix ensures MTP can be used with V1 scheduler as intended.

## Related
- `technique-speculative-decoding`, `technique-v1-scheduler`, `technique-configuration-cleanup`, `kernel-mla-v1`