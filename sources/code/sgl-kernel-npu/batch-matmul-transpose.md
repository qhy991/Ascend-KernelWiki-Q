---
id: code-sgl-kernel-npu-batch-matmul-transpose
title: SGL Kernel NPU Batch Matmul Transpose Operator
type: source-code
repo: sgl-project/sgl-kernel-npu
path: csrc/batch_matmul_transpose
url: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/batch_matmul_transpose
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- sglang
- matmul
- transpose
- ascendc
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- nz-format
- global-memory
techniques:
- format-conversion
- tiling-strategy
- pipeline-scheduling
kernel_types:
- matmul
- gemm
languages:
- cpp
- ascendc
---

# SGL Kernel NPU Batch Matmul Transpose Operator

SGL Kernel NPU batch matmul transpose operator with host tiling and kernel directories, anchoring GEMM layout-transform evidence.

## Code Location

- Repository: `sgl-project/sgl-kernel-npu`
- Path: `csrc/batch_matmul_transpose`
- URL: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/batch_matmul_transpose


## Fetched Source


### `csrc/batch_matmul_transpose/op_host/batch_matmul_transpose.cpp`
```cpp
#include <iostream>
#include <string>
#include "acl/acl.h"
#include "kernel_tiling/kernel_tiling.h"
#include "tiling/platform/platform_ascendc.h"
#include "tiling/tiling_data.h"
#include "defines.h"
#include "torch_helper.h"
#include "common_tiling.h"
#include "aclrtlaunch_batch_matmul_transpose.h"

namespace sglang {
namespace npu_kernel {
using namespace pp_matmul;

std::unordered_map<c10::string_view, uint16_t> quantModeMap = {
    {"per_channel_symm", 0},
    {"per_channel_asymm", 1},
    {"per_token_symm", 2},
};

std::unordered_map<c10::string_view, uint16_t> formatModeMap = {
    {"ND", 0},
    {"NZ", 1},
};

std::unordered_map<c10::ScalarType, TensorDType> atType2tensorDType = {
    {at::ScalarType::BFloat16, TensorDType::TENSOR_DTYPE_BF16},
    {at::ScalarType::Half, TensorDType::TENSOR_DTYPE_FLOAT16}};

// batch size -> memory index
constexpr uint32_t MAX_CAPTURE_NUM = 1024;

template <typename MapType>
inline int GetModeVal(const MapType &mode_map, c10::optional<c10::string_view> mode_opt, c10::string_view default_mode,
                      const char *mode_name)
{
    std::string modeStr(mode_name);
    c10::string_view mode_str = mode_opt.value_or(default_mode);
    auto it = mode_map.find(mode_str);
    // if input mode is unsupported, use default value
    TORCH_CHECK(it != mode_map.end(), modeStr, c10::str(": Unsupported mode value ", mode_str));
    return it->second;
}

HOST_API void batch_matmul_transpose(const at::Tensor &tensor_a, const at::Tensor &tensor_b, at::Tensor &tensor_c,
                                     c10::optional<c10::string_view> format_mode,
                                     c10::optional<c10::string_view> quant_mode)
{
    auto tensorAShape = tensor_a.sizes();
    auto tensorBShape = tensor_b.sizes();
    auto tensorCShape = tensor_c.sizes();
    uint32_t n;
    uint32_t block_dim;
    HardwareInfo hwInfo;
    std::map<c10::ScalarType, float> dTypeMap = {{at::ScalarType::Half, 2.0}, {at::ScalarType::BFloat16, 2.0}};

    at::ScalarType aType = tensor_a.scalar_type();
    at::ScalarType bType = tensor_b.scalar_type();
    at::ScalarType cType = tensor_c.scalar_type();
    TORCH_CHECK(aType == bType && bType == cType, "tensor type is not the same");
    TORCH_CHECK((aType == at::ScalarType::BFloat16) || (aType == at::ScalarType::Half),
                "tensor type only support half or bf16");

    TensorFormat formatMode = static_cast<TensorFormat>(GetModeVal(formatModeMap, format_mode, "ND", "format_mode"));
    MatMul::QuantMode quantMode =
        static_cast<MatMul::QuantMode>(GetModeVal(quantModeMap, quant_mode, "per_channel_symm", "quant_mode"));

    TORCH_CHECK(tensorAShape.size() == 3, "batch size is not same between srcTensor and dstTensor");
    if (formatMode == TensorFormat::TENSOR_FORMAT_ND) {
        TORCH_CHECK(tensorBShape.size() == 3, "tensor shape should be dim3 in ND format");
        TORCH_CHECK(tensorAShape[2] == tensorBShape[1], "tensor shape is wrong");
        n = tensorBShape[2];
    } else {
        TORCH_CHECK(tensorBShape.size() == 4, "tensor shape should be dim4 in nz format");
        TORCH_CHECK(tensorAShape[2] == tensorBShape[2], "tensor shape is wrong");
        n = tensorBShape[1] * tensorBShape[3];
    }
    TORCH_CHECK(tensorAShape[1] == tensorBShape[0], "tensor shape is wrong");

    OpShape opShape = {.batchSize = static_cast<uint32_t>(tensorAShape[1]),
                       .m = static_cast<uint32_t>(tensorAShape[0]),
                       .k = static_cast<uint32_t>(tensorAShape[2]),
                       .n = n};
    PpMatmulTilingData matmulTilingData = {
        .opShape = opShape,
    };
    auto dType = atType2tensorDType[aType];
    MatMulInfo mmInfo = {.batchSize = opShape.batchSize,
                         .m = opShape.m,
                         .k = opShape.k,
                         .n = opShape.n,
                         .dtypeA = dType,
                         .dtypeB = dType,
                         .dtypeC = dType,
                         .formatB = formatMode,
                         .mmType = MatMul::MatMulType::MATMUL_EIN_SUM,
                         .inDtype = dTypeMap[aType],
                         .outDtype = dTypeMap[cType],
                         .quantMode = quantMode};
    GetPpMatmulTiling(mmInfo, hwInfo, block_dim, matmulTilingData);
    host_utils::PpMatmulTilingCheck(matmulTilingData);

    // tiling
    int32_t batchIdx = opShape.m - 1;
    uint32_t tilingSize = sizeof(PpMatmulTilingData);
    static auto global_tiling_data = at::empty(
        {tilingSize * MAX_CAPTURE_NUM}, at::TensorOptions().dtype(at::kByte).device(tensor_a.options().device()));
    if (batchIdx >= 0 && batchIdx < MAX_CAPTURE_NUM) {
        aclrtMemcpy(global_tiling_data.data_ptr<uint8_t>() + (tilingSize * batchIdx), tilingSize, &matmulTilingData,
                    tilingSize, ACL_MEMCPY_HOST_TO_DEVICE);
    } else {
        // Handle the case where batchIdx is out of range
        TORCH_CHECK(false, "batchId
// ... (truncated due to length) ...

```

