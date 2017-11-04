"""tempfile library: Work with temporary files and directories."""

import os
import tempfile


# category: temporary files


def mktemp():
    """Depreticated version of mkstemp. Prefer mkstemp."""

    return "forget me..."


def mkstemp():
    """Unique temporary file. Not deleted on close."""

    fileno, filename = tempfile.mkstemp()
    created = os.path.exists(filename)

    os.close(fileno)
    os.remove(filename)
    return created and "filename {}".format(filename)


def named_temporary_file():
    """Unique temporary file. Delete on close."""

    with tempfile.NamedTemporaryFile(
            prefix='how_', suffix='.bin') as temp_file:
        created = os.path.exists(temp_file.name)
        return created and "filename {}".format(temp_file.name)


def spooled_temporary_file():
    """Unique temporary file, data on disc or memory. Delete on close."""

    max_size = 1234
    with tempfile.SpooledTemporaryFile(max_size=max_size) as temp_file:
        # data in memory
        created_in_memory = temp_file.name is None

        # move to disk, can also use fileno()
        temp_file.rollover()
        moved_to_disc = temp_file.name is not None

        return created_in_memory and moved_to_disc and (
            "fileno {}, in-memory limit {}".format(temp_file.name, max_size))


def temporary_file():
    """Unique anonymous temporary file. Delete on close."""

    with tempfile.TemporaryFile() as temp_file:
        created = os.path.exists(temp_file.name)
        return created and "fileno {}".format(temp_file.name)


# category: temporary directories


def gettempdir():
    """Temporary items root directory."""

    return "temp root is {}".format(tempfile.gettempdir())


def gettempprefix():
    """Prefix of temporary directories and files."""

    return "prefix is {}".format(tempfile.gettempprefix())


def mkdtemp():
    """Unique temporary directory."""

    dirname = tempfile.mkdtemp(prefix='how_', suffix='_tmp')
    created = os.path.exists(dirname)
    os.rmdir(dirname)

    return created and "directory {}".format(dirname)


def temporary_directory():
    """Unique temporary directory info. Delete on close."""

    with tempfile.TemporaryDirectory(prefix='how_', suffix='_tmp') as dirname:
        created = os.path.exists(dirname)
        return created and "directory {}".format(dirname)


def tempdir():
    """Set the temprary items root directory."""

    system_root = os.path.abspath(os.sep)
    old_tempdir = tempfile.gettempdir()

    tempfile.tempdir = system_root
    new_tempdir = os.path.abspath(os.path.dirname(tempfile.mktemp()))
    tempfile.tempdir = old_tempdir

    return (
        new_tempdir == system_root
        and "move temp root from {} to {}".format(old_tempdir, new_tempdir))
