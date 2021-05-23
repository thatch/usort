# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

try:
    from .version import version as __version__  # noqa: F401
except ImportError:
    __version__ = "dev"

__all__ = ["__version__"]
