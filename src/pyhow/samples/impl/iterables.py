""" Sequences implementation, create kind of iterators, lists, maps... """


# category: iterable, e.g. list


def iter_method():
    """ iter, for: Create an iterator for an iterable. """

    class _Iterable:
        def __iter__(self):
            return iter(["guitare"])

    return next(iter(_Iterable()))


def len_method():
    """ len: Get the number of items. """

    class _Iterable:
        def __len__(self):
            return 1337

    return len(_Iterable())


def contains_method():
    """ in: Check if an item is in an iterable. """

    class _Iterable:
        def __contains__(self, item):
            return item == "trap"

    return "trap" in _Iterable() and "trap music"


def reversed_method():
    """ reversed: Reverse a iterable. """

    class _Iterable:
        def __init__(self):
            self._sequence = ["Soca", "Zumba"]
        def __reversed__(self):
            return self._sequence[::-1]

    return next(iter(reversed(_Iterable())))


# category: iterator, e.g. itertools.chain


def next_method():
    """ next, for: Get one item of an iterators. """

    class _Iterator:
        def __init__(self):
            self._stop = False
        def __next__(self):
            if self._stop:
                raise StopIteration()
            self._stop = True
            return "drums"

    return next(_Iterator())


# category: indexable e.g. dict, list


def index():
    """ [...]: Use an item as a sequence index. """

    class _Index:
        def __index__(self):
            return -1

    return ["violin", "contrabass"][_Index()]


def delitem():
    """ del: Delete an item from a sequence. """

    class _Indexable:
        def __init__(self):
            self._deleted = []
        def __delitem__(self, key):
            self._deleted.append(key)
        def __getitem__(self, key):
            if key in self._deleted:
                raise KeyError()
            return True

    orchestra = _Indexable()
    del orchestra['dancer']
    try:
        return orchestra['dancer']
    except (KeyError, IndexError):
        return "no dancer found in orchestra"


def getitem():
    """ [...]: Get an item from a sequence. """

    class _Indexable:
        def __getitem__(self, key):
            if key not in ['piano', 'organ']:
                raise KeyError()
            return "play {}".format(key)

    return _Indexable()['piano']


def missing():
    """ [...]: Get a default item when the required item is not in dict. """

    # must be a subclass of dict
    class _Indexable(dict):
        def __missing__(self, key):
            return "silence..."

    return _Indexable()[0]


def setitem():
    """ [...] =: Set a sequence item value. """

    class _Indexable:
        def __init__(self):
            self._sequence = []
        def __getitem__(self, key):
            try:
                return self._sequence[self._sequence.index(key)+1]
            except ValueError:
                raise KeyError()
        def __setitem__(self, key, value):
            self._sequence += [key, value]

    singer = _Indexable()
    singer['type'] = "slam"
    return singer['type']

