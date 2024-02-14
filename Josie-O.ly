\version "2.22.1"
\paper { indent=0 system-count=5 }
\header {title="Josie-O"
  composer = "Traditional (arr. Hurt/Brown)"
  piece = "fDGCD"
}
music ={
\time 4/4
\repeat volta 2 {
\repeat volta 2 {\bar ".|:" \mark "A"   d'8\4 (f'8\4) r8 f''8\5 a'8\3 (g'8\3) f'8\4 f''8\5 g'4\3 a'4\3 c''4\2 a'8\3 c''8\2 d''4\1 c''4\2 a'8\3 (g'8\3) f'4\4 g'8\3 (f'8\4) r8 f''8\5 f'4\4 < f'\4 a'\3 >8 (f''8\5) d'8\4 (f'8\4) r8 f''8\5 a'8\3 (g'8\3) f'8\4 f''8\5 g'4\3 a'4\3 c''4\2 f''8\1 (e''8\1) d''4\1 c''4\2 a'8\3 (g'8\3) f'4\4 g'8\3 (f'8\4) r8 f''8\5 f'4\4 < f'\4 a'\3 >8 (f''8\5) 
}

{\section\mark "B"  f'4\4 f''4\1 f''8\1 (d''8\1) f''8\1 f''8\5 g''8\1 (a''8\1) c''8\2 f''8\5 a''8\1 (d''8\1) c''8\2 f''8\5 a''8\1 (d''8\1) c''8\2 g''8\1 f''4\5 g''8\1 f''8\5 d''8\1 c''8\2 r8 f''8\5 c''8\2 a'8\3 g'8\3 f''8\5 f'4\4 f''4\1 f''8\1 (d''8\1) f''8\1 f''8\5 g''8\1 (a''8\1) c''8\2 f''8\5 a''8\1 (d''8\1) c''8\2 f''8\5 a''8\1 (d''8\1) c''8\2 g''8\1 f''4\5 g''8\1 f''8\5 d''8\1 c''8\2 r8 f''8\5 c''4\2 a'8\3 (c''8\2)  \section\mark "C"  d''4\1 c''4\2 a'8\3 (g'8\3) d'4\4 d''8\1 c''8\2 < e''\1 c''\2 >4 f''4\1 e''8\1 (f''8\1) d''4\1 c''4\2 a'8\3 (g'8\3) f'8\4 f''8\5 g'8\3 (f'8\4) r8 f''8\5 f'8\4 (g'8\3) a'8\3 (c''8\2) d''4\1 c''4\2 a'8\3 (g'8\3) d'4\4 d''4\1 < e''\1 c''\2 >8 (f''8\5) f''4\1 < e''\1 c''\2 >8 (f''8\5) d''4\1 c''4\2 a'8\3 (g'8\3) f'8\4 f''8\5  }

\alternative {
  \volta 1 {  g'8\3 (f'8\4) r8 f''8\5 f'4\4 < f'\4 a'\3 >8 (f''8\5)  }
  \volta 2 {  g'8\3 (f'8\4) r8 f''8\5 f'2\4  }
}
\fine


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

