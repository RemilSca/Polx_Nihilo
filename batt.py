
ter ={'default': 0}
#kutas
class Battle:
    def __init__(self, player1, player2, ter='default'):
        self.player1 = player1
        self.player2 = player2
        self.phase = 0
        self.terrain = ter

    def load_slots(self):
        self.slot11 = self.player1.get_roster().slot1
        self.slot12 = self.player1.get_roster().slot2
        self.slot13 = self.player1.get_roster().slot3
        self.slot14 = self.player1.get_roster().slot4
        self.slot15 = self.player1.get_roster().slot5
        self.slot16 = self.player1.get_roster().slot6

        self.slot21 = self.player2.get_roster().slot1
        self.slot22 = self.player2.get_roster().slot2
        self.slot23 = self.player2.get_roster().slot3
        self.slot24 = self.player2.get_roster().slot4
        self.slot25 = self.player2.get_roster().slot5
        self.slot26 = self.player2.get_roster().slot6


    def pick_target(self, unit, p):
        x = p.get_roster().get_list()
        for i in range(0, 3):
            if x[i].alive == True:
                targets.append(x[i])
        l = []
        for i in targets:
            l.append(i.foc)
        unit.target = random.choices(targets, l)[0]

    def deal_damage(self, unit):
        target = unit.target
        target.hp -= unit.ak - target.df
        if target.hp <= 0:
            target.alive = False

    def tick(self):

        if self.phase == 0:
            self.load_slots()
            self.termod = ter[self.terrain]








