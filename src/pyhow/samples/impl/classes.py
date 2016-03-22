""" Play with class and object implementations. """

# using unfinished example classes
# pylint: disable=assigning-non-slot
# pylint: disable=attribute-defined-outside-init
# pylint: disable=no-member
# pylint: disable=protected-access
# pylint: disable=too-few-public-methods
# pylint: disable=unused-variable

import abc
import weakref


# category: attributes manipulation


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


# category: class hierarchy


def instancecheck_method():
    """ isinstance: Check if item is an instance of a class. """

    class _MetaBase(type):
        def __instancecheck__(cls, item):
            return 'x' in item

    class _Base(metaclass=_MetaBase):
        pass

    item = "saxophone"
    return isinstance(item, _Base) and item


def prepare():
    """ Cls(): Create the attributes dict needed to produce a new instance. """

    class _MetaBase(type):
        @staticmethod
        def __prepare__(class_name, _: 'baseclasses', **kw):
            namespace = kw.copy()
            namespace.update(
                {'{}_value'.format(class_name.lower()): "prepared"})
            return namespace

    class _ItemClass(list, metaclass=_MetaBase):
        pass

    return _ItemClass()._itemclass_value


def subclasscheck_method():
    """ issubclass: Check if a class is a subclass of an other one. """

    class _MetaBase(type):
        def __subclasscheck__(cls, subclass):
            return 's' in subclass.__name__

    class _Base(metaclass=_MetaBase):
        pass

    item = "xylophone"
    return issubclass(type(item), _Base) and item


def subclasshook():
    """ isinstance, issubclass: inheritance check for Abstract Base Classes. """

    class _AbstractBase(metaclass=abc.ABCMeta):
        @classmethod
        def __subclasshook__(cls, associated_class):
            return hasattr(associated_class, 'get_value')

    class _SubClass:
        def _get_value(self):
            return self and "subclass check OK"

    class _NonSubClass:
        pass

    _AbstractBase.register(_NonSubClass)
    _AbstractBase.register(_SubClass)

    sub_item = _SubClass()
    non_sub_item = _NonSubClass()
    return (
        not isinstance(non_sub_item, _AbstractBase) and
        isinstance(sub_item, _AbstractBase) and sub_item._get_value())


# category: descriptors


def delete_method():
    """ del obj.attr: Delete an attribute handled by another class. """

    class _Descriptor:
        def __init__(self):
            self.active = True
        def __delete__(self, item):
            item.shadow_value = "attribute deleted"
            self.active = False
        def __get__(self, *_):
            if not self.active:
                raise AttributeError('attribute not found')
            return "a value"

    class _ItemClass:
        value = _Descriptor()

    item = _ItemClass()
    del item.value
    try:
        return item.value
    except AttributeError:
        return item.shadow_value


def get_method():
    """ obj.attr: Link an attribute to a class that computes its value. """

    class _Descriptor:
        def __get__(self, item, item_class):
            return "generated value for an {0.__name__}".format(item_class)

    class _ItemClass:
        value = _Descriptor()

    return _ItemClass().value


def set_method():
    """ obj.attr=: Link an attribute to a class changes its value. """

    class _Descriptor:
        def __set__(self, item, value):
            item.shadow_value = "stored {}".format(value)

    class _ItemClass:
        value = _Descriptor()

    item = _ItemClass()
    item.value = 44
    return item.shadow_value


# category: class model


def bases_attribute():
    """ Cls.__bases__: Base classes of the current class. """

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

    # use __del__ with caution
    # it is difficult to know when the object will be actually removed

    context = ""

    class _Destroyable:
        def __del__(self):
            nonlocal context
            context = "burn the lyrics"

    item = _Destroyable()
    del item
    return context


def dict_attribute():
    """ Cls.__dict__: Bindings for class members. """

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


def mro_attribute():
    """ Cls.__mro__, super(): List of base types used to process class tree. """

    class _ItemClass(type(...), int):
        pass

    return "types: {}".format(
        ' + '.join(cls.__name__ for cls in _ItemClass.__mro__))


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

