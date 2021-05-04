notes={0:'c',1:'cis',2:'d',3:'dis',4:'e',5:'f',6:'fis',7:'g',8:'gis',9:'a',10:'ais',11:'b'}

frets={notes[k]:k for k in notes}

Tuning = {0:('d',1),1:('c',1),2:('g',0),3:('c',0),4:('g',1)}

staff_code = """

\\score {
\\new Staff \with {
     \omit StringNumber
     }
     {
      \key d \major
      \\numericTimeSignature
      {\\transpose c d {\\music}}
}
}
\\score {
\\new TabStaff \\with {
    tablatureFormat = #fret-number-tablature-format-banjo
    stringTunings = \\stringTuning <a'' d' a' d'' e''>
  }
  {
    {
      \\clef moderntab
      \\numericTimeSignature
      \\tabFullNotation
      {\\transpose c d {\\music}}
    }
  }
\header {
  piece = "aDADE"
}
}
"""


def fret_to_notes(base, fret):
    start_fret = frets[base]
    point = (start_fret+fret) % 12
    octave = (start_fret+fret) // 12
    octave_mark = '\'' if octave==0 else '\'\''
    return notes[point]+octave_mark


def decode(s):
    loc, fret, dur = s.split('.')
    tuning_note = Tuning[int(loc)][0]
    tuning_octave=Tuning[int(loc)][1]
    octave_mark = '' if tuning_octave==0 else '\''
    string_mark = '\\'+str(int(loc)+1)
    lily = fret_to_notes(tuning_note,int(fret))+octave_mark+dur+string_mark
    return lily


Apart1 = """
2.0.4 3.4.4 3.0.4 3.4.4
2.0.8 2.2.8 4.0.8 0.0.8 1.0.4 0.0.4
2.0.4 3.4.4 3.0.4 3.4.4
3.0.8 3.2.8 4.0.8 0.0.8 3.2.8 3.0.8 3.2.8 3.3.8
2.0.4 3.4.4 3.0.4 3.4.4
2.0.8 2.2.8 4.0.8 0.0.8 1.0.4 0.0.4
0.2.8 0.0.8 1.0.8 0.0.8 4.0.8 0.0.8 2.4.4
1.0.4 4.0.8 0.0.8 1.0.4 0.0.4
""".split()


Bpart1 = """
0.2.8 0.0.8 1.0.8 0.2.8 4.0.4 4.0.4
0.0.4 1.0.4 0.3.4 4.0.4
0.2.8 0.0.8 1.0.8 0.2.8 4.0.4 4.0.4
1.2.8 1.0.8 2.3.8 2.4.8 2.0.4 4.0.4
0.2.8 0.0.8 1.0.8 0.2.8 4.0.4 4.0.4
0.0.4 1.0.4 0.3.4 4.0.4
0.2.8 0.0.8 1.0.8 0.0.8 4.0.8 0.0.8 2.4.4
""".split()

Bpart_first_ending = "0.0.4 4.0.8 0.0.8 1.0.4 0.0.4".split()


Bpart_second_ending = "1.0.4 2.0.4 3.0.2".split()

print("\\version \"2.22.1\"")
print("\\paper { indent=0 }")
print("\\header {title=\"Soldiers Joy\"}")
print("music = {")
print("\\time 4/4")
print("\\repeat volta 2 {")
for x in Apart1:
    lily = decode(x)
    print(lily) 
print("}")
print("\\repeat volta 2 {")
for x in Bpart1:
    lily = decode(x)
    print(lily) 
print("}")
print("\\alternative {")
print("{")
for x in Bpart_first_ending:
    lily=decode(x)
    print(lily)
print("}")
print("{")
for x in Bpart_second_ending:
    lily=decode(x)
    print(lily)
print("}")
print("}")
print("\\bar \"|.\"")
print("}")
print(staff_code)
