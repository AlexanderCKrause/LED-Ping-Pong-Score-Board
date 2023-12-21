import requests
from game import PingPongGame

def increment_score(player):
    data = {}
    url = 'http://192.168.1.28:5000/increment_score/'+player
      
    response = requests.post(url, json=data)

    if response.status_code == 200:
        print("POST request was successful.")
        print("Response:", response.json())
    else:
        print("POST request failed. Status code:", response.status_code)

def decrement_score(player):
    data = {}
    url = 'http://192.168.1.28:5000/decrement_score/'+player
      
    response = requests.post(url, json=data)

    if response.status_code == 200:
        print("POST request was successful.")
        print("Response:", response.json())
    else:
        print("POST request failed. Status code:", response.status_code)

def end_game():
    data = {}
    url = 'http://192.168.1.28:5000/end_game/'
      
    response = requests.post(url, json=data)

    if response.status_code == 200:
        print("POST request was successful.")
        print("Response:", response.json())
    else:
        print("POST request failed. Status code:", response.status_code)

def start_game(game_type = 'doubles'):
    data = {}
    url = 'http://192.168.1.28:5000/start_game/' + game_type
      
    response = requests.post(url, json=data)

    if response.status_code == 200:
        print("POST request was successful.")
        print("Response:", response.json())
    else:
        print("POST request failed. Status code:", response.status_code)

def reset_score(player):
    data = {}
    url = 'http://192.168.1.28:5000/reset_score/'+player
      
    response = requests.post(url, json=data)

    if response.status_code == 200:
        print("GET request was successful.")
        return response.json()
    else:
        print("GET request failed. Status code:", response.status_code)

def get_game_info():
    data = {}
    url = 'http://192.168.1.28:5000/get_game_info'
      
    response = requests.get(url, json=data)

    if response.status_code == 200:
        print("GET request was successful.")
        game_data = response.json()
        print("Game data:", game_data)
        game = PingPongGame.from_dict(game_data)
        return game

    else:
        print("GET request failed. Status code:", response.status_code)