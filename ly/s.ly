\version "2.22.1"

music = {
  c' e' g'\5 g' d'\2 d'
}

<<
  \new TabStaff \with {
    tablatureFormat = #fret-number-tablature-format-banjo
    stringTunings = \stringTuning <g' c g c' d'>
  }
  { \music}
>>
  

