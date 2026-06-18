---
id: technique-pr-samples-603
title: "PR Insight: Ascend/samples #603"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - caffe
  - acl
  - quantization
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/603"
---

# PR Insight: Ascend/samples #603

**Title:** Add amct_caffe and amct_acl samples

## Overview
This PR adds samples for AMCT (Ascend Model Compression Toolkit) with both Caffe and ACL (Ascend Computing Language) backends. These demonstrate quantization workflows for Caffe models and direct ACL integration for low-level model compression.

## Technical Significance
Adding Caffe and ACL samples expands AMCT coverage to support legacy frameworks and low-level customization. ACL samples are particularly valuable for users who need fine-grained control over quantization parameters or are building custom quantization pipelines.

## Related
- technique-operator-fusion
- AMCT toolkit
- Caffe quantization
- ACL integration
- Model compression