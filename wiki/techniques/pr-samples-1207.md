---
id: technique-pr-samples-1207
title: "PR Insight: Ascend/samples #1207"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - video-encode
  - venc
  - api-cleanup
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1207"
---

# PR Insight: Ascend/samples #1207

**Title:** 【轻量级 PR】：删除venc中hi_mpi_venc_set_mod_param接口的调用

## Overview
This PR removes the call to the hi_mpi_venc_set_mod_param interface from the VENC (Video Encoder) sample code.

## Technical Significance
Removing deprecated or unnecessary API calls simplifies the codebase and can prevent compatibility issues. The hi_mpi_venc_set_mod_param interface may have been replaced by newer APIs or its functionality may now be handled automatically by the VENC driver. This cleanup improves code maintainability.

## Related
- technique-pipeline-scheduling