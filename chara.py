import random

#szans 100 duzo 1 malo
#szansa, hp, ak, mg, df, mp, spell
characters = {'Remi': [1, 10, 3, 7, 1, 5, 'g'], 'Flan': [2, 9, 6, 3, 0, 5, 'l'], 'Okuu': [50, 20, 2, 2, 1, 5, 'r'], 'Rumia': [100, 12, 3, 2, 0, 5,'d']}


class Character:
    def __init__(self, name, id=0):
        self.name = name
        self.chance = characters[name][0]
        self.id = id
        self.spell = characters[name][6]
        self.mpu = characters[name][5]
        self.df = characters[name][4]
        self.ak = characters[name][3]
        self.mg = characters[name][2]
        self.hp = characters[name][1]
        self.alive = True
        self.mp = 0

    def debug(self):
        name = self.name
        self.chance = characters[name][0]
        self.spell = characters[name][6]
        self.mpu = characters[name][5]
        self.df = characters[name][4]
        self.ak = characters[name][3]
        self.mg = characters[name][2]
        self.hp = characters[name][1]
        self.alive = True
        self.mp = 0

def gacha():
    c = list(characters.keys())
    l = []
    for x in c:
        ch = Character(x)
        l.append(ch.chance)
    g = random.choices(c, l)[0]
    getto = Character(g, gen_id())
    return getto


def gen_id():
    with open("source/ids.txt", 'r') as f:
        ids = eval(f.read())
    i = random.randint(1, 10000)
    while i in ids:
        i = random.randint(1, 10000)
    ids.append(i)
    with open("source/ids.txt", 'w') as f:
        f.write(str(ids))

    return i




