---
id: technique-pr-samples-1408
title: "PR Insight: Ascend/samples #1408"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - jpeg-decoding
  - dvpp
  - api-simplification
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1408"
---

# PR Insight: Ascend/samples #1408

**Title:** The user does not need to transfer the width and height while decoding jpeg

## Overview
This PR simplifies the JPEG decoding workflow by removing the requirement for users to explicitly transfer width and height parameters when decoding JPEG images. The DVPP JPEG decoder can now automatically extract image dimensions.

## Technical Significance
API simplification improves developer experience and reduces error potential. This change makes JPEG decoding samples easier to use while leveraging DVPP hardware acceleration capabilities.

## Related
- hw-dvpp
- technique-api-simplification