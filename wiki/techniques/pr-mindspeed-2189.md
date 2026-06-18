---
id: technique-pr-mindspeed-2189
title: "PR Insight: Ascend/MindSpeed #2189"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - api
  - compatibility
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2189"
---

# PR Insight: Ascend/MindSpeed #2189

**Title:** [BUGFIX!] 修复core0.9.0&master对老接口的错误导入

## Overview
This PR fixes incorrect import of legacy interfaces in the core0.9.0 and master branches of MindSpeed. The fix ensures backward compatibility with older API versions.

## Technical Significance
Correct interface imports are essential for maintaining backward compatibility and preventing breaking changes for users upgrading between MindSpeed versions. The bug fix addresses incorrect module imports that would cause runtime errors when using legacy APIs. This is particularly important for production environments where users may depend on stable interfaces across versions. The fix ensures smooth upgrades without requiring code changes in user applications.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`