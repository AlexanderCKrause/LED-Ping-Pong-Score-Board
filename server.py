from flask import Flask, jsonify
from flask_socketio import SocketIO
from game import PingPongGame

app = Flask(__name__)
socketio = SocketIO(app)
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

@app.route('/start_game/<game_type>', methods=['POST'])
def start_game(game_type):
    game.start_game(game_type)
    return jsonify(success=True)

@app.route('/end_game/', methods=['POST'])
def end_game():
    game.end_game()
    return jsonify(success=True)

@app.route('/get_game_info', methods=['GET'])
def get_game_info():
    return jsonify(game.to_dict())

# Handle a message event from the client
@socketio.on('update')
def handle_update(update):
    print(update)
    socketio.emit('update', update)

if __name__ == '__main__':
    socketio.run(app, host='192.168.1.45', port=5000, allow_unsafe_werkzeug=True)

