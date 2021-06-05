\version "2.22.1"
\layout {indent = 0}
\header {title="Time Has Made a Change in Me"
	 composer = "Traditional"
         piece = "gDGBD"}
music ={
\time 3/4
%\set Timing.beamExceptions = #'()
%\set Timing.beatStructure = 3,3
a4. a8 a8 b8
a2 a8 b8
d2 d4
d2.
e4. d8 e8 d8
e2 fis8 e8
d2 d8 e8
fis2.
fis4. e8 fis8 e8
fis8 e8 d4 fis8 e8
d2 d4
a2.
d4. a8 d8 e8
fis2 e4
d2.~ d2.

b4. a8 b8 a8
b2 b8 d8
d2 b4
a2.

d4. a8 d8 e8
fis2 e8 d8
e2 fis4
e2.

fis4. e8 fis8 e8
fis8 e8 d4 fis8 e8
d2 d4
a2.

d4. a8 d8 e8
fis2 e4
d2.~
d2.
\bar "|."
}


\score{
\new StaffGroup <<
  \new ChordNames \chordmode {
    g2. g2. c2. g2.
    d2. d2. g2. g2.
    g2. g2. c2. g2.
    g2. d2. g2. g2.
    e2.:m e2.:m g2. g2.
    g2. g2. d2. d2.
    g2. g2. c2. g2.
    g2. d2. g2. g2.

  }
  \new Staff \with {                                                             
     \omit StringNumber                                                         
     }                                                                          
     {                                                                          
      \key g \major                                                             
      \numericTimeSignature                                                    
      {\transpose d g, {\relative a' {\music}}}
      }
  \new TabStaff \with {                                                         
    tablatureFormat = #fret-number-tablature-format-banjo                       
    stringTunings = \stringTuning <g' d g b d'>
  }                                                                             
  {                                                                             
    {                                                                           
      \clef moderntab                                                          
      \tabFullNotation
      \numericTimeSignature                                                    
       {\transpose d g, {\relative a {\music}}}
    }                                                                           
  }
>>
%\midi{}
}  
