---
id: technique-pr-samples-461
title: "PR Insight: Ascend/samples #461"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - presenter-server
  - startup-script
  - port-configuration
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/461"
---

# PR Insight: Ascend/samples #461

**Title:** 更新公共presenter server 启动脚本，可替换端口

## Overview
This PR updates the common presenter server startup script to support port configuration, allowing users to specify custom ports instead of using hardcoded defaults.

## Technical Significance
Improves flexibility by enabling port configuration, which is essential for running multiple instances or avoiding port conflicts in different deployment scenarios.

## Related
- `pattern-configuration-management`
- `pattern-deployment`