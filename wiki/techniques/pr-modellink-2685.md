---
id: technique-pr-modellink-2685
title: "PR Insight: Ascend/ModelLink #2685"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspore
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2685"
---

# PR Insight: Ascend/ModelLink #2685

**Title:** 【bugfix】【master】删除无用patch

## Overview
This PR removes unused patches from the MindSpore backend. These patches were likely legacy files or experimental changes that are no longer needed in the current version of ModelLink.

## Technical Significance
Removing unused patches improves code maintainability and reduces confusion. It ensures that only active, necessary modifications are present in the codebase, making it easier to understand the current integration between ModelLink and MindSpore on Ascend hardware.

## Related