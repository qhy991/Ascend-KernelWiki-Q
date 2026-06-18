---
id: technique-pr-mindspeed-2232
title: "PR Insight: Ascend/MindSpeed #2232"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - gloo-group
  - disable
  - refactor
  - core
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2232"
---

# PR Insight: Ascend/MindSpeed #2232

**Title:** refactor:disable gloo group in core_r0.10.0

## Overview
This PR refactors the code to disable Gloo communication groups in core_r0.10.0. Gloo is a collective communication library, and disabling it indicates a transition to other communication backends or configuration changes.

## Technical Significance
Disabling Gloo groups in core_r0.10.0 suggests a strategic decision to use alternative communication backends, possibly for performance or compatibility reasons. This refactor ensures proper cleanup and configuration when Gloo is not used, maintaining framework flexibility.

## Related
- `pattern-communication-backend-compatibility`
- `pattern-configuration-management`
- `pattern-refactoring`
- `pattern-runtime-adaptation`