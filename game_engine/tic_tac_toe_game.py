from copy import deepcopy
from .tic_tac_toe_common_lib import *


class TicTacToeGame(AbstractTicTacToeGame):
    def __init__(self, game_id: str, first_player_id: str, second_player_id: str,
                 strategy: Callable[[TicTacToeGameInfo], TicTacToeTurn] = None) -> None:
        self.game_id = game_id
        self.now_player_id = first_player_id
        self.first_player_id = first_player_id
        self.second_player_id = second_player_id
        self.strategy = strategy
        self.game_info = TicTacToeGameInfo(game_id, [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], list(),
                                           first_player_id, second_player_id, '')

    def who_is_win(self) -> str:
        if self.game_info.field[0][0] == self.game_info.field[0][1] == self.game_info.field[0][2] != ' ':
            if self.game_info.field[0][0] == 'X':
                return self.first_player_id
            else:
                return self.second_player_id
        if self.game_info.field[1][0] == self.game_info.field[1][1] == self.game_info.field[1][2] != ' ':
            if self.game_info.field[1][0] == 'X':
                return self.first_player_id
            else:
                return self.second_player_id
        if self.game_info.field[2][0] == self.game_info.field[2][1] == self.game_info.field[2][2] != ' ':
            if self.game_info.field[2][0] == 'X':
                return self.first_player_id
            else:
                return self.second_player_id
        if self.game_info.field[0][0] == self.game_info.field[1][0] == self.game_info.field[2][0] != ' ':
            if self.game_info.field[0][0] == 'X':
                return self.first_player_id
            else:
                return self.second_player_id
        if self.game_info.field[0][1] == self.game_info.field[1][1] == self.game_info.field[2][1] != ' ':
            if self.game_info.field[0][1] == 'X':
                return self.first_player_id
            else:
                return self.second_player_id
        if self.game_info.field[0][2] == self.game_info.field[1][2] == self.game_info.field[2][2] != ' ':
            if self.game_info.field[0][2] == 'X':
                return self.first_player_id
            else:
                return self.second_player_id
        if self.game_info.field[0][0] == self.game_info.field[1][1] == self.game_info.field[2][2] != ' ':
            if self.game_info.field[0][0] == 'X':
                return self.first_player_id
            else:
                return self.second_player_id
        if self.game_info.field[0][2] == self.game_info.field[1][1] == self.game_info.field[2][0] != ' ':
            if self.game_info.field[0][2] == 'X':
                return self.first_player_id
            else:
                return self.second_player_id
        c = 0
        for i in range(3):
            bx = 0
            bo = 0
            for j in range(3):
                if self.game_info.field[i][j] == 'X':
                    bx = 1
                if self.game_info.field[i][j] == 'O':
                    bo = 1
            if (bx == 0) or (bo == 0):
                c = 1
        for j in range(3):
            bx = 0
            bo = 0
            for i in range(3):
                if self.game_info.field[i][j] == 'X':
                    bx = 1
                if self.game_info.field[i][j] == 'O':
                    bo = 1
            if (bx == 0) or (bo == 0):
                c = 1
        bx = 0
        bo = 0
        for i in range(3):
            if self.game_info.field[i][i] == 'X':
                bx = 1
            if self.game_info.field[i][i] == 'O':
                bo = 1
        if (bx == 0) or (bo == 0):
            c = 1
        bx = 0
        bo = 0
        for i in range(3):
            if self.game_info.field[i][2-i] == 'X':
                bx = 1
            if self.game_info.field[i][2-i] == 'O':
                bo = 1
        if (bx == 0) or (bo == 0):
            c = 1
        if c == 0:
            return "Draw"
        else:
            return ''

    def is_turn_correct(self, turn: TicTacToeTurn) -> bool:
        if self.game_info.winner_id == '':
            if (turn.x_coordinate >= 0) and (turn.y_coordinate >= 0) and (turn.x_coordinate < 3) and (
                    turn.y_coordinate < 3):
                if self.now_player_id == turn.player_id:
                    if self.game_info.field[turn.x_coordinate][turn.y_coordinate] == ' ':
                        return True
        return False

    def get_game_info(self) -> TicTacToeGameInfo:
        info = TicTacToeGameInfo(self.game_id, [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], list(), self.first_player_id, self.second_player_id, self.who_is_win())
        for i in range(3):
            for j in range(3):
                info.field[i][j] = self.game_info.field[i][j]
        for k in self.game_info.sequence_of_turns:
            info.sequence_of_turns.append(k)
        return info

    def do_turn(self, turn: TicTacToeTurn) -> TicTacToeGameInfo:
        if self.is_turn_correct(turn):
            self.game_info.sequence_of_turns.append(deepcopy(turn))
            if turn.player_id == self.first_player_id:
                self.game_info.field[turn.x_coordinate][turn.y_coordinate] = 'X'
            if turn.player_id == self.second_player_id:
                self.game_info.field[turn.x_coordinate][turn.y_coordinate] = 'O'
            self.game_info.winner_id = self.who_is_win()
            if self.now_player_id == self.first_player_id:
                self.now_player_id = self.second_player_id
            else:
                self.now_player_id = self.first_player_id
        return self.game_info


