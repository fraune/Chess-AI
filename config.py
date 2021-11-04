# utility.Logger
PRINT_TO_CONSOLE: bool = True
PRINT_TO_FILE: bool = True
LOG_FILE_NAME: str = None  # Only used if PRINT_TO_FILE is set. Overrides Logger's automatic file name generation.

# utility.SummaryWriter
SUMMARY_FILE_NAME: str = None  # Overrides SummaryWriter's automatic file name generation.

# utility.simulator
GAMES_TO_SIMULATE: int = 3
MAXIMUM_PLIES_PER_GAME: int = 1000  # Most "Random VS Random" games are completed in less than 300 total plies
