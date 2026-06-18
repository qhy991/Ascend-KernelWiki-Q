---
id: technique-pr-samples-2721
title: "PR Insight: Ascend/samples #2721"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - tiling
  - documentation
  - ascendc
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2721"
---

# PR Insight: Ascend/samples #2721

**Title:** fix tilingsink sample comment

## Overview
This PR fixes comments in the tiling sink sample. Tiling sink refers to techniques where tiling logic is moved or "sunk" into specific computation stages, potentially improving performance or reducing memory overhead.

## Technical Significance
Accurate documentation in tiling samples is crucial because tiling strategies directly impact kernel performance. Correct comments help developers understand the optimization techniques being applied and how to adapt them for their own use cases.

## Related
- technique-nz-tiling
- technique-data-reuse