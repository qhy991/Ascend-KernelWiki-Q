---
id: doc-ascendcl-memory-management
title: AscendCL Runtime Memory Management
type: source-doc
architectures:
- ascend910
- ascend910b
- ascend310p
tags:
- ascendcl
- memory
- runtime
- cann
date: '2026-06-18'
url: https://www.hiascend.com/document/detail/en/canncommercial/800/apiref/appdevgapi/aclcppdevg_03_0102.html
hardware_features:
- global-memory
techniques:
- workspace-management
confidence: source-reported
---

# AscendCL Runtime Memory Management

Official AscendCL runtime memory-management reference. The page documents host-memory lifetime restrictions such as aclrtFreeHost only releasing memory allocated by aclrtMallocHost and not performing implicit device or stream synchronization.

## Source

- https://www.hiascend.com/document/detail/en/canncommercial/800/apiref/appdevgapi/aclcppdevg_03_0102.html
