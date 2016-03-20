""" Implementation of Python operators. """

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
    """ __radd__: Todo. """


def rand():
    """ __rand__: Todo. """


def rdivmod():
    """ __rdivmod__: Todo. """


def rfloordiv():
    """ __rfloordiv__: Todo. """


def rlshift():
    """ __rlshift__: Todo. """


def rmatmul():
    """ @: Right operand matrice multiply operator. """

    # TODO: @ operator, new in python 3.5
    return NotImplemented


def rmod():
    """ __rmod__: Todo. """


def rmul():
    """ __rmul__: Todo. """


def ror():
    """ __ror__: Todo. """


def rpow():
    """ __rpow__: Todo. """


def rrshift():
    """ __rrshift__: Todo. """


def rsub():
    """ __rsub__: Todo. """


def rtruediv():
    """ __rtruediv__: Todo. """


def rxor():
    """ __rxor__: Todo. """

