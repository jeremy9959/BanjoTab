import re

notes = {
    0: 'c',
    1: 'cis',
    2: 'd',
    3: 'dis',
    4: 'e',
    5: 'f',
    6: 'fis',
    7: 'g',
    8: 'gis',
    9: 'a',
    10: 'ais',
    11: 'b'
}
frets = {notes[k]: k for k in notes}
Tuning = {0: ('d', 1), 1: ('c', 1), 2: ('g', 0), 3: ('c', 0), 4: ('g', 1)}

note = r'(?P<string>[0-9])\.(?P<fret>[0-9]+)\.(?P<duration>[0-9]+)'
chord = r'(?P<chord>\[\s*([0-9]\.[0-9]+\s+)+[0-9]\.[0-9]+\s*\])(?P<duration>[0-9]+)'
chord_note = r'(?P<string>[0-9])\.(?P<fret>[0-9]+)'
slur_start = r'(\()'
slur_end = r'(\))'
tie = r'~'
ws = r'\s+'


def fret_to_notes(base, fret):
    start_fret = frets[base]
    point = (start_fret + fret) % 12
    octave = (start_fret + fret) // 12
    octave_mark = '\'' if octave == 0 else '\'\''
    return notes[point] + octave_mark


def decode_simple(loc, fret):
    tuning_note = Tuning[int(loc)][0]
    tuning_octave = Tuning[int(loc)][1]
    octave_mark = '' if tuning_octave == 0 else '\''
    lily = fret_to_notes(tuning_note, int(fret)) + octave_mark
    return lily


def decode(loc, fret, dur):
    lily = decode_simple(loc, fret)
    return lily + dur


def parse(s):
    parsed = ''
    N = len(s)
    i = 0
    while i < N:
        if re.match(slur_start, s[i:]):
            parsed += '('
            i += 1
            continue

        if re.match(slur_end, s[i:]):
            parsed += ')'
            i += 1
            continue

        if re.match(tie, s[i:]):
            parsed += '~'
            i += 1
            continue

        ws_try = re.match(ws, s[i:])
        if ws_try:
            parsed += ' '
            i += ws_try.end() - ws_try.start()
            continue

        note_try = re.match(note, s[i:])
        if note_try:
            i += note_try.end() - note_try.start()
            lily = decode(note_try.group('string'), note_try.group('fret'),
                          note_try.group('duration'))
            parsed += lily + '\\{}'.format(int(note_try.group('string')) + 1)
            continue
        chord_try = re.match(chord, s[i:])
        if chord_try:
            i += chord_try.end() - chord_try.start()
            chord_string = chord_try.group('chord')
            chord_duration = chord_try.group('duration')
            chord_notes = re.findall(chord_note, chord_string)
            parsed += '< '
            for x in chord_notes:
                parsed += decode_simple(x[0],
                                        x[1]) + '\\{} '.format(int(x[0]) + 1)
            parsed += '>' + chord_duration
            continue
    return parsed


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
Apart1 = """                                                                    
2.0.4 0.2.8( 0.0.8 0.2.8 0.3.8 0.2.8 0.0.8)
1.0.8 0.2.8 0.0.8 1.0.8 2.2.8 2.4.8 1.0.8 2.2.8                                
2.0.8 2.2.8 2.0.8 3.5.8 3.4.8 3.5.8 2.0.4                                      
0.0.2~  0.0.2
2.0.4 0.2.8 0.0.8 0.2.8 0.3.8 0.2.8 0.0.8                                       
1.0.8 0.2.8 0.0.8 1.0.8 2.2.8 2.4.8 1.0.8 2.2.8                                 
2.0.8 3.5.8  3.4.8 3.0.8 3.2.2                                                  
"""
Apart_first_ending = "3.0.2~  3.0.2"
Apart_second_ending = "3.0.2 3.0.4 1.0.8 2.2.8"
Bpart1 = """                                                                    
2.0.8 3.2.8 3.4.8 3.5.8 3.4.4 1.0.8 2.2.8                                       
2.0.8 3.2.8 3.4.8 3.5.8 3.4.4 1.0.8 2.2.8                                       
2.0.4 3.4.4 3.5.4 3.4.4                                                         
3.2.2  3.2.4 1.0.8 2.2.8                                                        
2.0.8 3.4.8 3.0.8 3.4.8 2.0.8 3.4.8 3.0.8 3.2.16 3.4.16                         
3.5.8 3.4.8 3.5.8 2.0.8 2.2.8 2.4.8 1.0.8 2.2.8                                 
2.0.8 3.5.8  3.4.8 3.0.8 3.2.2                                                  
"""
Bpart_first_ending = "3.0.2 3.0.4  1.0.8 2.2.8"
Bpart_second_ending = "1.0.2~ 1.0.2"

print("\\version \"2.22.1\"")
print("\\paper { indent=0 }")
print("\\header {title=\"New Five Cent\"}")
print("music ={")
print("\\time 4/4")
print("\\repeat volta 2 {")
lily = parse(Apart1)
print(lily)
print("}")
print("\\alternative {")
print("{")
lily = parse(Apart_first_ending)
print(lily)
print("}")
print("{")
lily = parse(Apart_second_ending)
print(lily)
print("}")
print("}")
print("\\repeat volta 2 {")
lily = parse(Bpart1)
print(lily)
print("}")
print("\\alternative {")
print("{")
lily = parse(Bpart_first_ending)
print(lily)
print("}")
print("{")
lily = parse(Bpart_second_ending)
print(lily)
print("}")
print("}")
print("\\bar \"|.\"")
print("}")

print(staff_code)