### `csrc/batch_matmul_transpose/op_host/tiling/tiling_data.cpp`
```cpp
#include <map>
#include "tiling_data.h"
#include "common.h"
#include "common_tiling.h"

namespace pp_matmul {

constexpr uint32_t L1_DESCALE_BUFFER_LEN_MAX = 6144;
constexpr uint32_t CONST_3 = 3;
constexpr uint32_t CONST_4 = 4;
constexpr uint32_t CONST_16 = 16;
constexpr uint32_t CONST_32 = 32;
constexpr uint32_t CONST_256 = 256;
constexpr uint32_t CONST_512 = 512;

const std::map<TensorDType, uint32_t> G_DTYPE_MAP = {{TensorDType::TENSOR_DTYPE_FLOAT16, 1u},
                                                     {TensorDType::TENSOR_DTYPE_BF16, 2u}};
const std::map<TensorFormat, uint32_t> G_FORMAT_MAP = {{TensorFormat::TENSOR_FORMAT_ND, 0u},
                                                       {TensorFormat::TENSOR_FORMAT_NZ, 1u}};
using MmType = MatMul::MatMulType;
using QmType = MatMul::QuantMode;
using namespace host_utils;

bool IsI8Bf16Kernel(const MatMulInfo &mmInfo)
{
    bool isI8Bf16 = mmInfo.isInt8 && mmInfo.dtypeC == TensorDType::TENSOR_DTYPE_BF16;
    bool isI8Fp16 = mmInfo.isInt8 && mmInfo.dtypeC == TensorDType::TENSOR_DTYPE_FLOAT16 &&
                    mmInfo.quantMode == QmType::PER_TOKEN_SYMM;
    return isI8Bf16 || isI8Fp16;
}

HardwareInfo::HardwareInfo()
{
    auto &platform = PlatformInfo::Instance();
    coreNum = platform.coreNumAic;
    l2Size = platform.l2Size;
    l1Size = platform.l1Size;
    l0aSize = platform.l0aSize;
    l0bSize = platform.l0bSize;
    l0cSize = platform.l0cSize;
    hbmBandWidth = 1;
    l2BandWidth = 5;  // 5x faster than hbm.
}

void PpMatmulTilingData::SetBaseShape(uint32_t batchSize, uint32_t m, uint32_t k, uint32_t n)
{
    opShape.batchSize = batchSize;
    opShape.m = m;
    opShape.k = k;
    opShape.n = n;
}

void PpMatmulTilingData::SetBaseOp(uint32_t coreNum, uint32_t mBase, uint32_t nBase, const MatMulInfo &mmInfo)
{
    opShape.m0 = mBase;
    opShape.n0 = nBase;
    mLoop = CeilDiv(opShape.m, opShape.m0);
    nLoop = CeilDiv(opShape.n, opShape.n0);
    coreLoop = opShape.batchSize * mLoop * nLoop;

    if (mLoop == 1 && mmInfo.transB && coreLoop % coreNum < coreNum / CONST_4 * CONST_3) {
        mBase = RoundUp<uint32_t>(opShape.m, CONST_16);
        opShape.m0 = mBase;
        uint32_t maxN0 = PlatformInfo::Instance().l0cSize / (mBase * sizeof(float));
        if (mmInfo.isInt8 || mmInfo.mmType == MmType::MATMUL_WITH_BIAS) {
            maxN0 = maxN0 < CONST_256 ? maxN0 : CONST_256;
        }
        uint32_t x = CeilDiv(opShape.n, coreNum);
        uint32_t y = CeilDiv(x, maxN0);
        nBase = RoundUp<uint32_t>(CeilDiv(x, y), CONST_16);
        uint32_t rqdL0CSize = mBase * nBase * sizeof(float);
        if (rqdL0CSize < PlatformInfo::Instance().l0cSize &&
            (mBase + nBase) * CONST_256 * sizeof(uint16_t) < L1AB_PINGPONG_BUFFER_LEN) {
            opShape.n0 = nBase;
            nLoop = CeilDiv(opShape.n, opShape.n0);
            coreLoop = opShape.batchSize * nLoop;
        }
    }
    blockDim = std::min(coreLoop, coreNum);
}

// transA transB quantMode [dtype] format
void PpMatmulTilingData::SetTilingKey(const MatMulInfo &mmInfo, uint32_t swizzleDirect, uint32_t enSplitK)
{
    if (mmInfo.mmType == MmType::MATMUL_ACCUM_ATOMIC || mmInfo.mmType == MmType::MATMUL_WITH_BIAS ||
        mmInfo.mmType == MmType::MATMUL_EIN_SUM || mmInfo.mmType == MmType::MATMUL_DEQUANT || IsI8Bf16Kernel(mmInfo)) {
        // SwizzleDir[1] TransA[1] TransB[1] DtypeA[3] DtypeB[3] DtypeC[3] FormatA[1] FormatB[1] FormatC[1] WithBias[1]
        tilingKey = swizzleDirect;
        tilingKey = (tilingKey << 1) + static_cast<uint32_t>(mmInfo.transA);
        tilingKey = (tilingKey << 1) + static_cast<uint32_t>(mmInfo.transB);
        tilingKey = (tilingKey << 3) + G_DTYPE_MAP.at(mmInfo.dtypeA);  // 3bit for dtypeA.
        tilingKey = (tilingKey << 3) + G_DTYPE_MAP.at(mmInfo.dtypeB);  // 3bit for dtypeB.
        tilingKey = (tilingKey << 3) + G_DTYPE_MAP.at(mmInfo.dtypeC);  // 3bit for dtypeC.
        tilingKey = (tilingKey << 1) + G_FORMAT_MAP.at(mmInfo.formatA);
        tilingKey = (tilingKey << 1) + G_FORMAT_MAP.at(mmInfo.formatB);
        tilingKey = (tilingKey << 1) + G_FORMAT_MAP.at(mmInfo.formatC);
        tilingKey = (tilingKey << 1) + static_cast<uint32_t>(mmInfo.biasFlag);
    } else {
        tilingKey = swizzleDirect;
        tilingKey = (tilingKey << 1) + static_cast<uint32_t>(mmInfo.transA);
        tilingKey = (tilingKey << 1) + static_cast<uint32_t>(mmInfo.transB);
        tilingKey = (tilingKey << 1) + static_cast<uint32_t>(mmInfo.isInt8);
        tilingKey = (tilingKey << 1) + static_cast<uint32_t>(mmInfo.biasFlag);
        tilingKey = (tilingKey << 1) + enSplitK;
    }
}

uint32_t PpMatmulTilingData::End(const MatMulInfo &mmInfo)
{
    uint32_t cubeBlockSize = mmInfo.isInt8 ? CUBE_BLOCK_SIZE_INT8 : CUBE_BLOCK_SIZE;
    uint32_t kBlockSize = mmInfo.isInt8 ? BLOCK_SIZE_INT8_K : BLOCK_SIZE;
    uint32_t scaleBlockSize = mmInfo.isInt8 ? L1_DESCALE_BUFFER_LEN_MAX : 0;
    uint32_t shapeSum = opShape.m0 + opShape.n0;
    if (mmInfo.isInt8 && (mmInfo.
// ... (truncated due to length) ...

```