def test1():
    game = TicTacToeGame(
        game_id="0001",
        first_player_id="Petya",
        second_player_id="Vasya"
    )
    assert game.get_game_info() == TicTacToeGameInfo(
        game_id="0001",
        field=[
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ],
        sequence_of_turns=[],
        first_player_id="Petya",
        second_player_id="Vasya",
        winner_id=""
    )

    assert game.is_turn_correct(
        TicTacToeTurn(
            player_id="Petya",
            x_coordinate=0,
            y_coordinate=0
        )
    ) == True

    assert game.is_turn_correct(
        TicTacToeTurn(
            player_id="Petya",
            x_coordinate=-10,
            y_coordinate=-10
        )
    ) == False
    assert game.is_turn_correct(
        TicTacToeTurn(
            player_id="Vasya",
            x_coordinate=0,
            y_coordinate=0
        )
    ) == False

    game_info = game.get_game_info()
    game_info.field[0][0] = "@"
    assert game.get_game_info() == TicTacToeGameInfo(
        game_id="0001",
        field=[
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ],
        sequence_of_turns=[],
        first_player_id="Petya",
        second_player_id="Vasya",
        winner_id=""
    )

    assert game.do_turn(
        TicTacToeTurn(
            player_id="Petya",
            x_coordinate=0,
            y_coordinate=0
        )
    ) == TicTacToeGameInfo(
        game_id="0001",
        field=[
            ["X", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ],
        sequence_of_turns=[
            TicTacToeTurn(
                player_id="Petya",
                x_coordinate=0,
                y_coordinate=0
            )
        ],
        first_player_id="Petya",
        second_player_id="Vasya",
        winner_id=""
    )

    assert game.get_game_info() == TicTacToeGameInfo(
        game_id="0001",
        field=[
            ["X", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ],
        sequence_of_turns=[
            TicTacToeTurn(
                player_id="Petya",
                x_coordinate=0,
                y_coordinate=0
            )
        ],
        first_player_id="Petya",
        second_player_id="Vasya",
        winner_id=""
    )

    assert game.is_turn_correct(
        TicTacToeTurn(
            player_id="Vasya",
            x_coordinate=0,
            y_coordinate=0
        )
    ) == False

    assert game.is_turn_correct(
        TicTacToeTurn(
            player_id="Petya",
            x_coordinate=0,
            y_coordinate=0
        )
    ) == False

    game.do_turn(TicTacToeTurn("Petya", 1, 0))
    game.do_turn(TicTacToeTurn("Vasya", 1, 0))
    game.do_turn(TicTacToeTurn("Petya", 0, 1))
    game.do_turn(TicTacToeTurn("Vasya", 1, 1))
    game.do_turn(TicTacToeTurn("Petya", 0, 2))

    assert game.get_game_info() == TicTacToeGameInfo(
        game_id="0001",
        field=[
            ["X", "X", "X"],
            ["O", "O", " "],
            [" ", " ", " "]
        ],
        sequence_of_turns=[
            TicTacToeTurn("Petya", 0, 0),
            TicTacToeTurn("Vasya", 1, 0),
            TicTacToeTurn("Petya", 0, 1),
            TicTacToeTurn("Vasya", 1, 1),
            TicTacToeTurn("Petya", 0, 2)
        ],
        first_player_id="Petya",
        second_player_id="Vasya",
        winner_id="Petya"
    )
    assert game.is_turn_correct(
        TicTacToeTurn(
            player_id="Vasya",
            x_coordinate=1,
            y_coordinate=2
        )
    ) == False
