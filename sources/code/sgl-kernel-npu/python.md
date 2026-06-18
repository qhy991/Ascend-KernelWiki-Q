---
id: code-sgl-kernel-npu-python
title: SGL Kernel NPU Python Package
type: source-code
repo: sgl-project/sgl-kernel-npu
path: python
url: https://github.com/sgl-project/sgl-kernel-npu/tree/main/python
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- sglang
- npu
- python
- inference
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- global-memory
techniques:
- kv-cache-paging
- pipeline-scheduling
kernel_types:
- attention
- matmul
- softmax
- layernorm
languages:
- python
---

# SGL Kernel NPU Python Package

SGL Kernel NPU Python package source. This path provides evidence for how native kernels are exposed to serving code and how Python wrappers select Ascend implementations.

## Code Location

- Repository: `sgl-project/sgl-kernel-npu`
- Path: `python`
- URL: https://github.com/sgl-project/sgl-kernel-npu/tree/main/python


## Fetched Source


### `python/deep_ep/setup.py`
```python
import os
import re
import subprocess

import setuptools
from setuptools import find_namespace_packages, find_packages
from setuptools.command.build_py import build_py
from setuptools.dist import Distribution

# Eliminate timestamp differences in whl compressed packages
os.environ["SOURCE_DATE_EPOCH"] = "0"

current_version = os.getenv("VERSION", "1.0.0")


class CustomBuildPy(build_py):
    def run(self):
        logging_type = (
            "DEBUG" if os.environ.get("DEBUG_MODE", "OFF") == "ON" else "INFO"
        )
        config_content = (
            "import logging\nlogging.basicConfig(level=logging.%s)" % logging_type
        )
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_file = os.path.join(script_dir, "deep_ep", "build_config.py")

        with open(config_file, "w") as f:
            f.write(config_content)

        super().run()


class BinaryDistribution(Distribution):
    """Distribution which always forces a binary package with platform name"""

    def has_ext_modules(self):
        return True


def get_git_revision():
    """
    Get the short (8 characters) hash value of the current Git repository
    Returns:
        str: A string with a '+' prefix and an 8-character hash value, or an empty string if retrieval fails
    """
    try:
        cmd = ["git", "rev-parse", "--short=8", "HEAD"]
        revision = "+" + subprocess.check_output(cmd).strip().decode("utf-8")
    except Exception:
        revision = ""
    return revision


def get_cann_version():
    """
    Get the CANN version information of the current environment
    Returns:
        str: CANN version string, format like 'cann.8.2.rc1.b231'
             Returns an empty string if retrieval fails
    """
    try:
        ascend_home = os.getenv("ASCEND_TOOLKIT_HOME", "")
        if not ascend_home:
            return ""

        arch = subprocess.check_output(["uname", "-m"]).decode().strip()
        arch = arch.lower()

        info_file = os.path.join(
            ascend_home, f"{arch}-linux", "ascend_toolkit_install.info"
        )
        if not os.path.exists(info_file):
            return ""

        with open(info_file, "r") as f:
            lines = f.readlines()

        version = ""
        b_version = ""
        for line in lines:
            line = line.strip()
            if line.startswith("version="):
                version = line.split("=")[1]
            elif line.startswith("innerversion="):
                match = re.search(r"[Bb](\d+)", line)
                if match:
                    b_version = match.group(1)

        if version and b_version:
            version = version.lower()
            b_version = b_version.lower()
            return f".cann.{version}.b{b_version}"
        return ""

    except Exception:
        return ""


git_rev = get_git_revision()
cann_ver = get_cann_version()

version_suffix = (
    f"{git_rev}{cann_ver}"
    if git_rev
    else f"+{cann_ver.lstrip('.')}" if cann_ver else ""
)

setuptools.setup(
    name="deep_ep",
    version=current_version + version_suffix,
    author="",
    author_email="",
    description="python api for deep_ep",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=["torch"],
    python_requires=">=3.7",
    package_data={"deep_ep": ["deep_ep_cpp.cpython*.so", "vendors", "vendors/**"]},
    distclass=BinaryDistribution,
    cmdclass={
        "build_py": CustomBuildPy,
    },
)

```

