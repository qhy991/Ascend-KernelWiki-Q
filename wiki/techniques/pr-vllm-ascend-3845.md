---
id: technique-pr-vllm-ascend-3845
title: "PR Insight: vllm-project/vllm-ascend #3845"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - fullgraph
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3845"
---

# PR Insight: vllm-project/vllm-ascend #3845

**Title:** bugfix for mtp fullgraph

## Overview
This PR fixes bugs in MTP (multi-text-prompt) fullgraph mode. Changes were made to `vllm_ascend/utils.py` (47 additions, 18 deletions), `vllm_ascend/worker/model_runner_v1.py`, and `vllm_ascend/platform.py` to ensure correct behavior in full graph execution mode.

## Technical Significance
Fullgraph mode compiles the entire computation graph, requiring careful state and tensor management. This fix addresses bugs specific to MTP's spec decode pattern when running in fullgraph, ensuring correctness and stability for speculative decoding in graph mode.

## Related
- `technique-mtp`
- `technique-fullgraph`
- `technique-spec-decode`