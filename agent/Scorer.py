from enum import Enum

import chess

from agent.scorer_weights import white_pawn_weights, white_knight_weights, white_bishop_weights, white_rook_weights, \
    white_queen_weights, white_king_weights_middle_game, white_king_weights_end_game, black_pawn_weights, \
    black_knight_weights, black_bishop_weights, black_rook_weights, black_queen_weights, black_king_weights_middle_game, \
    black_king_weights_end_game


class PieceType(Enum):
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6


class Scorer:
    def evaluate(self, board: chess.Board) -> float:
        """
        Uses the simplified evaluation function.
        https://www.chessprogramming.org/Simplified_Evaluation_Function
        A positive value indicates the white player is in a stronger position, while
        a negative value indicates the black player is in a stronger position. The
        magnitude scores indicate the amount of advantage.
        """
        end_game: bool = self._is_end_game(board)

        white_score = 0

        for square_index in chess.scan_reversed(board.occupied_co[chess.WHITE]):
            if (piece_type := board.piece_type_at(square_index)) is None:
                continue
            white_score += self._get_weight(square_index, piece_type, end_game, True)

        for square_index in chess.scan_reversed(board.occupied_co[chess.BLACK]):
            if (piece_type := board.piece_type_at(square_index)) is None:
                continue
            white_score -= self._get_weight(square_index, piece_type, end_game, False)

        return white_score

    def _is_end_game(self, board: chess.Board):
        """ Is end game if:
                a. Both sides have no queens OR
                b. every side which has a queen has additionally no other pieces or one minorpiece maximum
        """
        fen = board.fen()

        num_white_queens = fen.count('Q')
        num_black_queens = fen.count('q')

        if num_white_queens == 0 and num_black_queens == 0:
            return True

        if num_white_queens == 1:
            num_white_rooks_pieces = fen.count('R')
            num_white_minor_pieces = fen.count('B') + fen.count('N')
            num_white_pawns_pieces = fen.count('P')
            if num_white_rooks_pieces > 0 or num_white_pawns_pieces > 0 or num_white_minor_pieces > 1:
                return False

        if num_black_queens == 1:
            num_black_rooks_pieces = fen.count('r')
            num_black_minor_pieces = fen.count('b') + fen.count('n')
            num_black_pawns_pieces = fen.count('p')
            if num_black_rooks_pieces > 0 or num_black_pawns_pieces > 0 or num_black_minor_pieces > 1:
                return False

        return True

    def _get_weight(self, sq: int, piece_type: PieceType, end_game: bool, white: bool):
        if piece_type == PieceType.PAWN.value:
            return white_pawn_weights[sq] if white else black_pawn_weights[sq]
        elif piece_type == PieceType.KNIGHT.value:
            return white_knight_weights[sq] if white else black_knight_weights[sq]
        elif piece_type == PieceType.BISHOP.value:
            return white_bishop_weights[sq] if white else black_bishop_weights[sq]
        elif piece_type == PieceType.ROOK.value:
            return white_rook_weights[sq] if white else black_rook_weights[sq]
        elif piece_type == PieceType.QUEEN.value:
            return white_queen_weights[sq] if white else black_queen_weights[sq]
        elif piece_type == PieceType.KING.value:
            if end_game:
                return white_king_weights_end_game[sq] if white else black_king_weights_end_game[sq]
            else:
                return white_king_weights_middle_game[sq] if white else black_king_weights_middle_game[sq]
        else:
            raise Exception(f'WTF: {piece_type}')
