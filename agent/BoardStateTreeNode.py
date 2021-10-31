import random

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
        self._children = []
        self._is_end_game = board.is_game_over()
        self._turn_color = board.turn == chess.WHITE
        self._max_children = max_children

    def populate_tree(self, depth: int):
        if depth <= 0:
            print('populate_tree: Reached depth base case.')
            return

        if self._board.is_game_over():
            print('populate_tree: No more moves to populate. Game is over at current node.')
            return

        moves = []
        for move in self._board.legal_moves:
            if self._max_children is None:
                moves.append(move)

        # Reduce move set to num max children
        print(f'populate_tree: {len(moves)} legal moves found')
        if self._max_children is not None:
            while len(moves) > self._max_children:
                index_to_remove = random.randint(0, len(moves) - 1)
                moves.pop(index_to_remove)

        print(f'populate_tree: {len(moves)} moves to be added as children')
        for move in moves:
            child_board = self._board.copy()
            child_board.push(move)  # push move here?
            child = BoardStateTreeNode(child_board, move, self._max_children)
            child.populate_tree(depth - 1)
            self._children.append(child)

    def evaluate_moves(self, score_func: Scorer, agg_func) -> list[(float, chess.Move)]:
        # might be more efficient to evaluate moves when the tree is built
        # agg func is _gather_leaf_scores?
        my_options = []
        for child in self._children:
            my_options.append((self._gather_leaf_scores(child, score_func), child._move))
        return my_options

    def enumerate_moves(self) -> list[chess.Move]:
        return self._board.legal_moves

    def _gather_leaf_scores(self, node: 'BoardStateTreeNode', score_func: Scorer) -> float:
        my_score = score_func.evaluate(node)
        scores = [my_score]
        for child in node._children:
            scores.append(self._gather_leaf_scores(child, score_func))

        return sum(scores) / len(scores)
