""" collections, tools to manage sequence of items. """

import collections


# category: chained dictionaries


def chain_map_maps():
    """ ChainMap.maps: Linked dictionaries. """

    map_one = {1: 0}
    map_two = {99: "Link"}
    chained = collections.ChainMap(map_two, map_one)
    return map_one in chained.maps and chained[99]


def chain_map_hierarchy():
    """ ChainMap.parents, ChainMap.new_child: Lookup hierarchy. """

    map_one = {1: 0}
    map_two = {99: "Link"}
    map_three = {99: "Triforce"}
    chained = collections.ChainMap(map_three, map_two, map_one)

    # select the parents
    parents_ok = chained.parents.maps == [map_two, map_one]
    # create a new child
    map_four = chained.new_child()
    map_four[99] = "Zelda"

    return parents_ok and chained[99]


# category: items counter


def counter():
    """ Counter: Dict-like item to count number of occurences. """

    counter = collections.Counter("Peach")
    missing_to_zero = counter['z'] == 0
    return missing_to_zero and "Princess {}".format(''.join(counter.keys()))


def counter_most_common():
    """ Counter.most_common: Most common items, with nb occurences. """

    counter = collections.Counter("Luigi")
    item, nb_occurences = counter.most_common(1)[0]
    return item * nb_occurences


def counter_elements():
    """ Counter.elements: Generate all items with the required repetitions. """

    return ''.join(collections.Counter(g=1, o=4).elements()).upper()


def counter_subtract():
    """ Counter.subtract: Substract counts, c1 -= c2. """

    counter = collections.Counter("Kart race")
    counter.subtract(collections.Counter("accidented Kirrrby"))
    return "Starting from {}-{}".format(*counter.most_common(1)[0])


def counter_update():
    """ Counter.update: Add counts, c1 += c2. """

    counter = collections.Counter("shell")
    counter.update(collections.Counter("lightning"))
    return "power-ups have {}ls".format(counter['l'])


def counter_operations():
    """ Numerical operations with counter elements: +, -, &, |. """

    counter_a = collections.Counter('Toad')
    counter_b = collections.Counter('Roy')
    # a + b     -> a[x] + b[x]    , x € keys(a, b)
    # a - b     -> a[x] - b[x]    , x € keys(a, b)
    # a & b     -> min(a[x], b[x]), x € keys(a, b)
    # a | b     -> max(a[x], b[x]), x € keys(a, b)
    return '(-_-)'.join((counter_a - counter_b).elements())


# category: deque


def _():
    """ """

