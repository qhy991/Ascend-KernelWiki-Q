---
id: technique-pr-modellink-2234
title: "PR Insight: Ascend/ModelLink #2234"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - distributed
  - hccl
  - timeout
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2234"
---

# PR Insight: Ascend/ModelLink #2234

**Title:** hccl time out to 3600

## Overview
Increases the HCCL (Huawei Collective Communication Library) timeout value to 3600 seconds. This change allows longer wait times for collective communication operations during distributed training.

## Technical Significance
Configuration update that accommodates longer-running distributed training scenarios. Increasing the timeout prevents premature failures during large-scale training runs where collective operations may take longer to complete.

## Related
- technique-hccl-optimization