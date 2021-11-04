# Chess AI

A Python 3.9 implementation of a lookahead algorithm for a computer to be "competetive" at chess.

## Library

python-chess 1.7.0

- https://python-chess.readthedocs.io/en/latest/index.html

## Scoring

Currently implemented with the dumb and quick **Simplified Evaluation Function**

- https://www.chessprogramming.org/Simplified_Evaluation_Function

Future update, change the algorithm to the smarter **PeSTO's Evaluation Function**

- https://www.chessprogramming.org/PeSTO%27s_Evaluation_Function

## Other

Unit testing aided by this board editor to generate arbitrary FENs

- https://lichess.org/editor

I found someone's Jupyter Notebook, which explains some basics of using the `python-chess` library. It also includes a
basic player implementation.

- https://jupyter.brynmawr.edu/services/public/dblank/CS371%20Cognitive%20Science/2016-Fall/Programming%20a%20Chess%20Player.ipynb

## TODO

- Catch errors at top level and log
- Log number of pieces left on board at end game