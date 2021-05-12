\version "2.22.1"
\paper { indent=0 }
\header {title="New Five Cent"}
music ={
\time 4/4
\repeat volta 2 {
 g'4\3 e''8\1( d''8\1 e''8\1 f''8\1 e''8\1 d''8\1) c''8\2 e''8\1 d''8\1 c''8\2 a'8\3 b'8\3 c''8\2 a'8\3 g'8\3 a'8\3 g'8\3 f'8\4 e'8\4 f'8\4 g'4\3 d''2\1~ d''2\1 g'4\3 e''8\1 d''8\1 e''8\1 f''8\1 e''8\1 d''8\1 c''8\2 e''8\1 d''8\1 c''8\2 a'8\3 b'8\3 c''8\2 a'8\3 g'8\3 f'8\4 e'8\4 c'8\4 d'2\4 
}                                                                                
\alternative {
{
 c'2\4~ c'2\4 
}
{
 c'2\4 c'4\4 c''8\2 a'8\3 
}
}
\repeat volta 2 {
 g'8\3[ d'8\4 e'8\4 f'8\4 ] e'4\4 c''8\2 a'8\3 g'8\3 d'8\4 e'8\4 f'8\4 e'4\4 c''8\2 a'8\3 g'4\3 e'4\4 f'4\4 e'4\4 d'2\4 d'4\4 c''8\2 a'8\3 g'8\3 e'8\4 c'8\4 e'8\4 g'8\3 e'8\4 c'8\4 d'16\4 e'16\4 f'8\4 e'8\4 f'8\4 g'8\3 a'8\3 b'8\3 c''8\2 a'8\3 g'8\3 f'8\4 e'8\4 c'8\4 d'2\4 
}
\alternative {
{
 c'2\4 c'4\4 c''8\2 a'8\3 
}
{
 c''2\2~ c''2\2 
}
}
\bar "|."
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
  

