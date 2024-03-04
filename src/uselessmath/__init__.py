"""Init file to handle import of all submodules"""

__all__ = ["uadd", "usub", "umult", "udiv", "Umath"]

from uselessmath.arith import uadd, udiv, umult, usub
from uselessmath.exponents import ucube, usquare
from uselessmath.uclass import Umath
