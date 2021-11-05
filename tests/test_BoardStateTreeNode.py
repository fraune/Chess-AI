import io
import sys

import chess

from app.agent.BoardStateTreeNode import BoardStateTreeNode


def test_initial_state(mocker):
    # Arrange
    mocker.patch('app.utility.Logger.PRINT_TO_CONSOLE', True)
    mocker.patch('app.utility.Logger.PRINT_TO_FILE', False)

    board = chess.Board()
    root_node = BoardStateTreeNode(board)
    # Assert
    assert root_node._board == board
    assert root_node._move is None
    assert root_node._children == []
    assert root_node._is_end_game is False
    assert root_node._turn_color is True
    assert root_node._max_children is None


def test_populate_tree_negative_depth_returns(mocker):
    # Arrange
    mocker.patch('app.utility.Logger.PRINT_TO_CONSOLE', True)
    mocker.patch('app.utility.Logger.PRINT_TO_FILE', False)

    board = chess.Board()
    root_node = BoardStateTreeNode(board)

    # Act
    result = root_node.populate_tree(-1)

    # Assert
    assert result is None


def test_populate_tree_game_over_returns(mocker):
    # Arrange
    mocker.patch('app.utility.Logger.PRINT_TO_CONSOLE', True)
    mocker.patch('app.utility.Logger.PRINT_TO_FILE', False)
    log_mock = mocker.patch('app.agent.BoardStateTreeNode.Logger.log')

    game_over_fen = '2Q2k2/1R6/7R/1P2P1P1/P6P/8/8/1NB1KBN1 b - - 4 37'
    board = chess.Board(game_over_fen)
    root_node = BoardStateTreeNode(board)

    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Act
    root_node.populate_tree(5)
    sys.stdout = sys.__stdout__  # Reset redirect.

    # Assert
    assert log_mock.call_args[0][0] == 'populate_tree: No more moves to populate. Game is over at current node.'
    # assert captured_output.getvalue()


def test_populate_tree_two_children(mocker):
    # Arrange
    mocker.patch('app.utility.Logger.PRINT_TO_CONSOLE', True)
    mocker.patch('app.utility.Logger.PRINT_TO_FILE', False)

    game_nearly_over_fen = '4k3/1R6/2Q4R/1P2P1P1/P6P/8/8/1NB1KBN1 b - - 2 36'
    board = chess.Board(game_nearly_over_fen)
    root_node = BoardStateTreeNode(board)

    # Act
    root_node.populate_tree(5)

    # Assert
    assert len(root_node._children) == 2
