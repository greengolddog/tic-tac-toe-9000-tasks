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
        self._games[game_id] = TicTacToeGame(
            game_id, 
            first_player_id, 
            second_player_id
        )
        return self._games[game_id].get_game_info()

    def get_game_by_id(self, game_id: str) -> TicTacToeGameInfo:
        if (self._games.get(game_id, 0) == 0):
            return "None"
        return self._games[game_id].get_game_info()

    def all_games_of_user(self, user_id: str):
        games = []
        for i in self._games.keys():
            if (self.get_game_by_id(i).first_player_id == user_id) or (self.get_game_by_id(i).second_player_id == user_id):
                games.append(self.get_game_by_id(i).game_id)
        return games

    def do_turn(self, turn: TicTacToeTurn, game_id: str) -> TicTacToeGameInfo:
        return self._games[game_id].do_turn(turn)
