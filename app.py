from flask import Flask, request, abort

from game_app import TicTacToeApp

from game_engine import TicTacToeTurn

from uuid import uuid4

from dataclasses import dataclass
from dataclasses_json import dataclass_json

app = Flask(__name__)
t_app = TicTacToeApp()

@dataclass_json
@dataclass
class Person:
    name: str

@dataclass_json
@dataclass
class per:
    n1: str
    n2: str

tokens = dict()
tokens2 = dict()
names = dict()

@app.route("/")
def hello():
    return "Hello it is a tic tac toe game"

@app.route("/hello", methods=["GET"])
def hello2():
    name = request.args.get('name')
    if name:
        return "hello "+name
    abort(400)

@app.route("/game_info", methods=["GET"])
def get_game_info():
    game_id = request.args.get('game_id')
    if game_id:
        if (t_app.get_game_by_id(game_id) == "None"):
            abort(404)
        game = t_app.get_game_by_id(game_id)
        game.first_player_id = tokens2[game.first_player_id]
        game.second_player_id = tokens2[game.second_player_id]
        return t_app.get_game_by_id(game_id).to_dict()
    abort(400)

@app.route("/sign_up", methods=["POST"])
def sing_up():
    person = Person.from_dict(request.json).name
    token = str(uuid4())
    token2 = str(uuid4())
    tokens[token] = token2
    tokens2[token2] = token
    if names.get(person, 0) == 0:
        names[person] = [token]
    else:
        names[person].append(token)
    return {"token":token, "secret_token":token2}

@app.route("/get_persons", methods=["GET"])
def pers():
    name = request.args.get('name')
    if name:
        if (names.get(name, 555) == 555):
            return "There is no users with this name"
        return {"names":names[name]}
    abort(400)

@app.route("/do_turn", methods=["POST"])
def do_turn():
    game_id = request.args.get('game_id')
    if game_id:
        turn = TicTacToeTurn.from_dict(request.json)
        turn.x_coordinate = int(turn.x_coordinate)
        turn.y_coordinate = int(turn.y_coordinate)
        if (t_app.get_game_by_id(game_id) == "None"):
            abort(404)
        game = t_app.do_turn(turn, game_id)
        game.first_player_id = tokens2[game.first_player_id]
        game.second_player_id = tokens2[game.second_player_id]
        return game.to_dict()
    abort(400)

@app.route("/my_games", methods=["GET"])
def my_games():
    token = request.args.get('token')
    if token:
        if (tokens.get(token, 0) == 0):
            abort(404)
        return {"games":t_app.all_games_of_user(tokens[token])}
    abort(400)

@app.route("/start_game", methods=["POST"])
def start():
    players = per.from_dict(request.json)
    if (tokens.get(players.n1, 0) == 0):
        abort(404)
    if (tokens.get(players.n2, 0) == 0):
        abort(404)
    game = t_app.start_game(tokens[players.n1], tokens[players.n2])
    game.first_player_id = players.n1
    game.second_player_id = players.n2
    return game.to_dict()

@app.route("/my_public_key", methods=["GET"])
def my_public():
    token = request.args.get('token')
    if token:
        if (tokens2.get(token, 0) == 0):
            abort(404)
        return tokens2[token]
    abort(400)
