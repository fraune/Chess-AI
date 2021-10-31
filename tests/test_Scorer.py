from unittest import TestCase

import chess

from agent.Scorer import Scorer


class TestScorer(TestCase):

    def test_scorer_starts_equal(self):
        # Arrange
        board = chess.Board()
        scorer = Scorer()
        expected_score = 0  # should start equal

        # Act
        actual_score = scorer.evaluate(board)

        # Assert
        assert expected_score == actual_score