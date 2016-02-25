""" functools library samples. """

import functools


# category: parameters


def partial():
    """ Set default parameters to an existing function. """

    def phrase(subject, verb, comp=""):
        """ Build a phrase with words. """
        return ' '.join((subject, verb, comp))

    robot_phrase = functools.partial(phrase, "robot", comp="bip bip")
    return robot_phrase("says")


def partialmethod():
    """ Set default parameters to an existing class method. """

    class Multiplier:
        """ Multiply numbers. """

        def __init__(self, base):
            self._base = base

        @property
        def base(self):
            """ Get the base number. """
            return self._base

        def times(self, value):
            """ Multiply with the base number. """
            return self._base * value

        times_2 = functools.partialmethod(times, 2)

    multiplier = Multiplier(3)
    return multiplier.times_2()


# category: optimisation


def lru_cache():
    """ Cache functions results. """

    @functools.lru_cache()
    def say_hi(name):
        """ Say Hi. """
        return 'Hi {}'.format(name)

    names = ['John'] + ['Doe'] * 4
    for name in names:
        say_hi(name)
    return say_hi.cache_info()


# category: adaptation


def cmp_to_key():
    """ Convert C style compare function to key function. """

    def compare_sizes(list_a, list_b):
        """ Old compare function. """
        size_a, size_b = len(list_a), len(list_b)
        return 1 if size_a > size_b else -1 if size_a < size_b else 0

    heroes = ['rahan', 'lucky luke', 'conan', 'samba']
    return max(heroes, key=functools.cmp_to_key(compare_sizes))


def wraps():
    """ Copy wrapped function information with a decorator. """

    def do_nothing(): "Doing nothing."

    @functools.wraps(do_nothing)
    def wrapper():
        """ Wraps a function that does nothing. """
        return do_nothing()

    return wrapper.__doc__.strip()


def update_wrapper():
    """ Copy wrapped function information. """

    def do_nothing(): "Doing nothing."

    def wrapper():
        """ Wraps a function that does nothing. """
        return do_nothing()

    wrapper_alias = functools.update_wrapper(wrapper, do_nothing)
    return wrapper_alias is wrapper and wrapper.__doc__.strip()


def total_ordering():
    """ Automaticaly create all high-level ordering function for a class. """

    @functools.total_ordering
    class FakeInt:
        """ Items comparables with integers. """

        def __init__(self, value):
            self._value = value

        def __lt__(self, value):
            return self._value < value

        def __eq__(self, value):
            return self._value == value

        def get_value(self):
            """ Retrieve the value. """
            return self._value

        def set_value(self, value):
            """ Change the value. """
            self._value = value

    fake_2 = FakeInt(2)
    return 1 < fake_2 <= 3


def singledispatch():
    """ Create a C++ like template function. """

    @functools.singledispatch
    def monkey_jump(height):
        """ Jumping monkey. """
        return 'monkey jumped {} meters'.format(height)

    @monkey_jump.register(list)
    def _(height):
        """ Monkey jumping lists. """
        return monkey_jump(len(height))

    return monkey_jump(list(range(10)))


# category: computing


def reduce():
    """ Apply recursively a function to an iterable. """

    reverse = functools.reduce(lambda result, x: x + result, 'MooD')
    return reverse

