from flask import Flask, jsonify
import threading
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
    return jsonify(success=True)

@app.route('/decrement_score/<player>', methods=['POST'])
def decrement_score(player):
    game.decrement_score(player)
    return jsonify(success=True)

@app.route('/get_score', methods=['GET'])
def get_score():
    return jsonify(
        player1Score=game.player1Score,
        player2Score=game.player2Score,
        serving=game.get_server()
    )

if __name__ == '__main__':
    app.run(host='192.168.1.72', port=5000)
