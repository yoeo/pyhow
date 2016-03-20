""" Built-in values and types samples. """

# ignore some coding flaws
# pylint: disable=bad-builtin
# pylint: disable=eval-used
# pylint: disable=exec-used
# pylint: disable=too-few-public-methods
# pylint: disable=undefined-variable
# pylint: disable=unused-variable

import io
import os
import sys
import tempfile
import types


# category: basic values


def ellipsis():
    """ Ellipsys: 3 dots for user defined syntax. """
    return ...


def false():
    """ False: Not true. """
    return bool(0)


def none():
    """ None: Null value. """


def not_implemented():
    """ NotImplemented: Used for partial comparison implementation. """

    class HugeValue:
        """ Huge integer. """
        def __gt__(self, other):
            if isinstance(other, int):
                return True
            else:
                return NotImplemented

    huge = HugeValue()
    if huge > 10**100:
        try:
            huge > 1j
        except TypeError:
            return "can't compare huge value with a complex"


def true():
    """ True: Not false. """
    return bool(...)


# category: basic types


def bool_builtin():
    """ bool: Immutable boolean value. """
    return bool([{}]) and "braces"


def bytearray_builtin():
    """ bytearray: Mutable bytes array. """
    data = bytearray(b"plain\0ext")
    data[5] = ord('t')
    return data.decode()


def byte_builtin():
    """ byte: Immutable bytes array. """
    return bytes("\xd0\xd2NUT", "utf-8").decode()


def complex_builtin():
    """ complex: Immutable complex numbers. """
    number = complex(1, 2) + 1j
    return number * number.conjugate()


def dict_builtin():
    """ dict: Mutable hash maps. """
    return dict(dog='bark', fox='???')['dog']


def float_builtin():
    """ float: Immutable floating point numbers. """
    return float('inf')


def frozenset_builtin():
    """ frozenset: Immutable items set. """
    return "{}!".format(
        ''.join(frozenset('here').union('rare').intersection('hats')).upper())


def int_builtin():
    """ int: Immutable natural numbers. """
    return int('1011', 2)


def list_builtin():
    """ list: Mutable items list. """
    items = list(range(10))
    items.insert(-1, 101)
    del items[::2]
    return "nice primes {}".format('-'.join(str(value) for value in items))


def memoryview_builtin():
    """ memoryview: Immutable access to buffers, no copy. """
    big_data = b'karma' * 2
    choices = ("yin", "yang")
    energy = []

    with memoryview(big_data) as access:
        for i in range(0, len(access), 4):
            access_chunk = access[i:i+4]  # no copy
            energy_flavour = sum(access_chunk.tolist())
            energy.append(choices[energy_flavour%2])

    return "your energy is like {}".format('+'.join(energy))


def set_builtin():
    """ set: Mutable items set. """
    items = set(abs(value) for value in range(-3, 4))
    items.difference_update([0])
    return "{0}, {0} drinks".format(' '.join(str(value) for value in items))


def str_builtin():
    """ str: Immutable strings. """
    return str(b"you are my prot\xe9g\xe9", 'latin-1')


def tuple_builtin():
    """ tuple: Immutable items sequence. """
    return tuple('Lucky Luke'.split())[-1]


# category: iterable utils


def all_builtin():
    """ all: Check if all elements are true. """
    return all('ready') and "already"


def any_builtin():
    """ any: Check if at least one element is true. """
    return any((None, False, 0, [], {}, tuple(), ...)) and "which one is true ?"


def enumerate_builtin():
    """ enumerate: Build a list of position-value tuples. """
    return ', '.join(
        "{} {}".format(i, value) for i, value in enumerate(('zero', 'one')))


def filter_builtin():
    """ filter: Filter items with a key function. Prefer list comprehension. """
    return "{}ged top secret".format(
        ''.join(filter(lambda info: info not in 'open', "pentagone")))


def iter_builtin():
    """ iter: Create an iterator for a sequence. """
    return next(iter("Love and War".split()))


def len_builtin():
    """ len: Number of elements of a sequence. """
    return len(str(...)) > 3 and "more than tree dots..."


def map_builtin():
    """ map: Apply a method to iterable items. Prefer list comprehension. """
    return ''.join(map(lambda value: chr(ord(value)-1), "tfdsfu\x21dpef"))


def max_builtin():
    """ map: Max element of an iterable. """
    return "Ma{}".format(max("Madmax"))


def min_buildin():
    """ min: Min element of an iterable. """
    return "{}innie".format(min("Mouse"))


def next_buildtin():
    """ next: Next element of an iterator. """
    return ''.join(next(zip("force", "laser", "energy", "xmen")))


