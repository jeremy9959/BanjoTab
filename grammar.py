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
tuning = Tunings["OpenG"]


def set_tuning(t):
    global tuning
    tuning = Tunings[t[0]]
    return t


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
    lily = decode(tok.note.pitch.string, tok.note.pitch.fret, tok.note.duration, tuning)
    answer = lily + "\\{}".format(int(tok.note.pitch.string) + 1)
    return answer


def parse_chord(tok):
    chord_pitches = tok.chord_pitches

    chord_duration = tok.duration
    answer = "< "
    for x in chord_pitches:
        answer += decode_simple(x.string, x.fret, tuning) + "\\{} ".format(
            int(x.string) + 1
        )
    answer += ">" + chord_duration
    return answer


def parse_rest(tok):
    return tok


def parse_xnote(tok):
    return r" \xNote "


def parse_accent(tok):
    return r" \accent "


def parse_tuplet(tok):
    tuplet_notes = tok.tuplet_notes
    tuplet_duration = tok.tuplet_duration
    answer = r"\tuplet" + f"{len(tuplet_notes)}/{tuplet_duration}" + " { "
    for x in tuplet_notes:
        answer += decode_simple(x.string, x.fret, tuning) + "\\{} ".format(
            int(x.string) + 1
        )
    answer += " } "
    return answer


LDELIM = pp.Literal("%!").suppress()
RDELIM = pp.Literal("!%").suppress()

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

pitch = pp.Combine(
    pp.Word(pp.nums, exact=1).set_results_name("string")
    + pp.Literal(".")
    + pp.Word(pp.nums, max=2).set_results_name("fret")
).set_results_name("pitch")

note = (
    pp.Combine(
        pitch.set_results_name("pitch")
        + pp.Literal(".")
        + pp.Word(pp.nums, max=2).set_results_name("duration")
    )
    .set_results_name("note")
    .set_parse_action(parse_note)
)


chord = (
    (
        pp.Literal("<")
        + pp.OneOrMore(pitch).set_results_name("chord_pitches")
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

rest = (
    pp.Combine(pp.Literal("r") + pp.Word(pp.nums, max=2))
    .set_results_name("rest")
    .set_parse_action(parse_rest)
)

tuplet_note = pp.Combine(
    pp.Word(pp.nums, exact=1).set_results_name("string")
    + pp.Literal(".")
    + pp.Word(pp.nums, max=2).set_results_name("fret")
).set_results_name("tuplet_note")

tuplet_notes = pp.OneOrMore(tuplet_note).set_results_name("tuplet_notes")

tuplet = (
    pp.Literal("=")
    + tuplet_notes
    + pp.Combine(
        pp.Literal("=") + pp.Word(pp.nums, max=2).set_results_name("tuplet_duration")
    )
).set_parse_action(parse_tuplet)

xnote = pp.Literal("x").set_results_name("xnote").set_parse_action(parse_xnote)
accent = pp.Literal("acc").set_results_name("accent").set_parse_action(parse_accent)

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


tune = r"%! <0.0 1.0 2.4>4 !%"
x = tab.parse_string(tune)
print(x.dump())

# with open("wwflower.rly", "r") as f:
#     tune = f.read().expandtabs()
#     loc = 0
#     for x, start, end in tab.scan_string(tune):
#         print(tune[loc:start])
#         print(" ".join(x))
#         loc = end
#     print(tune[loc:])
