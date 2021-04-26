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
        return t_app.get_game_by_id(game_id)
    abort(400)

@app.route("/sing_up", methods=["POST"])
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
    return ["your token: "+token, "you secret token: "+token2]

@app.route("/get_persons", methods=["GET"])
def per():
    name = request.args.get('name')
    if name:
        if (names.get(name, 555) == 555):
            return "There is no users with this name"
        return names[name]
    abort(400)

@app.route("/do_turn", methods=["POST"])
def do_turn():
    game_id = request.args.get('game_id')
    if game_id:
        turn = TicTacToeTurn.from_dict(request.json)
        if (t_app.get_game_by_id(game_id) == "None"):
            abort(404)
        game = t_app.do_turn(turn, game_id)
        game.first_player_id = tokens2[game.first_player_id]
        game.second_player_id = tokens2[game.second_player_id]
        return game
    abort(400)

@app.route("/my_games", methods=["GET"])
def my_games():
    token = request.args.get('token')
    if token:
        if (tokens.get(token, 0) == 0):
            abort(404)
        return t_app.all_games_of_user(tokens[token])
    abort(400)
@app.route("/start_game", methods=["POST"])
def start():
    players = per.from_dict(request.json)
    if (tokens.get(player.n1, 0) == 0):
        abort(404)
    if (tokens.get(player.n2, 0) == 0):
        abort(404)
    game = t_app.start_game(token[player.n1], token[player.n2])
    game.first_player_id = player.n1
    game.second_player_id = player.n2
    return game
