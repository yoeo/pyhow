"""re library: Extract information from text with regular expressions."""

import re


# category: library tools


def compile_re():
    """re.compile: Compile regular expression."""

    regex = re.compile(
        r'\d+  # grab integers\n', flags=re.VERBOSE | re.MULTILINE)
    match = regex.search('Rahan is 42 years old')
    return "age is {}".format(match.group())


def escape():
    """re.escape: Add '\\' to nonalphanumerical characters."""

    delimiters = re.escape('{([])}')
    return ' & '.join(re.findall(
        '[{0}][a-z]+[{0}]'.format(delimiters), "if (love) then {hate}"))


def purge():
    """re.purge: Purge internal regular expressions cache."""

    def _cache_empty():
        return not getattr(re, '_cache')

    re.match('', '')
    cache_created = not _cache_empty()
    re.purge()
    return cache_created and _cache_empty() and "empty cache"


# category: expressions


def fullmatch():
    """re.fullmatch, regex.fullmatch: Pattern matches exactly the text."""

    regex = re.compile(r'[a-z]+\d[a-z]+')
    found = regex.fullmatch('f3lix')
    miss = regex.fullmatch('inst4ble sil3x')
    return miss or 'password is {}'.format(found.group())


def findall():
    """re.findall, regex.findall: Find all nonoverlapping matchs."""

    games = re.findall(
        '[a-z]+ball', 'basketball, swimming, football, criquet, volleyball')
    return "need a ball to play {}".format(', '.join(games))


def finditer():
    """re.finditer, regex.finditer: Iter all nonoverlapping matchs."""

    favorite = re.finditer(
        '[A-Z][a-z]+',
        'my favorite characteres are Harry, Hermione and Draco.')
    next(favorite)
    return "her name is {}".format(next(favorite).group())


def groups():
    """regex.groups: Number of different match groups."""

    regex = re.compile(r'day: ((\d)\d)')
    return "{} recursive matchings possible".format(regex.groups)


def groupindex():
    """regex.groupindex: Index of each match group."""

    regex = re.compile(r'(?P<lowercase>[a-z]+) (?P<int>\d+)')
    return ' and '.join(
        '{} {}'.format(value, key) for key, value in regex.groupindex.items())


def match_re():
    """re.match, regex.match: Pattern matches the text from the start."""

    regex = re.compile(r'\d[a-z]')
    found = regex.match('the 9tails', pos=4)  # start at position 4
    miss = regex.match('not4sale', endpos=4)  # ends at position 4
    return miss or '{}h wonder'.format(found.group())


def pattern():
    """regex.pattern: String pattern of the expression."""

    return re.compile('identity').pattern


def search():
    """re.search, exp.search: Find the pattern in the text."""

    found = re.search('[A-Z]+', 'big DADDY')
    return "who's your {}?".format(found.group())


def split():
    """re.split, regex.split: Split a text with a pattern."""

    animals = re.split(r'\d+\W', '2 lions, 3 tigers, 45 bears')
    return "not scared of {}".format(''.join(animal for animal in animals))


def sub():
    """re.sub, regex.sub: Replace matching pattern from a text."""

    three_wise_monkeys = re.sub(r'\^', '°', 'd(-_-)b   +(^_^)+   d(^+^)b')
    return three_wise_monkeys


def subn():
    """re.subn, regex.subn: Replace and count the number of occurences."""

    sweat, count = re.subn('[^a-zA-Z]+', '', '(°c°) $€an d(-_-)~ y0£0')
    return count == 5 and "sweat {}".format(''.join(sweat))


# category: matchs


def expand():
    """match.expand: Fill a template with matching group content."""

    match = re.search(r'(?P<drink>\w+a)', "coffee, tea, juice")
    return match.expand(r"only drink \1, \g<1> or \g<drink>")


def group():
    """match.group: Extract matching sequences."""

    match = re.match(r'(?P<weekday>[a-z]+) (?P<day>\d{2})', 'friday 13')
    # match.group()     -> match.group(0)           -> 'friday 13'
    # match.group(1)    -> match.group('weekday')   -> 'friday'
    # match.group(2)    -> match.group('day')       -> '13'
    # match.group(2, 1)                             -> ('13', 'friday')
    # match.group('day', 'weekday')                 -> ('13', 'friday')
    # match.group(2, 'weekday')                     -> ('13', 'friday')

    return "{}!".format('! '.join(match.group('weekday', 1, 'weekday')))


def groups_match():
    """match.groups: Extract all groups."""

    match = re.match(r'^(\w+) .+ (\w+)$', 'hot men own a dog')
    return ''.join(match.groups())


def groupdict():
    """match.groups: Extract all named groups."""

    match = re.match(r'<(?P<tag>[^>]+)>', '<body>')
    return ' '.join(next(iter(match.groupdict().items())))


def start():
    """match.start: Starting position of matching text."""

    match = re.search('begin', "the story begins here")
    return match.string[match.start():]


def end():
    """match.end: End position of matching text."""

    match = re.search('(?P<when>end)', "The hero dies at the end of the movie")
    return match.string[:match.end('when')]


def span():
    """match.span: Start and end position of matching text."""

    match = re.match('(?P<size>tall)', "tallest man on earth")
    return match.string[slice(*match.span('size'))]


def pos():
    """match.pos: Start position for matching lookup."""

    match = re.compile('.').match("la vida loca", pos=3)
    return match.string[match.pos:]


def endpos():
    """match.endpos: End position for matching lookup."""

    match = re.compile('.').match("siempre siempre Marimar", endpos=16)
    return match.string[match.endpos:]


def lastindex():
    """match.lastindex: Last group of a match index."""

    match = re.match(r'(\w+) (\d+)hours', "work 24hours a day")
    return match.group(match.lastindex)


def lastgroup():
    """match.lastgroup: Last named group of a match."""

    return re.match(r'(?P<num>\d+)(?P<issue>[a-z]+)', '99problems').lastgroup


def re_match():
    """match.re: Regex used for the match."""

    return "all stars shine{}".format(re.search('.*', '').re.pattern)


def string():
    """match.string: Text used for the match."""

    return re.search('x', 'input text').string
