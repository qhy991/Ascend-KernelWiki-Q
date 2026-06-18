---
id: code-ascend-samples-hccl
title: "Ascend Samples \u2014 HCCL Communication Examples"
type: source-code
repo: Ascend/samples
path: cplusplus/level1_single_api/7_dvpp
url: https://gitee.com/ascend/samples/tree/master/cplusplus
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- samples
- hccl
- communication
- cpp
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- hccs
- global-memory
techniques:
- hccl-optimization
- tensor-parallel-overlap
languages:
- cpp
---

# Ascend Samples — HCCL Communication Examples

Official sample-code area that should be expanded into more precise HCCL examples as the distributed-source pass continues. It is a placeholder code-evidence anchor for host-side C++ communication and stream integration around HCCL workflows.

## Code Location

- Repository: `Ascend/samples`
- Path: `cplusplus/level1_single_api/7_dvpp`
- URL: https://gitee.com/ascend/samples/tree/master/cplusplus


## Fetched Source


### `cplusplus/level1_single_api/7_dvpp/pngd_sample/src/sample_comm.h`
```cpp
/**
 *  Copyright [2021] Huawei Technologies Co., Ltd
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef __SAMPLE_COMM_H__
#define __SAMPLE_COMM_H__
#include <cstdint>
#include <pthread.h>

#include "hi_dvpp.h"

/*******************************************************
    macro define
*******************************************************/
const uint32_t FILE_NAME_LEN = 128;

const uint64_t MULTIPLE_S_TO_US        = 1000000;
const uint32_t PNGD_DECODED_QUEUE_NUM = 10;

#define SAMPLE_PRT(fmt...)   \
    do { \
        printf("[%s]-%d: ", __FUNCTION__, __LINE__); \
        printf(fmt); \
    } while (0)

#define CHECK_NULL_PTR(ptr) \
    do { \
        if(NULL == ptr) \
        { \
            SAMPLE_PRT(" NULL pointer\n"); \
            return HI_FAILURE; \
        } \
    } while (0)

#define CHECK_CHN_RET(express, Chn, name) \
    do { \
        int32_t Ret; \
        Ret = express; \
        if (HI_SUCCESS != Ret) \
        { \
            SAMPLE_PRT(" %s chn %u failed with %#x!\n", name, Chn, Ret); \
            fflush(stdout); \
            return Ret; \
        } \
    } while (0)

/*******************************************************
    structure define
*******************************************************/
typedef enum hiTHREAD_CONTRL_E {
    THREAD_CTRL_INIT,
    THREAD_CTRL_START,
    THREAD_CTRL_PAUSE,
    THREAD_CTRL_STOP,
} THREAD_CONTRL_E;

typedef struct hiPNGD_THREAD_PARAM_S {
    char cFileName[FILE_NAME_LEN];
    bool bWholeDirDecode;
    uint8_t *perfStreamBuf;
    int32_t s32ChnId;
    int32_t s32StreamMode;
    int32_t s32MilliSec;
    int32_t s32IntervalTime;
    int32_t s32CircleSend;

    volatile uint32_t u32SendSucc;
    volatile uint32_t u32PicInPngd;
    volatile uint32_t u32Decoded;
    volatile uint32_t u32DecodeFail;
    volatile uint32_t u32DecodeSucc;

    uint64_t u64PtsInit;
    hi_pixel_format enPixFormat;
    THREAD_CONTRL_E enSendThreadCtrl;
    THREAD_CONTRL_E enGetThreadCtrl;
} PNGD_THREAD_PARAM_S;

/*******************************************************
    function announce
*******************************************************/
void pngd_init_start_time();
void pngd_usage(char *sPrgNm);
int32_t get_option(int32_t argc, char **argv);
int32_t check_option();
void print_arguement();

void pngd_cmd_ctrl(pthread_t *pJpegdSendTid, pthread_t *pJpegdGetTid);
int32_t pngd_start_send_stream(pthread_t *pJpegdSendTid);
void pngd_stop_send_stream();
int32_t pngd_start_get_pic(pthread_t *pJpegdGetTid);
void pngd_stop_get_pic();
int32_t pngd_create();
int32_t pngd_destroy();
void pngd_show_decode_state();
int32_t setup_acl_device();
int32_t deinit_pngd_mod();

#endif /* End of #ifndef __SAMPLE_COMMON_H__ */

```

