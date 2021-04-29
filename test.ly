\version "2.22.1"
\header {title="New Five Cent" composer="Traditional"}
\paper {indent=0}
music = {
\time 4/4
\key c \major
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
g'4
c''
e''4
c''4
d''4
g'4
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
g'4
e'4
f'8
e'8
d'4
}
\alternative {
{
c'4
c''4
c'2
}
{
c'4
c''4
c'4
c''8
a'8
}
}
\repeat volta 2 {
g'4
e'4
e'4
c''8
a'8
g'4
e'4
e'4
c''8
a'8
g'4
e'4
f'4
e'4
d'8
c'8
d'8
e'8
d'4
c''8
a'8
g'8
e'8
c'8
e'8
g'4
e'4
f'4
g'4
a'8
b'8
c''8
a'8
g'4
c''4
e''4
d''4
}
\alternative {
{
c''4
g'4
c''4
c''8
a'8
}
{
c''4
g'4
c''2
}
}
\bar "|."
}

\score {
  \new Staff {
    \transpose c d {\music }
}}