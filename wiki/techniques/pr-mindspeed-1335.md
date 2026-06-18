---
id: technique-pr-mindspeed-1335
title: "PR Insight: Ascend/MindSpeed #1335"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - gmm
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1335"
---

# PR Insight: Ascend/MindSpeed #1335

**Title:** GMM+ADD overlap适配 bugfix

## Overview
This PR fixes bugs related to GMM+ADD overlap adaptation. The issue likely involves incorrect handling of overlapped computation between GMM operations and addition operations.

## Technical Significance
Resolves bugs in GMM+ADD overlap optimization, ensuring correct execution and performance benefits. Overlapping operations is critical for hiding latency and improving throughput in kernel execution.

## Related
- `kernel-gmm`
- `technique-cube-vector-overlap`