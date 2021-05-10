\version "2.22.1"
\paper { indent=0 }
\header {title="New Five Cent"}
music ={
\time 4/4
\repeat volta 2 {
g'4
e''8
d''8
e''8
f''8
e''8
d''8
c''8
e''8
d''8
c''8
a'8
b'8
c''8
a'8
g'8
a'8
g'8
f'8
e'8
f'8
g'4
d''2
d''2
g'4
e''8
d''8
e''8
f''8
e''8
d''8
c''8
e''8
d''8
c''8
a'8
b'8
c''8
a'8
g'8
f'8
e'8
c'8
d'2
}
\alternative {
{
c'2
c'2
}
{
c'2
c'4
c''8
a'8
}
}
\repeat volta 2 {
g'8
d'8
e'8
f'8
e'4
c''8
a'8
g'8
d'8
e'8
f'8
e'4
c''8
a'8
g'4
e'4
f'4
e'4
d'2
d'4
c''8
a'8
g'8
e'8
c'8
e'8
g'8
e'8
c'8
d'16
e'16
f'8
e'8
f'8
g'8
a'8
b'8
c''8
a'8
g'8
f'8
e'8
c'8
d'2
}
\alternative {
{
c'2
c'4
c''8
a'8
}
{
c''2
c''2
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

