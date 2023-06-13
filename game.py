class PingPongGame:
    def __init__(self, player1Score=0, player2Score=0, serverSet=1, servingPlayer='1'):
        self.player1 = "80:e4:da:7b:34:e8"
        self.player2 = "80:e4:da:7b:2e:fc"
        self.player1Score = player1Score
        self.player2Score = player2Score
        self.serverSet = serverSet
        self.servingPlayer = servingPlayer

    def get_server(self):
        
        total = (self.player1Score + self.player2Score)
        num_str = repr(total)
        last_digit_str = num_str[-1]
        last_digit = int(last_digit_str)

        if last_digit < 5:
            if self.serverSet == 1:
                self.servingPlayer = "1"
            elif self.serverSet == 2:
                self.servingPlayer = "2"
        else:
            if self.serverSet == 1:
                self.servingPlayer = "2"
            elif self.serverSet == 2:
                self.servingPlayer = "1"


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

        if self.player1Score == 0 and self.player2Score == 0:
            self.servingPlayer = "1"

    def to_dict(self):
        return {
            'player1Score': self.player1Score,
            'player2Score': self.player2Score,
            'servingPlayer': self.servingPlayer,
            'serverSet': self.serverSet
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
