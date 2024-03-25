\version "2.24.1"
\paper { indent=0 systems-per-page=7}
\header {title="Lost Lula"
  composer = "Jason Romero"
  piece = "fDGCD"
}
music ={
\time 4/4
\repeat volta 2 {
\mark "A"  f''8\1 (d''8\1) e''8\1 (f''8\1) d''8\1 c''8\2 a'4\3 f''8\1  \glissando  g''4\1 f''8\5 g''8\1 (f''4\1) f''8\5 g''8\1  \glissando  a''4\1 f''8\5 \tuplet3/2 { a''\1 g''\1 f''\5 } d''8\1 c''8\2 a'4\3 c''4\2 d''4\1  \xNote  d''8\1 f''8\5 d''4\1 d''8\1 f''8\5  \accent   \xNote  d''8\1 c''8\2 a'4\3 f''8\1 (d''8\1) e''8\1 (f''8\1) d''8\1 c''8\2 a'4\3 ais'8\3 c''8\2 d''8\1 f''8\5 d''8\1 c''8\2 a'8\3 (g'8\3) f'4\4 g'8\3 (a'8\3) c''4\2 d''8\1 (f''8\1) f''8\1 d''8\2 f''8\1 f''8\5 d''8\1 c''8\2 a'4\3 f''8\1 \glissando  g''4\1 f''8\5 g''8\1 (f''4\1) f''8\5 g''8\1 \glissando  a''4\1 f''8\5 \tuplet3/2 { a''\1 g''\1 f''\5 } d''8\1 c''8\2 a'4\3 c''4\2 d''4\1  \xNote  d''8\1 f''8\5 d''4\1 d''8\1 f''8\5  \accent   \xNote  d''8\1 c''8\2 a'4\3 f''8\1 (d''8\1) e''8\1 (f''8\1) d''8\1 c''8\2 a'4\3 ais'8\3 c''8\2 d''8\1 f''8\5 d''8\1 c''8\2 a'8\3 g'8\3  \mark "B"  f'4\4 g'8\3 (a'8\3) c''4\2 d''4\1 d'4\4 d''8\1 (c''8\2) d''8\1 f''8\5 d''8\1 c''8\2 a'4\3 c''4\2 d''4\1 ais'8\3 (c''8\2) d''8\1 f''8\5 d''8\1 c''8\2 a'8\3 g'8\3 f'8\4 (d'8\4) d'8\4 (f'8\4) g'8\3 a'8\3 c''4\2 d''4\1 d'4\4 d''8\1 (c''8\2) d''8\1 f''8\5 d''8\1 c''8\2 a'4\3 c''4\2 d''4\1 ais'8\3 (c''8\2) d''8\1 f''8\5 d''8\1 c''8\2 a'8\3 g'8\3 f'8\4 (d'8\4) d'8\4 (f'8\4) g'8\3 a'8\3 c''4\2 d''4\1 d'4\4 d''8\1 (c''8\2) d''8\1 f''8\5 d''8\1 c''8\2 a'4\3 c''4\2 d''4\1 ais'8\3 (c''8\2) d''8\1 f''8\5 d''8\1 c''8\2 a'8\3 g'8\3 f'8\4 d'8\4 d'8\4 f'8\4 g'8\3 a'8\3 c''4\2 d''4\1 d'4\4 d''8\1 (c''8\2) d''8\1 f''8\5 d''8\1 c''8\2 a'4\3 c''4\2 d''4\1 ais'8\3 (c''8\2) d''8\1 f''8\5 d''8\1 c''8\2 a'8\3 g'8\3 f'8\4 d'8\4 f'4\4 g'8\3 (a'8\3) c''4\2 d''8\1 (f''8\1) 
}}

\new StaffGroup <<
\new Staff \with {                                                             
     \omit StringNumber                                                         
     }                                                                          
     {                                                                          
      \key f \major                                                             
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

