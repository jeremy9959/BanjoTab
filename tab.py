from collections import namedtuple

notes={0:'c',1:'cis',2:'d',3:'dis',4:'e',5:'f',6:'fis',7:'g',8:'gis',9:'a',10:'ais',11:'b'}

frets={notes[k]:k for k in notes}

Note = namedtuple('note',['string','fret','duration'])

Tuning = {0:'d',1:'c',2:'g',3:'c',4:'g'}

def fret_to_notes(base, fret):
    start_fret = frets[base]
    point = (start_fret+fret) % 12
    octave = (start_fret+fret) // 12
    octave_mark = '\'' if octave==0 else '\'\''
    return notes[point]+octave_mark


def decode(s):
    loc, fret, dur = s.split('.')
    lily = fret_to_notes(Tuning[int(loc)],int(fret))+dur
    return lily


test = "2.0.4 0.2.8 0.0.8 0.2.8 0.3.8 0.2.8 0.0.8"

print("\\version \"2.22.1\"")
print("{")
measure = test.split()
for x in measure:
    lily = decode(x)
    print(lily) 
print("}")
