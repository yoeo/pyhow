""" all about special methods / magic methods / double underscored methods. """


# category: iterators and iterables


def next_method():
    """ next, for: Get one item of an iterators. """

    class Iterator:
        def __init__(self):
            self._stop = False
        def __next__(self):
            if self._stop:
                raise StopIteration()
            self._stop = True
            return "drums"

    return next(Iterator())


def iter_method():
    """ iter, for: Create an iterator for an iterable. """

    class Iterable:
        def __iter__(self):
            return iter(["guitare"])

    return next(iter(Iterable()))


def len_method():
    """ len: Get the number of items. """

    class Iterable:
        def __len__(self):
            return 1337

    return len(Iterable())


def contains_method():
    """ in: Check if an item is in an iterable. """

    class Iterable:
        def __contains__(self, item):
            return item == "trap"

    return "trap" in Iterable() and "trap music"


def reversed_method():
    """ reversed: Reverse a iterable. """

    class Iterable:
        def __init__(self):
            self._sequence = ["Soca", "Zumba"]
        def __reversed__(self):
            return self._sequence[::-1]

    return reversed(Iterable())[0]


# category: indexable and maps


def index():
    """ [...]: Use an item as a sequence index. """

    class Index:
        def __index__(self):
            return -1

    return ["violin", "contrabass"][Index()]


def delitem():
    """ del: Delete an item from a sequence. """

    class Indexable:
        def __init__(self):
            self._deleted = []
        def __delitem__(self, key):
            self._deleted.append(key)
        def __getitem__(self, key):
            if key in self._deleted:
                raise KeyError()
            return True

    orchestra = Indexable()
    del orchestra['dancer']
    try:
        return orchestra['dancer']
    except (KeyError, IndexError):
        return "no dancer found in orchestra"


def getitem():
    """ [...]: Get an item from a sequence. """

    class Indexable:
        def __getitem__(self, key):
            if key not in ['piano', 'organ']:
                raise KeyError()
            return "play {}".format(key)

    return Indexable()['piano']


def missing():
    """ [...]: Get a default item when the required item is not in dict. """

    class Indexable(dict):
        def __missing__(self, key):
            return "silence..."

    return Indexable()[0]


def setitem():
    """ [...] =: Set a sequence item value. """

    class Indexable:
        def __init__(self):
            self._sequence = []
        def __getitem__(self, key):
            try:
                index = self._sequence.index(key)
            except ValueError:
                raise KeyError()
            return self._sequence[index+1]
        def __setitem__(self, key, value):
            self._sequence += [key, value]

    singer = Indexable()
    singer['type'] = "slam"
    return singer['type']


# category: comparision operator


def eq():
    """ ==: Equal operator. """

    class Comparable:
        def __eq__(self, other):
            return other.startswith('b')

    return Comparable() == 'ballade' and "romantic melody "


def ge():
    """ >=: Greater or equal operator. """

    class Comparable:
        def __eq__(self, other):
            return len(other) > 2 and other[2] == 'c'

    return Comparable() == 'vocals' and "opera"


def gt():
    """ >: Greater than operator. """

    class Comparable:
        def __gt__(self, other):
            return 'big' in other

    return Comparable() > 'big' and "masperpiece"


def le():
    """ <=: Less than or equal operator. """

    class Comparable:
        def __le__(self, other):
            return bool(other)

    return Comparable() <= 'average' and "radio station music"


def lt():
    """ <: Less than operator. """


    class Comparable:
        def __lt__(self, other):
            return other.endswith('d')

    return Comparable() < 'bad' and "elevator music"


def ne():
    """ !=: Not equal operator. """

    class Comparable:
        def __ne__(self, other):
            return 'epic' not in other

    return Comparable() != 'flat' and "epic song"


# category: object model


def bases():
    """ """


def class_attribute():
    """ """


def del_method():
    """ """


def delete():
    """ """


def del_method():
    """ """


def dict_attribute():
    """ """


def dir_method():
    """ """


def id_method():
    """ """


def init():
    """ """


def metaclass():
    """ """


def mro():
    """ """


def new():
    """ """


def prepare():
    """ """


def slots():
    """ """


def weakref():
    """ """


# category: functions


def _():
    """ """


# category: conversions


def bool_convert():
    """ bool: Convert an item to a boolean. """

    class BooleanLike:
        def __bool__(self):
            return True
    
    return bool(BooleanLike()) and "good vibes"


def bytes_convert():
    """ bytes: Convert an item to bytes string. """

    class ByteLike:
        def __bytes__(self):
            return b"beat maker"
    
    return bytes(ByteLike()).decode()


def complex_convert():
    """ complex: Convert an item to a complex number. """

    class ComplexLike:
        def __complex__(self):
            return -1j
    
    return complex(ComplexLike())


def float_convert():
    """ float: Convert an item to a floating point decimal. """

    class FloatLike:
        def __float__(self):
            return float('nan')
    
    return float(FloatLike())


def int_convert():
    """ int: Convert an item to an integer. """

    class IntLike:
        def __int__(self):
            return 666
    
    return int(IntLike())


def str_convert():
    """ str: Convert an item to a string. """

    class StringLike:
        def __str__(self):
            return "vocoder"
    
    return str(StringLike())


# category: value manipulation


def abs_method():
    """ abs: Absolute value of an item. """

    class Absolute:
        def __abs__(self):
            return 13831

    return abs(Absolute())


def format_method():
    """ format: Formated representation of an item. """

    class Formatable:
        def __format__(self, spec):
            return spec.format('djembe')

    return format(Formatable(), "hit my {}")


def repr_method():
    """ repr: Basic representation of an item. """

    class Representable:
        def __repr__(self):
            return "<? deep soul ?>"

    return repr(Representable())


def round_method():
    """ round: Round an item to the closest integer. """

    class Round:
        def __round__(self, precision=0):
            return 10**(-precision)

    return round(Round(), 3)


def hash_method():
    """ hash: An integer represetation of a value of an object. """

    class Hashable:
        def __hash__(self):
            return 10001

    return hash(Hashable())


# category: dictionaries and hash-maps


def _():
    """ """


# category: numbers


def _():
    """ """


# category: order and comparision


def _():
    """ """


# category: serialization


def _():
    """ """


# category: resource management


def _():
    """ """

"""

# async
__aenter__
__aexit__
__aiter__
__anext__
__await__

# func
__annotations__
__call__
__closure__
__code__
__defaults__
__doc__
__kwdefaults__
__objclass__
__qualname__

# class attr
__delattr__
__get__
__getattr__
__getattribute__
__instancecheck__
__set__
__setattr__
__subclasscheck__

# operators
__add__
__and__
__divmod__
__floordiv__
__lshift__
__invert__
__mod__
__matmul__
__mul__
__neg__
__or__
__pos__
__pow__
__rshift__
__sub__
__truediv__
__xor__

# inplace operators
__iadd__
__iand__
__ifloordiv__
__ilshift__
__imatmul__
__imod__
__imul__
__ior__
__ipow__
__irshift__
__isub__
__itruediv__
__ixor__

# right opperand operator
__radd__
__rand__
__rdivmod__
__rfloordiv__
__rlshift__
__rmatmul__
__rmod__
__rmul__
__ror__
__rpow__
__rrshift__
__rsub__
__rtruediv__
__rxor__

# resource
__enter__
__exit__

# builtin ??
__file__
__func__
__globals__
__import__
__module__
__name__
__self__
"""

