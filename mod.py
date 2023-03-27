import chara
import pickle

class Player:
    def __init__(self, name, pswd, id):
        self.id = id
        self.name = name
        self.pswd = pswd
        self.inv = Inv()
        self.roster = Roster()

    def debug(self):
        self.roster = Roster()

    def pull_gacha(self):
        x = chara.gacha()
        self.inv.units.append(x)
        self.save()
        return x

    def save(self):
        with open(f"source/players/{self.id}.pkl", 'wb') as f:
            pickle.dump(self, f)


    def get_units(self):
        return self.inv.units
    def get_roster(self):
        return self.roster

    def set_slot(self, slot, unit):
        self.roster.set_slot(slot, unit)
        self.save()


def load_player(id):
    with open(f"source/players/{id}.pkl", 'rb') as f:
        return pickle.load(f)


def create_player(name, pswd, id):
    p = Player(name, pswd, id)
    p.save()
    return p


class Inv:
    def __init__(self):
        self.units = []
        self.rmc = 0


class Roster:
    def __init__(self):
        self.slot1 = None
        self.slot2 = None
        self.slot3 = None
        self.slot4 = None
        self.slot5 = None
        self.slot6 = None

    def set_slot(self, slot, unit):
        if slot == 1:
            self.slot1 = unit
        elif slot == 2:
            self.slot2 = unit
        elif slot == 3:
            self.slot3 = unit
        elif slot == 4:
            self.slot4 = unit
        elif slot == 5:
            self.slot5 = unit
        elif slot == 6:
            self.slot6 = unit

    def get_list(self):
        return [self.slot1, self.slot2, self.slot3, self.slot4, self.slot5, self.slot6]

