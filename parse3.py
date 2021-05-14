import ply.lex as lex
import ply.yacc as yacc
import sys

# states
states = (
    ('tab', 'exclusive'),
)



# tokens
tokens = (
    "NUMBER",
    "TUNING",
    "START_SLUR",
    "END_SLUR",
    "START_CHORD",
    "END_CHORD",
    "DOT",
    "TIE",
    "R",
    )

t_tab_START_CHORD = r"\<"
t_tab_END_CHORD = r"\>"
t_tab_TIE = r"~"
t_tab_START_SLUR = r"\(|\["
t_tab_END_SLUR = r"\)|\]"
t_tab_R = r"r"
t_tab_DOT = '\.'

def t_BEGIN_TAB(t):
    r'%!'
    t.lexer.code_start = t.lexer.lexpos
    t.lexer.push_state('tab')

def t_tab_END_TAB(t):
    r'!%'
    t.value = t.lexer.lexdata[t.lexer.code_start:t.lexer.lexpos+1]
    t.type = "TAB"
    t.lexer.pop_state()


t_tab_ignore = " \t\n"

def t_tab_TUNING(t):
    r'OpenG|DoubleC|Modal'
    return t
    
def t_tab_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(t.value[0],end="")
    t.lexer.skip(1)

def t_tab_error(t):
    print("Unrecognized symbol in tablature: {}".format(t.value[0]))
    t.lexer.skip(1)

    
data = sys.stdin.read()
lexer = lex.lex()

    
def p_note(p):
    'note : NUMBER DOT NUMBER DOT NUMBER'
    p[0] = "STRING={},FRET={},DURATION={}".format(p[1],p[3],p[5])

def p_tuning(p):
    'tune : tuning'
    p[0] = p[1]
    
def p_rest(p):
    'rest : R NUMBER'
    p[0] = "REST {}".format(p[2])

def p_chord(p):
    "chord : START_CHORD chord_notes END_CHORD NUMBER"
    p[0] = "Chord Notes {}, Duration {}".format(p[2],p[4])

def p_chord_note(p):
    "chord_note :  NUMBER DOT NUMBER"
    p[0] = "Chord Note String = {}, Fret = {}".format(p[1],p[3])


def p_chord_notes(p):
    "chord_notes : chord_note"
    "chord_notes : chord_notes chord_note"
    if len(p)==5:
        p[0] = "Note String {}, Fret {}".format(p[1],p[3]) + p[4]
    else:
        p[0] = "Note String {}, Fret {}".format(p[1],p[3])


parser = yacc.yacc(debug=True)
result = parser.parse(data,debug=True)
print(result)
