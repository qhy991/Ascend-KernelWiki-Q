---
id: technique-pr-samples-1618
title: "PR Insight: Ascend/samples #1618"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - install-path
  - bugfix
  - path-validation
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1618"
---

# PR Insight: Ascend/samples #1618

**Title:** Bug fix : Parent path of install-path only characters in [a-z, A-Z, 0-9,-, _] are supported

## Overview
This PR fixes a bug related to install-path validation, correcting an issue where only specific characters (a-z, A-Z, 0-9, -, _) were supported in the parent path.

## Technical Significance
Path validation bugs can prevent sample installation or execution, especially on systems with non-ASCII characters or special symbols in directory paths. This fix broadens path compatibility, making samples more accessible to developers using different system configurations.

## Related
- technique-installation