### `cplusplus/level1_single_api/7_dvpp/pngd_sample/src/sample_comm_pngd.cpp`
```cpp
/**
 *  Copyright [2021] Huawei Technologies Co., Ltd
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <cstring>
#include <sstream>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/ioctl.h>
#include <sys/poll.h>
#include <sys/time.h>
#include <fcntl.h>
#include <cerrno>
#include <pthread.h>
#include <cmath>
#include <unistd.h>
#include <csignal>
#include <sys/prctl.h>
#include <dirent.h>
#include <getopt.h>
#include "sample_comm.h"
#include <vector>
#include "acl.h"
#include "acl_rt.h"

using namespace std;

bool g_whole_dir_decode  = HI_FALSE;
int32_t g_send_circle    = 0;
int32_t g_wait_time      = -1;
uint32_t g_width         = 3840;
uint32_t g_height        = 2160;
uint32_t g_chn_num       = 1;
uint32_t g_write_file    = 1;
uint32_t g_start_channel = 0;
uint32_t g_delay_time    = 5;
uint32_t g_performance   = 0;
uint32_t g_align         = 16;
uint64_t g_start_time    = 0;

char g_input_file_name[FILE_NAME_LEN]  = "infile";
char g_output_file_name[FILE_NAME_LEN] = "outfile";
char g_compatible_dir_name[FILE_NAME_LEN]  = "./";

int32_t g_device_id = 0;
aclrtContext g_context = nullptr;
aclrtRunMode g_run_mode = ACL_DEVICE;
hi_pixel_format g_pixel_format = HI_PIXEL_FORMAT_RGB_888;

vector<void *> g_out_buffer_pool[PNGD_MAX_CHN_NUM];
pthread_mutex_t g_out_buffer_pool_lock[PNGD_MAX_CHN_NUM];

static uint64_t g_end_get_time[PNGD_MAX_CHN_NUM] = {0};
static uint64_t g_start_send_time[PNGD_MAX_CHN_NUM] = {0};
static PNGD_THREAD_PARAM_S g_pngd_thread_param[PNGD_MAX_CHN_NUM]{};

const uint32_t PNGD_PERFOR_MODE_BUF_NUM   = 6;
const uint32_t PNGD_PERFOR_MODE_QUERY_CNT = 20000;

static void print_pngd_chn_status(int32_t chn)
{
    SAMPLE_PRT("---------------------------------------------------------------------------------------------------\n");
    SAMPLE_PRT("chn:%d, SendFrame:%u, DecodeFrames:%u, DecodeSucc:%u, DecodeFail:%u\n",
        chn,
        g_pngd_thread_param[chn].u32SendSucc,
        g_pngd_thread_param[chn].u32Decoded,
        g_pngd_thread_param[chn].u32DecodeSucc,
        g_pngd_thread_param[chn].u32DecodeFail);
    SAMPLE_PRT("---------------------------------------------------------------------------------------------------\n");
}

static int32_t save_file_type(hi_pixel_format pixel_format,
                              hi_compress_mode compress_mode,
                              char *type_name,
                              uint32_t type_name_len)
{
    int32_t ret;
    if (compress_mode == HI_COMPRESS_MODE_HFBC) {
        ret = snprintf(type_name, type_name_len - 1, "hfbc");
    } else if (pixel_format == HI_PIXEL_FORMAT_RGB_888) {
        ret = snprintf(type_name, type_name_len - 1, "rgb888");
    } else if (pixel_format == HI_PIXEL_FORMAT_BGR_888) {
        ret = snprintf(type_name, type_name_len - 1, "bgr888");
    } else if (pixel_format == HI_PIXEL_FORMAT_ARGB_8888) {
        ret = snprintf(type_name, type_name_len - 1, "argb8888");
    } else if (pixel_format == HI_PIXEL_FORMAT_RGBA_8888) {
        ret = snprintf(type_name, type_name_len - 1, "rgba8888");
    } else if (pixel_format == HI_PIXEL_FORMAT_ABGR_8888) {
        ret = snprintf(type_name, type_name_len - 1, "abgr8888");
    } else if ((pixel_format >= HI_PIXEL_FORMAT_YUV_400) && (pixel_format < HI_PIXEL_FORMAT_BUTT)) {
        ret = snprintf(type_name, type_name_len - 1, "yuv");
    } else {
        SAMPLE_PRT("pixel_format type err\n");
        return HI_FAILURE;
    }

    return ret;
}

static inline void pngd_get_time_stamp_us(uint64_t *val)
{
    struct timeval stTimeVal;
    gettimeofday(&stTimeVal, nullptr);
    *val = (uint64_t)stTimeVal.tv_sec * MULTIPLE_S_TO_US + stTimeVal.tv_usec;
}

void pngd_usage(char *sPrgNm)
{
    aclError aclRet = aclrtGetRunMode(&g_run_mode);
    if (aclRet == ACL_SUCCESS) {
        if (g_run_mode == ACL_HOST) {
            SAMPLE_PRT(" Running in Host!\n");
        } else if (g_run_mode == ACL_DEVICE) {
            SAMPLE_PRT(" Running in Device!\n");
        } else {
            SAMPLE_PRT(" Running in Invalid platform! runMode:%u\n", g_run_mode);
            return;
        }
    } else {
        SAMPLE_PRT(" Get run mode fail! acl ret:%#x\n", aclRet);
        return;
    }

    SAMPLE_PRT("\n/*********************************************************/\n");
    SAMPLE_PRT("Usage :\n");
    SAMPLE_PRT("\t:example: ./pngd_demo --in_image_file png_gray_32x32.png\
 --img_width 32 --img_height 32 --pix
// ... (truncated due to length) ...

```

