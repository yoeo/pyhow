""" collections library: Tools to manage sequence of items. """

import collections


# category: chained dictionaries


def chain_map_maps():
    """ chain_map.maps(): Linked dictionaries. """

    map_one = {1: 0}
    map_two = {99: "Link"}
    chained = collections.ChainMap(map_two, map_one)
    return map_one in chained.maps and chained[99]


def chain_map_hierarchy():
    """ chain_map.parents(), chain_map.new_child(): Lookup hierarchy. """

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
    """ Counter(): Dict-like item to count number of occurences. """

    occurences = collections.Counter("Peach")
    missing_to_zero = occurences['z'] == 0
    return missing_to_zero and "Princess {}".format(''.join(occurences.keys()))


def counter_most_common():
    """ counter.most_common(): Most common items, with nb occurences. """

    occurences = collections.Counter("Luigi")
    item, nb_occurences = occurences.most_common(1)[0]
    return item * nb_occurences


def counter_elements():
    """ counter.elements(): Generate all items with the required repetitions. """

    return ''.join(collections.Counter(g=1, o=4).elements()).upper()


def counter_subtract():
    """ counter.subtract(...): Substract counts, c1 -= c2. """

    occurences = collections.Counter("Kart race")
    occurences.subtract(collections.Counter("accidented Kirrrby"))
    return "Starting from {}-{}".format(*occurences.most_common(1)[0])


def counter_update():
    """ counter.update(...): Add counts, c1 += c2. """

    occurences = collections.Counter("shell")
    occurences.update(collections.Counter("lightning"))
    return "power-ups have {}ls".format(occurences['l'])


def counter_operations():
    """ +, -, &, |: Numerical operations with counter elements. """

    occurences_a = collections.Counter('Toad')
    occurences_b = collections.Counter('Roy')
    # a + b     -> a[x] + b[x]    , x € keys(a, b)
    # a - b     -> a[x] - b[x]    , x € keys(a, b)
    # a & b     -> min(a[x], b[x]), x € keys(a, b)
    # a | b     -> max(a[x], b[x]), x € keys(a, b)
    return '(-_-)'.join((occurences_a - occurences_b).elements())


# category: named tuple


def namedtuple():
    """ cls(...): Create an object class to store tuple value. """

    kart_class = collections.namedtuple('Kart', ('color', 'speed'))
    blue_kart = kart_class(*('blue', 50))
    return "the blue kart color is {}".format(blue_kart.color)


def namedtuple_make():
    """ cls._make(...): Create new instance from a tuple. """

    kart_class = collections.namedtuple('Kartx', 'celerity size')
    rocket_kart = kart_class._make((1000, 'small'))
    return "{} km/h is faaast!!".format(rocket_kart.celerity)


def namedtuple_asdict():
    """ obj._asdict(), dict(obj): Convert the instance to an ordered dict. """

    kart_class = collections.namedtuple('Kart', 'breaks, lights')
    kart = kart_class(*('off', 'on'))
    return ", ".join(
        '{} {}'.format(key, value) for key, value in kart._asdict().items())


def namedtuple_replace():
    """ cls._replace(...): Copy an instance by changing a member. """

    kart_class = collections.namedtuple('Kart', ['owner', 'color'])
    toad_kart = kart_class(owner='Toad', color='green')
    mario_kart = toad_kart._replace(owner='Mario')
    return "{} gave its {} kart to {}".format(
        toad_kart.owner, toad_kart.color, mario_kart.owner)


def namedtuple_source():
    """ cls._source: Source code of the named tuple class. """

    kart_class = collections.namedtuple('MegaKart', 'is_mega is_realy_mega')
    defined = 'class {}'.format(kart_class.__name__) in kart_class._source
    return defined and "{} defined".format(kart_class.__name__)


def namedtuple_fields():
    """ cls._fields: Attributes of the named tuple. """

    kart_class = collections.namedtuple('Kart', 'size mottor gears speed')
    return "Kart features are {}...".format(', '.join(kart_class._fields))


# category: deque


def _():
    """ """


# category: ordered dictionary


def _():
    """ """


# category: default dictionary


def _():
    """ """


# category: user dictionary


def _():
    """ """


# category: user list


def _():
    """ """


# category: user string


def _():
    """ """

