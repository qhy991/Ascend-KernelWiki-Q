---
id: technique-pr-samples-1155
title: "PR Insight: Ascend/samples #1155"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - acl
  - data-types
  - inference
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1155"
---

# PR Insight: Ascend/samples #1155

**Title:** 增加acl.mdl.get_output_data_type支持的数据种类

## Overview
This PR expands the data type support for acl.mdl.get_output_data_type API in the samples. The modification adds support for additional data types that the get_output_data_type function can handle, improving compatibility with various model output formats.

## Technical Significance
Expanding data type support in acl.mdl.get_output_data_type is important for working with diverse neural network models that may output data in different formats (FP16, FP32, INT8, etc.). This enhancement enables samples to correctly query and handle a wider range of model output types during inference on Ascend NPU.

## Related
- ACL model API usage
- Data type handling in inference
- Model output format support