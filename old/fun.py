notes={0:'c',1:'cis',2:'d',3:'dis',4:'e',5:'f',6:'fis',7:'g',8:'gis',9:'a',10:'ais',11:'b'}
frets={notes[k]:k for k in notes}
Tuning = {0:('d',1),1:('c',1),2:('g',0),3:('c',0),4:('g',1)}


def fret_to_notes(base, fret):
    start_fret = frets[base]
    point = (start_fret+fret) % 12
    octave = (start_fret+fret) // 12
    octave_mark = '\'' if octave==0 else '\'\''
    return notes[point]+octave_mark

s = "1.0.2 3.0.4~ <2.0 3.5>8 (2.1.4 3.2.5)"
def parse_string(s):
    L = s.split()
    k=0
    N=len(L)
    while k<N:
        token = L[k]
        print('token is',token)
        if token[0] == '<':
            chord_tokens=[token[1:]]
            k+=1
            while '>' not in L[k]:
                chord_tokens.append(L[k])
                k+=1
            chord_tokens.append(L[k])
            print(parse_chord(chord_tokens))
            k+=1
            continue
        if token[0]=='(':
            print(parse_slur_start(token))
        
        if token[-1]==')':
            print(parse_slur_end(token))
        
        if token[-1]=='~':
            print(parse_tie (token))
        
        print(parse_note(token))
        k+=1

        
def parse_note(token):
    loc, fret, dur = token.split('.')
    tuning_note = Tuning[int(loc)][0]
    tuning_octave=Tuning[int(loc)][1]
    octave_mark = '' if tuning_octave==0 else '\''
    lily = fret_to_notes(tuning_note,int(fret))+octave_mark+dur
    return lily

def parse_slur_start(token):
    print(token)
    note = parse_note(token[1:])
    return '('+note

def parse_slur_end(token):
    note = parse_note(token[:-1])
    return note+')'

def parse_tie(token):
    note = parse_note(token[:-1])
    return note+'~'

def parse_chord(chord_tokens):
    return chord_tokens

parse_string(s)
