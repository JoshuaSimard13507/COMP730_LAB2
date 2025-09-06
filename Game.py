class Game:
    def __init__(self):
        self.targetScore = None #Optional: In Game Type 2, if players score below this value, they win.
        self.currentScore = None
        self.gameType = None

    def get_target_score(self):
        return self.targetScore
    
    def set_target_score(self, score):
        self.targetScore = score

    def get_current_score(self):
        return self.currentScore
    
    def set_current_score(self, score):
        self.currentScore = score

    def get_win_condition(self):
        match (self.gameType):
            case 1:
                return self.currentScore <= 0
            case 2:
                return self.currentScore <= self.targetScore