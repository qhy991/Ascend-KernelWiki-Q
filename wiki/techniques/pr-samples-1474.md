---
id: technique-pr-samples-1474
title: "PR Insight: Ascend/samples #1474"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - samples
  - bugfix
  - 310p
  - compatibility
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1474"
---

# PR Insight: Ascend/samples #1474

**Title:** fix 310P

## Overview
This PR fixes issues specific to the Ascend 310P processor in the samples repository.

## Technical Significance
The 310P is an edge inference device with differences from datacenter 910/910B chips, including memory hierarchy, operator support, and ACL API behavior. Fixes may address device-specific operator availability, memory constraints, or runtime configuration issues unique to edge deployment.

## Related
- `technique-device-compatibility`
- `technique-edge-inference`
- `technique-hardware-adaptation`
- `hw-l1-buffer`