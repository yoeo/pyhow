""" Handle items conversion and value extraction. """

import math


# category: conversions


def bool_convert():
    """ bool: Convert an item to a boolean. """

    class _BooleanLike:
        def __bool__(self):
            return True

    return bool(_BooleanLike()) and "good vibes"


def bytes_convert():
    """ bytes: Convert an item to bytes string. """

    class _ByteLike:
        def __bytes__(self):
            return b"beat maker"

    return bytes(_ByteLike()).decode()


def complex_convert():
    """ complex: Convert an item to a complex number. """

    class _ComplexLike:
        def __complex__(self):
            return -1j

    return complex(_ComplexLike())


def float_convert():
    """ float: Convert an item to a floating point decimal. """

    class _FloatLike:
        def __float__(self):
            return float('nan')

    return float(_FloatLike())


def int_convert():
    """ int: Convert an item to an integer. """

    class _IntLike:
        def __int__(self):
            return 666

    return int(_IntLike())


def str_convert():
    """ str: Convert an item to a string. """

    class _StringLike:
        def __str__(self):
            return "vocoder"

    return str(_StringLike())


# category: value manipulation


def abs_method():
    """ abs: Absolute value of an item. """

    class _Absolute:
        def __abs__(self):
            return 13831

    return abs(_Absolute())


def divmod_operator():
    """ divmod(obj, other): Divison and modulo operation. """

    class _Divisible:
        def __divmod__(self, other):
            return (91, other % 91)

    return "{}{} techno".format(*divmod(_Divisible(), 92))


def format_method():
    """ format: Formated representation of an item. """

    class _Formatable:
        def __format__(self, spec):
            return spec.format('djembe')

    return format(_Formatable(), "hit my {}")


def hash_method():
    """ hash: An integer represetation of a value of an object. """

    class _Hashable:
        def __hash__(self):
            return 10001

    return hash(_Hashable())


def repr_method():
    """ repr: Basic representation of an item. """

    class _Representable:
        def __repr__(self):
            return "<- deep soul ->"

    return repr(_Representable())


def round_method():
    """ round: Round an item to the closest integer. """

    class _Pi:
        def __round__(self, precision=0):
            return float('3.1415'[:precision+2])

    return round(_Pi(), 2)


def floor_method():
    """ math.floor(obj): Round to the nearest lower integer. """

    class _MinusPi:
        def __floor__(self):
            return -4

    return math.floor(_MinusPi())


def ceil_method():
    """ math.ceil(obj): Round to the nearest greater integer. """

    class _Pi:
        def __ceil__(self):
            return 4

    return math.ceil(_Pi())


def trunc_method():
    """ math.trunc(obj): Round to the integer nearest to zero. """

    class _MinusPi:
        def __trunc__(self):
            return -3

    return math.trunc(_MinusPi())



