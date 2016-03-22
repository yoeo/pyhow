""" Custom methods to copy, serialize and unserialize items. """

# using unfinished example classes
# pylint: disable=too-few-public-methods

import copy
import pickle


# category: copy


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


# category: serialization


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
        def __init__(self):
            self.value = ''
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
        def __init__(self):
            self.value = ''
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

