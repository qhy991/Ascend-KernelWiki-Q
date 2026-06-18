---
id: technique-pr-modellink-2542
title: "PR Insight: Ascend/ModelLink #2542"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pipeline
  - logging
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2542"
---

# PR Insight: Ascend/ModelLink #2542

**Title:** fix:pipeline log目录生成路径

## Overview
This PR fixes a bug in the pipeline log directory path generation. Pipeline training uses structured logging for debugging and monitoring, and this fix ensures log files are created in the correct location.

## Technical Significance
Correct log directory handling is essential for debugging distributed pipeline training on Ascend hardware. Proper logging enables effective monitoring and troubleshooting of training jobs.

## Related
- pipeline training
- logging infrastructure