import random

characters = {'Remi': [1], 'Flan': [2], 'Okuu': [50], 'Rumia': [100]}


class Character:
    def __init__(self, name, id=0):
        self.name = name
        self.chance = characters[name][0]
        self.id = id


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




