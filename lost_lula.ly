\version "2.22.1"
\paper { indent=0 }
\header {title="Lost Lula"
  composer = "Jason Romero"
  piece = "fDGCD"
}
music ={
\time 4/4
 f''8\1 d''8\1 e''8\1 f''8\1 d''8\1 c''8\2 a'4\3 f''8\1 g''4\1 f''8\5 g''8\1 f''4\5 f''8\5 g''8\1 a''4\1 f''8\5  %-- triplet 0.7.8 0.5.8 4.0.8 
 d''8\1 c''8\2 a'4\3 c''4\2 d''4\1 d''8\1 f''8\5 d''4\1 d''8\1 f''8\5 d''8\1 c''8\2 a'4\3 f''8\1 d''8\1 e''4\1 f''8\1 d''8\1 c''8\2 a'4\3 ais'8\3 c''8\2 d''8\1 f''8\5 d''8\1 c''8\2 a'8\3 g'8\3 f'4\4 g'8\3 a'8\3 c''4\2 d''8\1 f''8\1 f''8\1 d''8\2 f''8\1 f''8\5 d''8\1 c''8\2 a'4\3 
}

\new StaffGroup <<
\new Staff \with {                                                             
     \omit StringNumber                                                         
     }                                                                          
     {                                                                          
      \key c \major                                                             
      \numericTimeSignature                                                    
       \music                                    
    }                                                                                 
                                                                         
  \new TabStaff \with {                                                         
    tablatureFormat = #fret-number-tablature-format-banjo                       
    stringTunings = \stringTuning <f'' d' g' c'' d''>
  }                                                                             
  {                                                                             
    {                                                                           
      \clef moderntab                                                          
      \numericTimeSignature                                                    
      \tabFullNotation                                                         
      \music                                  
    }                                                                      
  }
>>

