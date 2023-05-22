\version "2.22.1"
\paper { indent=0 }
\header {title="John Riley/Brushy Fork"
  composer = "Traditional (arr. Hurt/Brown)"
  piece = "fDGCD"
	}
music ={\bar ".|:"
\time 4/4
\repeat volta 3{
\repeat volta 2 {
 d''4\1 c''8\2 f''8\5 d''8\1 c''8\2 e''8\1 (f''8\1) d''8\1 c''8\2 a'8\3 (g'8\3) f'8\4 (d'8\4) f'8\4 f''8\5 g'8\3 (a'8\3) d''8\1 c''8\2 a'8\3 (g'8\3) f'8\4 (g'8\3) d'4\4 d''8\1 f''8\5 d'4\4 d'8\4 f''8\5 d''4\1 c''8\2 f''8\5 d''8\1 c''8\2 e''8\1 (f''8\1) d''8\1 c''8\2 a'8\3 (g'8\3) f'8\4 (d'8\4) f'8\4 f''8\5 g'8\3 (a'8\3) d''8\1 c''8\2 a'8\3 (g'8\3) f'8\4 (d'8\4) g'4\3 d''8\1 f''8\5 g'4\3 g'8\3 f''8\5 
}

 g'8\3 (a'8\3) d''8\1 c''8\2 a'8\3 (g'8\3) f'8\4 (g'8\3) d'4\4 d''8\1 f''8\5 d'4\4 d'8\4 f''8\5 g'8\3 (a'8\3) d''8\1 c''8\2 a'8\3 (g'8\3) f'8\4 (g'8\3) d'4\4 d''8\1 f''8\5 d'4\4 d'8\4 f''8\5 g'8\3 (a'8\3) d''8\1 c''8\2 a'8\3 (g'8\3) f'8\4 (g'8\3) d'4\4 d''8\1 f''8\5 a'8\3 (g'8\3) a'8\3 (c''8\2) d''4\1 c''8\2 f''8\5 a'8\3 (g'8\3) f'4\4 g'4\3 d''8\1 f''8\5 g'4\3 g'8\3 f''8\5 
}
\repeat volta 2 {
 d''8\1 (g''8\1) g'8\3 f''8\5 g''4\1 e''8\1 (f''8\1) d''8\1 c''8\2 d''8\1 f''8\5 f''8\1 (d''8\1) c''8\2 f''8\5 d''8\1 (g''8\1) g'8\3 f''8\5 g''4\1 e''8\1 (f''8\1) d''8\1 c''8\2 a'8\3 f''8\5 d'4\4 d'8\4 f''8\5 d''8\1 (g''8\1) g'8\3 f''8\5 g''4\1 f''8\1 g''8\1 a''4\1 a''8\1 f''8\5 g''8\1 f''8\5 d''8\1 c''8\2 d''8\1 (g''8\1) g'8\3 f''8\5 g''4\1 e''8\1 (f''8\1) d''8\1 c''8\2 a'8\3 f''8\5 d'4\4 d'8\4 f''8\5 
}
\repeat volta 2 {
 a'8\3 (g'8\3) a'8\3 (c''8\2) d''4\1 d'8\4 f''8\5 d''8\1 f''8\5 d''8\1 c''8\2 a'8\3 c''4\2 f''8\5 a'8\3 (g'8\3) a'8\3 (c''8\2) d''4\1 d'8\4 f''8\5 d''8\1 c''8\2 a'8\3 (c''8\2) g'4\3 g'8\3 f''8\5 a'8\3 (g'8\3) a'8\3 (c''8\2) d''4\1 d'8\4 f''8\5 d''8\1 f''8\5 d''8\1 c''8\2 a'8\3 f''8\5 d''8\1 c''8\2 g'4\3 a'8\3 (c''8\2) d''4\1 e''8\1 (f''8\1) d''8\1 c''8\2 a'8\3 c''8\2 g'4\3 g'8\3 f''8\5 
}
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

