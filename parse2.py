#!/usr/bin/env /home/jet08013/anaconda3/envs/pandas20/bin/python

import re
import sys


class UnrecognizedToken(Exception):
    pass


notes = {
    0: "c",
    1: "cis",
    2: "d",
    3: "dis",
    4: "e",
    5: "f",
    6: "fis",
    7: "g",
    8: "gis",
    9: "a",
    10: "ais",
    11: "b",
}
frets = {notes[k]: k for k in notes}
Tunings = {}
Tunings["OpenG"] = {0: ("d", 1), 1: ("b", 0), 2: ("g", 0), 3: ("d", 0), 4: ("g", 1)}
Tunings["DoubleC"] = {0: ("d", 1), 1: ("c", 1), 2: ("g", 0), 3: ("c", 0), 4: ("g", 1)}
Tunings["Modal"] = {0: ("d", 1), 1: ("c", 1), 2: ("g", 0), 3: ("d", 0), 4: ("g", 1)}
Tunings["JohnRiley"] = {
    0: ("d", 1),
    1: ("c", 1),
    2: ("g", 0),
    3: ("d", 0),
    4: ("f", 1),
}

# default is open G
default_tuning = Tunings["OpenG"]

tab = r"(%!(?P<tab>[^%]+)!%)"
tuning = r"(?P<tuning>OpenG|DoubleC|Modal|JohnRiley)"
note = r"(?P<note>(?P<note_string>[0-9])\.(?P<note_fret>[0-9]+)\.(?P<note_duration>[0-9]+))"
chord = r"(?P<chord>\<(?P<chord_strings>\s*([0-9]\.[0-9]+\s+)+[0-9]\.[0-9]+\s*)\>(?P<chord_duration>[0-9]+))"
chord_note = r"(?P<chord_string>[0-9])\.(?P<chord_fret>[0-9]+)"
slur_beam_start = r"(?P<beam_start>\(|\[)"
slur_beam_end = r"(?P<beam_end>\)|\])"
tie = r"(?P<tie>~)"
ws = r"(?P<ws>\s+)"
rest = r"(r(?P<rest_duration>[0-9]+))"

patterns = [
    tab,
    tuning,
    note,
    chord,
    chord_note,
    slur_beam_start,
    slur_beam_end,
    tie,
    ws,
    rest,
]
pattern = re.compile("|".join(patterns))


def fret_to_notes(base, tuning_octave, fret):
    start_fret = frets[base]
    point = (start_fret + fret) % 12
    octaves = (start_fret + fret) // 12 + tuning_octave

    return notes[point] + "'" * (octaves + 1)


def decode_simple(loc, fret, Tuning):
    tuning_note = Tuning[int(loc)][0]
    tuning_octave = Tuning[int(loc)][1]
    lily = fret_to_notes(tuning_note, tuning_octave, int(fret))
    return lily


def decode(loc, fret, dur, tuning):
    lily = decode_simple(loc, fret, tuning)
    return lily + dur


def filter(s):
    result = ""
    i = 0
    N = len(s)
    tuning = default_tuning
    while i < N:
        tab_try = re.match(tab, s[i:])
        if tab_try:
            parsed, tuning = parse(tab_try.group("tab"), pattern, tuning)
            result += parsed
            i += tab_try.end(0) - tab_try.start(0)
            continue
        result += s[i]
        i += 1
    return result


def parse(s, pattern=pattern, tuning=default_tuning):
    parsed = ""
    N = len(s)
    i = 0
    while i < N:
        mo = re.match(pattern, s[i:])
        match mo.lastgroup:
            case "tuning":
                tuning = Tunings[mo.group(0)]
                i += mo.end() - mo.start()
                continue

            case "beam_start":
                parsed += mo.group(0)
                i += 1
                continue

            case "beam_end":
                parsed += mo.group(0)
                i += 1
                continue

            case "tie":
                parsed += "~"
                i += 1
                continue

            case "ws":
                parsed += " "
                i += mo.end() - mo.start()
                continue

            case "note":
                i += mo.end() - mo.start()
                lily = decode(
                    mo.group("note_string"),
                    mo.group("note_fret"),
                    mo.group("note_duration"),
                    tuning,
                )
                parsed += lily + "\\{}".format(int(mo.group("note_string")) + 1)
                continue

            case "chord":
                i += mo.end() - mo.start()
                chord_strings = mo.group("chord_strings")
                chord_duration = mo.group("chord_duration")
                chord_notes = re.findall(chord_note, chord_strings)
                parsed += "< "
                for x in chord_notes:
                    parsed += decode_simple(x[0], x[1]) + "\\{} ".format(int(x[0]) + 1)
                parsed += ">" + chord_duration
                continue

            case "rest":
                i += mo.end() - mo.start()
                parsed += mo.group(0)
                continue

            case _:
                raise UnrecognizedToken(
                    "Unrecognized Token starting {}".format(s[i : i + 10])
                )

    return parsed, tuning


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("parse: Please supply a filename to parse", file=sys.stderr)
        sys.exit(1)

    fname = sys.argv[1]
    with open(fname, "r") as f:
        data = f.read()
        parsed = filter(data)

    print(parsed)
