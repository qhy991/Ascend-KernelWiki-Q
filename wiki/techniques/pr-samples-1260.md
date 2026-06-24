---
id: technique-pr-samples-1260
title: "PR Insight: Ascend/samples #1260"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - samples
  - platform-migration
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1260"
---

# PR Insight: Ascend/samples #1260

**Title:** 【轻量级 PR】：修改710为310P

## Overview
This PR updates sample code to replace references from Ascend710 to Ascend310P platform, continuing the migration effort.

## Technical Significance
Platform migration requires updating configuration files, build scripts, and potentially runtime parameters to match Ascend310P's characteristics. This includes memory size differences, supported operator sets, and performance tuning parameters specific to the Ascend310P architecture.

## Related
- wiki-hardware-unified-buffer
- wiki-hardware-l1-buffer