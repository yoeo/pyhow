""" collections library: Tools to manage sequence of items. """

import collections


# category: chained dictionaries


def chainmap_maps():
    """ obj.maps(): Linked dictionaries. """

    map_one = {1: 0}
    map_two = {99: "Link"}
    chained = collections.ChainMap(map_two, map_one)
    return map_one in chained.maps and chained[99]


def chainmap_hierarchy():
    """ obj.parents(), obj.new_child(): Lookup hierarchy. """

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
    """ obj.most_common(): Most common items, with nb occurences. """

    occurences = collections.Counter("Luigi")
    item, nb_occurences = occurences.most_common(1)[0]
    return item * nb_occurences


def counter_elements():
    """ obj.elements(): Generate all items with the required repetitions. """

    return ''.join(collections.Counter(g=1, o=4).elements()).upper()


def counter_subtract():
    """ obj.subtract(...): Substract counts, c1 -= c2. """

    occurences = collections.Counter("Kart race")
    occurences.subtract(collections.Counter("accidented Kirrrby"))
    return "Starting from {}-{}".format(*occurences.most_common(1)[0])


def counter_update():
    """ obj.update(...): Add counts, c1 += c2. """

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

    kart_class = collections.namedtuple('Kart', 'celerity size')
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


def deque():
    """ deque(...): List-like double edged queue. """

    power_ups = collections.deque(('star', 'lightning'))
    return "there are {} power ups".format(len(power_ups))


def deque_append():
    """ obj.append(...), obj.appendleft(...): Add element. """

    power_ups = collections.deque(('star', 'lightning'))
    power_ups.append('green-shell')
    power_ups.appendleft('red-shell')
    return "available power ups are {}".format(', '.join(power_ups))


def deque_extend():
    """ obj.extend(...), obj.extendleft(...): Add list of elements. """

    power_ups = collections.deque(('star', 'lightning'))
    power_ups.extend(('green-shell', 'rocket'))
    power_ups.extendleft(['red-shell'])
    return "extended power ups are {}".format(', '.join(power_ups))


def deque_pop():
    """ obj.pop(...), obj.popleft(...): Pop an element. """

    power_ups = collections.deque(('star', 'lightning', 'rocket'))
    _ = power_ups.popleft()
    _ = power_ups.pop()
    return "remaining power ups is {}".format(', '.join(power_ups))


def deque_rotate():
    """ obj.rotate(...): Move the position of elements. """

    power_ups = collections.deque(('star', 'lightning', 'rocket', 'banana'))
    power_ups.rotate(2)
    return "rotated power ups are {}".format(', '.join(power_ups))


# category: ordered dictionary


def ordereddict():
    """ OrderedDict(...): Sorted dictionary. """

    pilots = {pilot: len(pilot) for pilot in 'Peach Bowser Toad'.split()}
    ordered_pilots = collections.OrderedDict(sorted(
        pilots.items(), key=lambda item: item[1]))
    return "sorted pilot are {}".format(', '.join(
        '{}#{}'.format(score, name) for name, score in ordered_pilots.items()))


def ordereddict_popitem():
    """ obj.popitem(...): Pop last or first item, default is last. """

    pilots = {pilot: len(pilot) for pilot in 'Peach Bowser Toad'.split()}
    ordered_pilots = collections.OrderedDict(pilots)
    return "first pilot {} scores {}".format(
        *ordered_pilots.popitem(last=False))  # by default: last=True


def ordereddict_move_to_end():
    """ obj.move_to_end(...): Modify the position of an item. """

    pilots = {pilot: len(pilot) for pilot in 'Peach Bowser Toad'.split()}
    ordered_pilots = collections.OrderedDict(pilots)
    ordered_pilots.move_to_end('Toad', last=False)  # by default: last=True
    return "new first pilot {} scores {}".format(
        *next(iter(ordered_pilots.items())))


# category: default dictionary


def defaultdict():
    """ defaultdict(...): Dictionary with a value for missing keys. """

    kart = collections.defaultdict(lambda: 'unknown')
    kart['speed'] = 66
    return "kart specs are {}".format(''.join(
        '{} -> {}'.format(key, kart[key]) for key in ('speed', 'sound')))


def defaultdict_default_factory():
    """ obj.default_factory: Change default value factory method. """

    kart = collections.defaultdict()
    kart.default_factory = lambda: 'too high'
    return "kart speed is {}".format(kart['speed'])


# category: user managed dictionary, list and string


def userdict():
    """ Cls(UserDict): Managed dictionary. """

    class Kart(collections.UserDict):
        """ Custom kart. """
        def __getitem__(self, key):
            return '*{}*'.format(self.data[key])

    kart = Kart()
    kart['beauty'] = 'full'

    return "this cart beauty is {}".format(kart['beauty'])


def userlist():
    """ Cls(UserList): Managed lists. """

    class Motors(collections.UserList):
        """ Custom kart motors list. """
        def __str__(self):
            return 'Kart motors {}'.format(', '.join(self.data))

    karts = Motors(('50 CC', '100 CC', '150 CC'))
    return str(karts)


def userstring():
    """ Cls(UserString): Managed string. """

    class Pilot(collections.UserString):
        """ Custom kart pilot name. """
        def swap(self, new_pilot):
            """ Carjack the kart. """
            if not isinstance(new_pilot, str):
                raise TypeError('new_pilot is not a str')
            self.data = new_pilot

    pilot = Pilot('Toad')
    pilot.swap('Donkey Kong')
    return "pilot of the day is " + pilot

