"""How do we eliminate some of the boilerplate between having python functions
and making them pydantic?

>>> from i2.tests.objects_for_testing import formula1
>>> test_func_to_pyd_model_of_inputs(formula1)
>>> pyd_input_model = func_to_pyd_input_model_cls(formula1)
>>> pyd_input_model
<class 'pydantic.main.formula1'>
>>> from i2 import Sig
>>> Sig(formula1)
<Sig (w, /, x: float, y=1, *, z: int = 1)>
>>> Sig(pyd_input_model)
<Sig (*, w: Any, x: float, z: int = 1, y: int = 1) -> None>

>>> pyd_func = func_to_pyd_func(formula1)
>>> input_model_instance = pyd_input_model(w=1, x=2)
>>> input_model_instance
formula1(w=1, x=2.0, z=1, y=1)
>>> pyd_func(input_model_instance)
3.0
>>> formula1(1, x=2)  # can't say w=1 because w is position only
3

"""

from front.py2pydantic import *

from warnings import warn

warn(f"Module moved to front.py2pydantic: {__file__}")
