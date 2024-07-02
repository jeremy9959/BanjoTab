major_intervals = [2, 2, 1, 2, 2, 2, 1]
minor_intervals = [2, 1, 2, 2, 1, 2, 2]
c_major_scale = [
    "C,",
    "^C,",
    "D,",
    "^D,",
    "E,",
    "F,",
    "^F,",
    "G,",
    "^G,",
    "A,",
    "^A,",
    "B,",
    "C",
    "^C",
    "D",
    "^D",
    "E",
    "F",
    "^F",
    "G",
    "^G",
    "A",
    "^A",
    "B",
    "c",
    "^c",
    "d",
    "^d",
    "e",
    "f",
    "^f",
    "g",
    "^g",
    "a",
    "^a",
    "b",
    "c'",
    "^c'",
    "d'",
    "^d'",
    "e'",
    "f'",
    "^f'",
    "g'",
    "^g'",
    "a'",
    "^a'",
    "b'",
    "c''",
]

root = 2
scale = ""
for i in major_intervals * 4:

    scale = scale + c_major_scale[root] + " "
    root += i
    if root >= len(c_major_scale):
        break
print(scale)
