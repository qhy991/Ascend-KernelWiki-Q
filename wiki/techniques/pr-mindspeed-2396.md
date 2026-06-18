---
id: technique-pr-mindspeed-2396
title: "PR Insight: Ascend/MindSpeed #2396"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - gloo
  - distributed
  - communication
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2396"
---

# PR Insight: Ascend/MindSpeed #2396

**Title:** fix disable gloo noneffective issue

## Overview
This PR fixes an issue where disabling gloo (a CPU-based collective communication library) was ineffective. Gloo is typically used as a fallback for communication backends.

## Technical Significance
Ensures proper backend selection for distributed training. When gloo is disabled, the system should correctly fall back to HCCL or the appropriate Ascend NPU communication backend, avoiding performance issues from unintended CPU communication.

## Related
- `technique-hccl-optimization`
- `technique-distributed-training`
- `hw-hccs`