import ply.yacc as yacc

import  ply.lex as lex


tokens = ('NOTE','TIE', 'SLUR_START', 'SLUR_END','DURATION','CHORD_START', 'CHORD_END',)

t_TIE = r"~"
t_SLUR_START = r"\("
t_SLUR_END = r"\)"
t_CHORD_START = "<"
t_CHORD_END = ">"


t_ignore = ' \t\n'

notes={0:'c',1:'cis',2:'d',3:'dis',4:'e',5:'f',6:'fis',7:'g',8:'gis',9:'a',10:'ais',11:'b'}
frets={notes[k]:k for k in notes}
Tuning = {0:('d',1),1:('c',1),2:('g',0),3:('c',0),4:('g',1)}

def fret_to_notes(base, fret):
    start_fret = frets[base]
    point = (start_fret+fret) % 12
    octave = (start_fret+fret) // 12
    octave_mark = '\'' if octave==0 else '\'\''
    return notes[point]+octave_mark

def decode(s):
    loc, fret = s.split('.')
    tuning_note = Tuning[int(loc)][0]
    tuning_octave=Tuning[int(loc)][1]
    octave_mark = '' if tuning_octave==0 else '\''
    lily = fret_to_notes(tuning_note,int(fret))+octave_mark
    return lily


def t_NOTE(t):
    r"[0-4]\.[0-9]+"
    t.value = decode(t.value)
    return t

def t_DURATION(t):
    ":[0-9]+"
    t.value = t.value[1:]
    return t

def t_error(t):
    print("Unknown Token {}".format(t.value[0]))
    t.lexer.skip(1)


lexer = lex.lex()
lexer.input("2.0:8 3.0:8 < 3.1 2.0 1.2>:4")



