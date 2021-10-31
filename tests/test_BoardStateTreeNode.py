import io
import sys
from unittest import TestCase

import chess
from pytest import raises

from agent.BoardStateTreeNode import BoardStateTreeNode
from agent.Scorer import Scorer


class TestBoardStateTreeNode(TestCase):
    def test_initial_state(self):
        # Arrange
        board = chess.Board()
        root_node = BoardStateTreeNode(board)
        # Assert
        assert root_node._board == board
        assert root_node._move is None
        assert root_node._children == []
        assert root_node._is_end_game is False
        assert root_node._turn_color is True
        assert root_node._max_children is None

    def test_populate_tree_negative_depth_returns(self):
        board = chess.Board()
        root_node = BoardStateTreeNode(board)

        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Act
        root_node.populate_tree(-1)
        sys.stdout = sys.__stdout__  # Reset redirect.

        # Assert
        assert captured_output.getvalue() == 'populate_tree: Reached depth base case.\n'

    def test_populate_tree_game_over_returns(self):
        # Arrange
        game_over_fen = '2Q2k2/1R6/7R/1P2P1P1/P6P/8/8/1NB1KBN1 b - - 4 37'
        board = chess.Board(game_over_fen)
        root_node = BoardStateTreeNode(board)

        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Act
        root_node.populate_tree(5)
        sys.stdout = sys.__stdout__  # Reset redirect.

        # Assert
        assert captured_output.getvalue() == 'populate_tree: No more moves to populate. Game is over at current node.\n'

    def test_populate_tree_two_children(self):
        # Arrange
        game_nearly_over_fen = '4k3/1R6/2Q4R/1P2P1P1/P6P/8/8/1NB1KBN1 b - - 2 36'
        board = chess.Board(game_nearly_over_fen)
        root_node = BoardStateTreeNode(board)

        # Act
        root_node.populate_tree(5)

        # Assert
        assert len(root_node._children) == 2

    # def test_enumerate_moves(self):
    #     self.fail()
    #
    # def test__gather_leaf_scores(self):
    #     self.fail()
