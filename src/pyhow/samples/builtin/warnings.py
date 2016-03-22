""" Trigger and handle built-in warnings. """

# using depreticated function
# pylint: disable=deprecated-method

import platform
import warnings


# category: runtime issues


def byte_warning():
    """ Wrong Byte operation. """

    warnings.simplefilter('error', BytesWarning)
    try:
        # can be generated with: $ python3 -bb -c "'a'==b'a'"
        warnings.warn('beware', BytesWarning)
    except BytesWarning:
        return "are you mixing bytes and strings?"
    finally:
        warnings.simplefilter('ignore', BytesWarning)


def import_warning():
    """ Issues during import. """

    warnings.simplefilter('error', ImportWarning)
    try:
        warnings.warn("not fully loaded", ImportWarning)
    except ImportWarning:
        return "module not correctly loaded"


def ressource_warning():
    """ Bad resource usage. """

    warnings.simplefilter('error', ResourceWarning)
    try:
        warnings.warn("unfreed", ResourceWarning)
    except ResourceWarning:
        return "must clean all resources"
    finally:
        warnings.simplefilter('ignore', ResourceWarning)


def runtime_warning():
    """ Abnormal behaviour during runtime"""

    warnings.simplefilter('error', RuntimeWarning)
    try:
        warnings.warn("can fail", RuntimeWarning)
    except RuntimeWarning:
        return "something might go wrong"
    finally:
        warnings.simplefilter('ignore', RuntimeWarning)


def unicode_warning():
    """ Unicode convertion issue. """

    warnings.simplefilter('error', UnicodeWarning)
    try:
        warnings.warn("malformed", UnicodeWarning)
    except UnicodeWarning:
        return "check the unicode string"
    finally:
        warnings.simplefilter('ignore', UnicodeWarning)


def warning():
    """ Base of all warnings. """

    warnings.simplefilter('error', Warning)
    try:
        warnings.warn("danger", Warning)
    except Warning:
        return "something strange might happen"
    finally:
        warnings.simplefilter('ignore', Warning)


# category: usage of unsafe features


def deprecatioin_warning():
    """ Using depreticated features. """

    warnings.simplefilter('error', DeprecationWarning)
    try:
        platform.popen('/bin/true')
    except DeprecationWarning:
        return "use subprocess instead"
    finally:
        warnings.simplefilter('ignore', DeprecationWarning)


def future_warning():
    """ Using element / syntax that will soon change. """

    warnings.simplefilter('error', FutureWarning)
    try:
        warnings.warn("won't implement", FutureWarning)
    except FutureWarning:
        return "forget this feature"
    finally:
        warnings.simplefilter('ignore', FutureWarning)


def pending_depretication_warning():
    """ Using features that will soon be depreticated. """

    warnings.simplefilter('error', PendingDeprecationWarning)
    try:
        warnings.warn('soon depreticated', PendingDeprecationWarning)
    except PendingDeprecationWarning:
        return "avoid this feature"
    finally:
        warnings.simplefilter('ignore', PendingDeprecationWarning)


def syntax_warning():
    """ Strange syntax. """

    warnings.simplefilter('error', SyntaxWarning)
    try:
        warnings.warn("bad written", SyntaxWarning)
    except SyntaxWarning:
        return "check the syntax"
    finally:
        warnings.simplefilter('ignore', SyntaxWarning)

