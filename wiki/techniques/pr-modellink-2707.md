---
id: technique-pr-modellink-2707
title: "PR Insight: Ascend/ModelLink #2707"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - bugfix
  - gloo
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2707"
---

# PR Insight: Ascend/ModelLink #2707

**Title:** fix gloo feature patch mistakes

## Overview
This PR fixes mistakes in the Gloo backend feature patches. Gloo is a collective communications library, and these corrections ensure proper operation when using Gloo for distributed training.

## Technical Significance
Gloo provides CPU-based collective communication alternative to HCCL. Fixing these feature patches ensures reliable communication in distributed training scenarios on Ascend systems, particularly for smaller models or development environments where GPU-based communication isn't available.

## Related
- technique-hccl-optimization