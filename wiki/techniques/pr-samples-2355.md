---
id: technique-pr-samples-2355
title: "PR Insight: Ascend/samples #2355"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - custom-pass
  - error-handling
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2355"
---

# PR Insight: Ascend/samples #2355

**Title:** return GRAPH_SUCCESS when get subgraph failed in modify subgraph pass

## Overview
This PR fixes error handling in the modify subgraph pass by returning GRAPH_SUCCESS instead of an error when getting the subgraph fails, preventing unnecessary failures.

## Technical Significance
Improves robustness of custom graph transformation passes by handling edge cases more gracefully, allowing graph modifications to proceed when subgraph retrieval encounters non-critical issues.

## Related