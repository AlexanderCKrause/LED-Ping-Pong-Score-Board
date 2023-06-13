from flask import Flask, jsonify
from game import PingPongGame


app = Flask(__name__)
game = PingPongGame()

@app.route('/reset_score/<player>', methods=['POST'])
def reset_score(player):
    game.reset_score(player)
    return jsonify(success=True)

@app.route('/increment_score/<player>', methods=['POST'])
def increment_score(player):
    game.increment_score(player)
    game.get_server()
    return jsonify(success=True)

@app.route('/decrement_score/<player>', methods=['POST'])
def decrement_score(player):
    game.decrement_score(player)
    game.get_server()
    return jsonify(success=True)

@app.route('/start_game/', methods=['POST'])
def start_game():
    game.start_game()
    return jsonify(success=True)

@app.route('/end_game/', methods=['POST'])
def end_game():
    game.end_game()
    return jsonify(success=True)

@app.route('/get_game_info', methods=['GET'])
def get_game_info():
    return jsonify(game.to_dict())


if __name__ == '__main__':
    app.run(host='192.168.1.72', port=5000)