def range_builtin():
    """ range: Generate integers. """
    return "{} fire!".format(
        ', '.join(str(value) for value in range(3, 0, -1)))


def reversed_builtin():
    """ reversed: Reverse a sequence. """
    return ''.join(reversed("devreser"))


def slice_builtin():
    """ slice: Build a slicer to select items into a sequence. """
    return "ABRACADABRA!!!"[slice(0, 20, 5)]


def sorted_builtin():
    """ sorted: Sort a sequence. """
    return ''.join(sorted('noW', key=lambda value: value.lower(), reverse=True))


def sum_builtin():
    """ sum: Sum items. """
    return "evens {}".format(
        ', '.join(str(value) for value in sum(([4], [6]), [2])))


def zip_builtin():
    """ zip: Merge elements of different iterables. """
    return ''.join(first + second for first, second in zip("Jh o", "onDe"))


# category: value utils


def abs_builtin():
    """ abs: Absolute value. """
    return "{} faces".format(abs(~1))


def ascii_builtin():
    """ ascii: Ascii representation of an object. """
    return ascii("eìuted")


def bin_builtin():
    """ bin: Binary representation of an integer. """
    return bin(8-1)[2:].replace('1', '6')


def callable_builtin():
    """ callable: Check if an object is callable. """

    def messenger():
        """ Send a message. """
        return "Don't harm the messenger"

    return (callable(messenger) and messenger or (lambda: None))()


def chr_builtin():
    """ chr: Integer to corresponding unicode character. """
    return "mister " + chr(0x58)


def dir_builtin():
    """ dir: List attribute names of an object. """
    return "{}ine".format(''.join(name for name in dir(2) if 'ag' in name))


def divmod_builtin():
    """ divmod: Integer division and modulo results. """
    return "{}{} is the answer".format(*divmod(129, 20))


def format_builtin():
    """ format: Formated representation of an object. """
    return "{} ready".format(format(1, '.0%'))


def hash_builtin():
    """ hash: Hashed integer value of an object. """
    return "{} tag".format(hash('#'))


def hex_builtin():
    """ hex: Hexadecimal representation on an integer. """
    return "R{}nne".format(hex(10))


def id_builtin():
    """ id: Get the unique ID of an object. """
    empty_first = {}
    empty_second = {}
    return id(empty_first) != id(empty_second) and "same but different"


def oct_builtin():
    """ oct: Octodecimal representation of an integer. """
    return "fish ~({})~".format(oct(0))


def open_builtin():
    """ open: Open a file. """
    with tempfile.TemporaryFile() as data_file:
        data_file.write(b"read/write")
        data_file.seek(0)
        data = data_file.readline()
        return data.decode()


def pow_builtin():
    """ pow: Power of number. Can be modulated with a value. """
    return "difference between 1KiB and 1KB is {}".format(pow(2, 10, 1000))


def round_builtin():
    """ round: Round a number to a given precision. """
    return "short pi {}".format(round(3.1415, 2))


# category: object model


def classmethod_builtin():
    """ @classmethod: Decorator to define class methods. """

    class Words:
        """ Handle words. """
        separator = '★'

        @classmethod
        def unite(cls, *split_words):
            """ Unite words. """
            return cls.separator.join(split_words)

    return Words.unite("black", "star")


def delattr_builtin():
    """ delattr: Delete an attribute from an object. """
    suv = types.new_class('Car')()
    suv.gear = 1
    delattr(suv, 'gear')
    try:
        suv.gear += 1
    except AttributeError:
        return "no gear to switch"


def getattr_builtin():
    """ getattr: Get an object attribute. """
    return getattr(["pop up"], 'pop')()


def globals_builtin():
    """ globals: Access global variables. """

    def inject_global():
        """ Inject a variable into global space. """
        globals()['injected_gobal'] = "injected"

    inject_global()
    return injected_gobal


def hasattr_builtin():
    """ hasattr: Check if an object has a specified attribute. """
    return "how can false be real?" if hasattr(False, 'real') else None


def isinstance_builtin():
    """ isinstance: Check if an object is an instance of a type. """
    return isinstance([], list) and "whitelisted"


def issubclass_builtin():
    """ issubclass: Check if a class is a subclass of an other one. """
    return (
        issubclass(type(all), object) and "*all your base are belong to object")


def locals_builtin():
    """ locals: Access local variables. """
    dynamite = "Kaboom!!!"
    return locals()['dynamite']


