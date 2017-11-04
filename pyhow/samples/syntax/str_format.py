"""String formating language samples."""

import collections
import locale


# category: exemples


def basic_formating():
    """Simple replacement..."""

    return "{}".format('infinite')


def deep_formating():
    """Mix of many formating possibilities."""

    return "{value.__class__.__bases__[0].__name__!r}".format(
        **{'value': ...})


def composed_formating():
    """Composed formating."""

    return "{!s:.{}}".format(..., 1)


# category: value adaptation


def value_conversion():
    """Convert to: !r ↔ repr, !s ↔ str, !a ↔ ascii."""

    return "{0!r} or {0!s} or {0!a}".format('infinîte')


def value_formating():
    """Format a value with the underlying format function."""

    happy_value = type('HappyFormater', (object,), {
        '__format__': lambda _, template: template.replace('lol', '(^_^)')})()
    return "{:lol}".format(happy_value)


# category: field


def field_index():
    """Get field at a given position."""

    return "{1} and not {0}".format('infinite', 666)


def field_name():
    """Get field by name."""

    return "{value} and not {0}".format(9, value='sixty-nine')


def field_element_index():
    """Get field element by index."""

    return "{value[1]}".format(value='lol')


def field_attribute_index():
    """Get field attribute."""

    make_value = collections.namedtuple('Value', ['absolute_value'])
    return "{0.absolute_value}".format(make_value('absolute_zero'))


# category: spec align


def align_left():
    """Left aligned."""

    return "{:<10}!".format(-666)


def align_right():
    """Right aligned."""

    return "{:>10}!".format(-666)


def center():
    """Centered."""

    return "{:^10}!".format(-666)


def numerical_center():
    """Numerically centered."""

    return "{:=10}!".format(-666)


def fill():
    """Fill empty space."""

    return "{0:~^10}! or {0:010}".format(-666)


def truncate():
    """Truncate the value."""

    return "{:.7}".format('big_number')


def sign():
    """Show sign for positive numbers: + ↔ yes, - ↔ no, ' ' ↔ show space."""

    return "x may be {0:*^+5}, {0:*^-5}, {0:*^ 5}!".format(1)


# category: spec numerical presentation


def alternate_form():
    """Alternate form with extra 0x, 0b, 0o for int and .000 for float."""

    return "{0:#b} or {0:#g}".format(2**8-1)


def numerical_separator():
    """Use comma as big number separator."""

    return "{:,}!".format(10**6)


def precision():
    """Float precision."""

    return "{:.3f}".format(1000/3)


# category: spec type conversion


def binary():
    """Binary representation."""

    return "{:b}".format(2**8-1)


def character():
    """Character representation."""

    return "{:c}".format(65)


def decimal():
    """Decimal representation. Default integer format."""

    return "{:d}".format(2**8-1)


def octal():
    """Octal representation."""

    return "{:o}".format(2**8-1)


def hexadecimal():
    """Hexadecimal representation."""

    return "{0:x} or {0:X}".format(2**8-1)


def localized_number():
    """Localized number representation."""

    locale.setlocale(locale.LC_NUMERIC, ('fr_FR', 'UTF-8'))
    message = "{:n}".format(10**6)
    locale.setlocale(locale.LC_NUMERIC, (None, None))
    return message


def float_exponent():
    """Float exponent representation."""

    return "{0:.2e} or {0:.2E}".format(1/3)


def float_fixed_point():
    """Float fixed point representation."""

    return "({0:.2f}, {1:.2f}) or ({0:.2F}, {1:.2F})".format(1/3, 1e1000)


def float_general_format():
    """Float general format representation. Default float format."""

    return "({0:.2g}, {1:.2g}) or ({0:.2g}, {1:.2G})".format(1/3, 10**-9/3)


def string():
    """String representation."""

    return "{:s}".format('something')