### `csrc/batch_matmul_transpose/op_host/tiling/tiling_data.h`
```cpp
#ifndef PP_MATMUL_TILING_DATA
#define PP_MATMUL_TILING_DATA
#include <cstdint>

namespace pp_matmul {
struct MatMul {
    enum class MatMulType : uint32_t {
        MATMUL_DEFAULT = 0,   // C = op(A) * op(B)
        MATMUL_DEQUANT,       //
        MATMUL_ACCUM_ATOMIC,  // C += op(A) * op(B)
        MATMUL_WITH_BIAS,     // C = op(A) * op(B) + Bias, where Bias is a vector.
        MATMUL_EIN_SUM
    };
    enum class QuantMode : uint32_t { PER_CHANNEL_SYMM = 0, PER_CHANNEL_ASYMM, PER_TOKEN_SYMM };
};

enum class TensorDType : uint32_t { TENSOR_DTYPE_FLOAT16 = 0, TENSOR_DTYPE_BF16 };

enum class TensorFormat : uint32_t { TENSOR_FORMAT_ND = 0, TENSOR_FORMAT_NZ };

struct MatMulInfo {
    uint32_t batchSize{0};
    uint32_t m{0};  // actual input m
    uint32_t k{0};  // actual input k
    uint32_t n{0};  // actual input n
    TensorDType dtypeA{TensorDType::TENSOR_DTYPE_FLOAT16};
    TensorDType dtypeB{TensorDType::TENSOR_DTYPE_FLOAT16};
    TensorDType dtypeC{TensorDType::TENSOR_DTYPE_FLOAT16};
    TensorFormat formatA{TensorFormat::TENSOR_FORMAT_ND};
    TensorFormat formatB{TensorFormat::TENSOR_FORMAT_ND};
    TensorFormat formatC{TensorFormat::TENSOR_FORMAT_ND};
    MatMul::MatMulType mmType{MatMul::MatMulType::MATMUL_DEFAULT};
    bool transA{0};    // false: 0, true: 1
    bool transB{0};    // false: 0, true: 1
    bool biasFlag{0};  // false: 0, true: 1
    bool isInt8{0};    // 是否是 int8融合
    float inDtype{0};
    float outDtype{0};
    MatMul::QuantMode quantMode{MatMul::QuantMode::PER_CHANNEL_SYMM};
};

struct OpShape {
    uint32_t batchSize{0};
    uint32_t m{0};
    uint32_t k{0};
    uint32_t n{0};
    uint32_t m0{0};
    uint32_t k0{0};
    uint32_t n0{0};
};

struct HardwareInfo {
    uint32_t coreNum{0};
    uint32_t l2Size{0};
    uint32_t l1Size{0};
    uint32_t l0aSize{0};
    uint32_t l0bSize{0};
    uint32_t l0cSize{0};
    uint32_t hbmBandWidth{0};
    uint32_t l2BandWidth{0};

    HardwareInfo();
};

#pragma pack(push, 1)
struct PpMatmulTilingData {
    OpShape opShape{};
    uint32_t mLoop{1};
    uint32_t kLoop{1};
    uint32_t nLoop{1};
    uint32_t coreLoop{1};
    uint32_t swizzlCount{1};
    uint32_t tilingKey{0};
    uint32_t blockDim{1};
    uint32_t swizzlDirect{0};
    uint32_t splitk{0};
    uint32_t enShuffleK{0};
    uint32_t quantMode{0};

    void SetBaseShape(uint32_t batchSize, uint32_t m, uint32_t k, uint32_t n);
    void SetBaseOp(uint32_t coreNum, uint32_t mBase, uint32_t nBase, const MatMulInfo &mmInfo);
    void SetTilingKey(const MatMulInfo &mmInfo, uint32_t swizzleDirect, uint32_t enSplitK);
    uint32_t End(const MatMulInfo &mmInfo);
};
#pragma pack(pop)

void GetPpMatmulTiling(const MatMulInfo &mmInfo, const HardwareInfo &hwInfo, uint32_t &blockDim,
                       PpMatmulTilingData &tilingData);
}  // namespace pp_matmul
#endif

```
