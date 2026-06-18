---
id: technique-pr-samples-869
title: "PR Insight: Ascend/samples #869"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - signal-op
  - acl
  - compilation
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/869"
---

# PR Insight: Ascend/samples #869

**Title:** Add acl signal op compile sample

## Overview
This PR adds a sample demonstrating how to compile signal processing operators using the ACL (Ascend Computing Language) API. It shows the build process and compilation options for signal operations on Ascend hardware.

## Technical Significance
Provides a reference for signal processing operator development on Ascend, enabling DSP-like operations such as FFT, filtering, and modulation to be accelerated using ACL interfaces.

## Related
- `technique-operator-fusion`