""" all about special methods / magic methods / double underscored methods. """

# using exemple classes that do not have public methods
# pylint: disable=too-few-public-methods

import copy
import math
import pickle
import weakref


# category: iterators and iterables


def next_method():
    """ next, for: Get one item of an iterators. """

    class _Iterator:
        def __init__(self):
            self._stop = False
        def __next__(self):
            if self._stop:
                raise StopIteration()
            self._stop = True
            return "drums"

    return next(_Iterator())


def iter_method():
    """ iter, for: Create an iterator for an iterable. """

    class _Iterable:
        def __iter__(self):
            return iter(["guitare"])

    return next(iter(_Iterable()))


def len_method():
    """ len: Get the number of items. """

    class _Iterable:
        def __len__(self):
            return 1337

    return len(_Iterable())


def contains_method():
    """ in: Check if an item is in an iterable. """

    class _Iterable:
        def __contains__(self, item):
            return item == "trap"

    return "trap" in _Iterable() and "trap music"


def reversed_method():
    """ reversed: Reverse a iterable. """

    class _Iterable:
        def __init__(self):
            self._sequence = ["Soca", "Zumba"]
        def __reversed__(self):
            return self._sequence[::-1]

    return next(iter(reversed(_Iterable())))


# category: indexable and maps


def index():
    """ [...]: Use an item as a sequence index. """

    class _Index:
        def __index__(self):
            return -1

    return ["violin", "contrabass"][_Index()]


def delitem():
    """ del: Delete an item from a sequence. """

    class _Indexable:
        def __init__(self):
            self._deleted = []
        def __delitem__(self, key):
            self._deleted.append(key)
        def __getitem__(self, key):
            if key in self._deleted:
                raise KeyError()
            return True

    orchestra = _Indexable()
    del orchestra['dancer']
    try:
        return orchestra['dancer']
    except (KeyError, IndexError):
        return "no dancer found in orchestra"


def getitem():
    """ [...]: Get an item from a sequence. """

    class _Indexable:
        def __getitem__(self, key):
            if key not in ['piano', 'organ']:
                raise KeyError()
            return "play {}".format(key)

    return _Indexable()['piano']


def missing():
    """ [...]: Get a default item when the required item is not in dict. """

    class _Indexable(dict):
        def __missing__(self, key):
            return "silence..."

    return _Indexable()[0]


def setitem():
    """ [...] =: Set a sequence item value. """

    class _Indexable:
        def __init__(self):
            self._sequence = []
        def __getitem__(self, key):
            try:
                return self._sequence[self._sequence.index(key)+1]
            except ValueError:
                raise KeyError()
        def __setitem__(self, key, value):
            self._sequence += [key, value]

    singer = _Indexable()
    singer['type'] = "slam"
    return singer['type']


# category: comparision operator


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


# category: object attributes


def delattr_method():
    """ del, delattr: Remove an attribute. """

    class _ItemClass:
        def __init__(self):
            self._deleted = set()
        def __getattr__(self, attribute):
            if attribute in self._deleted:
                raise AttributeError()
            return 321
        def __delattr__(self, attribute):
            self._deleted.add(attribute)

    item = _ItemClass()
    delattr(item, 'value')
    try:
        _ = item.value
    except AttributeError:
        return "drop da bass"


def dir_method():
    """ dir: List of accessible attributes and methods. """

    class _ItemClass:
        def __dir__(self):
            return ['ghost_attribute'] + list(self.__dict__.keys())
        def __getattr__(self, attribute):
            if attribute != 'ghost_attribute':
                raise AttributeError()
            return "Fantom Flutist"

    item = _ItemClass()
    return 'ghost_attribute' in dir(item) and item.ghost_attribute


def getattr_method():
    """ obj.attr, getattr: Produce a value for missing attributes. """

    class _ItemClass:
        def __init__(self):
            self.value_found = True
        def __getattr__(self, attribute):
            return "sweet stream"

    item = _ItemClass()
    return item.value_found and item.value_missing


def getattribute_method():
    """ obj.attr, getattr: Produce a value for all attributes. """

    class _ItemClass:
        def __init__(self):
            self.value_found = True
        def __getattribute__(self, attribute):
            return Ellipsis

    item = _ItemClass()
    return item.value_found == item.value_missing == ... and "Make some Noise"


