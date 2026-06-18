---
id: technique-pr-mindspeed-1826
title: "PR Insight: Ascend/MindSpeed #1826"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - device-management
  - checkpoint
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1826"
---

# PR Insight: Ascend/MindSpeed #1826

**Title:** bugfix:fix get device error when enabling both --exit-signal-handler and --save

## Overview
This PR fixes a device retrieval error that occurs when both --exit-signal-handler and --save flags are enabled. The issue likely arises from device context management during signal handling and checkpoint saving.

## Technical Significance
Device error handling is critical for robust training. Fixing this bug prevents crashes when checkpointing with signal handling enabled, ensuring proper device management and checkpoint persistence on Ascend NPUs.

## Related
- checkpoint patterns
- device-management
- signal-handling