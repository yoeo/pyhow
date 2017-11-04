"""itertools library: Create, mix and extract data from iterators."""

import itertools


# category: computation


def accumulate():
    """Recursively apply function to items."""

    accumulated = itertools.accumulate(
        iterable='ABCDE', func=lambda result, current: result + current)
    return list(accumulated)


def starmap():
    """Expand and map arguments."""

    # starmap(fn, xs) -> for x in xs: fn(*x)
    # map(fn, xs)     -> for x in xs: fn(x)
    mapped = itertools.starmap(lambda x, y: x + '+' + y, ['AB', 'CD'])
    return list(mapped)


# category: combination


def chain():
    """Merge multiple iteratiors."""

    chained = itertools.chain('BAG', 'DAD')
    return ''.join(chained)


def groupby():
    """Group sorted elements."""

    def square(value):
        """Calculate the square of a number."""

        return value**2

    sorted_items = sorted(range(-2, 3), key=square)
    grouped = itertools.groupby(sorted_items, key=square)
    return dict((key, list(values)) for key, values in grouped)


def zip_longest():
    """Merge items from sequences, replace missing by None."""

    zipped = itertools.zip_longest('ABC', 'XY')
    return dict(zipped)


# category: probability


def combinations():
    """Produce all the combinations for different items."""

    combined = itertools.combinations('ABC', r=2)
    combined = [''.join(possibility) for possibility in combined]
    return combined


def combinations_with_replacement():
    """Produce all the combinations with duplicate items."""

    combined = itertools.combinations_with_replacement('AB', r=2)
    combined = [''.join(possibility) for possibility in combined]
    return combined


def permutations():
    """Produce all the permutations for different items."""

    permutated = itertools.permutations('AB', r=2)
    permutated = [''.join(possibility) for possibility in permutated]
    return permutated


def product():
    """Produce all the products possibility for sequences."""

    multiplicated = itertools.product('AB', 'CD')
    multiplicated = [''.join(possibility) for possibility in multiplicated]
    return multiplicated


# category: filtering


def compress():
    """Select specified elements."""

    compressed = itertools.compress(data='ABCD', selectors=(True, False, True))
    return ''.join(compressed)


def dropwhile():
    """Purge elements before the matching one."""

    purged = itertools.dropwhile(lambda x: x != 'C', 'ABCDEF')
    return ''.join(purged)


def filterfalse():
    """Remove matching element."""

    filtered = itertools.filterfalse(lambda x: 'B' < x < 'E', 'ABCDEF')
    return ''.join(filtered)


def islice():
    """Retrieve a portion of an iterable."""

    part = itertools.islice('ABCDEFGHIJ', 1, 6, 2)
    return ''.join(part)


# category: generation


def count():
    """Continiouly generate numbers."""

    counter = itertools.count(start=3.0, step=1.5)
    return [next(counter) for _ in range(3)]


def cycle():
    """Generate elements in an infinite loop."""

    cycler = itertools.cycle('ABC')
    return ''.join(next(cycler) for _ in range(5))


def repeat():
    """Repeate a sequence a number of times."""

    repeated = itertools.repeat('AB', times=2)
    return list(repeated)


def tee():
    """Duplicate a sequence by making independent iterators."""

    duplicates = itertools.tee('ABC', 2)
    duplicates = [''.join(copy) for copy in duplicates]
    return duplicates