def setattr_method():
    """ obj.attr=, setattr: Change value of all attributes. """

    class _ItemClass:
        value = ...
        def __init__(self):
            self.value = "spit some more rap"
        def __setattr__(self, attribute, value):
            _ItemClass.value = value

    return _ItemClass() and _ItemClass.value


# category: object class hierarchy


def instancecheck_method():
    """ isinstance: Check if item is an instance of a class. """

    class _MetaBase(type):
        def __instancecheck__(self, item):
            return 'x' in item

    class _Base(metaclass=_MetaBase):
        pass

    item = "saxophone"
    return isinstance(item, _Base) and item


def prepare():
    """ __prepare__: Todo. """


def subclasscheck_method():
    """ issubclass: Check if a class is a subclass of an other one. """

    class _MetaBase(type):
        def __subclasscheck__(self, cls):
            return 's' in cls.__name__

    class _Base(metaclass=_MetaBase):
        pass

    item = "xylophone"
    return issubclass(type(item), _Base) and item


def subclasshook():
    """ __subclasshook__: Todo. """




# category: object descriptors


def delete_method():
    """ __delete__: Todo. """


def get_method():
    """ __get__: Todo. """


def set_method():
    """ __set__: Todo. """


def mro_attribute():
    """ __mro__: Todo. """


# category: object model


def bases_attribute():
    """ cls.__bases__: Base classes of the current class. """

    class _SubClass(str):
        """ str sub-class. """

    return "{}ing instruments".format(_SubClass.__bases__[0].__name__)


def class_attribute():
    """ obj.__class__, type: Class of a given instance. """

    class _BeatBox:
        """ BeatBox class. """

    return _BeatBox().__class__.__name__


def del_method():
    """ del: Cleanup an item on destroy. """

    context = ""

    class _Destroyable:
        def __del__(self):
            nonlocal context
            context = "burn the lyrics"

    item = _Destroyable()
    del item
    return context


def dict_attribute():
    """ cls.__dict__: Bindings for class members. """

    class _ItemClass:
        def get_message(self):
            """ Give a positive message. """
            return "podcasts are good for self({})".format(id(self))

    item = _ItemClass()
    return type(item).__dict__['get_message'](item)


def init_method():
    """ Cls(): Initialize a new object. """

    class _ItemClass:
        def __init__(self, value):
            self.value = value

    return _ItemClass("silento").value


def new_method():
    """ Cls(): Create an object. """

    class _ItemClass:
        def __new__(cls):
            item = object.__new__(cls)
            item.value = "trumpet"
            return item

    return _ItemClass().value


def slots_attribute():
    """ obj.__slots__: Freaze the available attributes list. """

    class _ItemClass:
        __slots__ = ('value_found',)

    item = _ItemClass()
    item.value_found = "harmonica"
    try:
        item.value_missing = ...
    except AttributeError:
        return item.value_found


def weakref_attribute():
    """ obj.__weakref__, weakref.ref(obj): Weak references to an item. """

    class _ItemClass:
        pass

    item = _ItemClass()
    ref_item = weakref.ref(item)
    return ref_item is item.__weakref__ and "tap dance"


# category: functions


def annotations():
    """ func.__annotations__: Annotations for function parameters. """

    def _function(value: int) -> float:
        return float(value)

    return (
        _function.__annotations__['value'] is int and
        _function.__annotations__['return'] is float and "phone ringtone")


def call():
    """ func(): "Call" an item as a function. """

    class _FunctionLike:
        def __call__(self, value):
            return "{} beepping".format(value)

    return _FunctionLike()('pager')


def closure():
    """ func.__closure__: Variables trapped inside a function. """

    def _wrapper():
        encapsulated = "dial tone"
        def _wrapped():
            nonlocal encapsulated
        return _wrapped

    function = _wrapper()
    return function.__closure__[0].cell_contents


def code():
    """ eval, exec: Access the bytecode of a function. """

    def _function():
        return "vibrating device"

    return eval(_function.__code__)


def defaults():
    """ func.__defaults__: Default values of function parameters. """

    def _function(value="notification sound"):
        pass

    return _function.__defaults__[0]


def doc():
    """ func.__doc__, help(func): Docstring of a function. """

    def _function():
        " MIDI sheet music "

    return _function.__doc__.strip()


