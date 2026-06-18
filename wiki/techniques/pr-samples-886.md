---
id: technique-pr-samples-886
title: "PR Insight: Ascend/samples #886"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - documentation
  - contributor-guide
  - resources
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/886"
---

# PR Insight: Ascend/samples #886

**Title:** 修改贡献者指南，由于后台800和1951机器资源缺失，删除相关要求

## Overview
This PR modifies the contributor guide to remove requirements related to machine resources 800 and 1951, which are no longer available. The change updates documentation to reflect the current testing infrastructure constraints.

## Technical Significance
Keeping documentation aligned with available resources is important for contributor experience. This change removes outdated testing requirements, preventing confusion for developers trying to run sample code or contribute to the repository. It reflects the reality of hardware resource availability in the development environment.

## Related
- Contributor documentation
- Testing infrastructure requirements
- Sample validation workflows
- Resource planning for Ascend development