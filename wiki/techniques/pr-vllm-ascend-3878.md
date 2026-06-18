---
id: technique-pr-vllm-ascend-3878
title: "PR Insight: vllm-project/vllm-ascend #3878"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - fullgraph
  - bugfix
  - documentation
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3878"
---

# PR Insight: vllm-project/vllm-ascend #3878

**Title:** bugfix for mtp in fullgraph

## Overview
This PR fixes MTP (multi-text-prompt) bugs in fullgraph mode, including code changes to `vllm_ascend/utils.py` (41 additions, 16 deletions), `vllm_ascend/worker/model_runner_v1.py`, and `vllm_ascend/platform.py`. It also updates documentation for versioning policy, ModelRunner prepare inputs, and supported models.

## Technical Significance
This fix addresses fullgraph mode bugs for MTP, with additional documentation updates ensuring consistency across project documentation. Fullgraph mode requires careful state management, and these fixes ensure correct speculative decoding behavior in compiled graph execution.

## Related
- `technique-mtp`
- `technique-fullgraph`
- `technique-spec-decode`