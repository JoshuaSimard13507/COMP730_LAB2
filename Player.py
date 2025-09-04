class Player:

    def __init__(self):
        self.name = None
        self.score = None

    def get_name(self):
        return self.name

    def set_name(self, inp):
        self.name = inp

    def get_score(self):
        return self.score

    def set_score(self, inp):
        self.score = inp