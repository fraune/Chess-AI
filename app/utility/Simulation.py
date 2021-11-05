from app.agent.PlayerType import PlayerType
from app.config import MAXIMUM_TREE_WIDTH, MAXIMUM_TREE_DEPTH


class Simulation:
    def __init__(self, matches: int, white_player_type: PlayerType, black_player_type: PlayerType,
                 search_depth: int = MAXIMUM_TREE_DEPTH, search_width: int = MAXIMUM_TREE_WIDTH):
        self.matches = matches
        self.white_player_type = white_player_type
        self.black_player_type = black_player_type
        self.search_tree_depth = search_depth
        self.search_tree_width = search_width
