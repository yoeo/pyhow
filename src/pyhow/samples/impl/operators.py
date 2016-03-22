""" Implementation of Python operators. """

# using unfinished example classes
# pylint: disable=no-self-use
# pylint: disable=too-few-public-methods

import math


# category: comparison


def eq_comparison():
    """ ==: Equal operator. """

    class _Comparable:
        def __eq__(self, other):
            return other.startswith('b')

    return _Comparable() == 'ballade' and "romantic melody "


def ge_comparison():
    """ >=: Greater or equal operator. """

    class _Comparable:
        def __ge__(self, other):
            return len(other) > 2 and other[2] == 'c'

    return _Comparable() >= 'vocals' and "opera"


def gt_comparison():
    """ >: Greater than operator. """

    class _Comparable:
        def __gt__(self, other):
            return 'big' in other

    return _Comparable() > 'big' and "masperpiece"


def le_comparison():
    """ <=: Less than or equal operator. """

    class _Comparable:
        def __le__(self, other):
            return bool(other)

    return _Comparable() <= 'average' and "radio station music"


def lt_comparison():
    """ <: Less than operator. """


    class _Comparable:
        def __lt__(self, other):
            return other.endswith('d')

    return _Comparable() < 'bad' and "elevator music"


def ne_comparison():
    """ !=: Not equal operator. """

    class _Comparable:
        def __ne__(self, other):
            return 'epic' not in other

    return _Comparable() != 'flat' and "epic song"


# category: unary operators


def invert_operator():
    """ ~: Bitwise "not" operator. """

    class _Operand:
        def __invert__(self):
            return "no boogie woogie"

    return ~_Operand()


def neg_operator():
    """ -: Unary negation operator. """

    class _Operand:
        def __neg__(self):
            return "no boogie woogie"

    return -_Operand()


def pos_operator():
    """ +: Unary plus operator. """

    class _Operand:
        def __pos__(self):
            return "happy disco"

    return +_Operand()


# category: binary operators, left operand implementation


def add_operator():
    """ +: Addition operator. """

    class _Operand:
        def __add__(self, other):
            return "alternative <{}>".format(other)

    return _Operand() + "jazz"


def and_operator():
    """ &: Bitwise "and" operator. """

    class _Operand:
        def __and__(self, other):
            return " and ".join(('rhythm', other))

    return _Operand() & 'blues'


def divmod_operator():
    """ divmod(obj, other): Divison and modulo operator. """

    class _Operand:
        def __divmod__(self, other):
            return (91, other % 91)

    return "{}{} techno".format(*divmod(_Operand(), 92))


def floordiv_operator():
    """ //: Division and floor operator. """

    class _Operand:
        def __floordiv__(self, other):
            return math.floor(34/other)

    return _Operand() // 5


def lshift_operator():
    """ <<: Shift left operator. """

    class _Operand:
        def __lshift__(self, other):
            return "hip-hop" + "!" * other

    return _Operand() << 5


