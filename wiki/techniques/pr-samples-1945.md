---
id: technique-pr-samples-1945
title: "PR Insight: Ascend/samples #1945"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - acl
  - cleanup
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1945"
---

# PR Insight: Ascend/samples #1945

**Title:** delete amct_acl sample

## Overview
This PR removes the AMCT_ACL sample from the repository, likely due to deprecation or consolidation of functionality. The AMCT_ACL sample previously demonstrated combining AMCT quantization with AscendCL API usage, but this functionality may have been integrated elsewhere or is no longer recommended.

## Technical Significance
Sample code curation is important for maintaining a high-quality reference repository. Removing deprecated samples prevents confusion and directs developers to current best practices for using AMCT with AscendCL. The remaining samples likely provide updated approaches to quantization workflows on Ascend910/910B hardware.

## Related
- `technique-quantization`
- `pattern-api-evolution`