def kwdefaults():
    """ func.__kwdefaults__: Default values of keyword only parameters. """

    def _function(*_, value="phone alarm"):
        pass

    return _function.__kwdefaults__['value']


def name():
    """ f.__name__: The short name of the function. """

    class _New:
        class _Message:
            @staticmethod
            def _mutted():
                pass

    return _New._Message._mutted.__name__


def qualname():
    """ func.__qualname__: The full name of the function. """

    class _New:
        class _EMail:
            @staticmethod
            def _sound():
                pass

    return ''.join(_New._EMail._sound.__qualname__.split('.')[-3:])


def func():
    """ obj.meth.__func__: The unbound version of an instance method. """

    class _ItemClass:
        def _function(self):
            return self

    item = _ItemClass()
    return item._function.__func__("low battery chime")


def self_attribute():
    """ obj.meth.__self__: Instance bounded to a method. """

    class _ItemClass:
        def _function(self):
            return "device restart tone"

    item = _ItemClass()._function.__self__
    return item._function()


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


# category: copy and serialization


def copy_method():
    """ copy.copy(obj): Copy the content of an item. """

    class _Copyable:
        def __init__(self, value):
            self.value = value
        def __copy__(self):
            return _Copyable(self.value)

    return copy.copy(_Copyable("movie soundtrack")).value


def deepcopy_method():
    """ copy.deepcopy(obj): Recursively copy the content of an item. """

    class _Copyable:
        def __init__(self, values):
            self.values = values
        def __deepcopy__(self, memory):
            return _Copyable(copy.deepcopy(self.values, memo=memory))

    return '~'.join(copy.deepcopy(_Copyable(['anime', 'opening'])).values)


def getstate_method():
    """ pickle.dumps(obj): Get the "__dict__" of the serialized instance. """

    class _Serializable:
        def __getstate__(self):
            return {'value': "series credits song"}

    globals()['_Serializable'] = _Serializable
    value = pickle.loads(pickle.dumps(_Serializable())).value
    del globals()['_Serializable']

    return value


def reduce_method():
    """ pickle.dumps(obj): Info needed to rebuild the serialized instance. """

    def _build(value):
        item = _Serializable()
        item.value = "sorry for the {}".format(value)
        return item

    class _Serializable:
        def __reduce__(self):
            return (_build, ('intermission',))

    globals()['_build'] = _build
    globals()['_Serializable'] = _Serializable
    value = pickle.loads(pickle.dumps(_Serializable())).value
    del globals()['_build']
    del globals()['_Serializable']

    return value


def reduce_ex_method():
    """ pickle.dumps(obj): Same as "__reduce__" with protocole version. """

    def _build(value):
        item = _Serializable()
        item.value = "sorry for the {}".format(value)
        return item

    class _Serializable:
        def __reduce_ex__(self, protocol_version):
            if protocol_version == 0:
                return (_build, ('long intro music',))
            else:
                return (_Serializable.__new__, (_Serializable,))

    globals()['_build'] = _build
    globals()['_Serializable'] = _Serializable
    value = pickle.loads(pickle.dumps(_Serializable(), 0)).value
    del globals()['_build']
    del globals()['_Serializable']

    return value


def getnewargs_method():
    """ pickle.loads(dump): "__new__" method attributes when unserializing. """

    class _Serializable:
        def __new__(cls, value=None):
            item = object.__new__(cls)
            if value:
                item.value = value
            return item
        def __getnewargs__(self):
            return ("Bollywood filmi music",)

    globals()['_Serializable'] = _Serializable
    value = pickle.loads(pickle.dumps(_Serializable())).value
    del globals()['_Serializable']

    return value


def setstate_method():
    """ pickle.loads(dump): Set the "__dict__" of the deserialized instance. """

    # __setstate__ is called only when bool(obj.__getstate__()) is True
    class _Serializable:
        def __getstate__(self):
            return {'value': ''}
        def __setstate__(self, instance_dict):
            instance_dict.update({'value': "the ending of the short film"})
            self.__dict__.update(instance_dict)

    globals()['_Serializable'] = _Serializable
    value = pickle.loads(pickle.dumps(_Serializable())).value
    del globals()['_Serializable']

    return value


# category: resource management


def enter_exit():
    """ with: Use and release a resource."""

    class _Resource:
        def __enter__(self):
            return "enter concert"
        def __exit__(self, error_class, error, traceback):
            pass

    with _Resource() as resource:
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

