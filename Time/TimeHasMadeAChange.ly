\version "2.22.1"
\layout {indent = 0}
\header {title="Time Has Made a Change in Me"
	 composer = "Harkins Freye"
         piece = "gDGBD"
	 tagline = ##f
       }
verseA = \lyricmode {
  Time has made a change since my child  hood days,
  Ma -- --  ny of my friends ha -- ve gone a _ way,
  Some I nev -- er mo -- re _ in this life will see,
  Time has made a change in me.
}
verseB = \lyricmode {
  In my child hood days I was well and strong
  I could climb the hill --  sides _ all day _ long
  I am not to -- day _ _ what I  used to be
  Time has made a change in me.
}
verseC = \lyricmode {
  When I reach my home in that land some where
  With my friends who wait,to meet me o -- ver _ there
  Free from pain and care _ _ I'll for --  ev -- er be
  Time has made a change in me.
  }
chorus = \lyricmode {
  Time has made a change in the old home pla -- ce.
  Time has made a change in each smil -- ing face.
  And I know my friends _ _ can _  plain -- ly  see
  Time has made a change in me.
  }

musicVerse ={
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
}


musicChorus = {
b4. a8 b8 a8
b2 b8 d8
d2 d4
b8 a8~ a2

d4. a8 d8 e8
fis2 d8 e8
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

chordline = \chordmode {
    g2. g2. c2. g2.
    d2. d2. g2. g2.
    g2. g2. c2. g2.
    g2. d2. g2. g2.
    e2.:m e2.:m g2. g2.
    g2. g2. a2. d2.
    g2. g2. c2. g2.
    g2. d2. g2. g2.
}

\score{
   {
\new StaffGroup <<
  \new ChordNames  {
    \repeat volta 3 {\chordline}
  }
  \new Staff \with {                                                             
     \omit StringNumber                                                         
     }                                                                          
  \new Voice = "melody" {
      \key g \major                                                             
      \numericTimeSignature                                                    
      \repeat volta 3 {\transpose d g, {\relative a' {\musicVerse \musicChorus}}}
%      {\transpose d g, {\relative a' {\musicChorus}}}
    }
  \new Lyrics {
    \lyricsto "melody" {
      <<
	{ \verseA \chorus}
	\new Lyrics {
	  \set associatedVoice = "melody"
	  \verseB }
	\new Lyrics {
	  \set associatedVoice = "melody"
	  \verseC }
      >>
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
       \repeat volta 3 {\transpose d g, {\relative a {\musicVerse \musicChorus}}}
%      {\relative a {\musicChorus}}
    }                                                                           
  }
>>
}
\layout {}
\midi{
\tempo 4 = 90
}
}  
