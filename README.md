# bookbot
extremely simple toy script that parses a text file passed as an argument, and returns
a word count and letter count, sorted by most common letters. followed alongside
corresponding course from [boot.dev](https://boot.dev)

example usage (book not included but available [here](https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt)):
```
$ python3 main.py books/frankenstein.txt

```
output:

```
--- Report of books/frankenstein.txt ---
77986 words

Letter: e, Occurred 46043 times
Letter: t, Occurred 30365 times
Letter: a, Occurred 26743 times
Letter: o, Occurred 25225 times
Letter: i, Occurred 24613 times
Letter: n, Occurred 24367 times
Letter: s, Occurred 21155 times
Letter: r, Occurred 20818 times
Letter: h, Occurred 19725 times
Letter: d, Occurred 16863 times
Letter: l, Occurred 12739 times
Letter: m, Occurred 10604 times
Letter: u, Occurred 10407 times
Letter: c, Occurred 9243 times
Letter: f, Occurred 8731 times
Letter: y, Occurred 7914 times
Letter: w, Occurred 7638 times
Letter: p, Occurred 6121 times
Letter: g, Occurred 5974 times
Letter: b, Occurred 5026 times
Letter: v, Occurred 3833 times
Letter: k, Occurred 1755 times
Letter: x, Occurred 677 times
Letter: j, Occurred 504 times
Letter: q, Occurred 324 times
Letter: z, Occurred 243 times

```
