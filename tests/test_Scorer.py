from unittest import TestCase

import chess

from agent.Scorer import Scorer


class TestScorer(TestCase):

    def test_is_end_game_no_queens(self):
        # Arrange
        fen = '8/8/8/8/8/8/8/8 w - - 0 1'
        board = chess.Board(fen)
        scorer = Scorer()
        expected_is_end_game = True

        # Act
        actual_is_end_game = scorer._is_end_game(board)

        # Assert
        assert expected_is_end_game == actual_is_end_game

    def test_is_end_game_two_queen_and_minorpiece(self):
        # Arrange
        fen = '3q4/4n3/8/8/8/8/4N3/3Q4 w - - 0 1'
        board = chess.Board(fen)
        scorer = Scorer()
        expected_is_end_game = True

        # Act
        actual_is_end_game = scorer._is_end_game(board)

        # Assert
        assert expected_is_end_game == actual_is_end_game

    def test_is_end_game_two_queen_white_minorpiece_black_pawn(self):
        # Arrange
        fen = '3q4/4p3/8/8/8/8/4N3/3Q4 w - - 0 1'
        board = chess.Board(fen)
        scorer = Scorer()
        expected_is_end_game = False

        # Act
        actual_is_end_game = scorer._is_end_game(board)

        # Assert
        assert expected_is_end_game == actual_is_end_game

    def test_scorer_starts_equal(self):
        # Arrange
        board = chess.Board()
        scorer = Scorer()
        expected_score = 0  # should start equal

        # Act
        actual_score = scorer.evaluate(board)

        # Assert
        assert expected_score == actual_score

    def test_fen_white_pawns_diagonal(self):
        # Arrange
        fen = '7P/6P1/5P2/4P3/3P4/2P5/1P6/P7 w - - 0 1'
        board = chess.Board(fen)
        scorer = Scorer()
        expected_score = 115

        # Act
        actual_score = scorer.evaluate(board)

        # Assert
        assert expected_score == actual_score

    def test_fen_black_pawns_diagonal(self):
        # Arrange
        fen = '7p/6p1/5p2/4p3/3p4/2p5/1p6/p7 w - - 0 1'
        board = chess.Board(fen)
        scorer = Scorer()
        expected_score = -115

        # Act
        actual_score = scorer.evaluate(board)

        # Assert
        assert expected_score == actual_score

    def test_fen_white_knights_diagonal(self):
        # Arrange
        fen = '7N/6N1/5N2/4N3/3N4/2N5/1N6/N7 w - - 0 1'
        board = chess.Board(fen)
        scorer = Scorer()
        expected_score = -80

        # Act
        actual_score = scorer.evaluate(board)

        # Assert
        assert expected_score == actual_score

    def test_fen_black_knights_diagonal(self):
        # Arrange
        fen = '7n/6n1/5n2/4n3/3n4/2n5/1n6/n7 w - - 0 1'
        board = chess.Board(fen)
        scorer = Scorer()
        expected_score = 80

        # Act
        actual_score = scorer.evaluate(board)

        # Assert
        assert expected_score == actual_score

    def test_fen_white_bishops_diagonal(self):
        # Arrange
        fen = '7B/6B1/5B2/4B3/3B4/2B5/1B6/B7 w - - 0 1'
        board = chess.Board(fen)
        scorer = Scorer()
        expected_score = 0

        # Act
        actual_score = scorer.evaluate(board)

        # Assert
        assert expected_score == actual_score

    def test_fen_black_bishops_diagonal(self):
        # Arrange
        fen = '7b/6b1/5b2/4b3/3b4/2b5/1b6/b7 w - - 0 1'
        board = chess.Board(fen)
        scorer = Scorer()
        expected_score = 0

        # Act
        actual_score = scorer.evaluate(board)

        # Assert
        assert expected_score == actual_score

    def test_fen_white_rooks_diagonal(self):
        # Arrange
        fen = '7R/6R1/5R2/4R3/3R4/2R5/1R6/R7 w - - 0 1'
        board = chess.Board(fen)
        scorer = Scorer()
        expected_score = 10

        # Act
        actual_score = scorer.evaluate(board)

        # Assert
        assert expected_score == actual_score

    def test_fen_black_rooks_diagonal(self):
        # Arrange
        fen = '7r/6r1/5r2/4r3/3r4/2r5/1r6/r7 w - - 0 1'
        board = chess.Board(fen)
        scorer = Scorer()
        expected_score = -10

        # Act
        actual_score = scorer.evaluate(board)

        # Assert
        assert expected_score == actual_score

    def test_fen_white_queens_diagonal(self):
        # Arrange
        fen = '7Q/6Q1/5Q2/4Q3/3Q4/2Q5/1Q6/Q7 w - - 0 1'
        board = chess.Board(fen)
        scorer = Scorer()
        expected_score = -20

        # Act
        actual_score = scorer.evaluate(board)

        # Assert
        assert expected_score == actual_score

    def test_fen_black_queens_diagonal(self):
        # Arrange
        fen = '7q/6q1/5q2/4q3/3q4/2q5/1q6/q7 w - - 0 1'
        board = chess.Board(fen)
        scorer = Scorer()
        expected_score = 20

        # Act
        actual_score = scorer.evaluate(board)

        # Assert
        assert expected_score == actual_score

    def test_fen_white_kings_diagonal_mid_game(self):
        # Arrange
        fen = 'P6K/6K1/5K2/4K3/3K4/2K5/1K6/K6Q w - - 0 1'
        board = chess.Board(fen)
        scorer = Scorer()
        expected_score = -200

        # Act
        actual_score = scorer.evaluate(board)

        # Assert
        assert expected_score == actual_score

    def test_fen_black_kings_diagonal_mid_game(self):
        # Arrange
        fen = 'p6k/6k1/5k2/4k3/3k4/2k5/1k6/k6q w - - 0 1'
        board = chess.Board(fen)
        scorer = Scorer()
        expected_score = 200

        # Act
        actual_score = scorer.evaluate(board)

        # Assert
        assert expected_score == actual_score

    def test_fen_white_kings_diagonal_end_game(self):
        # Arrange
        fen = '7K/6K1/5K2/4K3/3K4/2K5/1K6/K7 w - - 0 1'
        board = chess.Board(fen)
        scorer = Scorer()
        expected_score = -30

        # Act
        actual_score = scorer.evaluate(board)

        # Assert
        assert expected_score == actual_score

    def test_fen_black_kings_diagonal_end_game(self):
        # Arrange
        fen = '7k/6k1/5k2/4k3/3k4/2k5/1k6/k7 w - - 0 1'
        board = chess.Board(fen)
        scorer = Scorer()
        expected_score = 30

        # Act
        actual_score = scorer.evaluate(board)

        # Assert
        assert expected_score == actual_score
