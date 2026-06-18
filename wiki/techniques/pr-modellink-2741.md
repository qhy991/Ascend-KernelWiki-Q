---
id: technique-pr-modellink-2741
title: "PR Insight: Ascend/ModelLink #2741"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - bugfix
  - pipeline
  - logging
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2741"
---

# PR Insight: Ascend/ModelLink #2741

**Title:** fix add daily pipeline log tar exception

## Overview
This PR fixes an exception that occurred when adding daily pipeline logs to a tar archive. The fix resolves issues with log archiving during training pipeline operations.

## Technical Significance
Reliable log archiving is important for training monitoring and debugging. This fix ensures that pipeline logs are correctly archived on Ascend systems, enabling better training observability and troubleshooting.

## Related
- technique-pipeline-scheduling