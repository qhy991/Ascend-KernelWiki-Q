---
id: technique-pr-modellink-3362
title: "PR Insight: ModelLink #3362"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - performance
  - bugfix
  - mindspore
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/3362"
---

# PR Insight: ModelLink #3362 - `fix_tolist`

## Overview
Pull Request #3362 in the `ascend/ModelLink` repository introduces a performance optimization and bug fix for the MindSpore backend, specifically addressing inefficiencies caused by the `.tolist()` method.

## Technical Explanation
In deep learning frameworks like MindSpore running on hardware accelerators such as Huawei Ascend NPUs, calling `.tolist()` on a tensor often triggers unintended performance penalties:

1. **Device-to-Host Synchronization**: Extracting data from an NPU tensor to a native Python list requires a synchronous memory copy from device memory to host CPU memory. This operation interrupts asynchronous execution, forcing the NPU to idle while waiting for the host to process the data extraction.
2. **Pipeline Stalls**: If `.tolist()` is used within the critical path (e.g., inside the training loop, loss computation, or frequent metric logging), it introduces recurrent host-device synchronization overheads. This breaks computation/communication overlap and drastically lowers overall throughput.

### The Fix
The `fix_tolist` patch targets these bottlenecks by eliminating or refactoring calls to `.tolist()`. Instead of extracting data into Python native structures eagerly, the fix typically involves:
- Keeping intermediate data as tensors and performing operations via native MindSpore graph execution.
- Delaying or batching data extraction to times when a synchronization boundary is explicitly required (e.g., end-of-epoch logging).
- Avoiding unnecessary type conversions during forward/backward passes.

## Impact
- **Performance**: Greatly reduces host-device sync overhead and prevents pipeline stalling, improving the overall iteration speed (Steps Per Second / Tokens Per Second).
- **Efficiency**: Allows the Ascend NPU to maintain higher utilization rates.
