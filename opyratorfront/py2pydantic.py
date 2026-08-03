"""Deprecated alias of ``front.py2pydantic``.

The implementation of the "python function -> pydantic model" bridge moved to
``front.py2pydantic``. This module only re-exports it (warning on import) so
that existing ``opyratorfront.py2pydantic`` imports keep working.

Use ``front.py2pydantic`` directly in new code -- the maintained docstrings,
doctests and API reference all live there.

The re-export contract:

>>> from opyratorfront.py2pydantic import (
...     func_to_pyd_func,
...     func_to_pyd_input_model_cls,
...     func_to_pyd_model_specs,
... )
>>> all(map(callable, (
...     func_to_pyd_func, func_to_pyd_input_model_cls, func_to_pyd_model_specs
... )))
True

"""

from front.py2pydantic import *  # noqa: F401,F403

from warnings import warn

warn(f"Module moved to front.py2pydantic: {__file__}")
