""" Play with class and object implementations. """


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

