\version "2.22.1"
\paper { indent=0 }
\header {title="Soldiers Joy"}
music = {
\time 4/4
\repeat volta 2 {
g'4\3
e'4\4
c'4\4
e'4\4
g'8\3
a'8\3
g''8\5
d''8\1
c''4\2
d''4\1
g'4\3
e'4\4
c'4\4
e'4\4
c'8\4
d'8\4
g''8\5
d''8\1
d'8\4
c'8\4
d'8\4
dis'8\4
g'4\3
e'4\4
c'4\4
e'4\4
g'8\3
a'8\3
g''8\5
d''8\1
c''4\2
d''4\1
e''8\1
d''8\1
c''8\2
d''8\1
g''8\5
d''8\1
b'4\3
c''4\2
g''8\5
d''8\1
c''4\2
d''4\1
}
\repeat volta 2 {
e''8\1
d''8\1
c''8\2
e''8\1
g''4\5
g''4\5
d''4\1
c''4\2
f''4\1
g''4\5
e''8\1
d''8\1
c''8\2
e''8\1
g''4\5
g''4\5
d''8\2
c''8\2
ais'8\3
b'8\3
g'4\3
g''4\5
e''8\1
d''8\1
c''8\2
e''8\1
g''4\5
g''4\5
d''4\1
c''4\2
f''4\1
g''4\5
e''8\1
d''8\1
c''8\2
d''8\1
g''8\5
d''8\1
b'4\3
}
\alternative {
{
d''4\1
g''8\5
d''8\1
c''4\2
d''4\1
}
{
c''4\2
g'4\3
c'2\4
}
}
\bar "|."
}


\score {
\new Staff \with {
     \omit StringNumber
     }
     {
      \key d \major
      \numericTimeSignature
      {\transpose c d {\music}}
}
}
\score {
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
\header {
  piece = "aDADE"
}
}

