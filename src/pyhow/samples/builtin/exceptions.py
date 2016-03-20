""" Built-in exceptions samples. """

# ignore some coding flaws
# pylint: disable=exec-used
# pylint: disable=broad-except
# pylint: disable=deprecated-method
# pylint: disable=undefined-variable
# pylint: disable=unused-variable

import codecs
import gc
import idlelib.rpc
import importlib
import multiprocessing
import platform
import pickle
import os
import signal
import smtplib
import socket
import sys
import tempfile
import threading
import warnings
import weakref


# category: type and value


def arithmetic_error():
    """ Basic math error. """
    try:
        1 / 0
    except ArithmeticError:
        return "wrong maths"


def floating_point_error():
    """ Floating point operation error. """
    try:
        # When SIGFPE is enabled:
        # $ python -c "import fpectl; fpectl.turnonsigfpe(); 1.0 / 0"
        raise FloatingPointError()
    except FloatingPointError:
        return "floating point number error"


def generator_exit():
    """ Exiting a generetor. """
    result = None

    def make_generator():
        """ Custom generator. """
        try:
            yield
        except GeneratorExit:
            nonlocal result
            result = "closed before finishing"

    generator = make_generator()
    next(generator)
    generator.close()
    return result


def index_error():
    """ Indexed element not in sequence. """
    try:
        [][0]
    except IndexError:
        return "indexing empty list"


def key_error():
    """ Indexed element not in map. """
    try:
        {}[0]
    except KeyError:
        return "indexing empty dictionary"


def reference_error():
    """ Accessing unreferenced object. """

    def do_nothing():
        """ Empty function. """
        pass

    proxy = weakref.proxy(do_nothing)
    del do_nothing
    try:
        proxy.func_name
    except ReferenceError:
        return "looking for a deleted value"


def stop_iteration():
    """ End of iterations. """
    try:
        next(iter([]))
    except StopIteration:
        return "empty list"


def type_error():
    """ Using the wrong type of object. """
    try:
        next((1, 2))
    except TypeError:
        return "try with an iterator"


def unicode_decode_error():
    """ Failed to decode sequence to unicode. """
    try:
        b'\x99'.decode()
    except UnicodeDecodeError:
        return "bad unicode char"


def unicode_encode_error():
    """ Failed to encode unicode string. """
    try:
        '€'.encode('ascii')
    except UnicodeEncodeError:
        return "can't encode this character to ascii"


def unicode_error():
    """ Failed to encode from / decode to unicode string. """
    try:
        'é'.encode('latin-1').decode('ascii')
    except UnicodeError:
        return "can't encode or decode"


def unicode_translate_error():
    """ Failed to translate unicode string. """
    try:
        # just throwing the exception...
        raise UnicodeTranslateError('\x99', 1, 2, 'Unknown char')
    except UnicodeTranslateError:
        return "can't translate unicode character"


def value_error():
    """ Bad value. """
    try:
        _, _ = range(1)
    except ValueError:
        return "not enough items to unpack"


def zero_division_error():
    """ Dividing by zero. """
    try:
        0 / 0
    except ZeroDivisionError:
        return "who knows the result?"


# category: input output


def blocking_io_error():
    """ Blocking I/O operation failed. """
    # broken in versions < 3.4.3 see http://python.org/sf/13322
    try:
        raise BlockingIOError()
    except BlockingIOError:
        return "read or write failed"


def broken_pipe_error():
    """ Broken pipe. """
    (pipe_end1, pipe_end2) = multiprocessing.Pipe()
    pipe_end1.send('txt')
    pipe_end2.recv()
    # break the PIPE
    pipe_end1.close()
    try:
        pipe_end2.send('txt')
    except BrokenPipeError:
        return "don't write in closed pipe"


def buffer_error():
    """ Wrong usage of memory buffer. """
    array = bytearray([1, 3, 5])
    del array[-1]
    try:
        # lock the memory structure
        with memoryview(array):
            del array[-1]
    except BufferError:
        return "cannot modify locked memory structure"


def connection_aborted_error():
    """ Connection aborted by peer. """
    try:
        # just throwing the exception...
        raise ConnectionAbortedError()
    except ConnectionAbortedError:
        return "connection broken"


