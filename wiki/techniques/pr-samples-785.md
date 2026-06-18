---
id: technique-pr-samples-785
title: "PR Insight: Ascend/samples #785"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - protobuf
  - dependencies
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/785"
---

# PR Insight: Ascend/samples #785

**Title:** add libascend_protobuf.a

## Overview
This PR adds the libascend_protobuf.a library to the samples repository, which provides Protocol Buffers support for Ascend applications. This is a dependency library that enables structured data serialization and deserialization for sample applications.

## Technical Significance
Adding libascend_protobuf.a provides essential infrastructure for samples that require Protocol Buffers functionality, commonly used in machine learning and communication protocols. This enables proper dependency management for sample applications that need protobuf support.

## Related
- N/A (infrastructure dependency addition)