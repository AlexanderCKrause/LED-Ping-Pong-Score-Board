import requests

def increment_score(player, game):
    data = {}
    url = 'http://192.168.1.72:5000/increment_score/'+player
      
    response = requests.post(url, json=data)

    # Check the response
    if response.status_code == 200:
        print("POST request was successful.")
        print("Response:", response.json())
    else:
        print("POST request failed. Status code:", response.status_code)

def decrement_score(player, game):
    data = {}
    url = 'http://192.168.1.72:5000/decrement_score/'+player
      
    response = requests.post(url, json=data)

    # Check the response
    if response.status_code == 200:
        print("POST request was successful.")
        print("Response:", response.json())
    else:
        print("POST request failed. Status code:", response.status_code)

def reset_score(player, game):
    data = {}
    url = 'http://192.168.1.72:5000/reset_score/'+player
      
    response = requests.post(url, json=data)

    # Check the response
    if response.status_code == 200:
        print("GET request was successful.")
        return response.json()
    else:
        print("GET request failed. Status code:", response.status_code)

def get_score():
    data = {}
    url = 'http://192.168.1.72:5000/get_score'
      
    response = requests.get(url, json=data)

    # Check the response
    if response.status_code == 200:
        print("GET request was successful.")
        return response.json()
    else:
        print("GET request failed. Status code:", response.status_code)