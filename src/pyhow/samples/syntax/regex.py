""" Regular expressions language samples. """

import re


# category: positions


def start():
    """ \\A: Match the start of the text. """

    regex = re.compile(r'\Aa', flags=re.MULTILINE)
    match_start = regex.search("album")
    match_starting_newline = regex.search("\nart")
    return match_start and not match_starting_newline and match_start.string


def start_or_empty():
    """ ^: Match the start or starting newline in multiline mode. """

    regex = re.compile('^a', flags=re.MULTILINE)
    match_start = regex.search("artist")
    match_starting_newline = regex.search("\nartwork")
    return match_start and match_starting_newline and match_start.string


def end():
    """ \\Z: Match the end of the text. """

    regex = re.compile(r'r\Z')
    match_end = regex.search("footballer")
    match_trailing_newline = regex.search("shot a corner\n")
    return match_end and not match_trailing_newline and match_end.string


def end_or_trailing_newline():
    """ $: Match the end of the text or trailing newline. """

    regex = re.compile('r$')
    match_end = regex.search("basketball player")
    match_trailing_newline = regex.search("great passer\n")
    return match_end and match_trailing_newline and match_end.string


def alphanumeric_edges():
    """ \\b: Match the start or end of a alphanumeric string. """

    return re.search(r'\b[a-z]{4}\b', "I'm Picasso baby!").group()


def alphanumeric_unfinished():
    """ \\B: Match an unfinished alphanumeric string. """

    return "zom{}e".format(re.search(r'bi\B', "biker gang").group())


# category: repetitions


def n_repetitions():
    """ {N}: N repetitions. """

    match_n = re.search('[lo]{3}', "trololololo")
    return "s{}".format(match_n.group())


def n_to_m():
    """ {N,M}: N -> M repetitions. """

    match_m = re.search(r'\d{2,3}m/s', "sound: 340m/s")
    match_many = re.search(r'\d{3,}m/s', "light: 299792458m/s")
    return match_m and "speed is {}".format(match_many.group())


def one_to_infinite():
    """ +: 1 -> infinite repetitions. """

    regex = re.compile('i+')
    match_one = regex.search("Kinect")
    match_two = regex.search("Wii")
    return match_one and match_two and match_two.string


def shortest():
    """ ??, *?, +?, {N,M}?: matches the shortest sequence. """

    match_shortest_star = re.search('-(.*?)-', "lol-lol-lol-lol")
    match_shortest_nm = re.search('[AH]{4,6}?', "HAHAHAHAHAHA")
    return '{} laughts, {}'.format(
        match_shortest_nm.group().count("HA"), match_shortest_star.group(1))


def zero_to_infinite():
    """ *: 0 -> infinite repetitions. """

    regex = re.compile('X*')
    match_zero = regex.search("Fast and Furious")
    match_three = regex.search("Triple XXX")
    return match_zero and match_three and match_three.string


def zero_to_one():
    """ ?: 0 -> 1 repetition. """

    regex = re.compile('i?')
    match_zero = regex.search("lama")
    match_one = regex.search("impala")
    return match_zero and match_one and match_one.string


# category: shortcuts


def any_except_newline():
    """ .: All, whitespaces, alphanumeric, etc... except new line. """

    return "ridi{}".format(re.search('.{4}$', "particule").group())


def numeric():
    """ \\d: Numeric characters. """

    return "sad {}...".format(re.match(r'\d+', "1939 was a bad year").group())


def non_numeric():
    """ \\D: Non-numerical characters. """

    return "{}dom is comming, tomorrow".format(
        re.search(r'\D+', "4free").group())


def whitespaces():
    """ \\s: Whitespaces. tab, space, new line, etc... """

    return re.sub(r'\s+', '~', "tic   \ttac\n \r toe")


def non_whitespaces():
    """ \\S: All except whitespaces. """

    return "the secret of a healthy life is {}".format(
        re.sub(r'\S+', '***', "fish & chips"))


def alphanumeric():
    """ \\w: Alphanumeric and underscore. """

    return " ".join(match.group() for match in re.finditer(
        r'\b\w+\b', "3_ducks: >@..  >@..  >@.. on a rocket"))


def non_alphanumeric():
    """ \\W: Non-alphanumeric nor underscore. """

    return "G{}".format(re.search(r'\W+$', "Þïg £°$$").group().strip())


# category: composition


def character_set():
    """ [...]: Match at least one character of the set. """

    regex = re.compile(r'''
        [olm]       # match any of: o, l, m
        [^xyz]      # match any except: x, must start with ^
        [\d]        # match shortcut
        [+)(*]      # no escape needed for special characters: +, ), (, *...
        [a-z]       # match range: a, b, ..., y, z
        [\-\]\\]    # escape needed for characters: -, ], \
    ''', flags=re.MULTILINE | re.VERBOSE)
    return "key of success = {}".format(regex.search("mc2+e-").group())


def or_operator():
    """ EXP1|EXP2: Match the first or the second expression. """

    return "{}y".format(re.match(r'\w+(fox|fax)', "starfox").group(1))


# category: style


def comment():
    """ (?#...): Ignored comment. """

    return re.search('(?# garbage...)sonic', "ultrasonic").group()


def compile_flags():
    """ (?F): Activate compile flags. F in 'aiLmsux'. """

    # Flags
    # a --> re.A, re.ASCII: matches ASCII only
    # i --> re.I, re.IGNORECASE: ignore character case
    # L --> re.L, re.LOCALE: locale dependent
    # m --> re.M, re.MULTILINE: multi-line matching
    # s --> re.S, re.DOTALL: character '.' matches all including newline
    # u : ??? unicode ?
    # x --> re.X, re.VERBOSE: multi-line commented pattern
    return re.match(r'(?x)\ w +  # a word', "rockstar")


# category: grouping


def group():
    """ (...): Group of matching string. """

    return re.fullmatch(r'([a-z]+) \d+', "zone 51").group(1)


def non_capturing():
    """ (?:...): Group that cannot be captured. """

    match = re.match(r'\w+(?:man)', "spokewoman")
    return not match.lastindex and match.group(0)


def named():
    """ (?P<name>...): Named group. """

    return re.search(r'\b(?P<animal>\w+)$', "big anaconda").group('animal')


def referenced_index():
    """ \\index: References group by it index. """

    return re.match(r'([neo]+) on \1', "one on one").group(1)


def referenced_name():
    """ (?P=name): References a named group. """

    return re.search(r'(?P<noise>\w+)-(?P=noise)', "bam-bam").group('noise')


def matches_if_followed_by():
    """ (?=...): Match only if the next group matches. """

    return re.match(r'\w+\B(?=s)', "flames").group()


def matches_if_not_followed_by():
    """ (?!...): Match only if the next group doesn't match. """

    return re.match(r'(?i)\w+(?!s)\b', "Asgard").group()


def matches_if_preceded_by():
    """ (?<=...): Match only if the previous group matches. """

    # needs a fixed width pattern
    return re.search(r'(?<=#)[A-Z\-]+', "#BI-WINNING").group()


def matches_if_not_preceded_by():
    """ (?<!...): Match only if the previous group doesn't match. """

    # needs a fixed width pattern
    return re.search(r'(?<!\w{6}) \w+$', "tunn€l vision").group()


def matches_if_reference_matches():
    """ (?(group_id_or_name)EXP1|EXP2): Conditional match by group ID. """

    regex = re.compile(r'(?P<at>@)?\w+(?(at)@|er)')
    return regex.match("@dream@") and regex.match("dreamer").group()
