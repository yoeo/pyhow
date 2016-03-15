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
        def __ge__(self, other):
            return len(other) > 2 and other[2] == 'c'

    return Comparable() >= 'vocals' and "opera"


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


# category: object attributes


def delattr_method():
    """ __delattr__: Todo. """


def getattr_method():
    """ __getattr__: Todo. """


def getattribute_method():
    """ __getattribute__: Todo. """


def instancecheck_method():
    """ __instancecheck__: Todo. """


def setattr_method():
    """ __setattr__: Todo. """


def subclasscheck_method():
    """ __subclasscheck__: Todo. """


def subclasshook():
    """ __subclasshook__: Todo. """


# category: object descriptors


def delete_method():
    """ __delete__: Todo. """


def get_method():
    """ __get__: Todo. """


def set_method():
    """ __set__: Todo. """


# category: object model


def bases_attribute():
    """ cls.__bases__: Base classes of the current class. """

    class SubClass(str):
        """ str sub-class. """

    return "{}ing instruments".format(SubClass.__bases__[0].__name__)


def class_attribute():
    """ obj.__class__, type: Class of a given instance. """

    class BeatBox:
        """ BeatBox class. """

    return BeatBox().__class__.__name__


def del_method():
    """ del: Cleanup an item on destroy. """

    context = ""

    class Destroyable:
        def __del__(self):
            nonlocal context
            context = "burn the lyrics"

    item = Destroyable()
    del item
    return context


def dict_attribute():
    """ cls.__dict__: Bindings for class members. """

    class ItemClass:
        def get_message(self):
            return "podcasts are good for health"

    item = ItemClass()
    return type(item).__dict__['get_message'](item)


def dir_method():
    """ __dir__: Todo. """


def init_method():
    """ __init__: Todo. """


def metaclass_attribute():
    """ __metaclass__: Todo. """


def mro_attribute():
    """ __mro__: Todo. """


def new():
    """ __new__: Todo. """


def prepare():
    """ __prepare__: Todo. """


def slots():
    """ __slots__: Todo. """


def weakref():
    """ __weakref__: Todo. """


# category: functions


def annotations():
    """ __annotations__: Todo. """


def call():
    """ __call__: Todo. """


def closure():
    """ __closure__: Todo. """


def code():
    """ __code__: Todo. """


def defaults():
    """ __defaults__: Todo. """


def doc():
    """ __doc__: Todo. """


def kwdefaults():
    """ __kwdefaults__: Todo. """


def objclass():
    """ __objclass__: Todo. """


def qualname():
    """ __qualname__: Todo. """


def func():
    """ __func__: Todo. """


def self__attribute():
    """ __self__: Todo. """


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


def floor_metod():
    """ __floor__: Todo. """


def ceil_method():
    """ __ceil__: Todo. """


def trunc_method():
    """ __trunc__: Todo. """


def hash_method():
    """ hash: An integer represetation of a value of an object. """

    class Hashable:
        def __hash__(self):
            return 10001

    return hash(Hashable())


# category: serialization


def copy():
    """ __copy__: Todo. """


def deepcopy():
    """ __deepcopy__: Todo. """


def getstate():
    """ __getstate__: Todo. """


def reduce():
    """ __reduce__: Todo. """


def reduce_ex():
    """ __reduce_ex__: Todo. """


def getnewargs():
    """ __getnewargs__: Todo. """


def setstate():
    """ __setstate__: Todo. """


# category: resource management


def enter_exit():
    """ with: Use and release a resource."""

    class Resource:
        def __enter__(self):
            return "enter concert"
        def __exit__(self, error_class, error, traceback):
            pass

    with Resource() as resource:
        return resource


# category: asynchronious operations


def aenter():
    """ __aenter__: Todo. """


def aexit():
    """ __aexit__: Todo. """


def aiter():
    """ __aiter__: Todo. """


def anext():
    """ __anext__: Todo. """


def await():
    """ __await__: Todo. """


# category: numerical operators


def add_operator():
    """ __add__: Todo. """


def and_operator():
    """ __and__: Todo. """


def divmod_operator():
    """ __divmod__: Todo. """


def floordiv_operator():
    """ __floordiv__: Todo. """


def lshift_operator():
    """ __lshift__: Todo. """


def invert_operator():
    """ __invert__: Todo. """


def mod_operator():
    """ __mod__: Todo. """


def matmul_operator():
    """ __matmul__: Todo. """


def mul_operator():
    """ __mul__: Todo. """


def neg_operator():
    """ __neg__: Todo. """


def or_operator():
    """ __or__: Todo. """


def pos_operator():
    """ __pos__: Todo. """


def pow_operator():
    """ __pow__: Todo. """


def rshift_operator():
    """ __rshift__: Todo. """


def sub_operator():
    """ __sub__: Todo. """


def truediv_operator():
    """ __truediv__: Todo. """


def xor_operator():
    """ __xor__: Todo. """


# category: numerical operators, inplace changes


def iadd():
    """ __iadd__: Todo. """


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

