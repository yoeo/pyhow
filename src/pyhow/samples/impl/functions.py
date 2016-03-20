""" Create function-like objects. """


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

