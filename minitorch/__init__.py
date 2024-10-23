"""Autodifferentiation library for tensors, scalars, and neural network operations.

Includes modules for:
- Tensors and tensor operations (`tensor`, `tensor_ops`, `tensor_functions`)
- Scalars and scalar operations (`scalar`, `scalar_functions`)
- Automatic differentiation (`autodiff`)
- Optimization (`optim`)
- Neural network modules (`module`)
- Dataset handling (`datasets`)
- Testing utilities (`testing`)
"""

from .testing import MathTest, MathTestVariable  # type: ignore # noqa: F401,F403
from .tensor_data import *  # noqa: F401,F403
from .tensor import *  # noqa: F401,F403
from .tensor_ops import *  # noqa: F401,F403
from .tensor_functions import *  # noqa: F401,F403
from .datasets import *  # noqa: F401,F403
from .optim import *  # noqa: F401,F403
from .testing import *  # noqa: F401,F403
from .module import *  # noqa: F401,F403
from .autodiff import *  # noqa: F401,F403
from .scalar import *  # noqa: F401,F403
from .scalar_functions import *  # noqa: F401,F403
from .module import *  # noqa: F401,F403
