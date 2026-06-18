---
id: technique-pr-modellink-2548
title: "PR Insight: Ascend/ModelLink #2548"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - deepseekv3
  - dualpipe
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2548"
---

# PR Insight: Ascend/ModelLink #2548

**Title:** [core-llm][dskv3]dualpipe need no embed init

## Overview
This PR removes embedding initialization requirements for dualpipe training in DeepSeekV3. The change optimizes the training pipeline by eliminating unnecessary embedding initialization steps.

## Technical Significance
Embedding initialization in dualpipe training can be redundant or inefficient. Removing this requirement reduces memory footprint, initialization time, and potential synchronization overhead. This optimization improves training startup efficiency and resource utilization when training DeepSeekV3 with dual pipeline parallelism on Ascend NPUs.

## Related
- `technique-pipeline-scheduling`