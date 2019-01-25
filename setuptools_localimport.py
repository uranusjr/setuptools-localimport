import functools
import sys

import setuptools.build_meta


def _with_sys_path_patch(f):

    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        # The current directory is added into sys.path to emulate setuptools's
        # behavior when setup.py is run globally (i.e. no PEP 517 isolation)
        # to maintain backward compatibility. (pypa/setuptools#1642)
        sys_path = sys.path
        if "" not in sys.path:
            sys.path.insert(0, "")
        retval = f(*args, **kwargs)
        sys.path = sys_path
        return retval

    return wrapped


_HOOKS = [
    "build_wheel",
    "build_sdist",
    "get_requires_for_build_wheel",
    "prepare_metadata_for_build_wheel",
    "get_requires_for_build_sdist",
]

for name in _HOOKS:
    try:
        f = getattr(setuptools.build_meta, name)
    except AttributeError:
        continue
    globals()[name] = _with_sys_path_patch(f)
