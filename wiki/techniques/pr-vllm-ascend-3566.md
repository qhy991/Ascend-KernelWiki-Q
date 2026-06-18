---
id: technique-pr-vllm-ascend-3566
title: "PR Insight: vllm-project/vllm-ascend #3566"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - torchair
  - fia
  - kv-cache
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3566"
---

# PR Insight: vllm-project/vllm-ascend #3566

**Title:** [BugFix]Fix mtp torchair bug caused by #2719

## Overview
This PR fixes a MTP (multi-text-prompt) torchair bug introduced by PR #2719. The fix ensures `self.max_num_seqs > self.scheduler_config.max_num_seqs` in the KV consumer when MTP is enabled, because FIA (Flash-Inference-Attention) requires extra space for padding. Changes were made to `vllm_ascend/torchair/torchair_model_runner.py` and `vllm_ascend/worker/model_runner_v1.py`.

## Technical Significance
The bug arose from a mismatch between the configured maximum sequences and the actual padding requirements of FIA operations. FIA's padding needs additional buffer space that wasn't accounted for, causing failures in MTP workloads. This fix ensures the sequence count constraint properly accommodates both scheduler limits and operator padding requirements.

## Related
- `technique-mtp`
- `technique-fia`
- `technique-kv-cache`