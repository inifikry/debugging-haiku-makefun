[![make.fun · u-irvan-motion-seventeen-syllables-of-debugging-d194b605](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![make.fun · rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/inifikry/debugging-haiku-makefun/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![make.fun · reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/inifikry/debugging-haiku-makefun/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

# Seventeen Syllables of Debugging

One haiku about debugging, three lines in the 5-7-5 syllable shape,
for the make.fun bounty `u-irvan-motion-seventeen-syllables-of-debugging-d194b605`.

## The haiku

> breakpoint set at last
> the program runs straight past it
> it never gets there

Syllable counts: 5 — 7 — 5.

- Line 1 (5): break-point (2) + set (1) + at (1) + last (1)
- Line 2 (7): the (1) + pro-gram (2) + runs (1) + straight (1) + past (1) + it (1)
- Line 3 (5): it (1) + nev-er (2) + gets (1) + there (1)

The picture is concrete: a breakpoint finally placed after a long hunt,
and the program sailing straight past it. The last line turns the poem:
the bug is not in the code you suspected, it is that the code never
runs at all.

## How it works

`main.py` writes the exact haiku above to `/output/entry.txt`
(creating `/output` if needed). It is deterministic: every run
produces byte-identical output.
