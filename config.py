from agent.Player import PlayerType

# utility.Logger.Logger
PRINT_TO_CONSOLE: bool = True
PRINT_TO_FILE: bool = True
LOG_FILE_NAME: str = None  # Only used if PRINT_TO_FILE is set. Overrides Logger's automatic file name generation.

# utility.SummaryWriter.SummaryWriter
SUMMARY_FILE_NAME: str = None  # Overrides SummaryWriter's automatic file name generation

# utility.simulator
GAMES_TO_SIMULATE: int = 3
MAXIMUM_PLIES_PER_GAME: int = 1000  # Most "Random VS Random" games are completed in less than 300 total plies

# agent.ChessGame.ChessGame
WHITE_PLAYER_TYPE: PlayerType = PlayerType.RANDOM
BLACK_PLAYER_TYPE: PlayerType = PlayerType.RANDOM

# agent.Player.SearchPlayer
MAXIMUM_TREE_DEPTH: int = 3  # Factor to limit the number of plies to look ahead
MAXIMUM_TREE_WIDTH: int = 15  # Factor to limit the number of possible moves per ply
