# API

### GET: /api/game_info?game_id=1
Что делать, если этот пользователь не играет в эту игру?

**response:**
```json
{
    "game_id": 1,
    "field": [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ],
    "sequence_of_turns": [],
    "first_player_id": "10",
    "second_player_id": "20",
    "winner_id": ""
}
```

### POST: /api/sign_up
**request:**
```json
{
  "user_name": "Vasya"
}
```

**response**
```json
{
  "user_name": "Vasya",
  "user_id": "af056ec7-4f62-4a38-b860-076d5b5d7ea4",
  "token": "9a5adaf4-9353-4d28-b1e7-f4c8753dea10"
}
```

### POST: /api/do_turn?game_id=1
**request:**
```json
{
  "user_name": "Vasya",
  "user_id" : "af056ec7-4f62-4a38-b860-076d5b5d7ea4",
  "token": "9a5adaf4-9353-4d28-b1e7-f4c8753dea10",
  "x": 0,
  "y": 0
}
```
если не авторизован то 401
**response**
```json
{
    "game_id": 1,
    "field": [
        ["X", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ],
    "sequence_of_turns": [
      {
        "user_id": "af056ec7-4f62-4a38-b860-076d5b5d7ea4",
        "x": 0,
        "y": 0
      }
    ],
    "first_player_id": "af056ec7-4f62-4a38-b860-076d5b5d7ea4",
    "second_player_id": "20",
    "winner_id": ""
}
```
### POST: /api/start_game
**request:**
```json
{
  "user_id" : "af056ec7-4f62-4a38-b860-076d5b5d7ea4",
  "token": "9a5adaf4-9353-4d28-b1e7-f4c8753dea10",
  "user_id2" : "20"
}
```
если не авторизован то 401
**response**
```json
{
    "game_id": 1,
    "field": [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ],
    "sequence_of_turns": [],
    "first_player_id": "af056ec7-4f62-4a38-b860-076d5b5d7ea4",
    "second_player_id": "20",
    "winner_id": ""
}
```
### POST: /api/my_games
**request:**
```json
{
  "user_id" : "20",
  "token": "145"
}
```
если не авторизован то 401
**response**
```json
{
    "games_id": [100, 1]
}
```
