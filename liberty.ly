\version "2.22.1"
\paper { indent=0 }
\header {title="Liberty"}
music ={
\time 4/4
\set Timing.beamExceptions = #'()
\set Timing.beatStructure = 1,1,1,1
\repeat volta 2 {
 e''8\1 g'8\3 e''8\1 g''8\5 e''8\1 g'8\3 e''8\1 g''8\5 e''8\1 g'8\3 e''8\1 g''8\5 e''8\1 d''8\1 c''4\2 f''8\1 a'8\3 f''8\1 g''8\5 f''8\1 a'8\3 f''8\1 g''8\5 f''8\1 a'8\3 f''8\1 g''8\5 f''8\1 e''8\2 d''8\1 g''8\5 e''8\1 g'8\3 e''8\1 g''8\5 e''8\1 g'8\3 e''8\1 g''8\5 e''8\1 g'8\3 e''8\1 g''8\5 e''8\1 d''8\1 c''4\2 f''8\1 e''8\2 d''8\1 g''8\5 e''8\1 d''8\1 c''8\2 g''8\5 d''8\1 c''8\2 d''8\1 g''8\5 c''2\2 
}
\repeat volta 2 {
 g'4\3 g'8\3 a'8\3 g'4\3 e'4\4 g'4\3 c''4\3 e''8\2 d''8\2 c''4\2 g'4\3 g'8\3 a'8\3 g'4\3 e'4\4 d'8\4 c'8\4 d'8\4 e'8\4 d'8\4 e'8\4 f'4\4 g'4\3 g'8\3 a'8\3 g'4\3 e'4\4 g'4\3 c''4\3 e''8\2 d''8\2 c''4\2 f''8\1 e''8\2 d''8\1 g''8\5 e''8\1 d''8\1 c''8\2 g''8\5 d''8\1 c''8\2 d''8\1 g''8\5 c''2\2 
}
}


\new StaffGroup <<
  \new Staff \with {                                                             
     \omit StringNumber                                                         
     }                                                                          
     {                                                                          
      \key d \major                                                             
      \numericTimeSignature                                                    
      {\transpose c d {\music}}                                               
    }                                                                               
  \new TabStaff \with {                                                         
    tablatureFormat = #fret-number-tablature-format-banjo                       
    stringTunings = \stringTuning <a'' d' a' d'' e''>
  }                                                                             
  {                                                                             
    {                                                                           
      \clef moderntab                                                          
      \numericTimeSignature                                                    
      \tabFullNotation                                                         
      {\transpose c d {\music}}                                               
    }                                                                           
  }
>>
  

