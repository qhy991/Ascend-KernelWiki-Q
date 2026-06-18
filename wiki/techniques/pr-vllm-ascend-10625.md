---
id: technique-pr-vllm-ascend-10625
title: "PR Insight: vllm-ascend #10625"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - doc
  - typo
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10625"
---

# PR Insight: vllm-ascend #10625

## Overview
This PR is a documentation bugfix that corrects a minor typo regarding the GLM-5.2 model's quantized name.

## Details
The PR specifically changes the incorrect model string reference `GLM5.2-w8v8` to the correct, properly hyphenated format `GLM-5.2-w8v8`. This modification is applied within the GLM-5.2 tutorial documentation file (`docs/source/tutorials/models/GLM5.2.md`).

Although this is a trivial change, accurately reflecting model naming conventions in the official documentation is vital for user clarity. It prevents potential errors and confusion that can occur if users attempt to copy-paste incorrect model identifiers to launch the quantized version of GLM-5.2 on the Ascend NPU platform.
