\version "2.22.1"
\paper { indent=0 }
\header {
  title="Wildwood Flower"
  composer = "Traditional (arr. Matt Brown)"
}

music ={
\time 4/4
\set Timing.beamExceptions = #'()
\set Timing.beatStructure = 1,1,1,1

r2 b'4\2 c''4\2
\repeat volta 2 {

d''4\1 g''8\5 d''8\1 e''4\2 g''4\5 b'4\2 g''8\5 d''8\1 c''4\2 b'4\2 a'4\3 g''8\5 d''8\1 b'8\3 a'8\3 fis'4\4 g'4\3 g''8\5 d''8\1 e'8\4 g'8\4 g''8\5 d''8\1

}                                                                                
\alternative {
{

g'4\3 g''8\5 d''8\1 b'4\2 c''4\2

}
{
g'4\3 g''4\5 d''4\1 g''4\5
}
}

a''8\1 ( b''8\1 ) g''8\5 b''8\1 g''4\5 a''4\1 g''4\2 g''4\5 d''4\1 g''4\5 < e''\1 c''\2 >4 g''4\5 fis''4\1 e''4\1 d''4\1 g''8\5 d''8\1 g'4\3 a'4\3 a'8\3 b'8\3 g''8\5 d''8\1 b'4\2 b'4\2 d''4\1 g''8\5 d''8\1 c''8\2 b'8\2 g''8\5 d''8\1 a'4\3 d'4\4 b'8\3 a'8\3 fis'4\4 g'4\3 g''8\5 d''8\1 e'8\4 g'8\4 g''8\5 d''8\1 g'4\3 < d''\1 g''\5 >4 b'4\2 c''4\2

\bar "|."
}

\score {
  \new StaffGroup <<
    \new Staff \with {                                                             
      \omit StringNumber                                                         
    }                                                                          
    {                                                                          
      \key g \major                                                             
      \numericTimeSignature                                                    
      {\music}                                               
    }                                                                               
    \new TabStaff \with {                                                         
      tablatureFormat = #fret-number-tablature-format-banjo                       
      stringTunings = \stringTuning <g'' d' g' b' d''>
    }                                                                             
    {                                                                             
      {                                                                           
        \clef moderntab                                                          
        \numericTimeSignature                                                    
        \tabFullNotation                                                         
        {\music}                                               
      }
    }
  >>
  \header {
    piece = "gDGBD"
  }
  }

