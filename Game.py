class Game:
    def __init__(self):
        self.target_score = None  # Optional: In Game Type 2, if players score below this value, they win.
        self.current_score = None
        self.game_type = None
        self.players = []

    def get_target_score(self):
        return self.target_score

    def set_target_score(self, score):
        self.target_score = score

    def get_current_score(self):
        return self.current_score

    def set_current_score(self, score):
        self.current_score = score

    def get_win_condition(self):
        match self.game_type:
            case 1:
                return self.current_score <= 0
            case 2:
                return self.current_score <= self.target_score
            case 3:
                return self.current_score <= self.target_score

    def set_players(self, players):
        self.players = players

    def get_players(self):
        return self.players