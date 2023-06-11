class PingPongGame:
    def __init__(self):
        self.player1 = "80:e4:da:7b:34:e8"
        self.player2 = "80:e4:da:7b:2e:fc"
        self.player1Score = 0
        self.player2Score = 0
        self.serverDirection = "right"
        self.serverSet = 0

    # Create methods for all actions that can be performed on the game

    def increment_score(self, player):
        if player == "player1":
            self.player1Score += 1
        elif player == "player2":
            self.player2Score += 1

    def decrement_score(self, player):
        if player == "player1":
            self.player1Score -= 1
        elif player == "player2":
            self.player2Score -= 1

    def reset_score(self, player):
        if player == "player1":
            self.player1Score = 0
        elif player == "player2":
            self.player2Score = 0
