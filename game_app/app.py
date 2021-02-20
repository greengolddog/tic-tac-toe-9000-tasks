from typing import Dict

from game_engine import TicTacToeGame, TicTacToeGameInfo, TicTacToeTurn

from uuid import uuid4

class TicTacToeApp:
    def __init__(self):
        """пока не знаю, мб что-то ещё тут будет :)
        в обоих случаях айдишник - ключ, значение - угадайте, что)"""
        self._games: Dict[str, TicTacToeGame] = {}

    def start_game(self, first_player_id: str, second_player_id: str) -> TicTacToeGameInfo:
        game_id = str(uuid4())
        self._games[game_id] = TicTacToeGame(\
        game_id, first_player_id, second_player_id)
        return self._games[game_id].get_game_info()

    def get_game_by_id(self, game_id: str) -> TicTacToeGameInfo:
        return self._games[game_id].get_game_info()

    def do_turn(self, turn: TicTacToeTurn, game_id: str) -> TicTacToeGameInfo:
        return self._games[game_id].do_turn(turn)
