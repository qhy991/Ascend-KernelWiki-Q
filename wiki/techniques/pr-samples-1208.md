---
id: technique-pr-samples-1208
title: "PR Insight: Ascend/samples #1208"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - jpeg
  - jpege
  - api-cleanup
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1208"
---

# PR Insight: Ascend/samples #1208

**Title:** 【轻量级 PR】：删除jpege中hi_mpi_venc_set_mod_param接口的调用

## Overview
This PR removes the call to the hi_mpi_venc_set_mod_param interface from the JPEGE (JPEG Encoder) sample code.

## Technical Significance
Removing this API call from JPEGE indicates that the module parameter setting is no longer required or is handled differently. This cleanup reduces code complexity and potential for API misuse. JPEGE operations benefit from efficient memory management and vector unit acceleration on Ascend hardware.

## Related
- hw-vector-unit
- hw-unified-buffer