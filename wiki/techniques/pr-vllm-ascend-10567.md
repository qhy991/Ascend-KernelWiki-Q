---
id: technique-pr-vllm-ascend-10567
title: "PR Insight: vllm-project/vllm-ascend #10567"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - graph-mode
  - hdk
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10567"
---

# PR Insight: vllm-project/vllm-ascend #10567

**Title:** [BugFix]Reduce the number of stages captured(#9962)

## Overview
This PR reduces the number of stages captured during graph compilation on Ascend 950 to address HDK (Hardware Development Kit) incompatibility issues. The reduction in captured stages helps avoid compilation or runtime problems that arise when too many stages are included in a single graph capture. This is a targeted fix for HDK compatibility on Ascend 950 platforms.

## Technical Significance
This fix addresses HDK limitations on Ascend 950 where capturing too many stages in a single graph can cause compatibility issues. The reduction in stage count improves graph capture reliability while maintaining the benefits of graph mode for performance. This demonstrates the trade-off between capturing more stages for potential optimization versus ensuring compatibility with hardware constraints. The fix ensures graph mode works reliably on Ascend 950 while still providing significant performance benefits over eager mode.

## Related
- `technique-graph-mode`
- `hw-ascend950`