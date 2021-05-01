#!/home/jet08013/anaconda3/bin/python

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
Tuning = {0: ("d", 1), 1: ("b",0 ), 2: ("g", 0), 3: ("d", 0), 4: ("g", 1)}

tab = r"(%!(?P<tab>[^%]+)!%)"
note = r"(?P<string>[0-9])\.(?P<fret>[0-9]+)\.(?P<duration>[0-9]+)"
chord = r"(?P<chord>\<\s*([0-9]\.[0-9]+\s+)+[0-9]\.[0-9]+\s*\>)(?P<duration>[0-9]+)"
chord_note = r"(?P<string>[0-9])\.(?P<fret>[0-9]+)"
slur_beam_start = r"(\(|\[)"
slur_beam_end = r"(\)|\])"
tie = r"~"
ws = r"\s+"
rest = r"(r(?P<duration>[0-9]+))"


def fret_to_notes(base, tuning_octave, fret):
    start_fret = frets[base]
    point = (start_fret + fret) % 12
    octaves = (start_fret + fret) //12 + tuning_octave
    
    return notes[point] + "'"*(octaves+1)


def decode_simple(loc, fret):
    tuning_note = Tuning[int(loc)][0]
    tuning_octave = Tuning[int(loc)][1]
    lily = fret_to_notes(tuning_note, tuning_octave, int(fret))
    return lily


def decode(loc, fret, dur):
    lily = decode_simple(loc, fret)
    return lily + dur


def filter(s):
    result = ""
    i = 0
    N = len(s)
    while i < N:
        tab_try = re.match(tab, s[i:])
        if tab_try:
            parsed = parse(tab_try.group("tab"))
            result += parsed
            i += tab_try.end(0) - tab_try.start(0)
            continue
        result += s[i]
        i += 1
    return result


def parse(s):
    parsed = ""
    N = len(s)
    i = 0
    while i < N:
        sbs_try = re.match(slur_beam_start,s[i:])
        if sbs_try:
            parsed += sbs_try.group(0)
            i += 1
            continue

        sbe_try = re.match(slur_beam_end,s[i:])
        if sbe_try:
            parsed += sbe_try.group(0)
            i += 1
            continue

        if re.match(tie, s[i:]):
            parsed += "~"
            i += 1
            continue

        ws_try = re.match(ws, s[i:])
        if ws_try:
            parsed += " "
            i += ws_try.end() - ws_try.start()
            continue

        note_try = re.match(note, s[i:])
        if note_try:
            i += note_try.end() - note_try.start()
            lily = decode(
                note_try.group("string"),
                note_try.group("fret"),
                note_try.group("duration"),
            )
            parsed += lily + "\\{}".format(int(note_try.group("string")) + 1)
            continue

        chord_try = re.match(chord, s[i:])
        if chord_try:
            i += chord_try.end() - chord_try.start()
            chord_string = chord_try.group("chord")
            chord_duration = chord_try.group("duration")
            chord_notes = re.findall(chord_note, chord_string)
            parsed += "< "
            for x in chord_notes:
                parsed += decode_simple(x[0], x[1]) + "\\{} ".format(int(x[0]) + 1)
            parsed += ">" + chord_duration
            continue

        rest_try = re.match(rest, s[i:])
        if rest_try:
            i += rest_try.end() - rest_try.start()
            parsed += rest_try.group(0)
            continue

        raise UnrecognizedToken("Unrecognized Token starting {}".format(s[i : i + 10]))

    return parsed

if __name__ == "__main__":
    with (sys.stdin) as f:
        data = f.read()
    parsed = filter(data)
    print(parsed)