def connection_error():
    """ Base of all connection errors. """
    try:
        socket.socket().connect(('localhost', 0))
    except ConnectionError:
        return "connection not possible"


def connection_refused():
    """ Connection refused by peer. """
    try:
        socket.socket().connect(('localhost', 0))
    except ConnectionRefusedError:
        return "don't want to connect with you"


def connection_reset_error():
    """ Connection reseted by peer. """
    server = socket.socket()
    server.bind(('localhost', 19900))
    server.listen(0)
    client = socket.socket()
    client.connect(('localhost', 19900))
    # break the socket
    server.close()
    try:
        client.recv(10)
    except ConnectionResetError:
        return "server closed connection"
    finally:
        client.close()


def eof_error():
    """ Reached end of file before loading all data. """
    try:
        pickle.loads(pickle.dumps({})[:1])
    except EOFError:
        return "missing data"


# category: syntax and semantic errors


def attribute_error():
    """ Missing attribute. """
    try:
        None.anything
    except AttributeError:
        return '404, member not found'


def import_error():
    """ Importing inaccessible module. """
    try:
        importlib.import_module('no_such_module')
    except ImportError:
        return "module not found"


def indentation_error():
    """ Bad indentation. """
    try:
        exec("None\n None")
    except IndentationError:
        return "extra indentation to remove"


def name_error():
    """ Name not defined. """
    try:
        no_name
    except NameError:
        return "using the variable before creating it"


def not_implemented_error():
    """ Code not yet implemented. """

    def todo():
        """ To implement one day. """
        raise NotImplementedError()

    try:
        todo()
    except NotImplementedError:
        return "work in progress..."


def syntax_error():
    """ Wrong Python syntax. """
    try:
        exec('if while')
    except SyntaxError:
        return "compile error"


def tab_error():
    """ Mixing tabs and spaces for indentation. """
    try:
        exec('if True:\n pass\n\tpass')
    except TabError:
        return "mixed tab and space"


def unbound_local_error():
    """ Wrong access to nonlocal variables. """
    result = None
    first_level_variable = 1

    def second_level():
        """ Encapsulated method. """
        try:
            first_level_variable += 1
        except UnboundLocalError:
            nonlocal result
            result = "declare the variable as nonlocal"

    second_level()
    return result


# category: system errors


def assertion_error():
    """ Wrong assertion. """
    try:
        assert True is False
    except AssertionError:
        return "not a Schrödinger value"


def base_exception():
    """ Base of all exceptions. """
    try:
        sys.exit(-1) or die
    except BaseException:
        return "never fail"


def child_process_error():
    """ Unable to access child process. """
    try:
        os.waitpid(0, os.WNOHANG)
    except ChildProcessError:
        return "this child is not yours"


def exception():
    """ Base of all nonexit exceptions. """
    try:
        catch_me_if_you_can
    except Exception:
        return "caught"


def interrupted_error():
    """ Process interrupted by signal. """
    try:
        # just throwing the exception...
        raise InterruptedError()
    except InterruptedError:
        return "processing interrupted"


def keyborad_interrupt():
    """ Process interrupted by exit signal. """
    try:
        os.kill(os.getpid(), signal.SIGINT)
    except KeyboardInterrupt:
        return "current process wont commit suicide"


def lookup_error():
    """ Unable to find / load an item. """
    try:
        codecs.getencoder('hieroglyphe')
    except LookupError:
        return "charset unavailable"


def memory_error():
    """ Doesn't fit in memory. """
    char_list = ['a', 'b']
    try:
        while True:
            char_list *= len(char_list)
    except MemoryError:
        return "infinite exponential growth is plain stupid"
    finally:
        del char_list
        gc.collect()


def os_error():
    """ Operating system error. AKA EnvironmentError / IOError. """
    try:
        smtplib.SMTP('localhost:a_port')
    except OSError:
        return "bad port number"


def overflow_error():
    """ Value doesn't fit in object. """
    try:
        int(float('inf'))
    except OverflowError:
        return "infinite is too big"


def process_loockup_error():
    """ Manipulating process that doesn't exist. """
    try:
        os.kill(99999999, signal.SIGKILL)
    except ProcessLookupError:
        return "no process to kill"


