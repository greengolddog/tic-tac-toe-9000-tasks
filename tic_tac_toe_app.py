from tic_tac_toe_app_abstract import AbstractTicTacToeApp
from typing import Dict
from tic_tac_toe_game import TicTacToeGame
from tic_tac_toe_common_lib import TicTacToeGameInfo, UserInfo, TicTacToeTurn

class TicTacToeApp(AbstractTicTacToeApp):
    def __init__(self):
        self._games: Dict[str, TicTacToeGame] = {}
        self._passwords: Dict[str, str] = {}
    
    def start_game(self, player_id: str) -> TicTacToeGameInfo:
        pass
        """создаём игру, кладём в словарик (или другую вашу любимую коллекцию) с играми"""

    def get_game_by_id(self, game_id: str, user_id: str) -> TicTacToeGameInfo:
        pass
        """получаем игру, отдавать нужно только если юзер с таким user_id реально в неё играет,
        но проверку секретного ключа пользователя нужно делать в обработчиках запросов,
        а не здесь, но здесь мы реализуем методы, которые в этом помогут"""
    
    def do_turn(self, turn: TicTacToeTurn, game_id: str) -> TicTacToeGameInfo:
        pass

    def add_user(self) -> UserInfo:
        pass
        """регистрация"""
    
    def is_autentified(self, user: UserInfo) -> bool:
        pass
        """проверка авторизации"""