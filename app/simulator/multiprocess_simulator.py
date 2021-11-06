import multiprocessing as mp
from datetime import datetime

from app.agent.ChessGame import ChessGame
from app.agent.Player import create_player_from_enum
from app.config import SIMULATION_CONFIGURATIONS, MAXIMUM_PLIES_PER_GAME
from app.simulator.Configuration import Configuration
from app.simulator.Simulation import Simulation
from app.utility.LogLevel import LogLevel
from app.utility.Logger import Logger
from app.utility.SummaryWriter import SummaryWriter


def process_data(data: Simulation, num_games):
    print(f'Game {data.id}/{num_games} running on process {mp.current_process().name}')
    summary = run_one_simulation_v3(data)
    dict_to_write = {'game': data.id, **summary}
    return dict_to_write


def run_one_simulation_v3(data: Simulation) -> dict:
    white_player = create_player_from_enum(data.white_player_type, data.search_tree_depth, data.search_tree_width)
    black_player = create_player_from_enum(data.black_player_type, data.search_tree_depth, data.search_tree_width)
    game = ChessGame(white_player, black_player)
    game.play_until(MAXIMUM_PLIES_PER_GAME)
    return game.summary()


def apply_async_with_callback():
    logger.log(f'Spinning up {mp.cpu_count()} processes', LogLevel.INFO)

    # results = []

    pool = mp.Pool()
    for job in jobs:
        # result = \
        pool.apply_async(process_data, args=(job, num_games), callback=sw.write_summary)
        # results.append(result)

    pool.close()
    pool.join()

    # return results


if __name__ == '__main__':
    start_datetime = datetime.now()

    logger = Logger()
    sw = SummaryWriter()
    experiment: list[Configuration] = SIMULATION_CONFIGURATIONS

    logger.log(f'Splitting games out of {len(experiment)} simulations', LogLevel.INFO)
    num_games = 0
    jobs = []
    for configuration in experiment:
        for match in range(0, configuration.matches):
            num_games += 1
            jobs.append(Simulation(num_games, configuration.white_player_type, configuration.black_player_type,
                                   configuration.search_tree_depth, configuration.search_tree_width))

    logger.log(f'Found {num_games} total games', LogLevel.INFO)

    now = start_datetime.strftime('%Y%m%d%H%M%S')
    file_name = f'{now}-{num_games}x-chess-summary.json'
    sw.initialize(file_name)

    # Majority of work done here
    # results = \
    apply_async_with_callback()

    # for result in results:
    #     sw.write_summary(result.get())

    end_datetime = datetime.now()
    time_delta = end_datetime - start_datetime
    avg_time = time_delta.total_seconds() / num_games
    logger.log(f'Ran {num_games} games in {str(time_delta)} for an average of {avg_time:.6f} seconds per game.',
               LogLevel.INFO)

    logger.flush()
    logger.close()
    sw.flush()
    sw.close()

    logger.log('Exiting Main Process', LogLevel.INFO)