def runtime_error():
    """ Error durring runtime. """
    try:
        threading.Lock().release()
    except RuntimeError:
        return "lock before releasing"


def system_error():
    """ Operating system or Python interpreter failure. """
    try:
        with socket.socket() as handle:
            idlelib.rpc.SocketIO(handle).decoderesponse(('BAD', 'DATA'))
    except SystemError:
        return "broken command"


def system_exit():
    """ Stopping the program. """
    try:
        sys.exit(-1)
    except SystemExit:
        return "you shall not quit"


def timeout_error():
    """ Reched a timeout. """
    try:
        # just throwing the exception...
        raise TimeoutError()
    except TimeoutError:
        return "can't wait anymore"


# category: file system


def environment_error():
    """ Base of all file system errors. AKA IOError / OSError. """
    try:
        os.rmdir(tempfile.mktemp())
    except EnvironmentError:
        return "removing a directory that doesn't exist"


def file_exists_error():
    """ File already exists. """
    with tempfile.TemporaryDirectory() as dirname:
        try:
            os.mkdir(dirname)
        except FileExistsError:
            return "creating a directory that already exists"


def file_not_found_error():
    """ File doesn't exist. """
    try:
        os.remove(tempfile.mktemp())
    except FileNotFoundError:
        return "deleting a file that doesn't exist"


def io_error():
    """ Base of all file system errors. AKA EnvironmentError / OSError. """
    try:
        open(tempfile.mktemp(), 'r')
    except IOError:
        return "reading a missing file"


def is_a_directory_error():
    """ Wrong usage of a directory. """
    with tempfile.TemporaryDirectory() as dirname:
        try:
            open(dirname, 'r')
        except IsADirectoryError:
            return "reading a directory as a file"


def not_a_directory_error():
    """ Try to use a nondirectory as a directory. """
    file_descriptor, filename = tempfile.mkstemp()
    os.close(file_descriptor)
    try:
        os.rmdir(filename)
    except NotADirectoryError:
        return "removing a file as a directory"
    finally:
        os.remove(filename)


def permission_error():
    """ No permission to process a file or directory. """
    file_descriptor, filename = tempfile.mkstemp()
    os.close(file_descriptor)
    os.chmod(filename, 0o444)
    try:
        open(filename, 'w')
    except PermissionError:
        return "cannot write on this file"
    finally:
        os.chmod(filename, 0o777)
        os.remove(filename)


# category: warnings


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
        # just throwing the exception...
        warnings.warn("won't implement", FutureWarning)
    except FutureWarning:
        return "forget this feature"
    finally:
        warnings.simplefilter('ignore', FutureWarning)


def import_warning():
    """ Issues during import. """
    warnings.simplefilter('error', ImportWarning)
    try:
        # just throwing the exception...
        warnings.warn("not fully loaded", ImportWarning)
    except ImportWarning:
        return "module not correctly loaded"


def pending_depretication_warning():
    """ Using features that will soon be depreticated. """
    warnings.simplefilter('error', PendingDeprecationWarning)
    try:
        # just throwing the exception...
        warnings.warn('soon depreticated', PendingDeprecationWarning)
    except PendingDeprecationWarning:
        return "avoid this feature"
    finally:
        warnings.simplefilter('ignore', PendingDeprecationWarning)


def ressource_warning():
    """ Bad resource usage. """
    warnings.simplefilter('error', ResourceWarning)
    try:
        # just throwing the exception...
        warnings.warn("unfreed", ResourceWarning)
    except ResourceWarning:
        return "must clean all resources"
    finally:
        warnings.simplefilter('ignore', ResourceWarning)


def runtime_warning():
    """ Abnormal behaviour during runtime"""
    warnings.simplefilter('error', RuntimeWarning)
    try:
        # just throwing the exception...
        warnings.warn("can fail", RuntimeWarning)
    except RuntimeWarning:
        return "something might go wrong"
    finally:
        warnings.simplefilter('ignore', RuntimeWarning)


def syntax_warning():
    """ Strange syntax. """
    warnings.simplefilter('error', SyntaxWarning)
    try:
        # just throwing the exception...
        warnings.warn("bad written", SyntaxWarning)
    except SyntaxWarning:
        return "check the syntax"
    finally:
        warnings.simplefilter('ignore', SyntaxWarning)


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

