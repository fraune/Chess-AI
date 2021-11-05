from datetime import datetime

from app.agent.ChessGame import ChessGame
from app.agent.Player import create_player_from_enum
from app.agent.PlayerType import PlayerType
from app.config import v1_GAMES_TO_SIMULATE, v1_MAXIMUM_PLIES_PER_GAME, BLACK_PLAYER_TYPE, WHITE_PLAYER_TYPE, \
    v2_SIMULATION_CONFIGURATIONS
from app.utility.LogLevel import LogLevel
from app.utility.Logger import Logger
from app.utility.Simulation import Simulation
from app.utility.SummaryWriter import SummaryWriter

logger = Logger()


def run_simulation_set_v2(configurations: list[Simulation] = v2_SIMULATION_CONFIGURATIONS):
    start_datetime = datetime.now()

    total_games = 0
    for configuration in configurations:
        total_games += configuration.matches

    now = start_datetime.strftime('%Y%m%d%H%M%S')
    file_name = f'{now}-{total_games}x-chess-summary.json'
    sw = SummaryWriter(file_name)

    current_game = 0
    for configuration_index in range(0, len(configurations)):
        configuration = configurations[configuration_index]
        logger.log(f'Starting configuration {configuration_index + 1}/{len(configurations)}', LogLevel.INFO)
        for simulation_number in range(1, configuration.matches + 1):
            current_game += 1
            logger.log(f'  Starting game {current_game}/{total_games}', LogLevel.INFO)
            summary = run_one_simulation_v2(simulation_number,
                                            configuration.white_player_type,
                                            configuration.black_player_type)
            dict_to_write = {'game': current_game, **summary}
            sw.write_summary(dict_to_write)

    end_datetime = datetime.now()
    time_delta = end_datetime - start_datetime
    avg_time = time_delta.total_seconds() / total_games
    logger.log(f'  Ran {total_games} games in {str(time_delta)} for an average of {avg_time:.6f} seconds per game.',
               LogLevel.INFO)

    logger.flush()
    logger.close()
    sw.flush()
    sw.close()


def run_one_simulation_v2(simulation_number, white_player_type: PlayerType, black_player_type: PlayerType) -> dict:
    logger.log(f'Simulation #{simulation_number} beginning')
    white_player = create_player_from_enum(white_player_type)
    black_player = create_player_from_enum(black_player_type)
    game = ChessGame(white_player, black_player)
    game.play_until(v1_MAXIMUM_PLIES_PER_GAME)
    logger.log(f'Simulation #{simulation_number} complete')
    return game.summary()


def run_simulation_set_v1():
    start_datetime = datetime.now()
    now = start_datetime.strftime('%Y%m%d%H%M%S')
    file_name = f'{now}-{v1_GAMES_TO_SIMULATE}x-chess-summary.json'
    sw = SummaryWriter(file_name)

    for simulation in range(1, v1_GAMES_TO_SIMULATE + 1):
        print(f'Starting game {simulation}/{v1_GAMES_TO_SIMULATE}')
        summary = run_one_simulation_v1(simulation)
        dict_to_write = {'simulation': simulation, **summary}
        sw.write_summary(dict_to_write)

    end_datetime = datetime.now()
    time_delta = end_datetime - start_datetime
    avg_time = time_delta.total_seconds() / v1_GAMES_TO_SIMULATE
    print(f'Ran {v1_GAMES_TO_SIMULATE} games in {str(time_delta)} for an average of {avg_time:.6f} seconds per game.')

    logger.flush()
    logger.close()
    sw.flush()
    sw.close()


def run_one_simulation_v1(simulation_number) -> dict:
    logger.log(f'Simulation #{simulation_number} beginning')
    white_player = create_player_from_enum(WHITE_PLAYER_TYPE)
    black_player = create_player_from_enum(BLACK_PLAYER_TYPE)
    game = ChessGame(white_player, black_player)
    game.play_until(v1_MAXIMUM_PLIES_PER_GAME)
    logger.log(f'Simulation #{simulation_number} complete')
    return game.summary()