def mod_operator():
    """ %: Modulo operator. """

    class _Operand:
        def __mod__(self, other):
            return 34 - other * (34 // other)

    return _Operand() % 5


def matmul_operator():
    """ @: Matrice multiplication operator. """

    # TODO: @ operator, new in python 3.5
    return NotImplemented


def mul_operator():
    """ *: Multiplication operator. """

    class _Operand:
        def __mul__(self, other):
            return "~".join("pop" for _ in range(other))

    return _Operand() * 3


def or_operator():
    """ |: Bitwise "or" operator. """

    class _Operand:
        def __or__(self, other):
            return " ~or~ ".join(('east coast', other))

    return _Operand() | 'dirty south'


def pow_operator():
    """ **: Power operator. """

    class _Operand:
        def __pow__(self, other):
            return "powefull {}".format(other)

    return _Operand()**'electro'



def rshift_operator():
    """ >>: Shift right operator. """

    class _Operand:
        def __rshift__(self, other):
            return "funky funk"[:-other]

    return _Operand() >> 5


def sub_operator():
    """ -: Substraction operator. """

    class _Operand:
        def __sub__(self, other):
            return "barbershop a cappella".replace(other, '').strip()

    return _Operand() - 'barbershop'


def truediv_operator():
    """ /: Division operator. """

    class _Operand:
        def __truediv__(self, other):
            return "hipster R&B"

    return _Operand() / 0


def xor_operator():
    """ ^: Exclusive "or" operator. """

    class _Operand:
        def __xor__(self, other):
            return "spiritual (^ ^) {}".format(other)

    return _Operand() ^ 'music'


# category: binary operators, inplace changes


def iadd():
    """ +=: Inplace plus operator. """

    class _Operand:
        def __init__(self):
            self.value = ''
        def __iadd__(self, other):
            self.value = " + ".join(('rock', other))
            return self

    item = _Operand()
    item += 'roll'
    return item.value


def iand():
    """ &=: Inplace bitwise "and" operator. """

    class _Operand:
        def __init__(self):
            self.value = ''
        def __iand__(self, other):
            self.value = "filtered by {}".format(bin(other))
            return self

    item = _Operand()
    item &= 3
    return item.value


def ifloordiv():
    """ //=: Inplace floor divide operator. """

    class _Operand:
        def __init__(self):
            self.value = ''
        def __ifloordiv__(self, other):
            self.value = "int(val/{})".format(other)
            return self

    item = _Operand()
    item //= 2
    return item.value


def ilshift():
    """ <<=: Inplace shift left operator. """

    class _Operand:
        def __init__(self):
            self.value = ''
        def __ilshift__(self, other):
            self.value = "{} digits added".format(other)
            return self

    item = _Operand()
    item <<= 4
    return item.value


def imatmul():
    """ @=: Inplace matrice multiplication operator. """

    # TODO: @ operator, new in python 3.5
    return NotImplemented


def imod():
    """ %=: Inplace modulo operator. """

    class _Operand:
        def __init__(self):
            self.value = ''
        def __imod__(self, other):
            self.value = "less_than({})".format(other)
            return self

    item = _Operand()
    item %= 4
    return item.value


def imul():
    """ *=: Inplace multiplication operator. """

    class _Operand:
        def __init__(self):
            self.value = ''
        def __imul__(self, other):
            self.value = "{} times".format(other)
            return self

    item = _Operand()
    item *= 5
    return item.value


def ior():
    """ |=: Inplace bitwise "or" operator. """

    class _Operand:
        def __init__(self):
            self.value = ''
        def __ior__(self, other):
            self.value = "filled with {}".format(bin(other))
            return self

    item = _Operand()
    item |= 6
    return item.value


def ipow():
    """ **=: Inplace power operator. """

    class _Operand:
        def __init__(self):
            self.value = ''
        def __ipow__(self, other):
            self.value = "exponent_{}".format(other)
            return self

    item = _Operand()
    item **= 7
    return item.value


def irshift():
    """ >>=: Inplace right shift operator. """

    class _Operand:
        def __init__(self):
            self.value = ''
        def __irshift__(self, other):
            self.value = "erase {} bits".format(other)
            return self

    item = _Operand()
    item >>= 8
    return item.value


def isub():
    """ -=: Inplace subtract operator. """

    class _Operand:
        def __init__(self):
            self.value = ''
        def __isub__(self, other):
            self.value = "{} missing".format(other)
            return self

    item = _Operand()
    item -= 9
    return item.value


def itruediv():
    """ /=: Inplace divide operator. """

    class _Operand:
        def __init__(self):
            self.value = ''
        def __itruediv__(self, other):
            self.value = "can you divide by {}".format(other)
            return self

    item = _Operand()
    item /= 0
    return item.value


def ixor():
    """ ^=: Inplace exclusive "or" operator. """

    class _Operand:
        def __init__(self):
            self.value = ''
        def __ixor__(self, other):
            self.value = "remove bits matching {}".format(bin(other))
            return self

    item = _Operand()
    item ^= 9
    return item.value


# category: binary operators, right operand implementation


def radd():
    """ +: Right operand addition operator. """

    class _Operand:
        def __radd__(self, other):
            return "{} more".format(other)

    return 5 + _Operand()


def rand():
    """ &: Right operand bitwise "and" operator. """

    class _Operand:
        def __rand__(self, other):
            return "choose bits from {}".format(other)

    return 4 & _Operand()


def rdivmod():
    """ rdivmod(obj, other): Right operand divison and modulo operation. """

    class _Operand:
        def __rdivmod__(self, other):
            return "{0}_divided & {0}_modulated".format(other)

    return divmod(13, _Operand())


def rfloordiv():
    """ : Right operand floor divide operator. """

    class _Operand:
        def __rfloordiv__(self, other):
            return "zero" if other == 0 else "something"

    return  0 // _Operand()


def rlshift():
    """ : Right operand shift left operator. """

    class _Operand:
        def __rlshift__(self, other):
            return "{} and many 0s".format(other)

    return  1 << _Operand()


def rmatmul():
    """ @: Right operand matrice multiply operator. """

    # TODO: @ operator, new in python 3.5
    return NotImplemented


def rmod():
    """ %: Right operand modulo operator. """

    class _Operand:
        def __rmod__(self, other):
            return "{} modulo self".format(other)

    return 2 % _Operand()


def rmul():
    """ *: Right operand multiply operator. """

    class _Operand:
        def __rmul__(self, other):
            return "{} repeated".format(other)

    return  3 * _Operand()


def ror():
    """ |: Right operand bitwise "or" operator. """

    class _Operand:
        def __ror__(self, other):
            return "keep true bits of {}".format(other)

    return  4 | _Operand()


def rpow():
    """ **: Right operand power operator. """

    class _Operand:
        def __rpow__(self, other):
            return "elevated {} to power".format(other)

    return  5**_Operand()


def rrshift():
    """ >>: Right operand shift right operator. """

    class _Operand:
        def __rrshift__(self, other):
            return "low bits taken from {}".format(other)

    return  6 >> _Operand()


def rsub():
    """ -: Right operand substract operator. """

    class _Operand:
        def __rsub__(self, other):
            return "inferior to {}".format(other)

    return  7 - _Operand()


def rtruediv():
    """ /: Right operand divide operator. """

    class _Operand:
        def __rtruediv__(self, other):
            return "inverted" if other == 1 else "something"

    return  1 / _Operand()


def rxor():
    """ ^: Right operand exclusive "or" operator. """

    class _Operand:
        def __rxor__(self, other):
            return "select unmatching bits from {}".format(other)

    return  8 ^ _Operand()

