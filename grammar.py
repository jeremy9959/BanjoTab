import pyparsing as pp


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


def parse_note(tok):
    lily = decode(tok.string, tok.fret, tok.duration, tuning)
    answer = lily + "\\{}".format(int(tok.string) + 1)
    return answer


def parse_chord(tok):
    chord_notes = tok.chord_notes
    chord_duration = tok.duration
    answer = "< "
    for x in chord_notes:
        answer += decode_simple(x.string, x.fret, tuning) + "\\{} ".format(
            int(x.string) + 1
        )
    answer += ">" + chord_duration
    return answer


# tab = r"(%!(?P<tab>[^%]+)!%)"
# tuning = r"(?P<tuning>OpenG|DoubleC|Modal|JohnRiley)"
# note = r"(?P<note>(?P<note_string>[0-9])\.(?P<note_fret>[0-9]+)\.(?P<note_duration>[0-9]+))"
# chord = r"(?P<chord>\<(?P<chord_strings>\s*([0-9]\.[0-9]+\s+)+[0-9]\.[0-9]+\s*)\>(?P<chord_duration>[0-9]+))"
# chord_note = r"(?P<chord_string>[0-9])\.(?P<chord_fret>[0-9]+)"
# slur_beam_start = r"(?P<beam_start>\(|\[)"
# slur_beam_end = r"(?P<beam_end>\)|\])"
# tie = r"(?P<tie>~)"
# ws = r"(?P<ws>\s+)"
# rest = r"(?P<rest>r(?P<rest_duration>[0-9]+))"
# tuplet = r"(?P<tuplet>=\s*(?P<tuplet_notes>(([0-9]\.[0-9]+\s+)+([0-9]\.[0-9]+\s*)))=(?P<tuplet_duration>[0-9]+))"
# xnote = r"(?P<xnote>x)"
# accent = r"(?P<accent>acc)"

LDELIM = pp.Literal("%!").suppress()
RDELIM = pp.Literal("!%").suppress()
tuning = Tunings["OpenG"]


def set_tuning(t):
    global tuning
    tuning = Tunings[t[0]]
    return t


tuning_key = (
    (
        pp.Literal("OpenG")
        | pp.Literal("DoubleC")
        | pp.Literal("Modal")
        | pp.Literal("JohnRiley")
    )
    .set_parse_action(set_tuning)
    .suppress()
)


note = pp.Combine(
    pp.Word(pp.nums, exact=1).set_results_name("string")
    + pp.Literal(".")
    + pp.Word(pp.nums, max=2).set_results_name("fret")
    + pp.Literal(".")
    + pp.Word(pp.nums, max=2).set_results_name("duration")
).set_parse_action(parse_note)


chord_note = pp.Combine(
    pp.Word(pp.nums, exact=1).set_results_name("string")
    + pp.Literal(".")
    + pp.Word(pp.nums, max=2).set_results_name("fret")
).set_results_name("chord_note")

chord_notes = (pp.OneOrMore(chord_note)).set_results_name("chord_notes")

chord = (
    (
        pp.Literal("<")
        + chord_notes
        + pp.Combine(
            pp.Literal(">") + pp.Word(pp.nums, max=2).set_results_name("duration")
        )
    )
    .set_results_name("chord")
    .set_parse_action(parse_chord)
)

slur_beam_start = (pp.Literal("(") | pp.Literal("[")).set_results_name("beam_start")
slur_beam_end = (pp.Literal(")") | pp.Literal("]")).set_results_name("beam_end")

tie = pp.Literal("~").set_results_name("tie")

rest = pp.Combine(pp.Literal("r") + pp.Word(pp.nums, max=2)).set_results_name("rest")

tuplet_note = pp.Combine(
    pp.Word(pp.nums, exact=1).set_results_name("string")
    + pp.Literal(".")
    + pp.Word(pp.nums, max=2).set_results_name("fret")
).set_results_name("tuplet_note")


tuplet = pp.Combine(
    pp.Literal("=") + pp.ZeroOrMore(tuplet_note) + pp.Literal("=")
) + pp.Word(pp.nums, max=2).set_results_name("tuplet_duration")

xnote = pp.Literal("x").set_results_name("xnote")
accent = pp.Literal("acc").set_results_name("accent")

tab = (
    LDELIM
    + pp.ZeroOrMore(tuning_key)
    + pp.OneOrMore(
        note
        | chord
        | slur_beam_start
        | slur_beam_end
        | tie
        | tuplet
        | rest
        | xnote
        | accent
    )
    + RDELIM
)

with open("Liberty.rly", "r") as f:
    tune = f.read().expandtabs()
    loc = 0
    for x, start, end in tab.scan_string(tune):
        print(tune[loc:start])
        print(" ".join(x))
        loc = end
    print(tune[loc:])
