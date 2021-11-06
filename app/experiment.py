from app.agent.PlayerType import PlayerType
from app.simulator.Configuration import Configuration

experiment_tiny = [
    Configuration(4, PlayerType.RANDOM, PlayerType.RANDOM),
    Configuration(4, PlayerType.SEARCH, PlayerType.RANDOM, 1, 1),
    Configuration(4, PlayerType.SEARCH, PlayerType.RANDOM, 1, 2),
    Configuration(4, PlayerType.SEARCH, PlayerType.RANDOM, 1, 3),
    Configuration(4, PlayerType.SEARCH, PlayerType.RANDOM, 1, 4),
    Configuration(4, PlayerType.SEARCH, PlayerType.RANDOM, 1, 5),
]

experiment_small = [
    Configuration(100, PlayerType.RANDOM, PlayerType.RANDOM),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 1, 1),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 1, 2),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 1, 3),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 1, 4),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 1, 5),
]

experiment_large = [
    Configuration(100, PlayerType.RANDOM, PlayerType.RANDOM),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 1, 1),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 1, 2),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 1, 3),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 1, 4),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 1, 5),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 1, 6),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 1, 7),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 1, 8),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 1, 9),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 1, 10),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 1, 11),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 1, 12),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 1, 13),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 1, 14),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 1, 15),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 1, 16),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 1, 17),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 1, 18),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 1, 19),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 1, 20),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 2, 1),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 2, 2),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 2, 3),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 2, 4),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 2, 5),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 2, 6),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 2, 7),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 2, 8),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 2, 9),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 2, 10),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 2, 11),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 2, 12),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 2, 13),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 2, 14),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 2, 15),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 2, 16),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 2, 17),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 2, 18),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 2, 19),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 2, 20),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 3, 1),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 3, 2),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 3, 3),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 3, 4),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 3, 5),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 3, 6),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 3, 7),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 3, 8),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 3, 9),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 3, 10),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 3, 11),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 3, 12),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 3, 13),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 3, 14),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 3, 15),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 3, 16),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 3, 17),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 3, 18),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 3, 19),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 3, 20),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 4, 1),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 4, 2),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 4, 3),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 4, 4),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 4, 5),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 4, 6),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 4, 7),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 4, 8),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 4, 9),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 4, 10),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 4, 11),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 4, 12),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 4, 13),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 4, 14),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 4, 15),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 4, 16),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 4, 17),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 4, 18),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 4, 19),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 4, 20),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 5, 1),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 5, 2),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 5, 3),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 5, 4),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 5, 5),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 5, 6),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 5, 7),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 5, 8),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 5, 9),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 5, 10),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 5, 11),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 5, 12),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 5, 13),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 5, 14),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 5, 15),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 5, 16),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 5, 17),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 5, 18),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 5, 19),
    Configuration(100, PlayerType.SEARCH, PlayerType.RANDOM, 5, 20),
]
