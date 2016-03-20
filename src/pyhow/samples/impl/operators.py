""" Implementation of Python operators. """


# category: comparison operator


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


# category: numerical operators


def add_operator():
    """ +: Addition operator. """

    class Operand:
        def __add__(self, other):
            return "alternative <{}>".format(other)

    return Operand() + "jazz"


def and_operator():
    """ &: Bitwise "and" operator. """

    class Operand:
        def __and__(self, other):
            return " and ".join(('rhythm', other))

    return Operand() & 'blues'


def floordiv_operator():
    """ //: Division and floor operator. """

    class Operand:
        def __floordiv__(self, other):
            return math.floor(34/other)

    return Operand() // 5


def lshift_operator():
    """ <<: Shift left operator. """

    class Operand:
        def __lshift__(self, other):
            return "hip-hop" + "!" * other

    return Operand() << 5


def invert_operator():
    """ ~: Bitwise "not" operator. """

    class Operand:
        def __invert__(self):
            return "no boogie woogie"

    return ~Operand()


def mod_operator():
    """ %: Modulo operator. """

    class Operand:
        def __mod__(self, other):
            return 34 - other * (34 // other)

    return Operand() % 5


# TODO: @ operator, new in python 3.5
def matmul_operator():
    """ @: Matrice multiplication operator. """


def mul_operator():
    """ *: Multiplication operator. """

    class Operand:
        def __mul__(self, other):
            return "~".join("pop" for _ in range(other))

    return Operand() * 3


def neg_operator():
    """ -: Unary negation operator. """

    class Operand:
        def __neg__(self):
            return "no boogie woogie"

    return -Operand()


def or_operator():
    """ |: Bitwise "or" operator. """

    class Operand:
        def __or__(self, other):
            return " ~or~ ".join(('east coast', other))

    return Operand() | 'dirty south'


def pos_operator():
    """ +: Unary plus operator. """

    class Operand:
        def __pos__(self):
            return "happy disco"

    return +Operand()


def pow_operator():
    """ **: Power operator. """

    class Operand:
        def __pow__(self, other):
            return "powefull {}".format(other)

    return Operand()**'electro'



def rshift_operator():
    """ >>: Shift right operator. """

    class Operand:
        def __rshift__(self, other):
            return "funky funk"[:-other]

    return Operand() >> 5


def sub_operator():
    """ -: Substraction operator. """

    class Operand:
        def __sub__(self, other):
            return "barbershop a cappella".replace(other, '').strip()

    return Operand() - 'barbershop'


def truediv_operator():
    """ /: Division operator. """

    class Operand:
        def __truediv__(self, other):
            return "hipster R&B"

    return Operand() / 0


def xor_operator():
    """ ^: Exclusive "or" operator. """

    class Operand:
        def __xor__(self, other):
            return "spiritual (^ ^) {}".format(other)

    return Operand() ^ 'music'


# category: numerical operators, inplace changes


def iadd():
    """ +: Unary plus operator. """

    class Operand:
        def __iadd__(self, other):
            self.value = " + ".join(('rock', other))
        def __repr__():
            return self.value

    item = Operand()
    item += 'roll'
    return item


def iand():
    """ __iand__: Todo. """


def ifloordiv():
    """ __ifloordiv__: Todo. """


def ilshift():
    """ __ilshift__: Todo. """


def imatmul():
    """ __imatmul__: Todo. """


def imod():
    """ __imod__: Todo. """


def imul():
    """ __imul__: Todo. """


def ior():
    """ __ior__: Todo. """


def ipow():
    """ __ipow__: Todo. """


def irshift():
    """ __irshift__: Todo. """


def isub():
    """ __isub__: Todo. """


def itruediv():
    """ __itruediv__: Todo. """


def ixor():
    """ __ixor__: Todo. """


# category: numerical operators, right operand implementation


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
    """ __rmatmul__: Todo. """


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

