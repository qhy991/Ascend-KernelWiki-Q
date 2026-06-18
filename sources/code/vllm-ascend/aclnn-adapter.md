---
id: code-vllm-ascend-aclnn-adapter
title: vLLM Ascend aclnn Torch Adapter
type: source-code
repo: vllm-project/vllm-ascend
path: csrc/aclnn_torch_adapter
url: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/aclnn_torch_adapter
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
- aclnn
- torch-adapter
- operator
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- global-memory
- cube-unit
- vector-unit
techniques:
- workspace-management
- format-conversion
kernel_types:
- attention
- matmul
- elementwise
languages:
- cpp
---

# vLLM Ascend aclnn Torch Adapter

vLLM Ascend aclnn Torch adapter source, anchoring code evidence for bridging PyTorch extension calls to CANN aclnn operators and workspace semantics.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `csrc/aclnn_torch_adapter`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/aclnn_torch_adapter


## Fetched Source


### `csrc/aclnn_torch_adapter/NPUStorageImpl.h`
```cpp
// Copyright (c) 2020, Huawei Technologies Co., Ltd
// All rights reserved.
//
// This source code is licensed under the BSD-style license found in the
// LICENSE file in the root directory of this source tree.

#pragma once

#include <ATen/Tensor.h>
#include <c10/core/StorageImpl.h>
#include <c10/core/Allocator.h>
#include <c10/core/ScalarType.h>
#include <c10/util/typeid.h>
#include <c10/util/order_preserving_flat_hash_map.h>

#include "acl/acl_rt.h"
#include "acl/acl_base.h"

namespace vllm_ascend
{

    struct NPUStorageDesc
    {
    public:
        struct use_byte_size_t
        {
        };

        c10::SmallVector<int64_t, 5> base_sizes_;
        c10::SmallVector<int64_t, 5> base_strides_;
        c10::SmallVector<int64_t, 5> storage_sizes_;
        int64_t base_offset_ = 0;
        use_byte_size_t base_dtype_ = {};
        aclFormat origin_format_ = ACL_FORMAT_UNDEFINED;
        aclFormat npu_format_ = ACL_FORMAT_ND;
        // used to make CANN GE tensor from storagImpl
        caffe2::TypeMeta data_type_ = caffe2::TypeMeta::Make<uint8_t>();
    };

    struct NPUStorageImpl : public c10::StorageImpl
    {
        explicit NPUStorageImpl(
            use_byte_size_t use_byte_size,
            size_t size_bytes,
            at::DataPtr data_ptr,
            at::Allocator *allocator,
            bool resizable);
        ~NPUStorageImpl() override = default;

        void release_resources() override;

        NPUStorageDesc npu_desc_;

        NPUStorageDesc get_npu_desc() const
        {
            return npu_desc_;
        }
    };

    c10::intrusive_ptr<c10::StorageImpl> make_npu_storage_impl(
        c10::StorageImpl::use_byte_size_t,
        c10::SymInt size_bytes,
        c10::DataPtr data_ptr,
        c10::Allocator *allocator,
        bool resizable);

}

```

### `csrc/aclnn_torch_adapter/NPUBridge.cpp`
```cpp
// Copyright (c) 2020, Huawei Technologies Co., Ltd
// All rights reserved.
//
// This source code is licensed under the BSD-style license found in the
// LICENSE file in the root directory of this source tree.

#include "NPUBridge.h"

namespace vllm_ascend
{
    NPUStorageImpl *NPUBridge::GetNpuStorageImpl(c10::StorageImpl *storageImpl)
    {
        return static_cast<NPUStorageImpl *>(storageImpl);
    }

    NPUStorageImpl *NPUBridge::GetNpuStorageImpl(c10::Storage &&storage)
    {
        return static_cast<NPUStorageImpl *>(storage.unsafeGetStorageImpl());
    }

    NPUStorageImpl *NPUBridge::GetNpuStorageImpl(const at::Tensor &tensor)
    {
        return static_cast<NPUStorageImpl *>(tensor.storage().unsafeGetStorageImpl());
    }

    NPUStorageDesc &NPUBridge::GetNpuStorageImplDesc(const at::Tensor &tensor)
    {
        return static_cast<NPUStorageImpl *>(tensor.storage().unsafeGetStorageImpl())->npu_desc_;
    }
}

```

### `csrc/aclnn_torch_adapter/NPUStorageImpl.cpp`
```cpp
// Copyright (c) 2020, Huawei Technologies Co., Ltd
// All rights reserved.
//
// This source code is licensed under the BSD-style license found in the
// LICENSE file in the root directory of this source tree.

#include "NPUStorageImpl.h"

namespace vllm_ascend
{

    NPUStorageImpl::NPUStorageImpl(
        use_byte_size_t use_byte_size,
        size_t size_bytes,
        at::DataPtr data_ptr,
        at::Allocator *allocator,
        bool resizable) : c10::StorageImpl(use_byte_size,
                                           size_bytes,
                                           at::DataPtr(std::move(data_ptr)),
                                           allocator,
                                           resizable)
    {
    }

    void NPUStorageImpl::release_resources()
    {
        StorageImpl::release_resources();
    }

    c10::intrusive_ptr<c10::StorageImpl> make_npu_storage_impl(
        c10::StorageImpl::use_byte_size_t,
        c10::SymInt size_bytes,
        c10::DataPtr data_ptr,
        c10::Allocator *allocator,
        bool resizable)
    {
        if (data_ptr == nullptr)
        {
            data_ptr = allocator->allocate(size_bytes.as_int_unchecked());
        }
        // Correctly create NPUStorageImpl object.
        c10::intrusive_ptr<c10::StorageImpl> npu_storage_impl = c10::make_intrusive<NPUStorageImpl>(
            c10::StorageImpl::use_byte_size_t(),
            size_bytes.as_int_unchecked(),
            std::move(data_ptr),
            allocator,
            resizable);
        // There is no need to consider the NPUStorageDesc information, it will be carried out in the subsequent processing.
        return npu_storage_impl;
    }

}

```
