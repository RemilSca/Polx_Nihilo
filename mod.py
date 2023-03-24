

class Player:
    def __init__(self, name, pswd):
        self.name = name
        self.pswd = pswd
        self.inv = Inv


class Inv:
    def __init__(self):
        self.units = []
        self.rmc = 0

