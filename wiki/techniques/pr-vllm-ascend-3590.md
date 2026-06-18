---
id: technique-pr-vllm-ascend-3590
title: "PR Insight: vllm-project/vllm-ascend #3590"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - torchair
  - deepseek
  - spec-decode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3590"
---

# PR Insight: vllm-project/vllm-ascend #3590

**Title:** [BugFix] Fix torchair+mtp bug after deleting deepseek_mtp.

## Overview
This PR fixes a torchair+MTP bug introduced when deepseek_mtp was deleted in PR #3561. The fix was applied to `vllm_ascend/spec_decode/mtp_proposer.py` and `vllm_ascend/torchair/models/torchair_deepseek_mtp.py`, updating the MTP proposer and DeepSeek-MTP model implementation for torchair compatibility.

## Technical Significance
The deletion of deepseek_mtp left residual dependencies in the torchair path and MTP spec decode logic, causing bugs. This fix ensures torchair's MTP implementation remains functional after the deepseek_mtp removal, demonstrating the complexity of maintaining compatibility across multiple backends and model configurations in vLLM.

## Related
- `technique-mtp`
- `technique-torchair`
- `technique-spec-decode`