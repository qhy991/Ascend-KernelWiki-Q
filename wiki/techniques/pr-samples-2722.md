---
id: technique-pr-samples-2722
title: "PR Insight: Ascend/samples #2722"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - llm
  - data-distribution
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2722"
---

# PR Insight: Ascend/samples #2722

**Title:** change sample2 depend from llm_engine to llm_datadist

## Overview
This PR changes sample2 dependencies from llm_engine to llm_datadist. The migration reflects architectural changes in how LLM samples are organized and depend on data distribution components.

## Technical Significance
Migrating from llm_engine to llm_datadist suggests a shift toward data distribution patterns for LLM workloads. This change helps developers understand the preferred architecture for multi-device LLM deployment.

## Related
- `pattern-data-parallelism`, `llm-data-distribution`