### `python/deep_ep/deep_ep/__init__.py`
```python
import os

import torch

current_dir = os.path.dirname(os.path.abspath(__file__))
opp_path = os.path.join(current_dir, "vendors", "hwcomputing")
lib_path = os.path.join(current_dir, "vendors", "hwcomputing", "op_api", "lib")
# Set environment variables related to custom operators
os.environ["ASCEND_CUSTOM_OPP_PATH"] = (
    f"{opp_path}:{os.environ.get('ASCEND_CUSTOM_OPP_PATH', '')}"
)
os.environ["LD_LIBRARY_PATH"] = f"{lib_path}:{os.environ.get('LD_LIBRARY_PATH', '')}"

from deep_ep_cpp import Config

# Import strategies to register them
from . import strategies
from .buffer import Buffer
from .ep_strategy import LowLatencyStrategy, NormalStrategy
from .utils import EventOverlap

```

### `python/deep_ep/deep_ep/utils.py`
```python
import functools
import inspect
import logging
import os
from typing import Optional, Tuple

import torch
import torch_npu
from deep_ep_cpp import Config, EventHandle


class EventOverlap:

    def __init__(
        self,
        event: Optional[EventHandle] = None,
        extra_tensors: Optional[Tuple[torch.Tensor]] = None,
    ) -> None:
        """
        Initialize the class.

        Arguments:
            event: the CUDA event captured.
            extra_tensors: an easier way to simulate PyTorch tensor `record_stream`, may be useful with CUDA graph.
        """
        self.event = event

        # NOTES: we use extra tensors to achieve stream recording, otherwise,
        # stream recording will be incompatible with CUDA graph.
        self.extra_tensors = extra_tensors

    def current_stream_wait(self) -> None:
        pass


logger = logging.getLogger()
torch.set_printoptions(profile="full")


def get_simplify_tensor(arg):
    if type(arg) in (tuple, list):
        return ", ".join([get_simplify_tensor(a) for a in arg])
    elif isinstance(arg, torch.Tensor):
        return str((arg.dtype, arg.shape))
    return str(arg)


def log_parameters(input_name_full_tensor=None, output_idx_full_tensor=None):
    """
    A decorator for printing the input and output of functions.
    By default, tensors print dtype and shape.

    Arguments:
        input_name_full_tensor: input names of tensors that need to be fully printed.
        output_idx_full_tensor: output indexes of the tensor that needs to be fully printed.
    """
    if input_name_full_tensor is None:
        input_name_full_tensor = []
    if output_idx_full_tensor is None:
        output_idx_full_tensor = []

    def log_parameters_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            rank_info = "unknown"
            if logger.isEnabledFor(logging.DEBUG):
                sig = inspect.signature(func)
                bound_args = sig.bind(*args, **kwargs)
                bound_args.apply_defaults()

                self_instance = bound_args.arguments.get("self")
                if self_instance is not None and hasattr(self_instance, "rank"):
                    rank_info = str(self_instance.rank)

                param_str = "\n".join(
                    [
                        f"{k}: {v if k in input_name_full_tensor else get_simplify_tensor(v)}"
                        for k, v in bound_args.arguments.items()
                        if k not in ("self", "cls")
                    ]
                )
                logger.debug(
                    "[rank %s]" % rank_info
                    + f"Calling {func.__name__} with parameters:\n{param_str}"
                )

            result = func(*args, **kwargs)

            if logger.isEnabledFor(logging.DEBUG):
                if isinstance(result, tuple):
                    result_str_list = []
                    for idx, v in enumerate(result):
                        if idx in output_idx_full_tensor:
                            result_str_list.append(str(v))
                        else:
                            result_str_list.append(get_simplify_tensor(v))
                    result_str = "\n".join(result_str_list)
                else:
                    if 0 in output_idx_full_tensor:
                        result_str = str(result)
                    else:
                        result_str = get_simplify_tensor(result)

                logger.debug(
                    "[rank %s]" % rank_info
                    + f"Function {func.__name__} returned:\n{result_str}\n{func.__name__} returned value finish."
                )

            return result

        return wrapper

    return log_parameters_decorator

```
