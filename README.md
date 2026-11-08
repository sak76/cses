# CSES in Python

Solutions to problems from the [CSES Problem Set](https://cses.fi/problemset/), written in Python.

## Layout

- One folder per topic, for example `graph/`.
- Solution files are named `<number>. <Problem Name>_<approach>.py`, for example `graph/1. Counting Rooms_bfs.py`.
- Test inputs live in `<topic>/test/<number>_<problem_name>/`.

## Running

Requires Python 3.9 or newer. Each solution reads from standard input:

```
python3 "graph/1. Counting Rooms_bfs.py" < graph/test/1_counting_rooms/1_counting_rooms_sample1.txt
```
