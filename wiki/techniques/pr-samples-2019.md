---
id: technique-pr-samples-2019
title: "PR Insight: Ascend/samples #2019"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - aclnn
  - attribute
  - testcase
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2019"
---

# PR Insight: Ascend/samples #2019

**Title:** Add Attr for AclOnlineModel testcase

## Overview
This PR adds attribute support to the AclOnlineModel test case. The enhancement enables testing of operator attributes in online model inference scenarios using the Ascend Compute Language Neural Network (AclNN) API.

## Technical Significance
Operator attributes (strides, pads, dilation rates, etc.) are critical for configuring kernel behavior. This sample demonstrates how to properly set and use attributes when invoking operators through the AclNN API, which is essential for correct model inference behavior.

## Related
- `technique-ascendc`