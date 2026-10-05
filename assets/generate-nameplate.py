GLYPHS = {
 "K": ["#...#","#..#.","#.#..","##...","#.#..","#..#.","#...#"],
 "A": [".###.","#...#","#...#","#####","#...#","#...#","#...#"],
 "R": ["####.","#...#","#...#","####.","#.#..","#..#.","#...#"],
 "M": ["#...#","##.##","#.#.#","#...#","#...#","#...#","#...#"],
 "L": ["#....","#....","#....","#....","#....","#....","#####"],
 "T": ["#####","..#..","..#..","..#..","..#..","..#..","..#.."],
 "I": ["#####","..#..","..#..","..#..","..#..","..#..","#####"],
 "Y": ["#...#","#...#",".#.#.","..#..","..#..","..#..","..#.."],
 " ": ["....."]*7,
}
NAME = "KARAM AL TAKRITY"
CELL, GAPC, PADX, PADY = 6, 1, 14, 12
GW, GH = 5, 7

def build(dim, lit, cursor, out):
    cw = GW + GAPC
    W = PADX*2 + len(NAME)*cw*CELL - GAPC*CELL + 3*CELL   # room for cursor
    H = PADY*2 + GH*CELL
    s = []
    s.append(f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H}' "
             f"width='{W}' height='{H}' role='img' aria-label='Karam Al Takrity'>")
    # staggered glow wave + blinking cursor, pure CSS keyframes
    s.append("<style>")
    s.append(f"rect.p{{fill:{dim};}}")
    s.append(f"@keyframes w{{0%,100%{{fill:{dim};}}45%{{fill:{lit};}}}}")
    s.append(f"@keyframes b{{0%,49%{{opacity:1;}}50%,100%{{opacity:0;}}}}")
    s.append("g.c rect.p{animation:w 2.8s ease-in-out infinite;}")
    for i in range(len(NAME)):
        s.append(f"g.c{i} rect.p{{animation-delay:{i*0.085:.3f}s;}}")
    s.append(f"rect.cur{{fill:{cursor};animation:b 1.1s steps(1) infinite;}}")
    s.append("</style>")
    for i, ch in enumerate(NAME):
        if ch == " ":
            continue
        ox = PADX + i*cw*CELL
        s.append(f"<g class='c c{i}'>")
        for r, row in enumerate(GLYPHS[ch]):
            for col, bit in enumerate(row):
                if bit == "#":
                    s.append(f"<rect class='p' x='{ox+col*CELL}' y='{PADY+r*CELL}' "
                             f"width='{CELL-1}' height='{CELL-1}'/>")
        s.append("</g>")
    cx = PADX + len(NAME)*cw*CELL
    s.append(f"<rect class='cur' x='{cx}' y='{PADY+GH*CELL-CELL+1}' "
             f"width='{CELL*4}' height='{CELL-1}'/>")
    s.append("</svg>")
    open(out, "w", encoding="utf-8").write("".join(s))
    print(f"{out}: {W}x{H}, {len(''.join(s))} bytes")

build("#3D8A52", "#9BF0A9", "#7CE38B", "nameplate-dark.svg")
build("#1A7F37", "#4AC26B", "#1A7F37", "nameplate.svg")
