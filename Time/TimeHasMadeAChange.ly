\version "2.22.1"
\layout {indent = 0}
\header {title="Time Has Made a Change in Me"
	 composer = "Harkins Freye"
         piece = "gDGBD"}
words = \lyricmode {
  Time has made a change since my child  hood days,
  Ma -- --  ny of my friends ha -- ve gone a _ way,
  Some I nev -- er mo -- re _ in this life will see,
  Time has made a change in me.
  Time has made a change in the old home place.
  Time has made a change in each smil -- ing face.
  And I know my friends _ _ can _  plain -- ly  see
  Time has made a change in me.
  }

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
  \new Voice = "melody" {
      \key g \major                                                             
      \numericTimeSignature                                                    
      {\transpose d g, {\relative a' {\music}}}
      }
  \new Lyrics {
    \lyricsto "melody" {
      \words
    }
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
\layout {}
\midi{
\tempo 4 = 90
}
}  
