import chess

from agent import Scorer


class BoardStateTreeNode:
    _board: chess.Board
    _move: chess.Move
    _children: list['BoardStateTreeNode']
    _is_end_game: bool
    _turn_color: bool  # True if white, False if black
    _max_children: int  # Limit width of tree

    def __init__(self, board: chess.Board, move: chess.Move = None, max_children: int = None):
        self._board = board
        self._move = move
        self._max_children = max_children

    def populate_tree(self, depth: int):
        # TODO: write this
        print('pop tree')

    def enumerate_moves(self) -> list[chess.Move]:
        # TODO: write this
        print('enum moves')

    def evaluate_moves(self, score_func: Scorer, agg_func) -> list[(float, chess.Move)]:
        # what is agg func?
        # TODO: write this
        print('eval moves')