### `cplusplus/level1_single_api/7_dvpp/pngd_sample/src/sample_pngd.cpp`
```cpp
/**
 *  Copyright [2021] Huawei Technologies Co., Ltd
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <cstring>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/ioctl.h>
#include <sys/poll.h>
#include <sys/time.h>
#include <fcntl.h>
#include <cerrno>
#include <pthread.h>
#include <cmath>
#include <unistd.h>
#include <csignal>
#include "sample_comm.h"
#include <vector>

using namespace std;

/******************************************************************************
* function    : main()
* Description : pngd ddk sample
******************************************************************************/
int32_t main(int32_t argc, char *argv[])
{
    int32_t ret;
    pthread_t pngdSendThreadTid[PNGD_MAX_CHN_NUM] = {0};
    pthread_t pngdGetThreadTid[PNGD_MAX_CHN_NUM] = {0};

    if (argc < 4) {
        SAMPLE_PRT("\nInput parameter's num:%d is not enough!\n", argc);
        pngd_usage(argv[0]);
        return HI_FAILURE;
    }

    ret = get_option(argc, &(*argv));
    if (ret != HI_SUCCESS) {
        SAMPLE_PRT("get_option failed!\n");
        return HI_FAILURE;
    }

    ret = check_option();
    if (ret != HI_SUCCESS) {
        SAMPLE_PRT("check_option failed!\n");
        return HI_FAILURE;
    }

    print_arguement();

    ret = setup_acl_device();
    if (ret != HI_SUCCESS) {
        SAMPLE_PRT("Setup Device failed! ret code:%#x\n", ret);
        return HI_FAILURE;
    }

    ret = hi_mpi_sys_init();
    if (ret != HI_SUCCESS) {
        SAMPLE_PRT("hi_mpi_sys_init failed!\n");
        return HI_FAILURE;
    }

    ret = pngd_create();
    if (ret != HI_SUCCESS) {
        SAMPLE_PRT("start PNGD fail for %#x!\n", ret);
        int32_t exit_ret = deinit_pngd_mod();
        if (exit_ret != HI_SUCCESS) {
            SAMPLE_PRT("exit PNGD fail for %#x!\n", exit_ret);
        }
        return ret;
    }

    pngd_init_start_time();

    ret = pngd_start_send_stream(&pngdSendThreadTid[0]);
    if (ret != 0) {
        pngd_stop_send_stream();
    } else {
        ret = pngd_start_get_pic(&pngdGetThreadTid[0]);
        if (ret != 0) {
            pngd_stop_send_stream();
            pngd_stop_get_pic();
        }
    }

    pngd_cmd_ctrl(&pngdSendThreadTid[0], &pngdGetThreadTid[0]);

    pngd_show_decode_state();

    ret = deinit_pngd_mod();
    if (ret != HI_SUCCESS) {
        SAMPLE_PRT("exit PNGD fail for %#x!\n", ret);
    }

    return ret;
}


```
