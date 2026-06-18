---
id: technique-pr-samples-1280
title: "PR Insight: Ascend/samples #1280"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - samples
  - platform-migration
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1280"
---

# PR Insight: Ascend/samples #1280

**Title:** 修改Ascend710为Ascend310P

## Overview
This PR updates the samples codebase to replace references from Ascend710 to Ascend310P platform. This represents a platform migration effort to ensure compatibility with the Ascend310P hardware across sample applications.

## Technical Significance
Platform migration PRs are critical for maintaining sample code relevance across Ascend's hardware portfolio. The Ascend310P is a different inference chipset with potentially different memory hierarchies, tiling requirements, and operator support compared to Ascend710. This migration likely involves updating build configurations, model conversion commands, and potentially memory alignment patterns specific to Ascend310P's unified buffer and L1 constraints.

## Related
- hw-unified-buffer
- hw-l1-buffer
- technique-tiling