def fajto(p1, p2):
    u1 = p1.get_roster()
    u2 = p2.get_roster()

    u1.slot1.debug()
    u1.slot2.debug()
    u1.slot3.debug()
    u1.slot4.debug()
    u1.slot5.debug()
    u1.slot6.debug()
    u2.slot1.debug()
    u2.slot2.debug()
    u2.slot3.debug()
    u2.slot4.debug()
    u2.slot5.debug()
    u2.slot6.debug()

    check = True

    while check:

        #faza 1
        if u1.slot1 != None and u2.slot1 != None:
            u1.slot1.hp -= u2.slot1.ak - u1.slot1.df
        if u2.slot1 != None and u1.slot1 != None:
            u2.slot1.hp -= u1.slot1.ak - u2.slot1.df

        if u1.slot2 != None and u2.slot2 != None:
            u1.slot2.hp -= u2.slot2.ak - u1.slot1.df
        if u2.slot2 != None and u1.slot2 != None:
            u2.slot2.hp -= u1.slot2.ak - u2.slot1.df

        if u1.slot3 != None and u2.slot3 != None:
            u1.slot3.hp -= u2.slot3.ak - u1.slot1.df
        if u2.slot3 != None and u1.slot3 != None:
            u2.slot3.hp -= u1.slot3.ak - u2.slot1.df

        #check
        if u1.slot1.hp <= 0:
            if u1.slot4 != None:
                u1.slot1 = u1.slot4
                u1.slot4 = None
            else:
                u1.slot1.alive = False
        if u1.slot2.hp <= 0:
            if u1.slot5 != None:
                u1.slot2 = u1.slot5
                u1.slot5 = None
            else:
                u1.slot2.alive = False
        if u1.slot3.hp <= 0:
            if u1.slot6 != None:
                u1.slot3 = u1.slot6
                u1.slot6 = None
            else:
                u1.slot3.alive = False

        if u2.slot1.hp <= 0:
            if u2.slot4 != None:
                u2.slot1 = u2.slot4
                u2.slot4 = None
            else:
                u2.slot1.alive = False
        if u2.slot2.hp <= 0:
            if u2.slot5 != None:
                u2.slot2 = u2.slot5
                u2.slot5 = None
            else:
                u2.slot2.alive = False
        if u2.slot3.hp <= 0:
            if u2.slot6 != None:
                u2.slot3 = u2.slot6
                u2.slot6 = None
            else:
                u2.slot3.alive = False

        if u1.slot1.alive == False and u1.slot2.alive == False and u1.slot3.alive == False:
            check = False
            return p2
        if u2.slot1.alive == False and u2.slot2.alive == False and u2.slot3.alive == False:
            check = False
            return p1

        #status
        try:
            print(f"user1: {u1.slot1.name} hp: {u1.slot1.hp}, {u1.slot2.name} hp: {u1.slot2.hp}, {u1.slot3.name} hp: {u1.slot3.hp}")
            print(f"user2: {u2.slot1.name} hp: {u2.slot1.hp}, {u2.slot2.name} hp: {u2.slot2.hp}, {u2.slot3.name} hp: {u2.slot3.hp}")
        except:
            print("error")

        #faza 2

        if u1.slot1 != None and u2.slot4 != None:
            u1.slot1.hp -= u2.slot4.mg
        if u2.slot1 != None and u1.slot4 != None:
            u2.slot1.hp -= u1.slot4.mg

        if u1.slot2 != None and u2.slot5 != None:
            u1.slot2.hp -= u2.slot5.mg
        if u2.slot2 != None and u1.slot5 != None:
            u2.slot2.hp -= u1.slot5.mg

        if u1.slot3 != None and u2.slot6 != None:
            u1.slot3.hp -= u2.slot6.mg
        if u2.slot3 != None and u1.slot6 != None:
            u2.slot3.hp -= u1.slot6.mg

        #check
        if u1.slot1.hp <= 0:
            if u1.slot4 != None:
                u1.slot1 = u1.slot4
                u1.slot4 = None
            else:
                u1.slot1.alive = False
        if u1.slot2.hp <= 0:
            if u1.slot5 != None:
                u1.slot2 = u1.slot5
                u1.slot5 = None
            else:
                u1.slot2.alive = False
        if u1.slot3.hp <= 0:
            if u1.slot6 != None:
                u1.slot3 = u1.slot6
                u1.slot6 = None
            else:
                u1.slot3.alive = False

        if u2.slot1.hp <= 0:
            if u2.slot4 != None:
                u2.slot1 = u2.slot4
                u2.slot4 = None
            else:
                u2.slot1.alive = False
        if u2.slot2.hp <= 0:
            if u2.slot5 != None:
                u2.slot2 = u2.slot5
                u2.slot5 = None
            else:
                u2.slot2.alive = False
        if u2.slot3.hp <= 0:
            if u2.slot6 != None:
                u2.slot3 = u2.slot6
                u2.slot6 = None
            else:
                u2.slot3.alive = False

        if u1.slot1.alive == False and u1.slot2.alive == False and u1.slot3.alive == False:
            check = False
            return p2
        if u2.slot1.alive == False and u2.slot2.alive == False and u2.slot3.alive == False:
            check = False
            return p1

        #status
        try:
            print(f"user1: {u1.slot1.name} hp: {u1.slot1.hp}, {u1.slot2.name} hp: {u1.slot2.hp}, {u1.slot3.name} hp: {u1.slot3.hp}")
            print(f"user2: {u2.slot1.name} hp: {u2.slot1.hp}, {u2.slot2.name} hp: {u2.slot2.hp}, {u2.slot3.name} hp: {u2.slot3.hp}")
        except:
            print("error")


        #faza 3

        s1 = u1.get_list()
        s2 = u2.get_list()

        for x in s1:
            if x != None:
                if x.mp == x.mpu:
                    x.mp = 0
                    #if x.spell == "f":
                else:
                    x.mp += 1

        for x in s2:
            if x != None:
                if x.mp == x.mpu:
                    x.mp = 0
                else:
                    x.mp += 1


        #check
        if u1.slot1.hp <= 0:
            if u1.slot4 != None:
                u1.slot1 = u1.slot4
                u1.slot4 = None
            else:
                u1.slot1.alive = False
        if u1.slot2.hp <= 0:
            if u1.slot5 != None:
                u1.slot2 = u1.slot5
                u1.slot5 = None
            else:
                u1.slot2.alive = False
        if u1.slot3.hp <= 0:
            if u1.slot6 != None:
                u1.slot3 = u1.slot6
                u1.slot6 = None
            else:
                u1.slot3.alive = False

        if u2.slot1.hp <= 0:
            if u2.slot4 != None:
                u2.slot1 = u2.slot4
                u2.slot4 = None
            else:
                u2.slot1.alive = False
        if u2.slot2.hp <= 0:
            if u2.slot5 != None:
                u2.slot2 = u2.slot5
                u2.slot5 = None
            else:
                u2.slot2.alive = False
        if u2.slot3.hp <= 0:
            if u2.slot6 != None:
                u2.slot3 = u2.slot6
                u2.slot6 = None
            else:
                u2.slot3.alive = False

        if u1.slot1.alive == False and u1.slot2.alive == False and u1.slot3.alive == False:
            check = False
            return p2
        if u2.slot1.alive == False and u2.slot2.alive == False and u2.slot3.alive == False:
            check = False
            return p1


# ╰⋃╯
