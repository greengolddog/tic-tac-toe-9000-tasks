from copy import deepcopy
from typing import Callable, List
from .tic_tac_toe_common_lib import AbstractTicTacToeGame, TicTacToeGameInfo, TicTacToeTurn


class TicTacToeGame(AbstractTicTacToeGame):
    def __init__(self, game_id: str, first_player_id: str, second_player_id: str,
                 strategy: Callable[[TicTacToeGameInfo], TicTacToeTurn] = None) -> None:
        self.game_id = game_id
        self.now_player_id = first_player_id
        self.first_player_id = first_player_id
        self.second_player_id = second_player_id
        self.strategy = strategy
        self.winner_id = ''
        self.field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.sequence_of_turns: List[TicTacToeTurn] = list()

    def winner(self) -> str:
        counter = 0
        for i in range(3):
            bee_x = 0
            bee_o = 0
            bee_r = 1
            first_in_row = self.field[i][0]
            for j in range(3):
                if self.field[i][j] != first_in_row:
                    bee_r = 0
                if self.field[i][j] == 'X':
                    bee_x = 1
                if self.field[i][j] == 'O':
                    bee_o = 1
            if bee_r == 1:
                if first_in_row == 'X':
                    return self.first_player_id
                if first_in_row == 'O':
                    return self.second_player_id
            if (bee_x == 0) or (bee_o == 0):
                counter = 1
        for j in range(3):
            bee_x = 0
            bee_o = 0
            bee_r = 1
            first_in_row = self.field[0][j]
            for i in range(3):
                if self.field[i][j] != first_in_row:
                    bee_r = 0
                if self.field[i][j] == 'X':
                    bee_x = 1
                if self.field[i][j] == 'O':
                    bee_o = 1
            if bee_r == 1:
                if first_in_row == 'X':
                    return self.first_player_id
                if first_in_row == 'O':
                    return self.second_player_id
            if (bee_x == 0) or (bee_o == 0):
                counter = 1
        bee_x = 0
        bee_o = 0
        bee_r = 1
        first_in_row = self.field[1][1]
        for i in range(3):
            if self.field[i][i] != first_in_row:
                bee_r = 0
            if self.field[i][i] == 'X':
                bee_x = 1
            if self.field[i][i] == 'O':
                bee_o = 1
        if bee_r == 1:
            if first_in_row == 'X':
                return self.first_player_id
            if first_in_row == 'O':
                return self.second_player_id
        if (bee_x == 0) or (bee_o == 0):
            counter = 1
        bee_x = 0
        bee_o = 0
        bee_r = 1
        first_in_row = self.field[1][1]
        for i in range(3):
            if self.field[i][2-i] != first_in_row:
                bee_r = 0
            if self.field[i][2-i] == 'X':
                bee_x = 1
            if self.field[i][2-i] == 'O':
                bee_o = 1
        if bee_r == 1:
            if first_in_row == 'X':
                return self.first_player_id
            if first_in_row == 'O':
                return self.second_player_id
        if (bee_x == 0) or (bee_o == 0):
            counter = 1
        if counter == 0:
            return "Draw"
        return ''

    def is_turn_correct(self, turn: TicTacToeTurn) -> bool:
        if self.winner_id == '':
            if (turn.x_coordinate >= 0)\
            and (turn.y_coordinate >= 0)\
            and (turn.x_coordinate < 3)\
            and (turn.y_coordinate < 3):
                if self.now_player_id == turn.player_id:
                    if self.field[turn.x_coordinate][turn.y_coordinate] == ' ':
                        return True
        return False

    def get_game_info(self) -> TicTacToeGameInfo:
        info = TicTacToeGameInfo(self.game_id, deepcopy(self.field), \
        deepcopy(self.sequence_of_turns), self.first_player_id,\
        self.second_player_id, self.winner_id)
        return info

    def do_turn(self, turn: TicTacToeTurn) -> TicTacToeGameInfo:
        if self.is_turn_correct(turn):
            self.sequence_of_turns.append(deepcopy(turn))
            if turn.player_id == self.first_player_id:
                self.field[turn.x_coordinate][turn.y_coordinate] = 'X'
            if turn.player_id == self.second_player_id:
                self.field[turn.x_coordinate][turn.y_coordinate] = 'O'
            self.winner_id = self.winner()
            if self.now_player_id == self.first_player_id:
                self.now_player_id = self.second_player_id
            else:
                self.now_player_id = self.first_player_id
        return self.get_game_info()