def property_builtin():
    """ property: Define getter setter and deleter for an attribute. """
    cars_horsepower = {}

    def get_power(car):
        """ Get car horsepower. """
        if id(car) not in cars_horsepower:
            raise AttributeError('ask me later')
        return cars_horsepower[id(car)]

    def set_power(car, horsepower):
        """ Set car horsepower. """
        cars_horsepower[id(car)] = (
            'goku power' if horsepower > 9000 else horsepower)

    def del_power(car):
        """ Delete car horsepower. """
        del cars_horsepower[id(car)]

    car_class = types.new_class('Car')
    car_class.horsepower = property(get_power, set_power, del_power)

    formula_one = car_class()
    formula_one.horsepower = 9001
    return formula_one.horsepower


def repr_builtin():
    """ repr: Representation of an object. """
    return repr(...)


def setattr_builtin():
    """ setattr: Set an object attribute. """
    cabriolet = types.new_class('Car')()
    setattr(cabriolet, 'roof', False)
    return not cabriolet.roof and "feel the wind"


def staticmethod_builtin():
    """ @staticmethod: Decorator to define class methods. """

    class Words:
        """ Manage words. """

        @staticmethod
        def last(phrase, separator):
            """ Get last words. """
            return phrase.split(separator)[-1].strip()

    return Words.last("Bond, James Bond", ",")


def super_builtin():
    """ super: Access base classes methods. """
    # super() rules:
    # 1/ the method exists in all classes
    # 2/ all the methods have the same signature
    # 3/ each occurence uses super()

    class Meal:
        """ A meal. """
        def cook(self):
            """ Cook a meal. """
            return "cooked {}".format(id(self))

    class Ramen(Meal):
        """ Some ramen. """
        def cook(self):
            """ Cook some ramen. """
            return super().cook()

    return Ramen().cook()


def type_builtin():
    """ type: Find objects type, make new types. """
    make_neo_int = type('NeoInt', (type(2),), {})
    return "friday {}".format(make_neo_int(13))


def vars_builtin():
    """ vars: Local variables or object attributes if obj.__dict__ exists. """
    return "{} wolf".format(
        locals() == vars() and [name for name in vars(str) if 'alp' in name][0])


# category: dynamic code generation


def compile_builtin():
    """ compile: Compile source code to bytecode. """
    bytecode = compile("'Sodom' or 'Gomorrah'", '/fake/sourcefile.py', 'eval')
    return eval(bytecode)


def eval_builtin():
    """ eval: Evaluate an expression and return the result. """
    luffy = True
    return eval('"one piece" if luffy else "teletubbies"')


def exec_builtin():
    """ exec: Execute source code. """
    exec('global new_global; new_global = "created on the fly"')
    return new_global


# category: interpreter features


def build_class():
    """ __build_class__: Low level class maker. Prefer types.new_class(...). """
    return __build_class__(lambda: None, 'NiceClass')().__class__.__name__


def copyright_builtin():
    """ copyright: Python copyright. """
    return str(copyright).splitlines()[0]


def credits_builtin():
    """ credits: Python development credit. """
    return str(credits).split('. ')[-1].lstrip()


def debug():
    """ __debug__: Interpreter in debug mode. Default is True. """
    # set __debug__ false to deactivate asserts:
    # $ python -O
    return __debug__


def exit_builtin():
    """ exit: Exit from interpreter. Prefer sys.exit(...). """
    sys.stdin = None
    try:
        # exit closes sys.stdin file descriptor if possible
        exit(0)
    except SystemExit:
        return "undead"
    finally:
        sys.stdin = sys.__stdin__


def help_builtin():
    """ help: View the doc of an object. """
    # ex: help(help)
    return help.__class__.__name__


def import_builtin():
    """ __import__: Interpreter import. Prefer importlib.import_module(...). """
    return __import__('sys').platform


def input_builtin():
    """ input: Retrieve data from the user. """
    with io.StringIO() as fake_input:
        fake_input.write("slim shady")
        fake_input.seek(0)
        sys.stdin = fake_input

        my_name_is = input()

    sys.stdin = sys.__stdin__
    return my_name_is


def loader():
    """ __loader__: Packages loader. """
    return "I'm a {}".format(__loader__.__doc__.splitlines()[0].strip().lower())


def name():
    """ __name__: Current module name. """
    return __name__


def package():
    """ __package__: Current package name. """
    return __package__


def print_builtin():
    """ print: Print an object on the standard input. """
    with io.StringIO() as fake_output:

        print("let's go to the beach", file=fake_output)

        fake_output.seek(0)
        return fake_output.read().rstrip()


def quit_builtin():
    """ quit: Exit from interpreter. Prefer sys.exit(...). """
    sys.stdin = None
    try:
        # quit closes sys.stdin file descriptor if possible
        quit(0)
    except SystemExit:
        return "immortal"
    finally:
        sys.stdin = sys.__stdin__


def spec():
    """ __spec__: Information used to load the module. """
    return os.path.basename(__spec__.origin)

