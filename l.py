import ly.lex
txt = r"\relative c' { 1.1 d e f-^ g }"
s =ly.lex.state("lilypond")
for t in s.tokens(txt):
	print(t,t.__class__.__name__)

